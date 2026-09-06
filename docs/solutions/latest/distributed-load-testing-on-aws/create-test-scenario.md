---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/create-test-scenario.html
---

# Create a test scenario
<a name="create-test-scenario"></a>

Creating a test scenario involves four main steps: configuring general settings, defining the scenario, shaping traffic patterns, and reviewing your configuration.

## Step 1: General settings
<a name="step-1-general-settings"></a>

Configure the basic parameters for your load test including test name, description, and general configuration options.

 **Test identification**
+  **Test name** (Required) - A descriptive name for your test scenario
+  **Test description** (Required) - Additional details about the test purpose and configuration
+  **Tags** (Optional) - Add up to 5 tags to categorize and organize your test scenarios

 **Scheduling options**

Configure when the test should run:
+  **Run Now** - Execute the test immediately after creation.
+  **Run Once** - Schedule the test to run at a specific date and time.
+  **Run on a Schedule** - Use cron-based scheduling to run tests automatically at regular intervals. You can select from common patterns (every hour, daily, weekly) or define a custom cron expression. For details on the accepted cron format, supported patterns, and constraints, refer to [Cron expression reference](cron-expression-reference.md) in the Developer guide.

 **Scheduling workflow**

When you schedule a test, the following workflow occurs:
+ The schedule parameters are sent to the solution’s API via Amazon API Gateway.
+ The API passes the parameters to a Lambda function that creates an Amazon EventBridge Scheduler schedule configured to run on the specified date.
+ For one-time tests (Run Once), the EventBridge Scheduler schedule invokes the `api-services` Lambda function at the specified date and time, which executes the test.
+ For recurring tests (Run on a Schedule), the EventBridge Scheduler schedule invokes the `api-services` Lambda function immediately and on the cadence defined by the cron or rate expression until the expiry date.

 **Live data**

Select the **Include live data** checkbox to view real-time metrics while your test is running. When enabled, you can monitor:
+ Average response time.
+ Virtual user counts.
+ Successful request counts.
+ Failed request counts.

