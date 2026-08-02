---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricsSource.html
---

# MetricsSource
<a name="API_MetricsSource"></a>

Details about the metrics source.

## Contents
<a name="API_MetricsSource_Contents"></a>

 ** ContentType **   <a name="sagemaker-Type-MetricsSource-ContentType"></a>
The metric source content type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-MetricsSource-S3Uri"></a>
The S3 URI for the metrics source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** ContentDigest **   <a name="sagemaker-Type-MetricsSource-ContentDigest"></a>
The hash key used for the metrics source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 72.
Pattern: `[Ss][Hh][Aa]256:[0-9a-fA-F]{64}`
Required: No

## See Also
<a name="API_MetricsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricsSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricsSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricsSource)
