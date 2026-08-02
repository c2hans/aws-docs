---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkConnectionAction.html
---

# NetworkConnectionAction
<a name="API_NetworkConnectionAction"></a>

Contains information about the NETWORK\_CONNECTION action described in the finding.

## Contents
<a name="API_NetworkConnectionAction_Contents"></a>

 ** blocked **   <a name="guardduty-Type-NetworkConnectionAction-blocked"></a>
Indicates whether EC2 blocked the network connection to your instance.
Type: Boolean
Required: No

 ** connectionDirection **   <a name="guardduty-Type-NetworkConnectionAction-connectionDirection"></a>
The network connection direction.
Type: String
Required: No

 ** localIpDetails **   <a name="guardduty-Type-NetworkConnectionAction-localIpDetails"></a>
The local IP information of the connection.
Type: [LocalIpDetails](API_LocalIpDetails.md) object
Required: No

 ** localNetworkInterface **   <a name="guardduty-Type-NetworkConnectionAction-localNetworkInterface"></a>
The EC2 instance's local elastic network interface utilized for the connection.
Type: String
Required: No

 ** localPortDetails **   <a name="guardduty-Type-NetworkConnectionAction-localPortDetails"></a>
The local port information of the connection.
Type: [LocalPortDetails](API_LocalPortDetails.md) object
Required: No

 ** protocol **   <a name="guardduty-Type-NetworkConnectionAction-protocol"></a>
The network connection protocol.
Type: String
Required: No

 ** remoteIpDetails **   <a name="guardduty-Type-NetworkConnectionAction-remoteIpDetails"></a>
The remote IP information of the connection.
Type: [RemoteIpDetails](API_RemoteIpDetails.md) object
Required: No

 ** remotePortDetails **   <a name="guardduty-Type-NetworkConnectionAction-remotePortDetails"></a>
The remote port information of the connection.
Type: [RemotePortDetails](API_RemotePortDetails.md) object
Required: No

## See Also
<a name="API_NetworkConnectionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkConnectionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkConnectionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkConnectionAction)
