---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ActiveVpnTunnelStatus.html
---

# ActiveVpnTunnelStatus
<a name="API_ActiveVpnTunnelStatus"></a>

Contains information about the current security configuration of an active VPN tunnel.

## Contents
<a name="API_ActiveVpnTunnelStatus_Contents"></a>

 ** ikeVersion **
The version of the Internet Key Exchange (IKE) protocol being used.
Type: String
Required: No

 ** phase1DHGroup **
The Diffie-Hellman group number being used in Phase 1 IKE negotiations.
Type: Integer
Required: No

 ** phase1EncryptionAlgorithm **
The encryption algorithm negotiated in Phase 1 IKE negotiations.
Type: String
Required: No

 ** phase1IntegrityAlgorithm **
The integrity algorithm negotiated in Phase 1 IKE negotiations.
Type: String
Required: No

 ** phase2DHGroup **
The Diffie-Hellman group number being used in Phase 2 IKE negotiations.
Type: Integer
Required: No

 ** phase2EncryptionAlgorithm **
The encryption algorithm negotiated in Phase 2 IKE negotiations.
Type: String
Required: No

 ** phase2IntegrityAlgorithm **
The integrity algorithm negotiated in Phase 2 IKE negotiations.
Type: String
Required: No

 ** provisioningStatus **
The current provisioning status of the VPN tunnel.
Type: String
Valid Values: `available | pending | failed`
Required: No

 ** provisioningStatusReason **
The reason for the current provisioning status.
Type: String
Required: No

## See Also
<a name="API_ActiveVpnTunnelStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ActiveVpnTunnelStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ActiveVpnTunnelStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ActiveVpnTunnelStatus)
