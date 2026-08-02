---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Spend.html
---

# Spend
<a name="API_budgets_Spend"></a>

The amount of cost or usage that's measured for a budget.

 *Cost example:* A `Spend` for `3 USD` of costs has the following parameters:
+ An `Amount` of `3`
+ A `Unit` of `USD`

 *Usage example:* A `Spend` for `3 GB` of S3 usage has the following parameters:
+ An `Amount` of `3`
+ A `Unit` of `GB`

## Contents
<a name="API_budgets_Spend_Contents"></a>

 ** Amount **   <a name="awscostmanagement-Type-budgets_Spend-Amount"></a>
The cost or usage amount that's associated with a budget forecast, actual spend, or budget threshold.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2147483647.
Pattern: `([0-9]*\.)?[0-9]+`
Required: Yes

 ** Unit **   <a name="awscostmanagement-Type-budgets_Spend-Unit"></a>
The unit of measurement that's used for the budget forecast, actual spend, or budget threshold.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2147483647.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_budgets_Spend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Spend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Spend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Spend)
