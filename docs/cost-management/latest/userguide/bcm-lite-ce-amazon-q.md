---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/bcm-lite-ce-amazon-q.html
---

# Ask questions about your costs using Amazon Q Developer in the AWS Billing and Cost Management console
<a name="bcm-lite-ce-amazon-q"></a>

**Warning**
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

Cost Explorer lets you ask questions about your AWS costs. You can use suggested prompts or ask in your own words. When you ask a question, Amazon Q Developer opens a new chat panel in the console, and Cost Explorer can automatically update charts and report parameters.

Amazon Q Developer draws from extensive knowledge beyond what is visible in your current Cost Explorer view, including pricing data and budget information, to provide richer context and more comprehensive answers. If a follow-up question produces a visualization that Cost Explorer can display, it updates automatically. Otherwise, the visualization appears in Amazon Q Developer's artifacts panel while insights continue in the chat.

## Use suggested prompts
<a name="bcm-lite-ce-amazon-q-suggested-prompts"></a>

Cost Explorer displays suggested prompts above your Cost & Usage Overview data. These prompts surface the most commonly asked cost questions.

When you choose a suggested prompt, the following occurs:
+ The Amazon Q Developer chat panel opens automatically.
+ The prompt is submitted to Amazon Q Developer without requiring additional input.
+ Amazon Q Developer generates detailed insights in the chat panel.
+ Cost Explorer refreshes with the corresponding visualization, and all report parameters including filters, groupings, and date ranges are automatically configured in the Report Parameters panel.

## Use the Ask question button
<a name="bcm-lite-ce-amazon-q-ask-button"></a>

If you have a question that goes beyond our suggested prompts, choose **Ask question** to open a chat panel. You can ask a question in this panel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
