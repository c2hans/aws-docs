---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/generative-bi-build-calculations.html
---

# Build calculations with Generative BI
<a name="generative-bi-build-calculations"></a>

With Generative BI, you can use natural language prompts to create calculated fields in Amazon Quick Sight, as shown in the following image. For more information about calculated fields in analyses, see [Adding calculated fields](adding-a-calculated-field-analysis.md).

![Adding a calculated field with the Build tool.](http://docs.aws.amazon.com/quick/latest/userguide/images/gen-bi-build-calculation-1.png)

**To build a calculated field with Generative BI**

1. Navigate to the analysis that you want to work in and choose **Data** from the toolbar at the top of the page. Then choose **Add calculated field**.

1. In the calculation editor that appears, choose **Build**.

1. Describe the calculation outcome that you want to achieve. For example, "year over year percent change in daily sales."

1. Choose **BUILD**.

1. Review the expression that's returned, and then choose **Insert** to add it to the expression editor. You can also choose the **Copy** icon to copy the expression to your clipboard. To delete the expression and start over, choose the **Delete** icon next to the expression.

1. When you're finished, close the editor.

After you add a calculation to the expression editor, you must name the calculation before you can save it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
