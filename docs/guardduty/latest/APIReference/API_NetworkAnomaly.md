---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkAnomaly.html
---

# NetworkAnomaly
<a name="API_NetworkAnomaly"></a>

Contains information about how network activity deviates from normal behavior.

## Contents
<a name="API_NetworkAnomaly_Contents"></a>

 ** baselineBytes **   <a name="guardduty-Type-NetworkAnomaly-baselineBytes"></a>
The amount of data that is typical for the normal behavior.
Type: String
Required: No

 ** deviation **   <a name="guardduty-Type-NetworkAnomaly-deviation"></a>
How much the activity deviates from normal behavior.
Type: String
Required: No

 ** duration **   <a name="guardduty-Type-NetworkAnomaly-duration"></a>
The duration of the activity.
Type: String
Required: No

 ** profileAgeDays **   <a name="guardduty-Type-NetworkAnomaly-profileAgeDays"></a>
The number of days of activity that the normal behavior is based on.
Type: Integer
Required: No

 ** remoteRegion **   <a name="guardduty-Type-NetworkAnomaly-remoteRegion"></a>
The Region of the remote endpoint.
Type: String
Required: No

 ** remoteService **   <a name="guardduty-Type-NetworkAnomaly-remoteService"></a>
The remote service that the activity involved.
Type: String
Required: No

 ** resetRatio **   <a name="guardduty-Type-NetworkAnomaly-resetRatio"></a>
The ratio of connection attempts that were reset.
Type: String
Required: No

 ** targetHostCount **   <a name="guardduty-Type-NetworkAnomaly-targetHostCount"></a>
The number of target hosts.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_NetworkAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkAnomaly)
