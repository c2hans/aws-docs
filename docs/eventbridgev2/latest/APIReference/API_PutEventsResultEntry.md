---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEventsResultEntry.html
---

# PutEventsResultEntry
<a name="API_PutEventsResultEntry"></a>

Result entry for a published event. The position of each entry in the response list aligns 1:1 with the corresponding request entry.

## Contents
<a name="API_PutEventsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridgev2-Type-PutEventsResultEntry-ErrorCode"></a>
Error code if the entry failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ErrorMessage **   <a name="eventbridgev2-Type-PutEventsResultEntry-ErrorMessage"></a>
Error message if the entry failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** EventId **   <a name="eventbridgev2-Type-PutEventsResultEntry-EventId"></a>
Unique event ID assigned by the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SequenceNumber **   <a name="eventbridgev2-Type-PutEventsResultEntry-SequenceNumber"></a>
Sequence number assigned to the message for ordering within the message group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SuccessCode **   <a name="eventbridgev2-Type-PutEventsResultEntry-SuccessCode"></a>
Indicates the outcome for a successfully processed publish entry.
Type: String
Valid Values: `PUBLISHED | DEDUPLICATED`
Required: No

## See Also
<a name="API_PutEventsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutEventsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutEventsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutEventsResultEntry)
