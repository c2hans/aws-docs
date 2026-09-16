---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DimensionValues.html
---

# DimensionValues
<a name="API_bcmDashboards_DimensionValues"></a>

Specifies the values and match options for dimension-based filtering in cost and usage queries.

## Contents
<a name="API_bcmDashboards_DimensionValues_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-bcmDashboards_DimensionValues-key"></a>
The key of the dimension to filter on (for example, `SERVICE`, `USAGE_TYPE`, or `OPERATION`).
Type: String
Valid Values: `AZ | INSTANCE_TYPE | LINKED_ACCOUNT | OPERATION | PURCHASE_TYPE | REGION | SERVICE | USAGE_TYPE | USAGE_TYPE_GROUP | RECORD_TYPE | RESOURCE_ID | SUBSCRIPTION_ID | TAG_KEY | OPERATING_SYSTEM | TENANCY | BILLING_ENTITY | RESERVATION_ID | COST_CATEGORY_NAME | DATABASE_ENGINE | LEGAL_ENTITY_NAME | SAVINGS_PLANS_TYPE | INSTANCE_TYPE_FAMILY | CACHE_ENGINE | DEPLOYMENT_OPTION | SCOPE | PLATFORM | BUDGET_NAME | BUDGET_THRESHOLD | HEALTH_STATUS | BILLING_VIEW_ARN | BUDGET_TYPE | SEVERITY | ASSESSMENT | MONITOR_TYPE | ANOMALY_ID`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-bcmDashboards_DimensionValues-values"></a>
The values to match for the specified dimension key.
Type: Array of strings
Required: Yes

 ** matchOptions **   <a name="awscostmanagement-Type-bcmDashboards_DimensionValues-matchOptions"></a>
The match options for dimension values, such as `EQUALS`, `CONTAINS`, `STARTS_WITH`, or `ENDS_WITH`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

## See Also
<a name="API_bcmDashboards_DimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/DimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/DimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/DimensionValues)
