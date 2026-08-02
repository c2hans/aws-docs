---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ConnectPeerAssociation.html
---

# ConnectPeerAssociation
<a name="API_ConnectPeerAssociation"></a>

Describes a core network Connect peer association.

## Contents
<a name="API_ConnectPeerAssociation_Contents"></a>

 ** ConnectPeerId **   <a name="networkmanager-Type-ConnectPeerAssociation-ConnectPeerId"></a>
The ID of the Connect peer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^connect-peer-([0-9a-f]{8,17})$`
Required: No

 ** DeviceId **   <a name="networkmanager-Type-ConnectPeerAssociation-DeviceId"></a>
The ID of the device to connect to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-ConnectPeerAssociation-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** LinkId **   <a name="networkmanager-Type-ConnectPeerAssociation-LinkId"></a>
The ID of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-ConnectPeerAssociation-State"></a>
The state of the Connect peer association.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | DELETED`
Required: No

## See Also
<a name="API_ConnectPeerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerAssociation)
