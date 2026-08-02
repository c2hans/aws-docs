---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ConnectPeerConfiguration.html
---

# ConnectPeerConfiguration
<a name="API_ConnectPeerConfiguration"></a>

Describes a core network Connect peer configuration.

## Contents
<a name="API_ConnectPeerConfiguration_Contents"></a>

 ** BgpConfigurations **   <a name="networkmanager-Type-ConnectPeerConfiguration-BgpConfigurations"></a>
The Connect peer BGP configurations.
Type: Array of [ConnectPeerBgpConfiguration](API_ConnectPeerBgpConfiguration.md) objects
Required: No

 ** CoreNetworkAddress **   <a name="networkmanager-Type-ConnectPeerConfiguration-CoreNetworkAddress"></a>
The IP address of a core network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** InsideCidrBlocks **   <a name="networkmanager-Type-ConnectPeerConfiguration-InsideCidrBlocks"></a>
The inside IP addresses used for a Connect peer configuration.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PeerAddress **   <a name="networkmanager-Type-ConnectPeerConfiguration-PeerAddress"></a>
The IP address of the Connect peer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** Protocol **   <a name="networkmanager-Type-ConnectPeerConfiguration-Protocol"></a>
The protocol used for a Connect peer configuration.
Type: String
Valid Values: `GRE | NO_ENCAP`
Required: No

## See Also
<a name="API_ConnectPeerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerConfiguration)
