---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HistoryRecord.html
---

# HistoryRecord
<a name="API_HistoryRecord"></a>

Describes an event in the history of the Spot Fleet request.

## Contents
<a name="API_HistoryRecord_Contents"></a>

 ** eventInformation **
Information about the event.
Type: [EventInformation](API_EventInformation.md) object
Required: No

 ** eventType **
The event type.
+  `error` - An error with the Spot Fleet request.
+  `fleetRequestChange` - A change in the status or configuration of the Spot Fleet request.
+  `instanceChange` - An instance was launched or terminated.
+  `Information` - An informational event.
Type: String
Valid Values: `instanceChange | fleetRequestChange | error | information`
Required: No

 ** timestamp **
The date and time of the event, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
Type: Timestamp
Required: No

## See Also
<a name="API_HistoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HistoryRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HistoryRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HistoryRecord)
