---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_Tag.html
---

# Tag
<a name="API_S3Files_Tag"></a>

A key-value pair for resource tagging.

## Contents
<a name="API_S3Files_Tag_Contents"></a>

 ** key **   <a name="AmazonS3-Type-S3Files_Tag-key"></a>
The tag key. The key can't start with `aws:`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Required: Yes

 ** value **   <a name="AmazonS3-Type-S3Files_Tag-value"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## See Also
<a name="API_S3Files_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/Tag)
