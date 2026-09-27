---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/design-considerations.html
---

# Design considerations
<a name="design-considerations"></a>

This section describes important design decisions and configuration options for the Distributed Load Testing on AWS solution, including supported applications, test types, scheduling options, and deployment considerations.

## Supported applications
<a name="supported-applications"></a>

This solution supports testing cloud-based applications and on-premises applications as long as you have network connectivity from your AWS account to your application. The solution supports APIs that use HTTP or HTTPS protocols.

## Test types
<a name="test-types"></a>

Distributed Load Testing on AWS supports multiple test types: simple HTTP endpoint tests, JMeter, k6, and Locust. Each test type except simple HTTP endpoint can run in either traffic shape mode. For more information, refer to [Traffic shape modes](#traffic-shape-modes-architecture).

**Note**
The solution distributes JMeter, k6, and Locust as third-party components without modification. For security considerations, patching options, and license information, refer to [Third-party testing frameworks](security-1.md#third-party-testing-frameworks).

### Simple HTTP endpoint tests
<a name="single-http-support"></a>

The web console provides an HTTP Endpoint Configuration interface that allows you to test any HTTP or HTTPS endpoint without writing custom scripts. You define the endpoint URL, select the HTTP method (GET, POST, PUT, DELETE, and so on) from a dropdown menu, and optionally add custom request headers and body payloads. This configuration enables you to test APIs with custom authorization tokens, content types, or any other HTTP headers and request bodies required by your application.

When you configure an HTTP endpoint, the solution converts your configuration into a test plan that is executed by the bundled Apache JMeter binary through the Taurus framework. Simple HTTP Endpoint tests do not accept a test archive, so they cannot override the bundled JMeter binary or plugins. If you need to run HTTP endpoint tests with a patched JMeter, use the [JMeter](#jmeter-script-support) test type instead. For security considerations, refer to [Apache JMeter](security-1.md#jmeter-security).

Because the solution generates the test plan for this test type, Simple HTTP Endpoint tests run in Standard mode only. Native mode requires a script you upload. For more information, refer to [Traffic shape modes](#traffic-shape-modes-architecture).

### JMeter tests
<a name="jmeter-script-support"></a>

When creating a test scenario using the web console, you can upload a JMeter test script. The solution uploads the script to the scenarios S3 bucket. When Amazon ECS tasks run, they download the JMeter script from S3 and execute the test.

**Important**
In Standard mode, your JMeter script can define concurrency (virtual users), transaction rates (TPS), ramp-up times, and other load parameters. The solution overrides all of them with the values you specify in the Traffic Shape screen during test creation. That configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.
In Native mode, the solution runs `jmeter -n -t` against your script and passes no load parameters. Your thread groups and timers run exactly as authored. For more information, refer to [Traffic shape modes](#traffic-shape-modes-architecture).

If you have JMeter input files, you can zip the input files together with the JMeter script. You can choose the zip file when you create a test scenario.

If you would like to include plugins, any .jar files that are included in a /plugins subdirectory in the bundled zip file will be copied to the JMeter extensions directory and be available for load testing.

**Note**
If you include JMeter input files with your JMeter script file, you must include the relative path of the input files in your JMeter script file. In addition, the input files must be at the relative path. For example, when your JMeter input files and script file are in the /home/user directory and you refer to the input files in the JMeter script file, the path of input files must be ./INPUT\_FILES. If you use /home/user/INPUT\_FILES instead, the test will fail because it will not be able to find the input files.

If you include JMeter plugins, the .jar files must be bundled in a subdirectory named /plugins within the root of the zip file. Relative to the root of the zip file, the path to the jar files must be ./plugins/BUNDLED\_PLUGIN.jar.

For more information about how to use JMeter scripts, refer to [JMeter User’s Manual](https://jmeter.apache.org/usermanual/index.html).

### k6 tests
<a name="k6-script-support"></a>

The solution supports k6 framework-based testing. You can upload the k6 test file along with any necessary input files in an archive file. The web console displays a license acknowledgment message when you create a new k6 test. For license and security details, refer to [Grafana k6](security-1.md#k6-security).

**Important**
In Standard mode, your k6 script can define concurrency (virtual users), stages, thresholds, and other load parameters. The solution overrides all of them with the values you specify in the Traffic Shape screen during test creation. That configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.
In Native mode, the solution runs `k6 run` against your script and passes no load parameters. k6 applies your options block, scenarios, stages, and thresholds exactly as written. For more information, refer to [Traffic shape modes](#traffic-shape-modes-architecture).

### Locust tests
<a name="locust-script-support"></a>

The solution supports Locust framework-based testing. You can upload the Locust test file along with any necessary input files in an archive file.

**Important**
In Standard mode, your Locust script can define concurrency (user count), spawn rate, and other load parameters. The solution overrides all of them with the values you specify in the Traffic Shape screen during test creation. That configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.
In Native mode, the solution runs `locust --headless` against your script and passes no load parameters. Locust applies your `LoadTestShape` classes and weighted task sets exactly as written. Your script must not set `processes`, because the solution counts requests only when Locust runs as a single process. For more information, refer to [Traffic shape modes](#traffic-shape-modes-architecture).

#### Test script naming
<a name="locust-script-naming"></a>

When you upload a single `.py` file, the solution stores it under the test ID and references it directly, so the file can have any name. When you upload a `.zip` archive, the solution searches the archive for a file named `locustfile.py`. If the archive contains a Python script under any other name, the test fails during container startup with the message `No test script (.py) in zip file`.

#### Custom Python dependencies
<a name="locust-custom-dependencies"></a>

The load testing container includes Locust and its dependencies. It does not include third-party Python packages. If your Locust script imports a package that is not present in the container, the test fails with `ModuleNotFoundError`. To make additional packages available, include a `requirements.txt` file in the root of your `.zip` archive. The container installs the packages listed in `requirements.txt` before the test starts.

You can supply dependencies in either of two ways:

 **Install from PyPI**
Include only a `requirements.txt` file. The container installs the packages listed in `requirements.txt` from PyPI at task startup. This requires outbound internet access from the subnets where the load testing tasks run.

 **Install from bundled wheels (offline)**
Include a `requirements.txt` file and a `packages` subdirectory containing Python wheel (`.whl`) files. The container installs from the bundled wheels only and does not contact PyPI. This option works in environments without outbound internet access. Bundling wheels also pins the exact package versions, so a new PyPI release cannot change your test environment between runs.

The following example shows the archive layout:

```
my-test.zip
├── locustfile.py         # Required — must use this name
├── requirements.txt      # Optional — packages to install
└── packages/             # Optional — wheels, for offline install only
    └── *.whl
```

Both `requirements.txt` and the `packages` subdirectory must be at the root of the archive, alongside `locustfile.py`. Omit both if your script imports only packages that the container already provides. The `packages` subdirectory takes effect only alongside a `requirements.txt` file; on its own, it is ignored and no packages are installed.

**Transitive dependencies**
When you bundle wheels, `requirements.txt` must list every package that your dependencies require, not only the packages you import directly. The offline install does not contact PyPI. A missing transitive dependency causes the install to fail and the task to stop before the test starts.

#### Preparing wheels for the container
<a name="locust-preparing-wheels"></a>

The load testing container runs Linux on the x86\_64 architecture with Python 3.11. Wheels compiled for a different operating system, architecture, or Python version do not install. Packages written in pure Python are distributed as platform-independent wheels and work anywhere, but packages containing compiled extensions require a wheel built for the container’s platform. Because the container does not include a compiler, it cannot build a source distribution at task startup.

Run the following command to download wheels compatible with the container’s platform. You can run this command from any operating system, including macOS and Windows. Then include the resulting `packages` directory in your archive:

```
pip download -r requirements.txt \
  --dest packages \
  --platform manylinux2014_x86_64 \
  --python-version 3.11 \
  --only-binary=:all:
```

The `--platform` and `--python-version` options target the container, not the machine you run the command on. The `--only-binary=:all:` option causes the command to fail rather than silently fall back to a source distribution that the container cannot build. The `manylinux2014` tag specifies a wheel compatible with glibc 2.17 and later, which includes the container’s version.

To bundle a package that you maintain yourself, build a wheel from your package’s source directory with `pip wheel . --wheel-dir packages`, then add the package name to `requirements.txt`.

## Traffic shape modes
<a name="traffic-shape-modes-architecture"></a>

Every test runs in one of two traffic shape modes, Standard or Native. The mode determines three things: which side controls the load, which container image the Fargate tasks use, and which load parameters the solution sends to the testing framework. For guidance on choosing a mode when you create a test, refer to [Traffic shape modes](create-test-scenario.md#traffic-shape-modes) in the Use the solution section.

 **Standard mode**

The Fargate tasks use the image with Taurus installed. Taurus receives your task count, concurrency, ramp-up, and hold duration from the solution. It translates these values into the underlying framework’s own load controls. Taurus takes precedence over the load your script declares. It rewrites or ignores a k6 options block, a Locust `LoadTestShape`, or a JMeter thread group. The virtual users a Region generates are the task count multiplied by the concurrency for each task. That shape is the same for every framework. This is how the solution ran every test before version 4.3.0.

 **Native mode**

The Fargate tasks use the dedicated image for the test’s framework, which does not include Taurus. Instead of writing a Taurus configuration, the solution invokes the framework directly: `jmeter -n -t`, `k6 run`, or `locust --headless`. It passes no load parameters. Your script is the sole authority on the traffic it generates.

Two consequences follow from that design, and both affect how you size a test:
+  **Tasks multiply the load.** Each task runs an independent framework process with no coordination between tasks. As a result, a Region generates one full copy of your script’s declared load for each task. For example, a k6 script holding 200 virtual users, run on five tasks, puts 1,000 virtual users on the target. Task count is the only load control the solution offers in this mode. It moves in whole multiples of what the script declares.
+  **A safety duration bounds the run.** Because the script decides when the test ends, the solution requires a safety duration of up to 24 hours. If the test is still running when the duration elapses, the solution stops the framework. It collects the results for the portion that ran and records the run as complete rather than failed.

## Scheduling tests
<a name="scheduling-tests"></a>

The solution provides three execution timing options for running load tests:
+  **Run Now** - Run the load test immediately after creation
+  **Run Once** - Run the test on a specific date and time in the future
+  **Run on a Schedule** - Create recurring tests using cron expressions to define the schedule

When you select **Run Once**, you specify the run time in 24-hour format and the run date when the load test should start running.

When you select **Run on a Schedule**, you can either manually enter a cron expression or select from common cron patterns (such as every hour, daily at a specific time, weekdays, or monthly). The cron expression uses a fine-grained schedule format with fields for minutes, hours, day of month, month, day of week, and year. You must also specify an expiry date, which defines when the scheduled test should stop running. For more information about scheduling validation rules, refer to the [Scheduling constraints](cron-expression-reference.md#cron-scheduling-constraints) section of this guide.

**Note**
Test duration: Consider the total duration of tests when scheduling. For example, a test with a 10-minute ramp-up time and 40-minute hold time will take approximately 80 minutes to complete.
Minimum interval: Ensure the interval between scheduled tests is longer than the estimated test duration. For example, if the test takes about 80 minutes, schedule it to run no more frequently than every 3 hours.
Hourly limitation: The system does not allow tests to be scheduled with only a one-hour difference even if the estimated test duration is less than an hour.

## Concurrent tests
<a name="concurrent-tests-architecture"></a>

Each time a load test runs, the task-runner AWS Lambda function creates an Amazon CloudWatch dashboard named `EcsLoadTesting-<testId>-<region> ` in each Region where the test runs. The CloudWatch dashboard displays the combined output of all tasks running in the Amazon ECS cluster in real time: average response time, number of concurrent users, number of successful requests, and number of failed requests. The solution aggregates each metric by the second and updates the dashboard every minute.

Subsequent runs of the same test scenario update the same dashboard, so your account contains one dashboard for each test scenario in each Region. These dashboards remain in your account after tests complete. They incur a monthly charge until you delete them. The solution deletes a scenario’s dashboards when you delete the test scenario (for example, through the web console). The dashboards are not deleted when you delete the solution’s CloudFormation stacks. For more information, refer to the [Cost](cost.md) section and the [Manually deleting retained resources](manually-deleting-retained-resources.md) section of this guide.

## User management
<a name="user-management"></a>

During initial configuration, you provide a username and email address that Amazon Cognito uses to grant you access to the solution’s web console. The console does not provide user administration. To add additional users, you must use the Amazon Cognito console. For more information, refer to [Managing Users in User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html) in the *Amazon Cognito Developer Guide*.

For migrating existing users to Amazon Cognito user pools, refer to the AWS blog [Approaches for migrating users to Amazon Cognito user pools](https://aws.amazon.com/blogs/security/approaches-for-migrating-users-to-amazon-cognito-user-pools).

## Identity provider federation
<a name="identity-provider-federation"></a>

The solution’s Amazon Cognito user pool supports federation with external identity providers (IdPs) using SAML 2.0 or OpenID Connect (OIDC) protocols. Federation allows users to sign in to the web console using their existing corporate or organizational credentials instead of Cognito-native credentials. Federated users receive the same access permissions as users created directly in the Cognito user pool.

The solution already deploys the Cognito user pool, domain, app client, and hosted UI. To enable federation, you only need to register your identity provider and enable it on the existing app client.

If you deploy the optional MCP Server integration, federated users can also access the MCP Server using the same Cognito user pool credentials.

### Prerequisites
<a name="prerequisites"></a>

Before configuring federation, you need the following:
+ An external identity provider that supports SAML 2.0 or OIDC
+ Admin access to configure the external IdP (to set redirect URIs or ACS URLs)
+ The solution’s Cognito user pool ID (available in the CloudFormation stack resources or the Amazon Cognito console)
+ The solution’s Cognito domain prefix (available in the CloudFormation stack outputs or the Cognito console under **App integration** > **Domain**)

 **Step 1: Configure your identity provider**

Configure your external identity provider with the following values so that it can communicate with the solution’s Cognito user pool.

For SAML identity providers:
+ SP entity ID: `urn:amazon:cognito:sp:_<UserPoolId>_`
+ ACS URL: `\https://<cognito-domain>.auth.<region>.amazoncognito.com/saml2/idpresponse`

For OIDC identity providers:
+ Redirect URI: `\https://<cognito-domain>.auth.<region>.amazoncognito.com/oauth2/idpresponse`

For details on what your IdP needs, refer to [Adding SAML identity providers to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html) or [Adding OIDC identity providers to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html) in the *Amazon Cognito Developer Guide*.

 **Step 2: Register the identity provider in Cognito**

Add your external identity provider to the solution’s existing Cognito user pool using the Amazon Cognito console.

For step-by-step instructions, refer to [Adding user pool sign-in through a third party](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-provider.html) in the *Amazon Cognito Developer Guide*.

 **Step 3: Configure attribute mappings**

Configure attribute mappings between your identity provider’s claims and the Cognito user pool attributes. At a minimum, map the user’s email claim from the external provider to the Cognito `email` attribute. Consider also mapping `name` or `nickname` if your identity provider supplies them.

For instructions, refer to [Specifying identity provider attribute mappings for your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html) in the *Amazon Cognito Developer Guide*.

 **Step 4: Enable the identity provider on the app client**

In the Amazon Cognito console, find the app client created by the solution and enable your new identity provider under the hosted UI settings.

For instructions, refer to [Configuring a user pool app client](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-integration.html) in the *Amazon Cognito Developer Guide*.

**Note**
The solution already configures the app client’s callback and sign-out URLs, OAuth scopes, and hosted UI domain. You do not need to modify these settings — only enable your identity provider on the existing app client.

**Important**
The solution intentionally omits the `SupportedIdentityProviders` property from the CloudFormation app client configuration. This allows you to add identity providers post-deployment without triggering CloudFormation drift detection. If this property were set in the template, any manual IdP changes through the console or CLI would be overwritten on the next stack update, reverting the app client to only the providers listed in the template.
Because this property is omitted, CloudFormation does not track or manage which identity providers are enabled on the app client. After you configure federation, you are responsible for managing the contents of `SupportedIdentityProviders` on the app client. To monitor for unauthorized changes, enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) logging and create [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html) to alert on `CreateIdentityProvider` and `UpdateUserPoolClient` API calls targeting the solution’s Cognito user pool.

**Note**
Adding an external identity provider does not remove the ability for existing Cognito-native users to sign in with their current credentials.
Federated users are subject to the same regional availability constraints as the Cognito user pool. For more information, refer to [Regional deployment](#regional-deployment).
Test federated sign-in with a small group of users before rolling it out to your organization.

### Disabling or deleting the default Cognito user
<a name="disabling-or-deleting-the-default-cognito-user"></a>

After configuring federation, you may want to disable or delete the default user that was created during stack deployment. This is optional — the default user continues to work alongside federated sign-in.

To disable a user, navigate to the solution’s Cognito user pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), select the **Users** tab, choose the user, and select **Disable user access**. To delete a user, you must first disable them, then choose **Delete user**. Disabling a user revokes their tokens and prevents sign-in while preserving the account; deleting permanently removes it.

For more details, refer to [Managing and searching for user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html) in the *Amazon Cognito Developer Guide*.

## Regional deployment
<a name="regional-deployment"></a>

This solution uses Amazon Cognito which is available in specific AWS Regions only. Therefore, you must deploy this solution in a Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
