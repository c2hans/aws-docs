---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_DeduplicationConfiguration.html
---

# DeduplicationConfiguration
<a name="API_DeduplicationConfiguration"></a>

Deduplication settings for a publish request.

## Contents
<a name="API_DeduplicationConfiguration_Contents"></a>

 ** DeduplicationType **   <a name="eventbridgev2-Type-DeduplicationConfiguration-DeduplicationType"></a>
How duplicate events are detected: by a hash of the event content (CONTENT\_BASED). To deduplicate by a caller-supplied token instead, omit DeduplicationConfiguration and set DeduplicationId on each entry.
Type: String
Valid Values: `CONTENT_BASED`
Required: Yes

## See Also
<a name="API_DeduplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/DeduplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/DeduplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/DeduplicationConfiguration)
