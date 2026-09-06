---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HistoryRecordEntry.html
---

# HistoryRecordEntry
<a name="API_HistoryRecordEntry"></a>

Describes an event in the history of an EC2 Fleet.

## Contents
<a name="API_HistoryRecordEntry_Contents"></a>

 ** eventInformation **
Information about the event.
Type: [EventInformation](API_EventInformation.md) object
Required: No

 ** eventType **
The event type.
Type: String
Valid Values: `instance-change | fleet-change | service-error`
Required: No

 ** timestamp **
The date and time of the event, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
Type: Timestamp
Required: No

## See Also
<a name="API_HistoryRecordEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HistoryRecordEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HistoryRecordEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HistoryRecordEntry)
