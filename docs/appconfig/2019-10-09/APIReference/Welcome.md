---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## AWS AppConfig
<a name="Welcome_Amazon_AppConfig"></a>

 AWS AppConfig helps you safely change application behavior in production without redeploying code. Using feature flags and dynamic free-form configurations, you can control how your application runs in real time. This approach reduces risk, accelerates releases, and enables faster responses to issues. You can gradually roll out new features to specific users, monitor their impact, and expand availability with confidence. You can also update block lists, allow lists, throttling limits, and logging levels instantly, allowing you to mitigate issues and fine-tune performance without a deployment.

 AWS AppConfig supports a broad spectrum of use cases:
+  **Feature flags and toggles** – Gradually release new capabilities to targeted users, monitor impact, and instantly roll back changes if issues occur.
+  **Application tuning** – Introduce changes safely in production, measure their effects, and refine behavior without redeploying code.
+  **Allow list or block list** – Control access to features or restrict specific users in real time, without modifying application code.
+  **Centralized configuration storage** – Manage configuration data consistently across workloads. AWS AppConfig can deploy configuration from the AWS AppConfig hosted configuration store, AWS Secrets Manager, Systems Manager, Systems Manager Parameter Store, or Amazon S3.

 **How AWS AppConfig works**

This section provides a high-level description of how AWS AppConfig works and how you get started.

1. Identify configuration data to manage in AWS AppConfig
Before creating a configuration profile, identify the configuration data in your code that you want to manage dynamically using AWS AppConfig. Common examples include feature flags, allow and block lists, logging levels, service limits, and throttling rules. These values tend to change frequently and can cause issues if misconfigured.
If your configuration data already exists in cloud services such as Systems Manager Parameter Store or Amazon S3, you can use AWS AppConfig to validate, deploy, and manage that data more effectively.

2. Create a configuration profile in AWS AppConfig
A configuration profile defines how AWS AppConfig locates and manages your configuration data. It includes a URI that points to the data source and a profile type.
 AWS AppConfig supports two profile types
+  **Feature flags** – Enable controlled feature releases, gradual rollouts, and testing in production.
+  **Free-form configurations** – Store and retrieve configuration data from external sources and update it without redeploying code.
Both profile types help decouple configuration from code, support continuous delivery, and reduce deployment risk.
You can also add optional validators to ensure that configuration data is syntactically and semantically correct. During deployment, AWS AppConfig evaluates these validators and automatically rolls back changes if validation fails.
Each configuration profile is associated with an application, which acts as a logical container for your configuration resources. For more information about creating a configuration profile, see [Creating a configuration profile in AWS AppConfig](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html) in the the * AWS AppConfig User Guide*.

3. Deploy configuration data
When you start a deployment, AWS AppConfig:

1. Retrieves configuration data from the source defined in the configuration profile

1. Validates the data using the configured validators

1. Delivers the validated configuration to AWS AppConfig Agent
The delivered configuration becomes the deployed version used by your application. For more information about deploying a configuration, see [Deploying feature flags and configuration data in AWS AppConfig](http://docs.aws.amazon.com/appconfig/latest/userguide/deploying-feature-flags.html).

4. Retrieve configuration data
Your application retrieves configuration data by calling a local endpoint exposed by AWS AppConfig Agent, which caches the deployed configuration. Retrieving data is a metered event. AWS AppConfig Agent supports a variety of use cases, as described in [How to use AWS AppConfig Agent to retrieve configuration data](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html).
If the agent is not suitable for your use case, your application can retrieve configuration data directly from AWS AppConfig by calling the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html) and [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) API actions.
For more information about retrieving a configuration, see [Retrieving feature flags and configuration data in AWS AppConfig](http://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html).

This reference is intended to be used with the [AWS AppConfig User Guide](http://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html).

## AWS AppConfig Data
<a name="Welcome_AWS_AppConfig_Data"></a>

 AWS AppConfig Data provides the data plane APIs your application uses to retrieve configuration data. Here's how it works:

Your application retrieves configuration data by first establishing a configuration session using the AWS AppConfig Data [StartConfigurationSession](API_appconfigdata_StartConfigurationSession.md) API action. Your session's client then makes periodic calls to [GetLatestConfiguration](API_appconfigdata_GetLatestConfiguration.md) to check for and retrieve the latest data available.

When calling `StartConfigurationSession`, your code sends the following information:
+ Identifiers (ID or name) of an AWS AppConfig application, environment, and configuration profile that the session tracks.
+ (Optional) The minimum amount of time the session's client must wait between calls to `GetLatestConfiguration`.

In response, AWS AppConfig provides an `InitialConfigurationToken` to be given to the session's client and used the first time it calls `GetLatestConfiguration` for that session.

**Important**
This token should only be used once in your first call to `GetLatestConfiguration`. You *must* use the new token in the `GetLatestConfiguration` response (`NextPollConfigurationToken`) in each subsequent call to `GetLatestConfiguration`.

When calling `GetLatestConfiguration`, your client code sends the most recent `ConfigurationToken` value it has and receives in response:
+  `NextPollConfigurationToken`: the `ConfigurationToken` value to use on the next call to `GetLatestConfiguration`.
+  `NextPollIntervalInSeconds`: the duration the client should wait before making its next call to `GetLatestConfiguration`. This duration may vary over the course of the session, so it should be used instead of the value sent on the `StartConfigurationSession` call.
+ The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration.

**Important**
The `InitialConfigurationToken` and `NextPollConfigurationToken` should only be used once. To support long poll use cases, the tokens are valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException`.

For more information and to view example AWS CLI commands that show how to retrieve a configuration using the AWS AppConfig Data `StartConfigurationSession` and `GetLatestConfiguration` API actions, see [Retrieving feature flags and configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html) in the * AWS AppConfig User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
