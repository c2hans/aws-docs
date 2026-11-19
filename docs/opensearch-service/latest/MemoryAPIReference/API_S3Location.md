---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_S3Location.html
---

# S3Location

An object in Amazon S3.

## Contents
<a name="API_S3Location_Contents"></a>

 ** uri **   <a name="opensearchmemory-Type-S3Location-uri"></a>
The object's S3 URI, for example `s3://bucket/key`. The bucket must be in the space's Region. You need `s3:GetObject` on the object, and `kms:Decrypt` on its key if the object uses SSE-KMS. The event doesn't store the object itself.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1024.
Pattern: `s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]/.+`
Required: Yes

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/S3Location)
