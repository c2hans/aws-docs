---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BlobSource.html
---

# BlobSource
<a name="API_BlobSource"></a>

The source of a blob's content. Set exactly one member. Currently, the only member is `s3Location`.

## Contents
<a name="API_BlobSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3Location **   <a name="opensearchmemory-Type-BlobSource-s3Location"></a>
The S3 object holding the document.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_BlobSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/BlobSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/BlobSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/BlobSource)
