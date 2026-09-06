---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CostCategoryValues.html
---

# CostCategoryValues
<a name="API_billing_CostCategoryValues"></a>

 The Cost Categories values used for filtering the costs.

## Contents
<a name="API_billing_CostCategoryValues_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-billing_CostCategoryValues-key"></a>
 The unique name of the Cost Category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-billing_CostCategoryValues-values"></a>
 The specific value of the Cost Category.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_billing_CostCategoryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CostCategoryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CostCategoryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CostCategoryValues)
