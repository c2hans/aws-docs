---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementApprovalResource.html
---

# AgreementApprovalResource

A resource involved in the agreement, such as a product.

## Contents
<a name="API_marketplace-agreements_AgreementApprovalResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalResource-id"></a>
The unique identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalResource-name"></a>
The name of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\p{C}]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalResource-type"></a>
Type of the resource, which is the product (for example, `SaaSProduct`, `AmiProduct`, `ContainerProduct`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** deployedOnAws **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalResource-deployedOnAws"></a>
Whether the product is deployed on AWS (for example, `DEPLOYED`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementApprovalResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementApprovalResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementApprovalResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementApprovalResource)
