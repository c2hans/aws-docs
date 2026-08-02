---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SupportTerm.html
---

# SupportTerm
<a name="API_marketplace-agreements_SupportTerm"></a>

Defines the customer support available for the acceptors when they purchase the software.

## Contents
<a name="API_marketplace-agreements_SupportTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_SupportTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** refundPolicy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_SupportTerm-refundPolicy"></a>
Free-text field about the refund policy description that will be shown to customers as is on the website and console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_SupportTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_SupportTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/SupportTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SupportTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/SupportTerm)
