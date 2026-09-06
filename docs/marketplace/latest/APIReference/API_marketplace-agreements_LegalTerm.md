---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_LegalTerm.html
---

# LegalTerm
<a name="API_marketplace-agreements_LegalTerm"></a>

Defines the list of text agreements proposed to the acceptors. An example is the end user license agreement (EULA).

## Contents
<a name="API_marketplace-agreements_LegalTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** documents **   <a name="AWSMarketplaceService-Type-marketplace-agreements_LegalTerm-documents"></a>
List of references to legal resources proposed to the buyers. An example is the EULA.
Type: Array of [DocumentItem](API_marketplace-agreements_DocumentItem.md) objects
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_LegalTerm-id"></a>
The unique identifer for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_LegalTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_LegalTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/LegalTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/LegalTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/LegalTerm)
