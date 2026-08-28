---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html
---

# AutoMLChannel
<a name="API_AutoMLChannel"></a>

A channel is a named input source that training algorithms can consume. The validation dataset size is limited to less than 2 GB. The training dataset size must be less than 100 GB. For more information, see [ Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html).

**Note**
A validation dataset must contain the same headers as the training dataset.

## Contents
<a name="API_AutoMLChannel_Contents"></a>

 ** TargetAttributeName **   <a name="sagemaker-Type-AutoMLChannel-TargetAttributeName"></a>
The name of the target variable in supervised learning, usually represented by 'y'.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** ChannelType **   <a name="sagemaker-Type-AutoMLChannel-ChannelType"></a>
The channel type (optional) is an `enum` string. The default value is `training`. Channels for training and validation must share the same `ContentType` and `TargetAttributeName`. For information on specifying training and validation channel types, see [How to specify training and validation datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-data-sources-training-or-validation).
Type: String
Valid Values: `training | validation`
Required: No

 ** CompressionType **   <a name="sagemaker-Type-AutoMLChannel-CompressionType"></a>
You can use `Gzip` or `None`. The default value is `None`.
Type: String
Valid Values: `None | Gzip`
Required: No

 ** ContentType **   <a name="sagemaker-Type-AutoMLChannel-ContentType"></a>
The content type of the data from the input source. You can use `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** DataSource **   <a name="sagemaker-Type-AutoMLChannel-DataSource"></a>
The data source for an AutoML channel.
Type: [AutoMLDataSource](API_AutoMLDataSource.md) object
Required: No

 ** SampleWeightAttributeName **   <a name="sagemaker-Type-AutoMLChannel-SampleWeightAttributeName"></a>
If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see [Metrics and validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html).
Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.
Support for sample weights is available in [Ensembling](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) mode only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_AutoMLChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
