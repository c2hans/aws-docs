---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-preview.html
---

# Previewing a custom lens for a workload in AWS WA Tool
<a name="lenses-preview"></a>

**To preview a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Only lenses in a **DRAFT** status can be previewed. Select the desired **DRAFT** custom lens and choose **Preview experience**.

1. Choose **Next** to navigate through the lens preview.

1. (Optional) You can review your **Improvement plan** by selecting best practices within each question in the preview, and choosing **Update based on answers** to test your risk logic. If there are changes needed, you can update the [Risk Rules](lenses-format-specification.md#lenses-format-risk-rules) in your JSON template before publishing.

1. Choose **Exit Preview** to go back to the custom lens.

**Note**
You can also preview a custom lens by selecting **Submit & Preview** when [Creating a custom lens](lenses-create.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
