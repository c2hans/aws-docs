---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html
---

# CostCategoryRule
<a name="API_CostCategoryRule"></a>

Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that cost category value.

## Contents
<a name="API_CostCategoryRule_Contents"></a>

 ** InheritedValue **   <a name="awscostmanagement-Type-CostCategoryRule-InheritedValue"></a>
The value the line item is categorized as if the line item contains the matched dimension.
Type: [CostCategoryInheritedValueDimension](API_CostCategoryInheritedValueDimension.md) object
Required: No

 ** Rule **   <a name="awscostmanagement-Type-CostCategoryRule-Rule"></a>
An [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object used to categorize costs. This supports dimensions, tags, and nested expressions. Currently the only dimensions supported are `LINKED_ACCOUNT`, `SERVICE_CODE`, `RECORD_TYPE`, `LINKED_ACCOUNT_NAME`, `REGION`, and `USAGE_TYPE`.
 `RECORD_TYPE` is a dimension used for Cost Explorer APIs, and is also supported for cost category expressions. This dimension uses different terms, depending on whether you're using the console or API/JSON editor. For a detailed comparison, see [Term Comparisons](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html#cost-categories-terms) in the * AWS Billing and Cost Management User Guide*.
Type: [Expression](API_Expression.md) object
Required: No

 ** Type **   <a name="awscostmanagement-Type-CostCategoryRule-Type"></a>
You can define the `CostCategoryRule` rule type as either `REGULAR` or `INHERITED_VALUE`. The `INHERITED_VALUE` rule type adds the flexibility to define a rule that dynamically inherits the cost category value. This value is from the dimension value that's defined by `CostCategoryInheritedValueDimension`. For example, suppose that you want to costs to be dynamically grouped based on the value of a specific tag key. First, choose an inherited value rule type, and then choose the tag dimension and specify the tag key to use.
Type: String
Valid Values: `REGULAR | INHERITED_VALUE`
Required: No

 ** Value **   <a name="awscostmanagement-Type-CostCategoryRule-Value"></a>
The default value for the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

## See Also
<a name="API_CostCategoryRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategoryRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategoryRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategoryRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
