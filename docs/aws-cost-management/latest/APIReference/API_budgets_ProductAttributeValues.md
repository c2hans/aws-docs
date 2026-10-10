---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ProductAttributeValues.html
---

# ProductAttributeValues
<a name="API_budgets_ProductAttributeValues"></a>

The product attribute values used for filtering the costs by key and value pairs. Product attributes are supported for Amazon Bedrock only.

## Contents
<a name="API_budgets_ProductAttributeValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-budgets_ProductAttributeValues-Key"></a>
The name of the product attribute to filter on. Valid values are the following:
+  `feature` – The feature that was used, such as `On-demand Inference`.
+  `inferenceType` – The type of inference usage, such as `Input tokens` or `Output tokens`.
+  `model` – The model, such as `Claude Sonnet 5` or `Claude Haiku 4.5`.
+  `provider` – The model provider, such as `Anthropic`, `Cohere`, or `Amazon`.
Keys are case-sensitive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** MatchOptions **   <a name="awscostmanagement-Type-budgets_ProductAttributeValues-MatchOptions"></a>
The match options for the `ProductAttributes` filter. Valid values:
+  `ABSENT` – Matches costs that have no value for the attribute.
+  `CASE_SENSITIVE` – Requires an exact case match.
+  `EQUALS` – Matches costs where the attribute equals the specified value.
Specify either `EQUALS` or `ABSENT`. You can add `CASE_SENSITIVE` to `EQUALS`, but you can't use it by itself or with `ABSENT`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

 ** Values **   <a name="awscostmanagement-Type-budgets_ProductAttributeValues-Values"></a>
The specific values of the product attribute, such as `Claude Sonnet 5` for the `model` key. Values are matched exactly.
 `Values` is required unless `MatchOptions` is `ABSENT`. To match costs that have no value for the key, set `MatchOptions` to `ABSENT` and omit `Values`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_budgets_ProductAttributeValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/ProductAttributeValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/ProductAttributeValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/ProductAttributeValues)
