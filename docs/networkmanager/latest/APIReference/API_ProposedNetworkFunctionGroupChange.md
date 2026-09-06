---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ProposedNetworkFunctionGroupChange.html
---

# ProposedNetworkFunctionGroupChange
<a name="API_ProposedNetworkFunctionGroupChange"></a>

Describes proposed changes to a network function group.

## Contents
<a name="API_ProposedNetworkFunctionGroupChange_Contents"></a>

 ** AttachmentPolicyRuleNumber **   <a name="networkmanager-Type-ProposedNetworkFunctionGroupChange-AttachmentPolicyRuleNumber"></a>
The proposed new attachment policy rule number for the network function group.
Type: Integer
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-ProposedNetworkFunctionGroupChange-NetworkFunctionGroupName"></a>
The proposed name change for the network function group name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Tags **   <a name="networkmanager-Type-ProposedNetworkFunctionGroupChange-Tags"></a>
The list of proposed changes to the key-value tags associated with the network function group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ProposedNetworkFunctionGroupChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ProposedNetworkFunctionGroupChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ProposedNetworkFunctionGroupChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ProposedNetworkFunctionGroupChange)
