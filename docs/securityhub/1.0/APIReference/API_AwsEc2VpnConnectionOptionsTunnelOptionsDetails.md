---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpnConnectionOptionsTunnelOptionsDetails.html
---

# AwsEc2VpnConnectionOptionsTunnelOptionsDetails
<a name="API_AwsEc2VpnConnectionOptionsTunnelOptionsDetails"></a>

The VPN tunnel options.

## Contents
<a name="API_AwsEc2VpnConnectionOptionsTunnelOptionsDetails_Contents"></a>

 ** DpdTimeoutSeconds **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-DpdTimeoutSeconds"></a>
The number of seconds after which a Dead Peer Detection (DPD) timeout occurs.
Type: Integer
Required: No

 ** IkeVersions **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-IkeVersions"></a>
The Internet Key Exchange (IKE) versions that are permitted for the VPN tunnel.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** OutsideIpAddress **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-OutsideIpAddress"></a>
The external IP address of the VPN tunnel.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Phase1DhGroupNumbers **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase1DhGroupNumbers"></a>
The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of integers
Required: No

 ** Phase1EncryptionAlgorithms **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase1EncryptionAlgorithms"></a>
The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Phase1IntegrityAlgorithms **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase1IntegrityAlgorithms"></a>
The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Phase1LifetimeSeconds **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase1LifetimeSeconds"></a>
The lifetime for phase 1 of the IKE negotiation, in seconds.
Type: Integer
Required: No

 ** Phase2DhGroupNumbers **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase2DhGroupNumbers"></a>
The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of integers
Required: No

 ** Phase2EncryptionAlgorithms **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase2EncryptionAlgorithms"></a>
The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Phase2IntegrityAlgorithms **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase2IntegrityAlgorithms"></a>
The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Phase2LifetimeSeconds **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-Phase2LifetimeSeconds"></a>
The lifetime for phase 2 of the IKE negotiation, in seconds.
Type: Integer
Required: No

 ** PreSharedKey **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-PreSharedKey"></a>
The preshared key to establish initial authentication between the virtual private gateway and the customer gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RekeyFuzzPercentage **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-RekeyFuzzPercentage"></a>
The percentage of the rekey window, which is determined by `RekeyMarginTimeSeconds` during which the rekey time is randomly selected.
Type: Integer
Required: No

 ** RekeyMarginTimeSeconds **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-RekeyMarginTimeSeconds"></a>
The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the VPN connection performs an IKE rekey.
Type: Integer
Required: No

 ** ReplayWindowSize **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-ReplayWindowSize"></a>
The number of packets in an IKE replay window.
Type: Integer
Required: No

 ** TunnelInsideCidr **   <a name="securityhub-Type-AwsEc2VpnConnectionOptionsTunnelOptionsDetails-TunnelInsideCidr"></a>
The range of inside IPv4 addresses for the tunnel.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpnConnectionOptionsTunnelOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpnConnectionOptionsTunnelOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpnConnectionOptionsTunnelOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpnConnectionOptionsTunnelOptionsDetails)
