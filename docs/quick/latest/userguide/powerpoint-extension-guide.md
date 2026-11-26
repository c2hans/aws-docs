---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/powerpoint-extension-guide.html
---

# AWS Quick Microsoft PowerPoint extension

The AWS Quick extension for PowerPoint helps you go from an idea to a presentation-ready deck. Quick builds slides directly in your deck using your company's brand assets, your organization's knowledge, and live data from your dashboards.

You can search for AWS Quick in the Microsoft PowerPoint app store or visit the [Quick for PowerPoint Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010606) to add the extension.

Key capabilities include:
+ **Draft decks from your enterprise knowledge:** Generate complete presentations from an outline, a topic, or an existing document. Ground slides in your spaces, knowledge bases, connected tools, and the web, and bring in charts and metrics from your Quick dashboards and datasets. Run research on a market, competitor, or trend, and turn its findings and charts into slides. For more information about research, see [Using AWS Quick Research](using-amazon-quick-research.md).
+ **Stay on brand:** Apply your company's brand assets so that every deck uses approved themes, fonts, and colors. Quick respects your existing primary slides, layouts, and formatting, and generates images and visuals that fit your slide design. For more information, see [Managing brand assets](brand-assets.md).
+ **Review and refine with natural language:** Select slides or content and ask Quick to rewrite, redesign, or restructure them. Add, delete, and reorder slides, and review every change that Quick makes.
+ **Connect your work across tools:** Build a deck from a flow's results, such as an account briefing flow that gathers a customer's CRM history, support tickets, and usage trends. Use your [connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html) to act on your deck, such as sharing it to a team channel or logging commitments from a customer pitch in your CRM. Pick up where you left off, such as turning an analysis from the AWS Quick desktop application or a Word document into a deck.
+ **Get personalized results:** Quick learns your preferences and writing style over time. For more information, see [Memory and response personalization](using-quick-chat.md#chat-memory).

**Important**
The AWS Quick PowerPoint extension uses generative AI to create and execute code within your PowerPoint application sandbox. AI can make mistakes and perform inaccurate actions within your PowerPoint slide deck. No presentation data is read when the side panel is closed, and no data is sent to AWS Quick unless you explicitly send a prompt.
AWS Quick does not use your user data for service improvement or for training its underlying large language models (LLMs).

**Note**
The AWS Quick Microsoft PowerPoint extension supports two runtimes. On Windows, it uses the Microsoft Edge WebView2 runtime. On macOS, it uses the WebKit2 runtime.
To understand Office add-in runtimes and install Microsoft Edge WebView2, see [Understanding the Office Add-ins runtime](https://devblogs.microsoft.com/microsoft365dev/understanding-office-add-ins-runtime/) on the Microsoft Developer Blogs website.

**Note**
When you use the extension, the time AWS Quick spends working on your requests is metered per second and counts toward agent hours. For more information, see the [AWS Quick pricing page](https://aws.amazon.com/quick/pricing/).

## AWS Quick Microsoft PowerPoint extension usage guidelines
<a name="powerpoint-usage-guidelines"></a>

As a user, you are responsible for keeping company information safe. The following guidance helps you use AWS Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy
<a name="powerpoint-conversation-retention"></a>

AWS Quick keeps each conversation for 365 days. It keeps conversations that you pin or move to a folder for 750 days. You can review and manage your conversation history by choosing the conversation history button in the PowerPoint extension. For more information about retention periods, see [Usage limits](usage-limits.md).

AWS Quick uses generative AI. You should review responses for accuracy.

Usage of the AWS Quick extension for Microsoft PowerPoint is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations
<a name="powerpoint-security-considerations"></a>

To protect your organization's data, carefully evaluate usage and plan deployment with data privacy in mind. AWS Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft PowerPoint conversations into your company's AWS Quick instance.

## Sample prompts
<a name="powerpoint-sample-prompts"></a>

The following prompts demonstrate common ways to use Quick within PowerPoint. You can adapt these to your specific needs.
+ "Create a 10-slide presentation on [topic] including key metrics and recommendations, pulling data from my Quick dashboard."
+ "Research the top 3 competitors in [market] and add a comparison slide with your findings."
+ "Turn [Word document name] into a 6-slide deck using our brand assets."
+ "Make this deck more executive-friendly by reducing text and emphasizing key numbers."
+ "Generate an image for the title slide that fits the deck's design."
+ "Run my account briefing flow for [customer name] and build a quarterly business review deck from the results."
+ "Create a chart slide comparing actual vs. target performance by department using data from my Quick space."

**Tip**
For best results, be specific in your prompts. Include names, dates, and goals. You can also reference your Quick spaces, dashboards, and knowledge bases for personalized results.
