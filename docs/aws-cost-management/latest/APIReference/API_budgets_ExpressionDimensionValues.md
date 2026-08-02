---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ExpressionDimensionValues.html
---

# ExpressionDimensionValues
<a name="API_budgets_ExpressionDimensionValues"></a>

Contains the specifications for the filters to use for your request.

## Contents
<a name="API_budgets_ExpressionDimensionValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-budgets_ExpressionDimensionValues-Key"></a>
The name of the dimension that you want to filter on.
Type: String
Valid Values: `AZ | INSTANCE_TYPE | LINKED_ACCOUNT | LINKED_ACCOUNT_NAME | OPERATION | PURCHASE_TYPE | REGION | SERVICE | SERVICE_CODE | USAGE_TYPE | USAGE_TYPE_GROUP | RECORD_TYPE | OPERATING_SYSTEM | TENANCY | SCOPE | PLATFORM | SUBSCRIPTION_ID | LEGAL_ENTITY_NAME | INVOICING_ENTITY | DEPLOYMENT_OPTION | DATABASE_ENGINE | CACHE_ENGINE | INSTANCE_TYPE_FAMILY | BILLING_ENTITY | RESERVATION_ID | RESOURCE_ID | RIGHTSIZING_TYPE | SAVINGS_PLANS_TYPE | SAVINGS_PLAN_ARN | PAYMENT_OPTION | RESERVATION_MODIFIED | TAG_KEY | COST_CATEGORY_NAME`
Required: Yes

 ** Values **   <a name="awscostmanagement-Type-budgets_ExpressionDimensionValues-Values"></a>
The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** MatchOptions **   <a name="awscostmanagement-Type-budgets_ExpressionDimensionValues-MatchOptions"></a>
The match options that you can use to filter your results. You can specify only one of these values in the array.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

## See Also
<a name="API_budgets_ExpressionDimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/ExpressionDimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/ExpressionDimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/ExpressionDimensionValues)
