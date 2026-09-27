---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutRawEventsSystemMetadata.html
---

# PutRawEventsSystemMetadata
<a name="API_PutRawEventsSystemMetadata"></a>

System metadata for PutRawEvents entries. ContentType is required because PutRawEvents supports arbitrary binary formats.

## Contents
<a name="API_PutRawEventsSystemMetadata_Contents"></a>

 ** ContentType **   <a name="eventbridgev2-Type-PutRawEventsSystemMetadata-ContentType"></a>
Content type of the event data (e.g., "application/cloudevents\+json").
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `application/.*`
Required: Yes

 ** DeduplicationId **   <a name="eventbridgev2-Type-PutRawEventsSystemMetadata-DeduplicationId"></a>
Deduplication ID for FIFO deduplication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*[^\u0009-\u000D\u001C-\u0020\u1680\u2000-\u2006\u2008-\u200A\u2028\u2029\u205F\u3000][\s\S]*`
Required: No

 ** EventGroupId **   <a name="eventbridgev2-Type-PutRawEventsSystemMetadata-EventGroupId"></a>
Event group ID for FIFO ordering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_PutRawEventsSystemMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutRawEventsSystemMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutRawEventsSystemMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutRawEventsSystemMetadata)
