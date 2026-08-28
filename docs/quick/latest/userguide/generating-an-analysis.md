---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/generating-an-analysis.html
---

# Generating an analysis with natural language prompts
<a name="generating-an-analysis"></a>

With Quick Sight, you can generate multi-sheet analyses from natural language prompts. Describe the analysis you want, and Quick Sight creates multiple organized sheets with visuals, filter controls, and calculated fields such as year-over-year growth and month-over-month comparisons.

Before generation begins, you can review and modify an interactive plan that outlines the proposed structure.

The generated output is a native Quick Sight analysis. It works with existing publishing workflows, embedding patterns, CI/CD pipelines, and point-and-click editing in the analysis surface. After generation, you can refine each visual.

## Prerequisites
<a name="generate-analysis-prerequisites"></a>

To generate an analysis from a natural language prompt, you need the following:
+ An AWS account
+ Amazon Quick Enterprise Edition with at least one Author Pro user
+ At least one dataset in your Quick Sight account

## Generating an analysis
<a name="generate-analysis-procedure"></a>

Use the following procedure to generate an analysis from a natural language prompt.

**To generate an analysis from a natural language prompt**

1. Do one of the following:
   + Open a dataset and choose **Generate analysis**.
   + From the **Analyses** page, choose **Generate analysis**.
![Dataset page with Generate analysis button](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-1.png)

1. Choose **Add data** to select one to three datasets for the analysis. If your data spans multiple tables (for example, orders in one dataset and products in another), you can select them together.
![Add additional datasets](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-2a.png)
![Add additional datasets](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-2b.png)

1. Enter a natural language prompt that describes the analysis that you want to create. You can describe the business questions that you want answered, the metrics that you care about, and how you want the information organized across sheets.

   Example prompt:

   "Create an operations dashboard showing order volume trends, revenue KPIs, delivery performance comparing estimated vs actual delivery dates, and product category breakdown by revenue and order count. Include calculated fields for total revenue, average order value, and month-over-month order growth."
![Prompt input screen with example](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-3.png)

1. Do one of the following:
   + Choose **Generate analysis** to begin generation immediately.
   + Choose **Preview analysis outline** to review an outline first.

1. Wait while Quick Sight analyzes your dataset structure and column statistics. Real-time progress updates display the current status.
![Streaming progress screen showing steps completing](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-4.png)
**Note**
If you navigate away from the progress screen, you can check the generation status on the **Analyses** page by choosing the **Generations** tab. Choose the generation name to return to the progress screen.
![Generations tab to check status](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-5.png)

1. Quick Sight presents a two-pane view:
   + The left pane shows your initial prompt and a summary of the selected datasets.
   + The right pane shows the proposed filter controls, sheets, and visuals planned for each sheet.

   You can edit sheet names, add or remove visuals, adjust the plan, and refine the prompt before generating.
![Two-pane plan view with context on left, outline details on right](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-6.png)

1. Choose **Generate**. Real-time progress updates display the current status. Generation takes 2 to 5 minutes depending on the number of sheets and visuals.
![Generation progress showing sheets being created one by one](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-7.png)

![Completed analysis with multiple sheets and visuals](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-8.gif)

## Publishing a generated analysis
<a name="generate-analysis-publish"></a>

 After you are satisfied with the generated analysis, choose **Publish** to create a dashboard.

You can share the dashboard with other users, embed it in applications, or schedule email deliveries. For more information about publishing and sharing, see [Publishing dashboards](creating-a-dashboard.md) and [Sharing Quick Sight analyses](sharing-analyses.md).

![Publish and share dialog](http://docs.aws.amazon.com/quick/latest/userguide/images/visualize-data-figure-9.gif)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
