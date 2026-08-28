---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/hiding-a-visual-by-default.title.html
---

# Hiding a visual by default
<a name="hiding-a-visual-by-default.title"></a>

In the **Interactions** pane of the **Properties** pane, you can choose to hide a visual by default. Doing this can be useful if you want the viewer to only see visuals based on specific conditions.

**To hide a visual by default**

1. From the Quick homepage, choose **Analyses**, and then choose the analysis that you want to customize.

1. Choose the visual that you want to add a rule to.

1. On the menu in the upper-right hand side of the visual, choose **Properties**.

1. In the **Properties** pane that opens, choose **Interactions** and open the **Rules** dropdown.

1. In the **Rules** menu, choose **Hide this visual by default**.

Hidden visuals appear fully hidden in a viewing dashboard. In the **Analyses** pane, hidden visuals are visible with the message “Hidden based on rule”. With this display, you can see where all of a dashboard's visuals are located.

**Note**
You can't create conditional rules that hide visuals that are already hidden by default or that show visuals that already appear by default. If you change the default appearance of a visual, existing rules that contradict the new default appearance will be disabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
