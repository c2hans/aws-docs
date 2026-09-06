---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/analyses.html
---

# Analyses
<a name="analyses"></a>

 Analyses module allows you to create and modify dashboards based on the clickstream datasets in a drag-and-drop approach. It provides greater flexibility for users to create business-specific metrics and visualizations. You can use the module to:
+  create dashboard that are not provided in preset dashboard or not supported by explorations.
+  make changes to the custom dashboard saved from exploration analysis, such as adding calculation fields to calculate custom metrics, adjust visual types etc.
+  join clickstream data with external datasets, such as adding item master data to enrich clickstream datasets.

## Access Analyses
<a name="access-analyses"></a>

 To access Analyses, follow below steps:

1.  Go to **Clickstream Analytics on AWS Console**, in the **Navigation Bar**, click on "**Analytics Studio**", a new tab will be opened in your browser.

1.  In the Analytics Studio page, click the **Analyses** icon in the left navigation panel.

## How it works
<a name="how-it-works"></a>

 Analyses module is essentially the author interface of QuickSight, in which you have the admin access to all the QuickSight functionalities, for example, create analysis, add or manage datasets, publish and share dashboards.

**Note**
 Only the user with Administrator or Analyst role can access this module.

The guidance automatically added the following datasets for each project and app, which contains all fields of event, user, and session tables, making it easy for you do custom analysis.

|  **Dataset name**  |  **Description**  |
| --- | --- |
|  Event\_View\_app\_name\_project\_name  |  Event data that includes all public event parameters  |

 To create a custom analysis, you can follow below QuickSight documentation to prepare data and create visualization:

1.  [Connecting to data](https://docs.aws.amazon.com/quicksight/latest/user/working-with-data.html)

1.  [Preparing data](https://docs.aws.amazon.com/quicksight/latest/user/preparing-data.html)

1.  [Visualizing data](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html)
