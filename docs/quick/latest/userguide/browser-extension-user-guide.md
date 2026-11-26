---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/browser-extension-user-guide.html
---

# AWS Quick browser extension

**Important**
The AWS Quick browser extension extension doesn't need any admin setup to install and use.

The AWS Quick browser extension helps you get answers about any web page without switching tabs. Quick understands the page you're viewing, grounds its answers in your organization's knowledge, and helps you act on the page in your connected apps.

Key capabilities include:
+ **Understand any web page:** Ask questions about the page you're viewing or about several open tabs at once. Right-click any selection to get an explanation or to chat about it with Quick. Pull out key details, compare sources, and draft content from what you're reading.
+ **Reach your enterprise knowledge:** Type **@Quick** in your address bar or open Quick from your browser toolbar to ask anything. Get answers from your spaces, knowledge bases, dashboards, and connected apps, or switch to a specialized agent for curated responses.
+ **Curate your organization's knowledge:** Ask Quick to add a web page to a space so that your team can use it in future work.
+ **Connect your work across tools:** Use your [connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html) to act on the page, such as updating a ticket's status or logging a prospect in your CRM. Run flows with the page as context, and turn your web research into a Word document or a PowerPoint deck.
+ **Get personalized responses:** Quick learns your preferences and writing style over time. For more information, see [Memory and response personalization](using-quick-chat.md#chat-memory).

**Topics**
+ [Supported browsers](#browser-extension-supported-browsers)
+ [Browser extension benefits](#browser-extension-benefits)
+ [Browser extension use cases](#browser-extension-use-cases)
+ [Run AWS Quick Flows in the browser extension](#browser-extension-run-flows)
+ [Sample prompts](#browser-extension-sample-prompts)
+ [Install and configure the browser extension](#install-and-configure-browser)
+ [Deploy the browser extension in your organization](#deploy-browser-extension-organization)
+ [Browser extension usage guidelines](#browser-extensions-usage-guidelines)
+ [Browser extension known limitations](#browser-extension-known-limitations)

## Supported browsers
<a name="browser-extension-supported-browsers"></a>

The Quick browser extension is compatible with the following browsers:
+ Google Chrome
+ Mozilla Firefox
+ Microsoft Edge

## Browser extension benefits
<a name="browser-extension-benefits"></a>

The Quick browser extension brings your enterprise knowledge and connected apps into the browser, so you can work with web content without switching applications.
+ Ask questions about the page you're viewing or several open tabs, and compare information across sources.
+ Get an explanation of any text that you select on a page.
+ Get answers from your spaces, knowledge bases, dashboards, and connected apps from your address bar or browser toolbar.
+ Analyze files that you upload alongside the web pages in your conversation.
+ Add useful web pages to a space for your team.
+ Run flows and take actions in your connected apps using the page as context, without leaving your browser.

## Browser extension use cases
<a name="browser-extension-use-cases"></a>

The following are common use cases that help you make the best use of your Quick browser extension:

**Ask about the page you're viewing**

Use this procedure to summarize a web page, pull out key details, or ask questions about it without reading the entire page.

1. Navigate to the web page that you want to ask about.

1. Open the Quick browser extension and sign in.

1. In the chat window, enter your request, such as **Summarize this page**.

You can continue to chat about the web page and ask follow-up questions.

**Add tabs to a conversation**

Use this procedure to include several open tabs in your conversation so that you can analyze and compare information across web pages.

1. In the chat window, choose the **\+** button, and then choose **Add tabs**.

1. Choose the tabs that you want to include in your Quick conversation.

You can now chat about all of the tabs that you added to the conversation.

**Ask about a selection on a page**

Use this procedure to get an explanation of specific text on a web page.

1. On the web page, select the text that you want to ask about.

1. Right-click the selection, and then choose the Quick option to get an explanation or to chat about the selection.

**Ask Quick from your address bar**

Use this procedure to ask a question of your enterprise knowledge from any tab.

1. In your browser's address bar, enter **@Quick** followed by your question.

1. Press **Enter**.

Quick answers from your spaces, knowledge bases, dashboards, and connected apps. You can also open Quick from your browser toolbar to ask a question.

**Add a web page to a space**

Use this procedure to save a web page to a space so that your team can use it in future work.

1. Navigate to the web page that you want to add.

1. In the chat window, ask Quick to add the page to a space, such as **Add this page to my [space name] space**.

**Add files to a conversation**

Upload files to enhance your conversation with document analysis capabilities.

1. Choose the **paperclip** icon.

1. Choose the files to add to the conversation.

1. Choose **Add to chat**.

The files are now available to use in the Quick conversation.

**Reset conversation context**

Start fresh when you need to clear your current conversation context.

1. Choose the **\+ icon inside the bubble** to start a new conversation.

1. Alternatively, reset your conversation by choosing the **X** icon to end the current conversation, then open the Quick extension to start a new one.

This clears all previous context and allows you to begin with a clean slate.

**Use actions in chat**

Take actions in your connected apps using the web page as context.

1. Ask Quick to perform a specific action, such as **Update the status of this ticket to resolved** or **Log this prospect's details in our CRM**.

1. Follow the prompts in the chat and on-screen to complete the action.

This enables you to perform tasks in external applications without leaving your browser.

## Run AWS Quick Flows in the browser extension
<a name="browser-extension-run-flows"></a>

You can run any flow that you created or that was shared with you directly from the browser extension chat. The flow can use the web pages in your conversation as context. You need permission to run flows in your AWS Quick account.

**Run a flow**

1. Open the Quick browser extension.

1. (Optional) To include other open tabs as context, choose the **\+** button, choose **Add tabs**, and then choose the tabs.

1. In the chat window, ask Quick to run the flow by name, such as **Run my account briefing flow for this customer**.

1. When Quick prompts you for required inputs, provide them in the chat.

While the flow runs, the extension shows a progress tracker with the completed and remaining steps, and displays the flow's outputs in the chat. To stop the flow, choose **End** in the progress tracker. You can then continue your conversation.

Quick saves your flow runs in your conversation history. To view a past run or resume an incomplete flow, open your conversation history and choose the conversation that contains the flow run.

For more information about flows, see the [flows documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html).

## Sample prompts
<a name="browser-extension-sample-prompts"></a>

The following prompts demonstrate common ways to use Quick in your browser. You can adapt these to your specific needs.
+ "Summarize this page and list the three most important points."
+ "Compare the pricing and features described in these tabs in a table."
+ "How does this article relate to our strategy in my [space name] space?"
+ "Draft a short email to my team summarizing this announcement."
+ "Add this page to my [space name] space."
+ "Log this prospect's company details as a new lead in our CRM."

**Tip**
For best results, be specific in your prompts. Include names, dates, and goals. You can also reference your Quick spaces, dashboards, and knowledge bases for personalized results.

## Install and configure the browser extension
<a name="install-and-configure-browser"></a>

As a user, you can install and configure the browser extensions with the following steps.
+ Mozilla based browsers — [Mozilla Firefox Add-ons web store](https://addons.mozilla.org/en-GB/firefox/addon/amazon-quick/)
+ Chromium based browsers (including Microsoft Edge) — [Chrome Web Store](https://chromewebstore.google.com/detail/amazon-quick/innkphffipcmiflfibbeghfnkifiokgo)

Once you have successfully logged on, you can use your Quick browser extension.

**Note**
You can also **pin** your Quick browser extension to have it readily accessible while using your browser. Instructions for this are specific to your browser of choice. The following third-party information about pinning extensions might be helpful.
Google Chrome — [https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar](https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar)
Mozilla Firefox — [https://support.mozilla.org/en-US/kb/extensions-button\#w\_manage-pinned-extensions](https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions)
Microsoft Edge — [https://www.microsoft.com/en-us/edge/features/pin-to-taskbar](https://www.microsoft.com/en-us/edge/features/pin-to-taskbar)

## Deploy the browser extension in your organization
<a name="deploy-browser-extension-organization"></a>

As an author, after enabling the browser extension in your Quick application, you can deploy it across your organization using enterprise management tools and policies.

For Google Chrome Enterprise environments, you can use organizational unit policies to manage extension deployment. The Chrome Web Store for Enterprise provides additional deployment options specifically designed for organizational use. Mozilla Firefox Enterprise offers similar capabilities through policy templates and enterprise distribution methods that allow for automated extension deployment across the organization. Microsoft Edge Enterprise provides policy settings for managing extensions through mobile device management (MDM) software.

Policy settings from browser vendors: [Firefox](https://mozilla.github.io/policy-templates/#extensionsettings), [Chrome](https://chromeenterprise.google/policies/#ExtensionSettings), and [Edge](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings).

**Deploy to Google Chrome Enterprise**

Follow these steps to deploy the browser extension across your Chrome Enterprise environment.

1. Access your Google Admin console and navigate to the Chrome management section.

1. Configure extension policies using organizational units to target specific user groups or departments.

1. Use the [Chrome extension management guide](https://support.google.com/chrome/a/answer/9296680?hl=en) to set up automated installation policies.

1. Reference the [Chrome Web Store Enterprise documentation](https://developer.chrome.com/docs/webstore/cws-enterprise) for advanced deployment configurations.

The extension will now be automatically installed for all users in your Chrome Enterprise environment.

**Deploy to Mozilla Firefox Enterprise**

Use these steps to deploy the extension across your Firefox Enterprise environment.

1. Configure Firefox deployment policies using the enterprise policy framework.

1. Follow the [Firefox extension deployment guide](https://support.mozilla.org/en-US/kb/deploying-firefox-with-extensions) for step-by-step instructions.

1. Use the [enterprise distribution documentation](https://extensionworkshop.com/documentation/enterprise/enterprise-distribution/) to configure organization-wide deployment.

1. Apply extension settings using [Mozilla policy templates](https://mozilla.github.io/policy-templates/#extensionsettings) for centralized configuration management.

The extension is now deployed across your Firefox Enterprise environment with centralized management.

**Deploy to Microsoft Edge Enterprise**

Deploy the extension to Microsoft Edge Enterprise using these organizational deployment steps.

1. Install the browser extension for all users using the software deployment processes of your organization.

1. Configure extension settings using [Edge policy settings](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings) through mobile device management (MDM) software.

1. Follow the [Microsoft Edge extension management guide](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide) for detailed deployment instructions.

Your Microsoft Edge Enterprise deployment is complete with centralized policy management.

## Browser extension usage guidelines
<a name="browser-extensions-usage-guidelines"></a>

As a user, you are responsible for keeping company information safe. The following guidelines help you use Quick browser extensions securely while maintaining data privacy and compliance.

### Using the browser extension
<a name="browser-extensions-usage"></a>

When using the Quick browser extension, users can review past conversations and attachments to maintain context across browsing sessions.

### Conversation retention and data privacy
<a name="conversation-retention-policy"></a>

AWS Quick keeps each conversation for 365 days. It keeps conversations that you pin or move to a folder for 750 days. You can review and manage your conversation history by choosing the conversation history button in the browser extension. For more information about retention periods, see [Usage limits](usage-limits.md).

## Browser extension known limitations
<a name="browser-extension-known-limitations"></a>

The following are known limitations of the AWS Quick browser extension:
+ The browser extension supports up to a total of 20 web pages and uploaded files at a time. For more information, see [Upload files and chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html#file-uploads).
