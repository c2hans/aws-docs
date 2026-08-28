---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentIoTJobConfiguration.html
---

# DeploymentIoTJobConfiguration
<a name="API_DeploymentIoTJobConfiguration"></a>

Contains information about an AWS IoT job configuration.

## Contents
<a name="API_DeploymentIoTJobConfiguration_Contents"></a>

 ** abortConfig **   <a name="greengrassv2-Type-DeploymentIoTJobConfiguration-abortConfig"></a>
The stop configuration for the job. This configuration defines when and how to stop a job rollout.
Type: [IoTJobAbortConfig](API_IoTJobAbortConfig.md) object
Required: No

 ** jobExecutionsRolloutConfig **   <a name="greengrassv2-Type-DeploymentIoTJobConfiguration-jobExecutionsRolloutConfig"></a>
The rollout configuration for the job. This configuration defines the rate at which the job rolls out to the fleet of target devices.
Type: [IoTJobExecutionsRolloutConfig](API_IoTJobExecutionsRolloutConfig.md) object
Required: No

 ** timeoutConfig **   <a name="greengrassv2-Type-DeploymentIoTJobConfiguration-timeoutConfig"></a>
The timeout configuration for the job. This configuration defines the amount of time each device has to complete the job.
Type: [IoTJobTimeoutConfig](API_IoTJobTimeoutConfig.md) object
Required: No

## See Also
<a name="API_DeploymentIoTJobConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DeploymentIoTJobConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DeploymentIoTJobConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DeploymentIoTJobConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
