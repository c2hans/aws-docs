---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/details-report.html
---

# Details report
<a name="details-report"></a>

 You can use the Details report to view common and custom dimensions for individual events, query all user attributes for a specific user, and see the events that a particular user has performed

**Note**
This article describes the default report. You can customize the report by applying filters or comparisons or by changing the dimensions, metrics, or charts in QuickSight. For more information, refer to [Visualizing data in Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

## View the report
<a name="view-the-report-6"></a>

1.  Access the dashboard for your application. Refer to [Access dashboard](dashboards-1.md#view-dashboards).

1.  In the dashboard, choose the sheet with name of `Details`.

## Data sources
<a name="where-the-data-comes-from-6"></a>

 User reports are created based on the following QuickSight dataset:

| **QuickSight dataset**  |  **Redshift view / table**  |  **Description**  |
| --- | --- | --- |
| Event\_View-<app>-<project>  | clickstream\_event\_view\_v3  | This datasets stores all the raw event data joined with user attributes and session attributes.  |

### Dimensions
<a name="dimensions-2"></a>

 This report includes all the available dimensions for event, user, and session tables. Please refer to [Data Schema](data-schema.md) for each dimensions.

### Metrics
<a name="metrics-2"></a>

 This report does not any metrics by default.

## Sample dashboard
<a name="sample-dashboard-6"></a>

Below image is a sample dashboard for your reference.

![Dashboard displaying event details, custom parameters, and user attributes tables.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/details.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
