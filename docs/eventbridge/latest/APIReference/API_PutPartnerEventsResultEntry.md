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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
