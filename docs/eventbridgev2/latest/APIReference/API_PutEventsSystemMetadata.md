---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEventsSystemMetadata.html
---

# PutEventsSystemMetadata
<a name="API_PutEventsSystemMetadata"></a>

System metadata for PutEvents entries. ContentType is not applicable (always application/eventbridge\+json, set server-side).

## Contents
<a name="API_PutEventsSystemMetadata_Contents"></a>

 ** DeduplicationId **   <a name="eventbridgev2-Type-PutEventsSystemMetadata-DeduplicationId"></a>
Deduplication ID for FIFO deduplication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*[^\u0009-\u000D\u001C-\u0020\u1680\u2000-\u2006\u2008-\u200A\u2028\u2029\u205F\u3000][\s\S]*`
Required: No

 ** EventGroupId **   <a name="eventbridgev2-Type-PutEventsSystemMetadata-EventGroupId"></a>
Event group ID for FIFO ordering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_PutEventsSystemMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutEventsSystemMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutEventsSystemMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutEventsSystemMetadata)
