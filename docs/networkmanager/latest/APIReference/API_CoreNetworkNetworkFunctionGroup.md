---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkNetworkFunctionGroup.html
---

# CoreNetworkNetworkFunctionGroup
<a name="API_CoreNetworkNetworkFunctionGroup"></a>

Describes a network function group.

## Contents
<a name="API_CoreNetworkNetworkFunctionGroup_Contents"></a>

 ** EdgeLocations **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroup-EdgeLocations"></a>
The core network edge locations.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** Name **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroup-Name"></a>
The name of the network function group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Segments **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroup-Segments"></a>
The segments associated with the network function group.
Type: [ServiceInsertionSegments](API_ServiceInsertionSegments.md) object
Required: No

## See Also
<a name="API_CoreNetworkNetworkFunctionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroup)
