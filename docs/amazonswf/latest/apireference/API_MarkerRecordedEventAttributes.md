---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_MarkerRecordedEventAttributes.html
---

# MarkerRecordedEventAttributes
<a name="API_MarkerRecordedEventAttributes"></a>

Provides the details of the `MarkerRecorded` event.

## Contents
<a name="API_MarkerRecordedEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-MarkerRecordedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RecordMarker` decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** markerName **   <a name="SWF-Type-MarkerRecordedEventAttributes-markerName"></a>
The name of the marker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** details **   <a name="SWF-Type-MarkerRecordedEventAttributes-details"></a>
The details of the marker.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_MarkerRecordedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/MarkerRecordedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/MarkerRecordedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/MarkerRecordedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
