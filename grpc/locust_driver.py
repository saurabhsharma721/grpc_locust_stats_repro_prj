import gevent
import os
from locust.env import Environment
from locust.stats import StatsCSVFileWriter, stats_printer
from locustfile import HelloGrpcUser

env = Environment(user_classes=[HelloGrpcUser])

user_count = 20
spawn_rate = 10

test_run_time = 30
print(f"user_count {user_count},spawn_rate {spawn_rate},test_run_time {test_run_time}")
# Using local runner in start
runner = env.create_local_runner()

### Perform global setup
for cls in env.user_classes:
    cls.perform_global_setup() # Is it correct approach?

#CSV writer

stats_path = os.path.join(os.getcwd(), "result")
csv_writer = StatsCSVFileWriter(
        environment=env,
        base_filepath=stats_path,
        full_history=True,
        percentiles_to_report=[50.0, 75.0, 90.0, 95.0],
)

print(f"Started non UI Test")
# start a greenlet that periodically outputs the current stats
gevent.spawn(stats_printer(env.stats))
# start a csv writer
gevent.spawn(csv_writer)
env.runner.start(user_count, spawn_rate=spawn_rate)
print(f"locust test have started running")

# Stop the test after test_run_time seconds(Default 120)
gevent.spawn_later(test_run_time, lambda: env.runner.quit())

env.runner.greenlet.join()
### Perform global teardown
for cls in env.user_classes:
    cls.perform_global_teardown() # Is it correct approach?
print(f"locust test have completed running")
print(f"Test run completed.")
print(f"requests after run : {env.stats.num_requests}")
print(f"Failures after run : {env.stats.num_failures}")
