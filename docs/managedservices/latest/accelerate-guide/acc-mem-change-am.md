---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-change-am.html
---

# Changing the Accelerate alarm configuration
<a name="acc-mem-change-am"></a>

To add or update new alarm definitions, you can either deploy configuration document [Using CloudFormation to deploy Accelerate configuration changes](acc-mem-deploy-change-cfn.md), or invoke the [CreateHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html) API.

This is a Linux command line command that generates the parameter value in base64, which is what the AppConfig CLI command expects. For information, see the AWS CLI documentation, [Binary/Blob (binary large object)](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-blob).

As an example:

```
aws appconfig create-hosted-configuration-version --application-id {{application-id}} --configuration-profile-id {{configuration-profile-id}} --content {{base64-string}}
      --content-type application/json
```
+ **Application ID:** ID of the application AMS AlarmManager; you can find this out with the [ListApplications](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListApplications.html) API call.
+ **Configuration Profile ID**: ID of the configuration CustomerManagedAlarms; you can find this out with the [ListConfigurationProfiles](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.html) API call.
+ **Content**: Base64 string of the content, to be created by creating a document and encoding it in base64: cat alarms-v2.json \| base64 (see [Binary/Blob (binary large object)](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-blob)).

  **Content Type**: MIME type, `application/json` because alarm definitions are written in JSON.

**Important**
Restrict access to the [StartDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StartDeployment.html) and [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html) API actions to trusted users who understand the responsibilities and consequences of deploying a new configuration to your targets.

To learn more about how to use AWS AppConfig features to create and deploy a configuration, see [Working with AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-working.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
