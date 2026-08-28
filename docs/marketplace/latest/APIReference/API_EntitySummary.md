---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_EntitySummary.html
---

# EntitySummary
<a name="API_EntitySummary"></a>

This object is a container for common summary information about the entity. The summary doesn't contain the whole entity structure, but it does contain information common across all entities.

## Contents
<a name="API_EntitySummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AmiProductSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-AmiProductSummary"></a>
An object that contains summary information about the AMI product.
Type: [AmiProductSummary](API_AmiProductSummary.md) object
Required: No

 ** ContainerProductSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-ContainerProductSummary"></a>
An object that contains summary information about the container product.
Type: [ContainerProductSummary](API_ContainerProductSummary.md) object
Required: No

 ** DataProductSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-DataProductSummary"></a>
An object that contains summary information about the data product.
Type: [DataProductSummary](API_DataProductSummary.md) object
Required: No

 ** EntityArn **   <a name="AWSMarketplaceService-Type-EntitySummary-EntityArn"></a>
The ARN associated with the unique identifier for the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-EntitySummary-EntityId"></a>
The unique identifier for the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** EntityType **   <a name="AWSMarketplaceService-Type-EntitySummary-EntityType"></a>
The type of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-EntitySummary-LastModifiedDate"></a>
The last time the entity was published, using ISO 8601 format (2018-02-27T13:45:22Z).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** MachineLearningProductSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-MachineLearningProductSummary"></a>
A summary of a machine learning product.
Type: [MachineLearningProductSummary](API_MachineLearningProductSummary.md) object
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-EntitySummary-Name"></a>
The name for the entity. This value is not unique. It is defined by the seller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^\\S+[\\S\\s]*`
Required: No

 ** OfferSetSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-OfferSetSummary"></a>
An object that contains summary information about the offer set.
Type: [OfferSetSummary](API_OfferSetSummary.md) object
Required: No

 ** OfferSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-OfferSummary"></a>
An object that contains summary information about the offer.
Type: [OfferSummary](API_OfferSummary.md) object
Required: No

 ** ResaleAuthorizationSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-ResaleAuthorizationSummary"></a>
An object that contains summary information about the Resale Authorization.
Type: [ResaleAuthorizationSummary](API_ResaleAuthorizationSummary.md) object
Required: No

 ** SaaSProductSummary **   <a name="AWSMarketplaceService-Type-EntitySummary-SaaSProductSummary"></a>
An object that contains summary information about the SaaS product.
Type: [SaaSProductSummary](API_SaaSProductSummary.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-EntitySummary-Visibility"></a>
The visibility status of the entity to buyers. This value can be `Public` (everyone can view the entity), `Limited` (the entity is visible to limited accounts only), or `Restricted` (the entity was published and then unpublished and only existing buyers can view it).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: No

## See Also
<a name="API_EntitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/EntitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/EntitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/EntitySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
