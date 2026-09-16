---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSourceEvent.html
---

# TestRunSourceEvent
<a name="API_TestRunSourceEvent"></a>

A state-change event observed for a test run monitoring source.

## Contents
<a name="API_TestRunSourceEvent_Contents"></a>

 ** detail **   <a name="ngresiliencehub-Type-TestRunSourceEvent-detail"></a>
The event payload.
Type: [TestRunSourceEventDetail](API_TestRunSourceEventDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** eventType **   <a name="ngresiliencehub-Type-TestRunSourceEvent-eventType"></a>
The type of the event. ALARM indicates an event from a CloudWatch alarm source; the detail member carries either the alarm state change or a collection error.
Type: String
Valid Values: `ALARM`
Required: Yes

 ** sourceArn **   <a name="ngresiliencehub-Type-TestRunSourceEvent-sourceArn"></a>
The ARN of the monitoring source the event belongs to.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 1024.
Pattern: `arn:aws[a-zA-Z-]*:[a-z][a-z0-9-]*:[a-z]{2}(-[a-z]+)+-\d{1}:\d{12}:.+`
Required: Yes

 ** timestamp **   <a name="ngresiliencehub-Type-TestRunSourceEvent-timestamp"></a>
The timestamp when the event occurred.
Type: Timestamp
Required: Yes

## See Also
<a name="API_TestRunSourceEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSourceEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSourceEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSourceEvent)
