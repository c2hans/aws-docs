---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SchedulerConfiguration.html
---

# SchedulerConfiguration
<a name="API_SchedulerConfiguration"></a>

The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.

## Contents
<a name="API_SchedulerConfiguration_Contents"></a>

 ** maxConcurrentRuns **   <a name="emrserverless-Type-SchedulerConfiguration-maxConcurrentRuns"></a>
The maximum concurrent job runs on this application. If scheduler configuration is enabled on your application, the default value is 15. The valid range is 1 to 1000.
Type: Integer
Required: No

 ** queueTimeoutMinutes **   <a name="emrserverless-Type-SchedulerConfiguration-queueTimeoutMinutes"></a>
The maximum duration in minutes for the job in QUEUED state. If scheduler configuration is enabled on your application, the default value is 360 minutes (6 hours). The valid range is from 15 to 720.
Type: Integer
Required: No

## See Also
<a name="API_SchedulerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/SchedulerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/SchedulerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/SchedulerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
