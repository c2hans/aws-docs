---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutRawEventsResultEntry.html
---

# PutRawEventsResultEntry
<a name="API_PutRawEventsResultEntry"></a>

Result entry for a published event. The position of each entry in the response list aligns 1:1 with the corresponding request entry, enabling co-location by index.

## Contents
<a name="API_PutRawEventsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridgev2-Type-PutRawEventsResultEntry-ErrorCode"></a>
Error code if the entry failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ErrorMessage **   <a name="eventbridgev2-Type-PutRawEventsResultEntry-ErrorMessage"></a>
Error message if the entry failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** EventId **   <a name="eventbridgev2-Type-PutRawEventsResultEntry-EventId"></a>
Unique event ID assigned by the service. Present on successful entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SequenceNumber **   <a name="eventbridgev2-Type-PutRawEventsResultEntry-SequenceNumber"></a>
Sequence number for ordering within the event group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SuccessCode **   <a name="eventbridgev2-Type-PutRawEventsResultEntry-SuccessCode"></a>
Indicates how the entry was processed. Present only on successful entries.
Type: String
Valid Values: `PUBLISHED | DEDUPLICATED`
Required: No

## See Also
<a name="API_PutRawEventsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutRawEventsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutRawEventsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutRawEventsResultEntry)
