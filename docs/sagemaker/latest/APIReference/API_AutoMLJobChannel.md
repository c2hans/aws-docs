---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html
---

# AutoMLJobChannel
<a name="API_AutoMLJobChannel"></a>

A channel is a named input source that training algorithms can consume. This channel is used for AutoML jobs V2 (jobs created by calling [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)).

## Contents
<a name="API_AutoMLJobChannel_Contents"></a>

 ** ChannelType **   <a name="sagemaker-Type-AutoMLJobChannel-ChannelType"></a>
The type of channel. Defines whether the data are used for training or validation. The default value is `training`. Channels for `training` and `validation` must share the same `ContentType`
The type of channel defaults to `training` for the time-series forecasting problem type.
Type: String
Valid Values: `training | validation`
Required: No

 ** CompressionType **   <a name="sagemaker-Type-AutoMLJobChannel-CompressionType"></a>
The allowed compression types depend on the input format and problem type. We allow the compression type `Gzip` for `S3Prefix` inputs on tabular data only. For all other inputs, the compression type should be `None`. If no compression type is provided, we default to `None`.
Type: String
Valid Values: `None | Gzip`
Required: No

 ** ContentType **   <a name="sagemaker-Type-AutoMLJobChannel-ContentType"></a>
The content type of the data from the input source. The following are the allowed content types for different problems:
+ For tabular problem types: `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
+ For image classification: `image/png`, `image/jpeg`, or `image/*`. The default value is `image/*`.
+ For text classification: `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
+ For time-series forecasting: `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
+ For text generation (LLMs fine-tuning): `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** DataSource **   <a name="sagemaker-Type-AutoMLJobChannel-DataSource"></a>
The data source for an AutoML channel (Required).
Type: [AutoMLDataSource](API_AutoMLDataSource.md) object
Required: No

## See Also
<a name="API_AutoMLJobChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLJobChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLJobChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLJobChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
