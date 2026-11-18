---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BlobPayload.html
---

# BlobPayload
<a name="API_BlobPayload"></a>

A document stored in Amazon S3, such as a PDF, PNG, or JPEG file, and its media type.

## Contents
<a name="API_BlobPayload_Contents"></a>

 ** contentType **   <a name="opensearchmemory-Type-BlobPayload-contentType"></a>
The document's media type: `application/pdf`, `image/png`, or `image/jpeg`. Any other value fails with `ValidationException`.
Type: String
Valid Values: `application/pdf | image/png | image/jpeg`
Required: Yes

 ** source **   <a name="opensearchmemory-Type-BlobPayload-source"></a>
The location of the document.
Type: [BlobSource](API_BlobSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_BlobPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/BlobPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/BlobPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/BlobPayload)
