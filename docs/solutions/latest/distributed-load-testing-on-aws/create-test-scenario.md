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
+  **Run Now** - Run the test immediately after creation.
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
+  **Simple HTTP Endpoint** - Test a single API endpoint or web page with simple configuration.
+  **JMeter** - Upload JMeter test scripts (.jmx files or .zip archives).
+  **k6** - Upload k6 test scripts (.js files or .zip archives).
+  **Locust** - Upload Locust test scripts (.py files or .zip archives).

**Note**
All four test types rely on third-party components. The solution runs tests through the Taurus test automation framework, which executes JMeter, k6, or Locust depending on the test type; Simple HTTP Endpoint tests are converted to a JMeter test plan and run by the bundled Apache JMeter. Before creating a test, review [Third-party testing frameworks](security-1.md#third-party-testing-frameworks) for security considerations, license information, and patching options.

 **Traffic shape mode**

Choose which side controls the load the test generates. The mode you select changes the fields the console shows in [Step 3: Traffic shape](#step-3-traffic-shape).
+  **Standard** - The solution controls the load. You set the virtual users, the ramp-up period, and the hold duration. Standard is the default, and it is the only mode that supports Simple HTTP Endpoint tests.
+  **Native** - Your script controls the load. The solution runs your script under the testing framework’s own command line and sets only the task count per Region and a safety duration.

Native requires an uploaded script, so you can’t select it when you choose the Simple HTTP Endpoint test type. For the full definitions and guidance on which mode to choose, refer to [Traffic shape modes](#traffic-shape-modes).

 **HTTP endpoint configuration**

When "Simple HTTP Endpoint" is selected, the solution generates a JMeter test plan from your configuration and executes it with the bundled Apache JMeter binary. Configure these settings:

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

When using JMeter, k6, or Locust, upload your test script file or a .zip archive containing your test script and supporting files.

For JMeter, you can include custom plugins in a `/plugins` folder within your .zip archive.

For Locust, a test script inside a .zip archive must be named `locustfile.py`. To install third-party Python packages into the container at run time, include a `requirements.txt` file in the archive, and optionally a `packages` subdirectory of wheel files to install them without internet access. For more information, refer to [Locust tests](design-considerations.md#locust-script-support).

**Important**
In Standard mode, the solution controls the load and overrides what your script declares. Your test script (JMeter, k6, or Locust) can define concurrency (virtual users), transaction rates (TPS), ramp-up times, and other load parameters. The solution applies the values you specify in the Traffic Shape screen instead. That configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.
In Native mode, your script controls the load and the solution passes no load parameters to the framework. For the difference between the two modes, refer to [Traffic shape modes](#traffic-shape-modes).

 **Safety duration (Native mode)**

When you select Native mode, the console shows a **Safety duration** field alongside the script upload. The default is 4 hours and the maximum is 24 hours.

In Native mode, the safety duration ends a test that runs longer than you intended, because your script decides when the run finishes. It is a guard, not a schedule. If the test is still running when the duration elapses, the solution stops the testing framework. It keeps the results for the portion that ran and records the run as complete rather than failed. Set it above the longest run you expect the script to need.

## Step 3: Traffic shape
<a name="step-3-traffic-shape"></a>

Configure how traffic will be distributed during your test, including multi-Region support.

### Traffic shape modes
<a name="traffic-shape-modes"></a>

The solution offers two traffic shape modes, Standard and Native. They differ in which side controls the load: the solution, or the script you upload. You select the mode in [Step 2: Scenario configuration](#step-2-scenario-configuration), and it determines which of the fields below apply.

**Note**
Native mode is a preview feature in version 4.3.0. Standard mode is the default and is the behavior the solution has always used.

 **Standard**

Standard mode puts the solution in control of the load. You set the number of Fargate tasks per Region, the concurrent virtual users per task, a ramp-up period, and a hold duration. The solution runs your test through the Taurus automation framework, which translates those values into the underlying framework’s own load controls. Taurus takes precedence over whatever load your script declares, so a k6 options block, a Locust `LoadTestShape`, or a JMeter thread group is rewritten or ignored. A Region’s virtual users are the task count multiplied by the concurrency for each task, and the shape is the same whichever framework you chose. This is how every test ran before version 4.3.0, so scenarios created earlier keep behaving exactly as they did and need no changes.

Choose Standard when the load shape belongs outside the script, set from the console, the CLI, or an agent. Standard is the only mode that lets you set an exact virtual-user count and change the ramp-up and hold shape without touching the script. Only Standard supports the Simple HTTP Endpoint type, where the solution generates the test plan for you. Typical uses: a capacity check stepping 500 to 5,000 virtual users, a nightly regression holding 1,000 users for ten minutes, or any comparison needing an identical ramp. Its limit is expressiveness. Anything Taurus cannot represent is unavailable here, including multiple weighted scenarios, per-stage thresholds, and arrival-rate executors.

 **Native**

Native mode puts your script in control of the load. The solution runs the file you uploaded under the framework’s own command line: `jmeter -n -t`, `k6 run`, or `locust --headless`. It passes no load flags, so your script is the sole authority on the traffic it generates and the solution never rewrites it. Two controls remain: how many Fargate tasks to launch per Region, and a required safety duration of up to 24 hours. The safety duration is a guard against a script that never exits, not a schedule. If a test is still running when the duration elapses, the solution stops the framework, collects the results for the portion that ran, and records the run as complete rather than failed. Each task runs as an independent framework process with no coordination between tasks, so a Region generates one full copy of your script’s declared load for each task. For example, a k6 script that holds 200 virtual users, run on five tasks, puts 1,000 virtual users on the target. Task count is therefore the only load control Native gives you, and it moves in whole multiples of whatever the script declares. Changing the ramp, the hold time, or the virtual-user count itself means editing the script.

Choose Native when you want to run a script exactly as it was written. A script that already runs locally or in CI runs unchanged on the solution, which is the main reason to reach for Native. Native preserves everything the framework can express: k6 scenarios, stages, and thresholds; Locust `LoadTestShape` classes and weighted task sets; JMeter timers and thread groups. Pick it when the load shape is part of what the test means, and reproducing it faithfully matters more than steering it from outside. Typical uses: reusing a k6 script from a pipeline without rewriting it, a spike-then-recover profile, or weighted scenarios that a single concurrency number cannot express. Two constraints follow from running the framework as authored. Native requires an uploaded script, so Simple HTTP Endpoint is unavailable. Locust scripts must not set `processes`, because the solution counts requests only when Locust runs as a single process.

 **Choosing a mode**

| If you need | Choose |
| --- | --- |
| An exact virtual-user count, set from outside the script | Standard |
| To change the ramp-up or hold time without editing the script | Standard |
| A single URL with no script at all | Standard |
| The same load shape regardless of framework | Standard |
| To reuse a CI or local script unchanged | Native |
| The script’s own stages, thresholds, or shape honored | Native |
| k6 scenarios, thresholds, or arrival-rate executors | Native |
| A Locust `LoadTestShape` or weighted task set | Native |
| JMeter timers and thread groups run exactly as authored | Native |
| To scale load only in whole multiples of the script’s own load | Native |

 **Multi-Region traffic configuration**

Select one or more AWS Regions to distribute your load test geographically. For each selected Region, configure:

 **Task Count**
The number of containers (tasks) that will be launched in the Fargate cluster for the test scenario. Additional tasks will not be created once the account has reached the "Fargate resource has been reached" limit. Task Count applies to both traffic shape modes. In Native mode it is the only load control the console offers, because each task runs a full copy of your script.

 **Concurrency**
The number of concurrent virtual users generated per task. The recommended limit is based on default settings of 2 vCPUs per task. Concurrency is limited by CPU and Memory resources. This field applies to Standard mode only. In Native mode the console displays a read-only value of "Defined by script" for each Region, because your script sets its own virtual-user count.

### Determine the number of users
<a name="determine-number-of-users"></a>

The number of users a container can support for a test can be determined by gradually increasing the number of users and monitoring performance in Amazon CloudWatch. Once you observe that CPU and memory performance are approaching their limits, you’ve reached the maximum number of users a container can support for that test in its default configuration (2 vCPU and 4 GB of memory).

This calibration sets the Concurrency value, so it applies to Standard mode. The container limits it establishes apply to Native mode as well. There you raise or lower the load your script declares, instead of setting the Concurrency field.

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
The solution displays available capacity information for each Region, helping you plan your test configuration within available limits.

 **Table of available tasks**

The **Table of Available Tasks** displays resource availability for each selected Region:
+  **Region** - The AWS Region name.
+  **vCPUs per Task** - The number of virtual CPUs allocated to each task (default: 2).
+  **DLT Task Limit** - The maximum number of tasks that can be created based on your account’s Fargate on-demand vCPU quota. New accounts typically have a lower quota; verify your current limit in the Service Quotas console and request an increase if needed.
+  **Available DLT Tasks** - The current number of tasks available in the Region, calculated as your DLT Task Limit minus the vCPUs already in use by running Fargate tasks.

To increase the number of available tasks or vCPUs per task, refer to the Developer Guide.

 **Test duration**

Define how long your load test will run. The console shows this section in Standard mode only. In Native mode your script determines how long the test runs, bounded by the safety duration you set in [Step 2: Scenario configuration](#step-2-scenario-configuration).

 **Ramp Up**
The time to reach target concurrency. The load gradually increases from 0 to the configured concurrency level over this period.

 **Hold For**
The duration to maintain target load. The test continues at full concurrency for this period.

## Step 4: Review and create
<a name="step-4-review-create"></a>

Review all your configurations before creating the test scenario. Verify:
+ General settings (name, description, schedule).
+ Scenario configuration (test type, endpoint or script).
+ Traffic shape (mode, tasks, users, duration, Regions).

After reviewing, choose **Create** to save your test scenario.

 **Managing test scenarios**

After creating a test scenario, you can:
+  **Edit** - Modify the test configuration. Common use cases include:
  + Refining traffic shape to achieve the desired transaction rate.
+  **Copy** - Duplicate an existing test scenario to create variations. Common use cases include:
  + Updating endpoints or adding headers/body parameters.
  + Adding or modifying test scripts.
+  **Delete** - Remove test scenarios you no longer need.
