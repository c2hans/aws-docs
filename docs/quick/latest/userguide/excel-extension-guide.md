---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/excel-extension-guide.html
---

# AWS Quick Microsoft Excel extension

The AWS Quick extension for Excel helps you build models and workbooks faster. Quick works directly in your spreadsheet, pulls in data from your dashboards, knowledge bases, and connected tools, and helps you validate your numbers before you share them.

You can search for AWS Quick in the Microsoft Excel app store or visit the [Quick for Excel Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010611) to add the extension.

Key capabilities include:
+ **Build models and workbooks from your data:** Pull data from Quick dashboards, datasets, spaces, connected tools, and uploaded files into your workbook. Describe the model or report that you need, and Quick builds it with formulas, structure, and formatting. Quick applies templates, filters, formatting, and conditional formatting directly to your cells.
+ **Validate and debug:** Ask Quick to explain the logic behind any cell, formula, or table. Find and fix formula errors, inconsistencies, and anomalies, and review every change that Quick makes to your workbook.
+ **Run deep analysis:** Analyze trends, run sensitivity analysis, and plan scenarios using natural language. Create pivot tables and charts with a single prompt, and turn your analysis into a report that's ready to share.
+ **Use enterprise knowledge:** Choose an agent or a space to respond from, and bring relevant information from your organization's knowledge into your spreadsheets.
+ **Connect your work across tools:** Use your [connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html) to act on your workbook, such as updating forecasts in your planning system or filing a ticket for each budget variance. Pick up where you left off, such as using an Excel analysis to write a Word document or a PowerPoint deck.

**Important**
The AWS Quick Excel extension uses generative AI to create and execute code within your Excel application sandbox. AI can make mistakes and perform inaccurate actions within your Excel workbook. No spreadsheet data is read when the side panel is closed, and no data is sent to AWS Quick unless you explicitly send a prompt.
AWS Quick does not use your user data for service improvement or for training its underlying large language models (LLMs).

**Note**
The AWS Quick Microsoft Excel extension supports two runtimes. On Windows, it uses the Microsoft Edge WebView2 runtime. On macOS, it uses the WebKit2 runtime.
To understand Office add-in runtimes and install Microsoft Edge WebView2, see [Understanding the Office Add-ins runtime](https://devblogs.microsoft.com/microsoft365dev/understanding-office-add-ins-runtime/) on the Microsoft Developer Blogs website.

**Note**
When you use the extension, the time AWS Quick spends working on your requests is metered per second and counts toward agent hours. For more information, see the [AWS Quick pricing page](https://aws.amazon.com/quick/pricing/).

## AWS Quick Microsoft Excel extension usage guidelines
<a name="excel-usage-guidelines"></a>

As a user, you are responsible for keeping company information safe. The following guidance helps you use AWS Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy
<a name="excel-conversation-retention"></a>

AWS Quick keeps each conversation for 365 days. It keeps conversations that you pin or move to a folder for 750 days. You can review and manage your conversation history by choosing the conversation history button in the Excel extension. For more information about retention periods, see [Usage limits](usage-limits.md).

AWS Quick uses generative AI. You should review responses for accuracy.

Usage of the AWS Quick extension for Microsoft Excel is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations
<a name="excel-security-considerations"></a>

To protect your organization's data, carefully evaluate usage and plan deployment with data privacy in mind. AWS Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Excel conversations into your company's AWS Quick instance.

## Sample prompts
<a name="excel-sample-prompts"></a>

The following prompts demonstrate common ways to use Quick within Excel. You can adapt these to your specific needs.
+ "Import data from my Quick dashboard and identify which items are trending above or below target."
+ "Create a pivot table showing totals by category and region."
+ "Build a 12-month revenue forecast model with assumptions on a separate sheet."
+ "Explain the formula in cell D5 and suggest a more efficient approach."
+ "Find and fix any formula errors or inconsistencies in this sheet."
+ "Run a sensitivity analysis on gross margin if unit costs rise by 5%, 10%, and 15%."
+ "File a ticket for each budget line that's more than 10% over plan."

**Tip**
For best results, be specific in your prompts. Include names, dates, and goals. You can also reference your Quick spaces, dashboards, and knowledge bases for personalized results.
