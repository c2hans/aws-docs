---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_EntityDetail.html
---

# EntityDetail
<a name="API_EntityDetail"></a>

An object that contains metadata and details about the entity.

## Contents
<a name="API_EntityDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DetailsDocument **   <a name="AWSMarketplaceService-Type-EntityDetail-DetailsDocument"></a>
An object that contains all the details of the entity.
Type: JSON value
Required: No

 ** EntityArn **   <a name="AWSMarketplaceService-Type-EntityDetail-EntityArn"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`
Required: No

 ** EntityIdentifier **   <a name="AWSMarketplaceService-Type-EntityDetail-EntityIdentifier"></a>
The ID of the entity, in the format of `EntityId@RevisionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@]+$`
Required: No

 ** EntityType **   <a name="AWSMarketplaceService-Type-EntityDetail-EntityType"></a>
The entity type of the entity, in the format of `EntityType@Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-EntityDetail-LastModifiedDate"></a>
The last time the entity was modified.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

## See Also
<a name="API_EntityDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/EntityDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/EntityDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/EntityDetail)
