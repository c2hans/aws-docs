---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkPorts.html
---

# NetworkPorts
<a name="API_NetworkPorts"></a>

Contains information about the ports that network activity involved. A port value can be a single port, a range such as `51000-51010`, or a comma-separated list such as `443,8080`.

## Contents
<a name="API_NetworkPorts_Contents"></a>

 ** portCount **   <a name="guardduty-Type-NetworkPorts-portCount"></a>
The number of ports that the activity involved.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ports **   <a name="guardduty-Type-NetworkPorts-ports"></a>
The ports that the activity involved.
Type: String
Required: No

 ** portsUsed **   <a name="guardduty-Type-NetworkPorts-portsUsed"></a>
The ports that the activity used.
Type: String
Required: No

 ** remotePort **   <a name="guardduty-Type-NetworkPorts-remotePort"></a>
The port on the remote host.
Type: String
Required: No

 ** resolverPort **   <a name="guardduty-Type-NetworkPorts-resolverPort"></a>
The port of the DNS resolver.
Type: String
Required: No

 ** targetPort **   <a name="guardduty-Type-NetworkPorts-targetPort"></a>
The port on the target of the activity.
Type: String
Required: No

## See Also
<a name="API_NetworkPorts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkPorts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkPorts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkPorts)
