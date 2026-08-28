---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TotalResourceUtilization.html
---

# TotalResourceUtilization
<a name="API_TotalResourceUtilization"></a>

The aggregate vCPU, memory, and storage resources used from the time job start executing till the time job is terminated, rounded up to the nearest second.

## Contents
<a name="API_TotalResourceUtilization_Contents"></a>

 ** memoryGBHour **   <a name="emrserverless-Type-TotalResourceUtilization-memoryGBHour"></a>
The aggregated memory used per hour from the time job start executing till the time job is terminated.
Type: Double
Required: No

 ** storageGBHour **   <a name="emrserverless-Type-TotalResourceUtilization-storageGBHour"></a>
The aggregated storage used per hour from the time job start executing till the time job is terminated.
Type: Double
Required: No

 ** vCPUHour **   <a name="emrserverless-Type-TotalResourceUtilization-vCPUHour"></a>
The aggregated vCPU used per hour from the time job start executing till the time job is terminated.
Type: Double
Required: No

## See Also
<a name="API_TotalResourceUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/TotalResourceUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/TotalResourceUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/TotalResourceUtilization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
