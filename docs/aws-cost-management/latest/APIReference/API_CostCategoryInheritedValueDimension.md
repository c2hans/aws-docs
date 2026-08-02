---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryInheritedValueDimension.html
---

# CostCategoryInheritedValueDimension
<a name="API_CostCategoryInheritedValueDimension"></a>

When you create or update a cost category, you can define the `CostCategoryRule` rule type as `INHERITED_VALUE`. This rule type adds the flexibility to define a rule that dynamically inherits the cost category value from the dimension value that's defined by `CostCategoryInheritedValueDimension`. For example, suppose that you want to dynamically group costs that are based on the value of a specific tag key. First, choose an inherited value rule type, and then choose the tag dimension and specify the tag key to use.

## Contents
<a name="API_CostCategoryInheritedValueDimension_Contents"></a>

 ** DimensionKey **   <a name="awscostmanagement-Type-CostCategoryInheritedValueDimension-DimensionKey"></a>
The key to extract cost category values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DimensionName **   <a name="awscostmanagement-Type-CostCategoryInheritedValueDimension-DimensionName"></a>
The name of the dimension that's used to group costs.
If you specify `LINKED_ACCOUNT_NAME`, the cost category value is based on account name. If you specify `TAG`, the cost category value is based on the value of the specified tag key.
Type: String
Valid Values: `LINKED_ACCOUNT_NAME | TAG`
Required: No

## See Also
<a name="API_CostCategoryInheritedValueDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategoryInheritedValueDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategoryInheritedValueDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategoryInheritedValueDimension)
