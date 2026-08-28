---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GroupDefinition.html
---

# GroupDefinition
<a name="API_bcmDashboards_GroupDefinition"></a>

Specifies how to group cost and usage data.

## Contents
<a name="API_bcmDashboards_GroupDefinition_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-bcmDashboards_GroupDefinition-key"></a>
The key to use for grouping cost and usage data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** type **   <a name="awscostmanagement-Type-bcmDashboards_GroupDefinition-type"></a>
The type of grouping to apply.
Type: String
Valid Values: `DIMENSION | TAG | COST_CATEGORY`
Required: No

## See Also
<a name="API_bcmDashboards_GroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/GroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/GroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/GroupDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
