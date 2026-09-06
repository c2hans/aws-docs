---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AdditionalModelDataSource.html
---

# AdditionalModelDataSource
<a name="API_AdditionalModelDataSource"></a>

Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.

## Contents
<a name="API_AdditionalModelDataSource_Contents"></a>

 ** ChannelName **   <a name="sagemaker-Type-AdditionalModelDataSource-ChannelName"></a>
A custom name for this `AdditionalModelDataSource` object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** S3DataSource **   <a name="sagemaker-Type-AdditionalModelDataSource-S3DataSource"></a>
Specifies the S3 location of ML model data to deploy.
Type: [S3ModelDataSource](API_S3ModelDataSource.md) object
Required: Yes

## See Also
<a name="API_AdditionalModelDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AdditionalModelDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AdditionalModelDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AdditionalModelDataSource)
