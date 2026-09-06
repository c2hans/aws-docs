---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InterruptionInfo.html
---

# InterruptionInfo
<a name="API_InterruptionInfo"></a>

 Contains information about how and when instances in an interruptible reservation can be terminated when capacity is reclaimed.

## Contents
<a name="API_InterruptionInfo_Contents"></a>

 ** interruptionType **
 The interruption type that determines how instances are terminated when capacity is reclaimed.
Type: String
Valid Values: `adhoc`
Required: No

 ** sourceCapacityReservationId **
 The ID of the source Capacity Reservation from which the interruptible reservation was created.
Type: String
Required: No

## See Also
<a name="API_InterruptionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InterruptionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InterruptionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InterruptionInfo)
