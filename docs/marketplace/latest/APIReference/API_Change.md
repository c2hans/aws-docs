---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Change.html
---

# Change
<a name="API_Change"></a>

An object that contains the `ChangeType`, `Details`, and `Entity`.

## Contents
<a name="API_Change_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChangeType **   <a name="AWSMarketplaceService-Type-Change-ChangeType"></a>
Change types are single string values that describe your intention for the change. Each change type is unique for each `EntityType` provided in the change's scope. For more information about change types available for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products). Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Z][\w]*$`
Required: Yes

 ** Entity **   <a name="AWSMarketplaceService-Type-Change-Entity"></a>
The entity to be changed.
Type: [Entity](API_Entity.md) object
Required: Yes

 ** ChangeName **   <a name="AWSMarketplaceService-Type-Change-ChangeName"></a>
Optional name for the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 72.
Pattern: `^[a-zA-Z]$`
Required: No

 ** Details **   <a name="AWSMarketplaceService-Type-Change-Details"></a>
This object contains details specific to the change type of the requested change. For more information about change types available for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products). Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 16384.
Pattern: `^[\s]*\{[\s\S]*\}[\s]*$`
Required: No

 ** DetailsDocument **   <a name="AWSMarketplaceService-Type-Change-DetailsDocument"></a>
Alternative field that accepts a JSON value instead of a string for `ChangeType` details. You can use either `Details` or `DetailsDocument`, but not both.
To download the "DetailsDocument" shapes, see the [Python](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python) and [Java](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main) shapes on GitHub.
Type: JSON value
Required: No

 ** EntityTags **   <a name="AWSMarketplaceService-Type-Change-EntityTags"></a>
The tags associated with the change.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## See Also
<a name="API_Change_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/Change)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/Change)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/Change)
