---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkEdge.html
---

# CoreNetworkEdge
<a name="API_CoreNetworkEdge"></a>

Describes a core network edge.

## Contents
<a name="API_CoreNetworkEdge_Contents"></a>

 ** Asn **   <a name="networkmanager-Type-CoreNetworkEdge-Asn"></a>
The ASN of a core network edge.
Type: Long
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-CoreNetworkEdge-EdgeLocation"></a>
The Region where a core network edge is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** InsideCidrBlocks **   <a name="networkmanager-Type-CoreNetworkEdge-InsideCidrBlocks"></a>
The inside IP addresses used for core network edges.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkEdge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkEdge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkEdge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkEdge)
