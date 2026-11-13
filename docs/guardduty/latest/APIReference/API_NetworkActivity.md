---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkActivity.html
---

# NetworkActivity
<a name="API_NetworkActivity"></a>

Contains details about network activity.

## Contents
<a name="API_NetworkActivity_Contents"></a>

 ** anomaly **   <a name="guardduty-Type-NetworkActivity-anomaly"></a>
Details about how the network activity deviates from normal behavior.
Type: [NetworkAnomaly](API_NetworkAnomaly.md) object
Required: No

 ** blocked **   <a name="guardduty-Type-NetworkActivity-blocked"></a>
Indicates whether the network connection was blocked.
Type: String
Required: No

 ** counts **   <a name="guardduty-Type-NetworkActivity-counts"></a>
Counts that describe the network activity, such as the number of requests or connection attempts.
Type: [NetworkCounts](API_NetworkCounts.md) object
Required: No

 ** direction **   <a name="guardduty-Type-NetworkActivity-direction"></a>
The direction of the network connection, such as inbound or outbound.
Type: String
Required: No

 ** dns **   <a name="guardduty-Type-NetworkActivity-dns"></a>
DNS details about the network activity.
Type: [DnsContext](API_DnsContext.md) object
Required: No

 ** enrichment **   <a name="guardduty-Type-NetworkActivity-enrichment"></a>
Additional context about the network activity, such as geolocation and threat intelligence information.
Type: [Enrichment](API_Enrichment.md) object
Required: No

 ** method **   <a name="guardduty-Type-NetworkActivity-method"></a>
The method that the network activity used.
Type: String
Required: No

 ** platform **   <a name="guardduty-Type-NetworkActivity-platform"></a>
The platform on which the network activity was observed.
Type: String
Required: No

 ** ports **   <a name="guardduty-Type-NetworkActivity-ports"></a>
The ports that the network activity involved.
Type: [NetworkPorts](API_NetworkPorts.md) object
Required: No

 ** protocol **   <a name="guardduty-Type-NetworkActivity-protocol"></a>
The network protocol of the activity.
Type: String
Required: No

 ** traffic **   <a name="guardduty-Type-NetworkActivity-traffic"></a>
The amount of data that the network activity transferred.
Type: [NetworkTraffic](API_NetworkTraffic.md) object
Required: No

## See Also
<a name="API_NetworkActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkActivity)
