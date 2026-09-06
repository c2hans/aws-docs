---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-entitlements_Entitlement.html
---

# Entitlement
<a name="API_marketplace-entitlements_Entitlement"></a>

An entitlement represents capacity in a product owned by the customer. For example, a customer might own some number of users or seats in an SaaS application or some amount of data capacity in a multi-tenant database.

## Contents
<a name="API_marketplace-entitlements_Entitlement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomerAWSAccountId **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-CustomerAWSAccountId"></a>
 The `CustomerAWSAccountId` parameter specifies the AWS account ID of the buyer.
Type: String
Pattern: `\S+`
Required: No

 ** CustomerIdentifier **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-CustomerIdentifier"></a>
The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service.
Type: String
Pattern: `\S+`
Required: No

 ** Dimension **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-Dimension"></a>
The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
Type: String
Pattern: `\S+`
Required: No

 ** ExpirationDate **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-ExpirationDate"></a>
The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date.
Type: Timestamp
Required: No

 ** LicenseArn **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-LicenseArn"></a>
The `LicenseArn` is a unique identifier for a specific granted license. These are used for software purchased through AWS Marketplace.
Type: String
Required: No

 ** ProductCode **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-ProductCode"></a>
The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Value **   <a name="AWSMarketplaceService-Type-marketplace-entitlements_Entitlement-Value"></a>
The EntitlementValue represents the amount of capacity that the customer is entitled to for the product.
Type: [EntitlementValue](API_marketplace-entitlements_EntitlementValue.md) object
Required: No

## See Also
<a name="API_marketplace-entitlements_Entitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entitlement.marketplace-2017-01-11/Entitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entitlement.marketplace-2017-01-11/Entitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entitlement.marketplace-2017-01-11/Entitlement)
