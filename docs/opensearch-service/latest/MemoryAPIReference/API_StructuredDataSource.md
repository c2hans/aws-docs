---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_StructuredDataSource.html
---

# StructuredDataSource
<a name="API_StructuredDataSource"></a>

The source of structured content. Set exactly one member. Currently, the only member is `json`.

## Contents
<a name="API_StructuredDataSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="opensearchmemory-Type-StructuredDataSource-json"></a>
The structured content, as a JSON object of at most 1 MiB when serialized as UTF-8, nested at most 10 levels deep.
Type: JSON value
Required: No

## See Also
<a name="API_StructuredDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/StructuredDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/StructuredDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/StructuredDataSource)
