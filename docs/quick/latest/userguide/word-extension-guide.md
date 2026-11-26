---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/word-extension-guide.html
---

# AWS Quick Microsoft Word extension

The AWS Quick extension for Word helps you go from a blank page to a review-ready draft without leaving Word. Quick writes directly in your document, grounds every draft in your organization's knowledge, and learns your preferences and writing style over time.

You can search for AWS Quick in the Microsoft Word app store or visit the [Quick for Word Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010615) to add the extension.

Key capabilities include:
+ **Draft documents from scratch:** Describe what you need, and Quick writes it directly into your document, complete with headings, tables, and styling. Ground drafts in your spaces, knowledge bases, dashboards, connected tools, and the web.
+ **Edit and refine:** Ask Quick to rewrite, restructure, shorten, or change the tone of any section or selection. Quick matches your document's existing styles and formatting, or applies a template that you provide. Review every change that Quick makes and keep only what you want.
+ **Review and redline against your rules:** Ask Quick to review your document against your criteria, policies, or reference documents. Suggestions appear in Word's track changes and comments, so you decide what gets accepted.
+ **Connect your work across tools:** Run flows and use your [connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html) to act on your document, such as filing tickets for open issues or adding redlined terms to a deal record. Pick up where you left off, such as turning an analysis from the AWS Quick desktop application into a Word document. Add your document to a space to curate your organization's knowledge for future drafts.
+ **Get personalized drafts:** Quick learns your preferences and writing style over time. For more information, see [Memory and response personalization](using-quick-chat.md#chat-memory).

**Important**
The AWS Quick Word extension uses generative AI to create and execute code within your Word application sandbox. AI can make mistakes and perform inaccurate actions within your Word document. No document content is read when the side panel is closed, and no data is sent to AWS Quick unless you explicitly send a prompt.
AWS Quick does not use your user data for service improvement or for training its underlying large language models (LLMs).

**Note**
The AWS Quick Microsoft Word extension supports two runtimes. On Windows, it uses the Microsoft Edge WebView2 runtime. On macOS, it uses the WebKit2 runtime.
To understand Office add-in runtimes and install Microsoft Edge WebView2, see [Understanding the Office Add-ins runtime](https://devblogs.microsoft.com/microsoft365dev/understanding-office-add-ins-runtime/) on the Microsoft Developer Blogs website.

**Note**
When you use the extension, the time AWS Quick spends working on your requests is metered per second and counts toward agent hours. For more information, see the [AWS Quick pricing page](https://aws.amazon.com/quick/pricing/).

## AWS Quick Microsoft Word extension usage guidelines
<a name="word-usage-guidelines"></a>

As a user, you are responsible for keeping company information safe. The following guidance helps you use AWS Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy
<a name="word-conversation-retention"></a>

AWS Quick keeps each conversation for 365 days. It keeps conversations that you pin or move to a folder for 750 days. You can review and manage your conversation history by choosing the conversation history button in the Word extension. For more information about retention periods, see [Usage limits](usage-limits.md).

AWS Quick uses generative AI. You should review responses for accuracy.

Usage of the AWS Quick extension for Microsoft Word is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations
<a name="word-security-considerations"></a>

To protect your organization's data, carefully evaluate usage and plan deployment with data privacy in mind. AWS Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Word conversations into your company's AWS Quick instance.

## Sample prompts
<a name="word-sample-prompts"></a>

The following prompts demonstrate common ways to use Quick within Word. You can adapt these to your specific needs.
+ "Create a project proposal including an executive summary, timeline, and budget section, pulling data from my Quick space."
+ "Review this contract against our standard terms in [reference document] and redline any deviations with track changes."
+ "Read the comments in this document and address each piece of feedback, making the requested changes directly."
+ "Shorten the background section by half and make the tone more formal."
+ "Add a competitive comparison table to this document using data from my Quick dashboard."
+ "File a ticket for each open issue in this review."
+ "Add this document to my [space name] space."

**Tip**
For best results, be specific in your prompts. Include names, dates, and goals. You can attach reference documents or templates to guide formatting and style.
