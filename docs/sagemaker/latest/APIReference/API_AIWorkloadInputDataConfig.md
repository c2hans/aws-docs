---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIWorkloadInputDataConfig.html
---

# AIWorkloadInputDataConfig
<a name="API_AIWorkloadInputDataConfig"></a>

A channel of input data for an AI workload configuration. Each channel has a name and a data source.

## Contents
<a name="API_AIWorkloadInputDataConfig_Contents"></a>

 ** ChannelName **   <a name="sagemaker-Type-AIWorkloadInputDataConfig-ChannelName"></a>
The logical name for the data channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** DataSource **   <a name="sagemaker-Type-AIWorkloadInputDataConfig-DataSource"></a>
The data source for this channel.
Type: [AIWorkloadDataSource](API_AIWorkloadDataSource.md) object
Required: Yes

## See Also
<a name="API_AIWorkloadInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIWorkloadInputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIWorkloadInputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIWorkloadInputDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
