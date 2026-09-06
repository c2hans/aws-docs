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

Distributed Load Testing on AWS supports multiple test types: simple HTTP endpoint tests, JMeter, k6, and Locust.

**Note**
The solution distributes JMeter, k6, and Locust as third-party components without modification. For security considerations, patching options, and license information, refer to [Third-party testing frameworks](security-1.md#third-party-testing-frameworks).

### Simple HTTP endpoint tests
<a name="single-http-support"></a>

The web console provides an HTTP Endpoint Configuration interface that allows you to test any HTTP or HTTPS endpoint without writing custom scripts. You define the endpoint URL, select the HTTP method (GET, POST, PUT, DELETE, etc.) from a dropdown menu, and optionally add custom request headers and body payloads. This configuration enables you to test APIs with custom authorization tokens, content types, or any other HTTP headers and request bodies required by your application.

When you configure an HTTP endpoint, the solution converts your configuration into a test plan that is executed by the bundled Apache JMeter binary through the Taurus framework. Simple HTTP Endpoint tests do not accept a test archive, so they cannot override the bundled JMeter binary or plugins. If you need to run HTTP endpoint tests with a patched JMeter, use the [JMeter](#jmeter-script-support) test type instead. For security considerations, refer to [Apache JMeter](security-1.md#jmeter-security).

### JMeter tests
<a name="jmeter-script-support"></a>

When creating a test scenario using the web console, you can upload a JMeter test script. The solution uploads the script to the scenarios S3 bucket. When Amazon ECS tasks run, they download the JMeter script from S3 and execute the test.

**Important**
Although your JMeter script might define concurrency (virtual users), transaction rates (TPS), ramp-up times, and other load parameters, the solution overrides these configurations with the values you specify in the Traffic Shape screen during test creation. The Traffic Shape configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.

If you have JMeter input files, you can zip the input files together with the JMeter script. You can choose the zip file when you create a test scenario.

If you would like to include plugins, any .jar files that are included in a /plugins subdirectory in the bundled zip file will be copied to the JMeter extensions directory and be available for load testing.

**Note**
If you include JMeter input files with your JMeter script file, you must include the relative path of the input files in your JMeter script file. In addition, the input files must be at the relative path. For example, when your JMeter input files and script file are in the /home/user directory and you refer to the input files in the JMeter script file, the path of input files must be ./INPUT\_FILES. If you use /home/user/INPUT\_FILES instead, the test will fail because it will not be able to find the input files.

If you include JMeter plugins, the .jar files must be bundled in a subdirectory named /plugins within the root of the zip file. Relative to the root of the zip file, the path to the jar files must be ./plugins/BUNDLED\_PLUGIN.jar.

For more information about how to use JMeter scripts, refer to [JMeter User’s Manual](https://jmeter.apache.org/usermanual/index.html).

### k6 tests
<a name="k6-script-support"></a>

The solution supports k6 framework-based testing. You can upload the k6 test file along with any necessary input files in an archive file. The web console displays a license acknowledgment message when you create a new k6 test; for license and security details, refer to [Grafana k6](security-1.md#k6-security).

**Important**
Although your k6 script might define concurrency (virtual users), stages, thresholds, and other load parameters, the solution overrides these configurations with the values you specify in the Traffic Shape screen during test creation. The Traffic Shape configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.

### Locust tests
<a name="locust-script-support"></a>

The solution supports Locust framework-based testing. You can upload the Locust test file along with any necessary input files in an archive file.

**Important**
Although your Locust script might define concurrency (user count), spawn rate, and other load parameters, the solution overrides these configurations with the values you specify in the Traffic Shape screen during test creation. The Traffic Shape configuration controls the task count, concurrency (virtual users per task), ramp-up duration, and hold duration for the test execution.

## Scheduling tests
<a name="scheduling-tests"></a>

The solution provides three execution timing options for running load tests:
+  **Run Now** - Execute the load test immediately after creation
+  **Run Once** - Execute the test on a specific date and time in the future
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

Subsequent runs of the same test scenario update the same dashboard, so your account contains one dashboard for each test scenario in each Region. These dashboards remain in your account after tests complete and incur a monthly charge until they are deleted. The solution deletes a scenario’s dashboards when you delete the test scenario (for example, through the web console); the dashboards are not deleted when you delete the solution’s CloudFormation stacks. For more information, refer to the [Cost](cost.md) section and the [Manually deleting retained resources](manually-deleting-retained-resources.md) section of this guide.

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

This solution uses Amazon Cognito which is available in specific AWS Regions only. Therefore, you must deploy this solution in a region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
