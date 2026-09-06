---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobS3DataSource.html
---

# LabelingJobS3DataSource
<a name="API_LabelingJobS3DataSource"></a>

The Amazon S3 location of the input data objects.

## Contents
<a name="API_LabelingJobS3DataSource_Contents"></a>

 ** ManifestS3Uri **   <a name="sagemaker-Type-LabelingJobS3DataSource-ManifestS3Uri"></a>
The Amazon S3 location of the manifest file that describes the input data objects.
The input manifest file referenced in `ManifestS3Uri` must contain one of the following keys: `source-ref` or `source`. The value of the keys are interpreted as follows:
+  `source-ref`: The source of the object is the Amazon S3 object specified in the value. Use this value when the object is a binary object, such as an image.
+  `source`: The source of the object is the value. Use this value when the object is a text value.
If you are a new user of Ground Truth, it is recommended you review [Use an Input Manifest File ](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-input-data-input-manifest.html) in the Amazon SageMaker Developer Guide to learn how to create an input manifest file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_LabelingJobS3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobS3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobS3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobS3DataSource)
