---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/customizing-missing-data-controls.html
---

# Missing data on visual types in Quick
<a name="customizing-missing-data-controls"></a>

You can customize how missing data points are visualized in your line charts and area charts. You can choose to have your missing data points appear in the following formats:
+ *Broken line*: A disjointed line that breaks when a data point is missing. This is the default missing data format.
+ *Continuous line*: Displays a continuous line by skipping over the missing data point and connecting the line to the next available data point in the series. To show a continuous line, the **Show date gaps** box on the **X axis** pane should be unchecked.
+ *Show as zero*: Sets the value of the missing data point to zero.

**To customize a visual's missing data settings**

1. On the analysis page, choose the visual that you want to format.

1. Choose the **Format visual** icon in the upper right corner of the visual to access the **Format visual** menu.

1. Open the **Y axis** pane of the format visual menu and navigate to the **Missing data** section.

1. Select the missing data format that you want.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
