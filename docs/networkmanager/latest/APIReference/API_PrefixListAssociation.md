---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PrefixListAssociation.html
---

# PrefixListAssociation
<a name="API_PrefixListAssociation"></a>

Information about a prefix list association with a core network.

## Contents
<a name="API_PrefixListAssociation_Contents"></a>

 ** CoreNetworkId **   <a name="networkmanager-Type-PrefixListAssociation-CoreNetworkId"></a>
The core network id in the association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** PrefixListAlias **   <a name="networkmanager-Type-PrefixListAssociation-PrefixListAlias"></a>
The alias of the prefix list in the association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PrefixListArn **   <a name="networkmanager-Type-PrefixListAssociation-PrefixListArn"></a>
The ARN of the prefix list in the association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_PrefixListAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PrefixListAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PrefixListAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PrefixListAssociation)
