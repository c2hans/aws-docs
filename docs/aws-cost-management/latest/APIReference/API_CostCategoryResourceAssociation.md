---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryResourceAssociation.html
---

# CostCategoryResourceAssociation
<a name="API_CostCategoryResourceAssociation"></a>

A reference to a cost category association that contains information on an associated resource.

## Contents
<a name="API_CostCategoryResourceAssociation_Contents"></a>

 ** CostCategoryArn **   <a name="awscostmanagement-Type-CostCategoryResourceAssociation-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** CostCategoryName **   <a name="awscostmanagement-Type-CostCategoryResourceAssociation-CostCategoryName"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** ResourceArn **   <a name="awscostmanagement-Type-CostCategoryResourceAssociation-ResourceArn"></a>
 The unique identifier for an associated resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

## See Also
<a name="API_CostCategoryResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategoryResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategoryResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategoryResourceAssociation)
