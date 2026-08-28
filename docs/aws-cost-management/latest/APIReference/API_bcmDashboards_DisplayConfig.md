---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DisplayConfig.html
---

# DisplayConfig
<a name="API_bcmDashboards_DisplayConfig"></a>

Defines how the widget's data should be visualized, including chart type, color schemes, axis configurations, and other display preferences.

## Contents
<a name="API_bcmDashboards_DisplayConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** graph **   <a name="awscostmanagement-Type-bcmDashboards_DisplayConfig-graph"></a>
The configuration for graphical display of the widget data, including chart type and visual options.
Type: String to [GraphDisplayConfig](API_bcmDashboards_GraphDisplayConfig.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Required: No

 ** table **   <a name="awscostmanagement-Type-bcmDashboards_DisplayConfig-table"></a>
The configuration for tabular display of the widget data.
Type: [TableDisplayConfigStruct](API_bcmDashboards_TableDisplayConfigStruct.md) object
Required: No

## See Also
<a name="API_bcmDashboards_DisplayConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/DisplayConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/DisplayConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/DisplayConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
