---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html
---

# DimensionValues
<a name="API_DimensionValues"></a>

The metadata that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

## Contents
<a name="API_DimensionValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-DimensionValues-Key"></a>
The names of the metadata types that you can use to filter and group your results. For example, `AZ` returns a list of Availability Zones.
Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.
 `LINKED_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html).
 `ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE` can only be used in [AnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html).
Type: String
Valid Values: `AZ | INSTANCE_TYPE | LINKED_ACCOUNT | PAYER_ACCOUNT | LINKED_ACCOUNT_NAME | OPERATION | PURCHASE_TYPE | REGION | SERVICE | SERVICE_CODE | USAGE_TYPE | USAGE_TYPE_GROUP | RECORD_TYPE | OPERATING_SYSTEM | TENANCY | SCOPE | PLATFORM | SUBSCRIPTION_ID | LEGAL_ENTITY_NAME | DEPLOYMENT_OPTION | DATABASE_ENGINE | CACHE_ENGINE | INSTANCE_TYPE_FAMILY | BILLING_ENTITY | RESERVATION_ID | RESOURCE_ID | RIGHTSIZING_TYPE | SAVINGS_PLANS_TYPE | SAVINGS_PLAN_ARN | PAYMENT_OPTION | AGREEMENT_END_DATE_TIME_AFTER | AGREEMENT_END_DATE_TIME_BEFORE | INVOICING_ENTITY | ANOMALY_TOTAL_IMPACT_ABSOLUTE | ANOMALY_TOTAL_IMPACT_PERCENTAGE`
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-DimensionValues-MatchOptions"></a>
The match options that you can use to filter your results.
 `MatchOptions` is only applicable for actions related to cost category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.
The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | CASE_SENSITIVE | CASE_INSENSITIVE | GREATER_THAN_OR_EQUAL`
Required: No

 ** Values **   <a name="awscostmanagement-Type-DimensionValues-Values"></a>
The metadata values that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_DimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DimensionValues)
