---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_TagValues.html
---

# TagValues
<a name="API_bcmDashboards_TagValues"></a>

Specifies tag-based filtering options for cost and usage queries.

## Contents
<a name="API_bcmDashboards_TagValues_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-bcmDashboards_TagValues-key"></a>
The key of the tag to filter on.
Type: String
Required: No

 ** matchOptions **   <a name="awscostmanagement-Type-bcmDashboards_TagValues-matchOptions"></a>
The match options for tag values, such as `EQUALS`, `CONTAINS`, `STARTS_WITH`, or `ENDS_WITH`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

 ** values **   <a name="awscostmanagement-Type-bcmDashboards_TagValues-values"></a>
The values to match for the specified tag key.
Type: Array of strings
Required: No

## See Also
<a name="API_bcmDashboards_TagValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/TagValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/TagValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/TagValues)
