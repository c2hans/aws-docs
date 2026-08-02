---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementEntitlement.html
---

# AgreementEntitlement
<a name="API_marketplace-agreements_AgreementEntitlement"></a>

Represents an entitlement associated with an agreement, including the provisioning status, resource, and type.

## Contents
<a name="API_marketplace-agreements_AgreementEntitlement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** licenseArn **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-licenseArn"></a>
The Amazon Resource Name (ARN) of the AWS License Manager license associated with the entitlement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** registrationToken **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-registrationToken"></a>
A short-lived token required by acceptors to register their account with the product provider. The token is only valid for 30 minutes after creation and is only applicable for purchase agreements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[A-Za-z0-9+/=.:_-]+`
Required: No

 ** resource **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-resource"></a>
The resource that the entitlement is provisioned to, such as a product.
Type: [Resource](API_marketplace-agreements_Resource.md) object
Required: No

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-status"></a>
The current state of an entitlement.
Type: String
Valid Values: `PROVISIONED | SCHEDULED | PENDING | FAILED | DEPROVISIONED`
Required: No

 ** statusReasonCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-statusReasonCode"></a>
Provides more information about the status of an entitlement.
Type: String
Valid Values: `PROVISIONING_IN_PROGRESS | FUTURE_START_DATE | INVALID_PAYMENT_INSTRUMENT | INCOMPATIBLE_CURRENCY | ACCOUNT_SUSPENDED | UNSUPPORTED_OPERATION | AGREEMENT_INACTIVE | AGREEMENT_ACTIVE | PRODUCT_RESTRICTED`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementEntitlement-type"></a>
The type of entitlement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z:]+`
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementEntitlement)