The live data feature provides real-time charting with data aggregated at one-second intervals. For more information, refer to [Monitoring with live data](run-test-scenario.md#monitoring-live-data).

## Step 2: Scenario configuration
<a name="step-2-scenario-configuration"></a>

Define the specific testing scenario and select your preferred testing framework.

 **Test type selection**

Choose the type of load test you want to perform:
+  **Single HTTP Endpoint** - Test a single API endpoint or web page with simple configuration.
+  **JMeter** - Upload JMeter test scripts (.jmx files or .zip archives).
+  **k6** - Upload k6 test scripts (.js files or .zip archives).
+  **Locust** - Upload Locust test scripts (.py files or .zip archives).

**Note**
All four test types rely on third-party components. The solution runs tests through the Taurus test automation framework, which executes JMeter, k6, or Locust depending on the test type; Single HTTP Endpoint tests are converted to a JMeter test plan and run by the bundled Apache JMeter. Before creating a test, review [Third-party testing frameworks](security-1.md#third-party-testing-frameworks) for security considerations, license information, and patching options.

 **HTTP endpoint configuration**

When "Single HTTP Endpoint" is selected, the solution generates a JMeter test plan from your configuration and executes it with the bundled Apache JMeter binary. Configure these settings:

 **HTTP Endpoint** (Required)
Enter the full URL of the endpoint you want to test. For example, `https://api.example.com/users`. Ensure the endpoint is accessible from AWS infrastructure.

 **HTTP Method** (Required)
Select the HTTP method for your requests. Default is `GET`. Other options include `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, and `OPTIONS`.

 **Request Header** (Optional)
Add custom HTTP headers to your requests. Common examples include:
+  `Content-Type: application/json`
+  `Authorization: Bearer <token>`
+  `User-Agent: LoadTest/1.0`

  Choose **Add Header** to include multiple headers.

 **Body Payload** (Optional)
Add request body content for POST or PUT requests. Supports JSON, XML, or plain text formats. For example: `{"userId": 123, "action": "test"}`.

 **Test framework scripts**

When using JMeter, k6, or Locust, upload your test script file or a .zip archive containing your test script and supporting files. For JMeter, you can include custom plugins in a `/plugins` folder within your .zip archive.

**Important**
Although your test script (JMeter, k6, or Locust) might define concurrency (virtual users), transaction rates (TPS), ramp-up times, and other load parameters, the solution overrides these configurations with the values you specify in the Traffic Shape screen during test creation. The Traffic Shape configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.

## Step 3: Traffic shape
<a name="step-3-traffic-shape"></a>

Configure how traffic will be distributed during your test, including multi-region support.

 **Multi-region traffic configuration**

Select one or more AWS regions to distribute your load test geographically. For each selected region, configure:

 **Task Count**
The number of containers (tasks) that will be launched in the Fargate cluster for the test scenario. Additional tasks will not be created once the account has reached the "Fargate resource has been reached" limit.

 **Concurrency**
The number of concurrent virtual users generated per task. The recommended limit is based on default settings of 2 vCPUs per task. Concurrency is limited by CPU and Memory resources.

### Determine the number of users
<a name="determine-number-of-users"></a>

The number of users a container can support for a test can be determined by gradually increasing the number of users and monitoring performance in Amazon CloudWatch. Once you observe that CPU and memory performance are approaching their limits, you’ve reached the maximum number of users a container can support for that test in its default configuration (2 vCPU and 4 GB of memory).

 **Calibration process**

You can begin determining the concurrent user limits for your test by using the following example:

1. Create a test with no more than 200 users.

1. While the test runs, monitor the CPU and Memory using the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home):

   1. In the navigation pane, under **Container Insights**, select **Performance Monitoring**.

   1. On the **Performance monitoring** page, from the left drop down menu, select **ECS Clusters**.

   1. From the right drop down menu, select your Amazon Elastic Container Service (Amazon ECS) cluster.

1. While monitoring, watch the CPU and Memory. If the CPU does not surpass 75% or the Memory does not surpass 85% (ignore one-time peaks), you can run another test with a higher number of users.

Repeat steps 1-3 if the test did not exceed the resource limits. Optionally, you can increase the container resources to allow for a higher number of concurrent users. However, this results in a higher cost. For details, refer to the Developer Guide.

**Note**
For accurate results, run only one test at a time when determining concurrent user limits. All tests use the same cluster, and CloudWatch container insights aggregates the performance data based on the cluster. This causes both tests to be reported to CloudWatch Container Insights simultaneously, which results in inaccurate resource utilization metrics for a single test.

For more information on calibrating users per engine, refer to [Calibrating a Taurus Test](https://guide.blazemeter.com/hc/en-us/articles/360000864389-Calibrating-a-Taurus-Test-Calibrating-a-Taurus-Test) in the BlazeMeter documentation.

**Note**
The solution displays available capacity information for each region, helping you plan your test configuration within available limits.

 **Table of available tasks**

The **Table of Available Tasks** displays resource availability for each selected region:
+  **Region** - The AWS region name.
+  **vCPUs per Task** - The number of virtual CPUs allocated to each task (default: 2).
+  **DLT Task Limit** - The maximum number of tasks that can be created based on your account’s Fargate on-demand vCPU quota. New accounts typically have a lower quota; verify your current limit in the Service Quotas console and request an increase if needed.
+  **Available DLT Tasks** - The current number of tasks available in the region, calculated as your DLT Task Limit minus the vCPUs already in use by running Fargate tasks.

To increase the number of available tasks or vCPUs per task, refer to the Developer Guide.

 **Test duration**

Define how long your load test will run:

 **Ramp Up**
The time to reach target concurrency. The load gradually increases from 0 to the configured concurrency level over this period.

 **Hold For**
The duration to maintain target load. The test continues at full concurrency for this period.

## Step 4: Review and create
<a name="step-4-review-create"></a>

Review all your configurations before creating the test scenario. Verify:
+ General settings (name, description, schedule).
+ Scenario configuration (test type, endpoint or script).
+ Traffic shape (tasks, users, duration, regions).

After reviewing, choose **Create** to save your test scenario.

 **Managing test scenarios**

After creating a test scenario, you can:
+  **Edit** - Modify the test configuration. Common use cases include:
  + Refining traffic shape to achieve the desired transaction rate.
+  **Copy** - Duplicate an existing test scenario to create variations. Common use cases include:
  + Updating endpoints or adding headers/body parameters.
  + Adding or modifying test scripts.
+  **Delete** - Remove test scenarios you no longer need.
