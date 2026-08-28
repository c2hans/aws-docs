---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_WidgetConfig.html
---

# WidgetConfig
<a name="API_bcmDashboards_WidgetConfig"></a>

Defines the complete configuration for a widget, including data retrieval settings and visualization preferences.

## Contents
<a name="API_bcmDashboards_WidgetConfig_Contents"></a>

 ** displayConfig **   <a name="awscostmanagement-Type-bcmDashboards_WidgetConfig-displayConfig"></a>
The configuration that determines how the retrieved data should be visualized in the widget.
Type: [DisplayConfig](API_bcmDashboards_DisplayConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** queryParameters **   <a name="awscostmanagement-Type-bcmDashboards_WidgetConfig-queryParameters"></a>
The parameters that define what data the widget should retrieve and how it should be filtered or grouped.
Type: [QueryParameters](API_bcmDashboards_QueryParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_bcmDashboards_WidgetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/WidgetConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/WidgetConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/WidgetConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
