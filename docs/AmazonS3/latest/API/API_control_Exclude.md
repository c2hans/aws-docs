---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Exclude.html
---

# Exclude
<a name="API_control_Exclude"></a>

A container for what Amazon S3 Storage Lens will exclude.

## Contents
<a name="API_control_Exclude_Contents"></a>

 ** Buckets **   <a name="AmazonS3-Type-control_Exclude-Buckets"></a>
A container for the S3 Storage Lens bucket excludes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[^:]+:s3:.*`
Required: No

 ** Regions **   <a name="AmazonS3-Type-control_Exclude-Regions"></a>
A container for the S3 Storage Lens Region excludes.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z0-9\-]+`
Required: No

## See Also
<a name="API_control_Exclude_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Exclude)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Exclude)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Exclude)
