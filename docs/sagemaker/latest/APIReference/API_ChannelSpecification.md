---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ChannelSpecification.html
---

# ChannelSpecification
<a name="API_ChannelSpecification"></a>

Defines a named input source, called a channel, to be used by an algorithm.

## Contents
<a name="API_ChannelSpecification_Contents"></a>

 ** Name **   <a name="sagemaker-Type-ChannelSpecification-Name"></a>
The name of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** SupportedContentTypes **   <a name="sagemaker-Type-ChannelSpecification-SupportedContentTypes"></a>
The supported MIME types for the data.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** SupportedInputModes **   <a name="sagemaker-Type-ChannelSpecification-SupportedInputModes"></a>
The allowed input mode, either FILE or PIPE.
In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.
In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `Pipe | File | FastFile`
Required: Yes

 ** Description **   <a name="sagemaker-Type-ChannelSpecification-Description"></a>
A brief description of the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** IsRequired **   <a name="sagemaker-Type-ChannelSpecification-IsRequired"></a>
Indicates whether the channel is required by the algorithm.
Type: Boolean
Required: No

 ** SupportedCompressionTypes **   <a name="sagemaker-Type-ChannelSpecification-SupportedCompressionTypes"></a>
The allowed compression types, if data compression is used.
Type: Array of strings
Valid Values: `None | Gzip`
Required: No

## See Also
<a name="API_ChannelSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ChannelSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ChannelSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ChannelSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
