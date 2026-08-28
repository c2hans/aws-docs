---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ScheduledUpdateConfig.html
---

# ScheduledUpdateConfig
<a name="API_ScheduledUpdateConfig"></a>

The configuration object of the schedule that SageMaker follows when updating the AMI.

## Contents
<a name="API_ScheduledUpdateConfig_Contents"></a>

 ** ScheduleExpression **   <a name="sagemaker-Type-ScheduledUpdateConfig-ScheduleExpression"></a>
A cron expression that specifies the schedule that SageMaker follows when updating the AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** DeploymentConfig **   <a name="sagemaker-Type-ScheduledUpdateConfig-DeploymentConfig"></a>
The configuration to use when updating the AMI versions.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

## See Also
<a name="API_ScheduledUpdateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ScheduledUpdateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ScheduledUpdateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ScheduledUpdateConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
