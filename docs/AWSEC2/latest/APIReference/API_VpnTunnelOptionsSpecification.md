---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html
---

# VpnTunnelOptionsSpecification
<a name="API_VpnTunnelOptionsSpecification"></a>

The tunnel options for a single VPN tunnel.

## Contents
<a name="API_VpnTunnelOptionsSpecification_Contents"></a>

 ** DPDTimeoutAction **
The action to take after DPD timeout occurs. Specify `restart` to restart the IKE initiation. Specify `clear` to end the IKE session.
Valid Values: `clear` \| `none` \| `restart`
Default: `clear`
Type: String
Required: No

 ** DPDTimeoutSeconds **
The number of seconds after which a DPD timeout occurs.
Constraints: A value greater than or equal to 30.
Default: `30`
Type: Integer
Required: No

 ** EnableTunnelLifecycleControl **
Turn on or off tunnel endpoint lifecycle control feature.
Type: Boolean
Required: No

 ** IKEVersion.N **
The IKE versions that are permitted for the VPN tunnel.
Valid values: `ikev1` \| `ikev2`
Type: Array of [IKEVersionsRequestListValue](API_IKEVersionsRequestListValue.md) objects
Required: No

 ** LogOptions **
Options for logging VPN tunnel activity.
Type: [VpnTunnelLogOptionsSpecification](API_VpnTunnelLogOptionsSpecification.md) object
Required: No

 ** Phase1DHGroupNumber.N **
One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `2` \| `14` \| `15` \| `16` \| `17` \| `18` \| `19` \| `20` \| `21` \| `22` \| `23` \| `24`
Type: Array of [Phase1DHGroupNumbersRequestListValue](API_Phase1DHGroupNumbersRequestListValue.md) objects
Required: No

 ** Phase1EncryptionAlgorithm.N **
One or more encryption algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `AES128` \| `AES256` \| `AES128-GCM-16` \| `AES256-GCM-16`
Type: Array of [Phase1EncryptionAlgorithmsRequestListValue](API_Phase1EncryptionAlgorithmsRequestListValue.md) objects
Required: No

 ** Phase1IntegrityAlgorithm.N **
One or more integrity algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `SHA1` \| `SHA2-256` \| `SHA2-384` \| `SHA2-512`
Type: Array of [Phase1IntegrityAlgorithmsRequestListValue](API_Phase1IntegrityAlgorithmsRequestListValue.md) objects
Required: No

 ** Phase1LifetimeSeconds **
The lifetime for phase 1 of the IKE negotiation, in seconds.
Constraints: A value between 900 and 28,800.
Default: `28800`
Type: Integer
Required: No

 ** Phase2DHGroupNumber.N **
One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `2` \| `5` \| `14` \| `15` \| `16` \| `17` \| `18` \| `19` \| `20` \| `21` \| `22` \| `23` \| `24`
Type: Array of [Phase2DHGroupNumbersRequestListValue](API_Phase2DHGroupNumbersRequestListValue.md) objects
Required: No

 ** Phase2EncryptionAlgorithm.N **
One or more encryption algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `AES128` \| `AES256` \| `AES128-GCM-16` \| `AES256-GCM-16`
Type: Array of [Phase2EncryptionAlgorithmsRequestListValue](API_Phase2EncryptionAlgorithmsRequestListValue.md) objects
Required: No

 ** Phase2IntegrityAlgorithm.N **
One or more integrity algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `SHA1` \| `SHA2-256` \| `SHA2-384` \| `SHA2-512`
Type: Array of [Phase2IntegrityAlgorithmsRequestListValue](API_Phase2IntegrityAlgorithmsRequestListValue.md) objects
Required: No

 ** Phase2LifetimeSeconds **
The lifetime for phase 2 of the IKE negotiation, in seconds.
Constraints: A value between 900 and 3,600. The value must be less than the value for `Phase1LifetimeSeconds`.
Default: `3600`
Type: Integer
Required: No

 ** PreSharedKey **
The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.
Constraints: Allowed characters are alphanumeric characters, periods (.), and underscores (\_). Must be between 8 and 64 characters in length and cannot start with zero (0).
Type: String
Required: No

 ** RekeyFuzzPercentage **
The percentage of the rekey window (determined by `RekeyMarginTimeSeconds`) during which the rekey time is randomly selected.
Constraints: A value between 0 and 100.
Default: `100`
Type: Integer
Required: No

 ** RekeyMarginTimeSeconds **
The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for `RekeyFuzzPercentage`.
Constraints: A value between 60 and half of `Phase2LifetimeSeconds`.
Default: `270`
Type: Integer
Required: No

 ** ReplayWindowSize **
The number of packets in an IKE replay window.
Constraints: A value between 64 and 2048.
Default: `1024`
Type: Integer
Required: No

 ** StartupAction **
The action to take when the establishing the tunnel for the VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify `start` for AWS to initiate the IKE negotiation.
Valid Values: `add` \| `start`
Default: `add`
Type: String
Required: No

 ** TunnelInsideCidr **
The range of inside IPv4 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway.
Constraints: A size /30 CIDR block from the `169.254.0.0/16` range. The following CIDR blocks are reserved and cannot be used:
+  `169.254.0.0/30`
+  `169.254.1.0/30`
+  `169.254.2.0/30`
+  `169.254.3.0/30`
+  `169.254.4.0/30`
+  `169.254.5.0/30`
+  `169.254.169.252/30`
Type: String
Required: No

 ** TunnelInsideIpv6Cidr **
The range of inside IPv6 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same transit gateway.
Constraints: A size /126 CIDR block from the local `fd00::/8` range.
Type: String
Required: No

## See Also
<a name="API_VpnTunnelOptionsSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnTunnelOptionsSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnTunnelOptionsSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnTunnelOptionsSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
