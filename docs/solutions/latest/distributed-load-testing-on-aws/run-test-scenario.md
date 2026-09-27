---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/run-test-scenario.html
---

# Run a test scenario
<a name="run-test-scenario"></a>

After creating a test scenario, you can run it immediately or schedule it to run at a specific time in the future. When you navigate to a running test, the console displays the Scenario Details tab with real-time task status and metrics.

## Scenario details view
<a name="scenario-details-view"></a>

The Scenario Details tab displays key information about your test. The task status table shows real-time information for every Region.

 **Task status table**

The Task Status table shows real-time information for each Region:
+  **Region** - The AWS Region where tasks are running
+  **Task Counts** - The total number of tasks configured for the Region
+  **Concurrency** - The number of virtual users per task
+  **Running** - Number of tasks currently executing the test
+  **Pending** - Number of tasks waiting to start
+  **Provisioning** - Number of tasks being provisioned

## Test execution workflow
<a name="test-execution-workflow"></a>

When a test starts, the following workflow occurs:

1.  **Task provisioning** - The solution provisions containers (tasks) in the specified AWS Regions. Tasks appear in the "Provisioning" column.

1.  **Task startup** - The solution continues to provision tasks until the target task count is reached in each Region. Tasks move from "Provisioning" to "Pending" to "Running".

1.  **Traffic generation** - After the solution provisions all tasks in a Region, they begin sending traffic to your target endpoint.

1.  **Test execution** - The test runs for the configured duration (ramp-up \+ hold time).

1.  **Results parsing** - When the test ends, a background parsing job aggregates and processes results from all Regions.

## Test run statuses
<a name="test-statuses"></a>

Test runs can have the following statuses:
+  **Scheduled** - The test is scheduled to run in the future.
+  **Running** - The test is currently in progress.
+  **Cancelled** - A user cancelled an in-progress test run.
+  **Errored** - The test run encountered an error.
+  **Complete** - The test run completed successfully and results are ready.

## Monitoring with live data
<a name="monitoring-live-data"></a>

If you enabled live data when creating the test scenario, you can view real-time metrics while the test is running. The Real Time Metrics section displays four graphs that update continuously as the test progresses, with data aggregated at one-second intervals.

![Real Time Metrics graphs showing live test performance data](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/real-time-metrics.png)

 **Graph descriptions**

 **Average Response Time**
Displays the average response time in seconds for requests processed by each Region. The Y-axis shows response time in seconds, and the X-axis shows the time of day. Each Region is represented by a different color in the legend.

 **Virtual Users**
Shows the number of concurrent virtual users actively generating load in each Region. The graph displays how virtual users ramp up during the test and maintains the target concurrency level.

 **Successful Requests**
Displays the cumulative count of successful requests over time for each Region. The graph shows the rate at which successful requests are being processed.

 **Failed Requests**
Shows the cumulative count of failed requests over time for each Region. A low or zero count indicates healthy test execution.

 **Multi-Region visualization**

When running tests across multiple Regions, each graph displays data for all Regions simultaneously. The legend at the bottom of each graph identifies which color represents each Region (for example, us-west-2 and us-east-1).

 **Technical implementation**

The CloudWatch log group for the Fargate tasks contains a subscription filter that captures test results. When the pattern is detected, a Lambda function structures the data and publishes it to an AWS IoT Core topic. The web console subscribes to this topic and displays the metrics in real-time.

**Note**
Live data is ephemeral and only available while the test is running. The web console persists a maximum of 5,000 data points, after which the oldest data is replaced with the newest. If the page refreshes, the graphs will be blank and start from the next available data point. Once a test is complete, the solution stores the results data in DynamoDB and Amazon S3. If no data is available yet, the graphs display "There is no data available."

## Cancelling a test
<a name="cancelling-tests"></a>

You can cancel a running test from the web console. When you cancel a test, the following workflow occurs:

1. The cancellation request is sent to the `microservices` API

1. The `microservices` API calls the `task-canceler` Lambda function which stops all currently launched tasks

1. If the `task-runner` Lambda function continues to run after the initial cancellation call, tasks may continue to launch briefly

1. Once the `task-runner` Lambda function finishes, AWS Step Functions proceeds to the `Cancel Test` step, which runs the `task-canceler` Lambda function again to stop any remaining tasks

**Note**
Cancelled tests take time to complete the shutdown process as the solution terminates all containers. The test status will change to "Cancelled" once all resources are cleaned up.
