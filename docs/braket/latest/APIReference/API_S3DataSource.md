---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_S3DataSource.html
---

# S3DataSource
<a name="API_S3DataSource"></a>

Information about the Amazon S3 storage used by the Amazon Braket hybrid job.

## Contents
<a name="API_S3DataSource_Contents"></a>

 ** s3Uri **   <a name="braket-Type-S3DataSource-s3Uri"></a>
Depending on the value specified for the `S3DataType`, identifies either a key name prefix or a manifest that locates the S3 data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_S3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/S3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/S3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/S3DataSource)
