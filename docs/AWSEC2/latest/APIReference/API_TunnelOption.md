---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TunnelOption.html
---

# TunnelOption
<a name="API_TunnelOption"></a>

The VPN tunnel options.

## Contents
<a name="API_TunnelOption_Contents"></a>

 ** dpdTimeoutAction **
The action to take after a DPD timeout occurs.
Type: String
Required: No

 ** dpdTimeoutSeconds **
The number of seconds after which a DPD timeout occurs.
Type: Integer
Required: No

 ** enableTunnelLifecycleControl **
Status of tunnel endpoint lifecycle control feature.
Type: Boolean
Required: No

 ** IkeVersionSet.N **
The IKE versions that are permitted for the VPN tunnel.
Type: Array of [IKEVersionsListValue](API_IKEVersionsListValue.md) objects
Required: No

 ** logOptions **
Options for logging VPN tunnel activity.
Type: [VpnTunnelLogOptions](API_VpnTunnelLogOptions.md) object
Required: No

 ** outsideIpAddress **
The external IP address of the VPN tunnel.
Type: String
Required: No

 ** Phase1DHGroupNumberSet.N **
The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of [Phase1DHGroupNumbersListValue](API_Phase1DHGroupNumbersListValue.md) objects
Required: No

 ** Phase1EncryptionAlgorithmSet.N **
The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of [Phase1EncryptionAlgorithmsListValue](API_Phase1EncryptionAlgorithmsListValue.md) objects
Required: No

 ** Phase1IntegrityAlgorithmSet.N **
The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of [Phase1IntegrityAlgorithmsListValue](API_Phase1IntegrityAlgorithmsListValue.md) objects
Required: No

 ** phase1LifetimeSeconds **
The lifetime for phase 1 of the IKE negotiation, in seconds.
Type: Integer
Required: No

 ** Phase2DHGroupNumberSet.N **
The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of [Phase2DHGroupNumbersListValue](API_Phase2DHGroupNumbersListValue.md) objects
Required: No

 ** Phase2EncryptionAlgorithmSet.N **
The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of [Phase2EncryptionAlgorithmsListValue](API_Phase2EncryptionAlgorithmsListValue.md) objects
Required: No

 ** Phase2IntegrityAlgorithmSet.N **
The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of [Phase2IntegrityAlgorithmsListValue](API_Phase2IntegrityAlgorithmsListValue.md) objects
Required: No

 ** phase2LifetimeSeconds **
The lifetime for phase 2 of the IKE negotiation, in seconds.
Type: Integer
Required: No

 ** preSharedKey **
The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and the customer gateway.
Type: String
Required: No

 ** rekeyFuzzPercentage **
The percentage of the rekey window determined by `RekeyMarginTimeSeconds` during which the rekey time is randomly selected.
Type: Integer
Required: No

 ** rekeyMarginTimeSeconds **
The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the VPN connection performs an IKE rekey.
Type: Integer
Required: No

 ** replayWindowSize **
The number of packets in an IKE replay window.
Type: Integer
Required: No

 ** startupAction **
The action to take when the establishing the VPN tunnels for a VPN connection.
Type: String
Required: No

 ** tunnelInsideCidr **
The range of inside IPv4 addresses for the tunnel.
Type: String
Required: No

 ** tunnelInsideIpv6Cidr **
The range of inside IPv6 addresses for the tunnel.
Type: String
Required: No

## See Also
<a name="API_TunnelOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TunnelOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TunnelOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TunnelOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
