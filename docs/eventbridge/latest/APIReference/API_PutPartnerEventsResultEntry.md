---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEventsResultEntry.html
---

# PutPartnerEventsResultEntry
<a name="API_PutPartnerEventsResultEntry"></a>

The result of an event entry the partner submitted in this request. If the event was successfully submitted, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

## Contents
<a name="API_PutPartnerEventsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridge-Type-PutPartnerEventsResultEntry-ErrorCode"></a>
The error code that indicates why the event submission failed.
Type: String
Required: No

 ** ErrorMessage **   <a name="eventbridge-Type-PutPartnerEventsResultEntry-ErrorMessage"></a>
The error message that explains why the event submission failed.
Type: String
Required: No

 ** EventId **   <a name="eventbridge-Type-PutPartnerEventsResultEntry-EventId"></a>
The ID of the event.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_PutPartnerEventsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutPartnerEventsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutPartnerEventsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutPartnerEventsResultEntry)
