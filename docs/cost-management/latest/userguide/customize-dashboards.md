---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/customize-dashboards.html
---

# Customizing dashboards
<a name="customize-dashboards"></a>

After adding widgets, you can customize your dashboard layout and settings. You can drag widgets to different positions and resize them to emphasize important information.

Time periods can be managed at both the dashboard and widget level:
+ Set a dashboard-level time period that applies to all widgets. This setting affects all widgets temporarily and resets when you leave or refresh the dashboard.
+ Configure individual widget time periods. These settings are saved with each widget and persist when you return to the dashboard.

**Note**
The Budget report widget displays data in table format only. Visualization type options (line chart, bar chart, stacked bar chart) do not apply to Budget report widgets. The dashboard level time period filter does not apply to Budget report widgets, as budget data is retrieved directly from the AWS Budgets service.

**Note**
The Cost Efficiency widget supports only line chart and table visualization types. In line chart view, the widget shows your efficiency score percentage over time. In table view, it shows cost efficiency percentage grouped by your selected dimension (AWS account, region, or overall).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
