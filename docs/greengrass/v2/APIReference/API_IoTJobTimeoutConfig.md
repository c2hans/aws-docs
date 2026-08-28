---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobTimeoutConfig.html
---

# IoTJobTimeoutConfig
<a name="API_IoTJobTimeoutConfig"></a>

Contains information about the timeout configuration for a job.

## Contents
<a name="API_IoTJobTimeoutConfig_Contents"></a>

 ** inProgressTimeoutInMinutes **   <a name="greengrassv2-Type-IoTJobTimeoutConfig-inProgressTimeoutInMinutes"></a>
The amount of time, in minutes, that devices have to complete the job. The timer starts when the job status is set to `IN_PROGRESS`. If the job status doesn't change to a terminal state before the time expires, then the job status is set to `TIMED_OUT`.
The timeout interval must be between 1 minute and 7 days (10080 minutes).
Type: Long
Required: No

## See Also
<a name="API_IoTJobTimeoutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/IoTJobTimeoutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/IoTJobTimeoutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/IoTJobTimeoutConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
