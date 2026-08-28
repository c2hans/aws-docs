---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_Widget.html
---

# Widget
<a name="API_bcmDashboards_Widget"></a>

A configurable visualization component within a dashboard that displays specific cost and usage metrics. Each widget can show data as charts or tables and includes settings for data querying, filtering, and visual presentation.

## Contents
<a name="API_bcmDashboards_Widget_Contents"></a>

 ** configs **   <a name="awscostmanagement-Type-bcmDashboards_Widget-configs"></a>
An array of configurations that define the data queries and display settings for the widget.
Type: Array of [WidgetConfig](API_bcmDashboards_WidgetConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** title **   <a name="awscostmanagement-Type-bcmDashboards_Widget-title"></a>
The title of the widget.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z0-9_-][ a-zA-Z0-9_-]*[a-zA-Z0-9_-]`
Required: Yes

 ** description **   <a name="awscostmanagement-Type-bcmDashboards_Widget-description"></a>
A description of the widget's purpose or the data it displays.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** height **   <a name="awscostmanagement-Type-bcmDashboards_Widget-height"></a>
The height of the widget in row spans. The dashboard layout consists of a grid system.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 10.
Required: No

 ** horizontalOffset **   <a name="awscostmanagement-Type-bcmDashboards_Widget-horizontalOffset"></a>
Specifies the starting column position of the widget in the dashboard's grid layout. Used to control widget placement.
Type: Integer
Required: No

 ** id **   <a name="awscostmanagement-Type-bcmDashboards_Widget-id"></a>
The unique identifier for the widget.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** width **   <a name="awscostmanagement-Type-bcmDashboards_Widget-width"></a>
The width of the widget in column spans. The dashboard layout consists of a grid system.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 6.
Required: No

## See Also
<a name="API_bcmDashboards_Widget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/Widget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/Widget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/Widget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
