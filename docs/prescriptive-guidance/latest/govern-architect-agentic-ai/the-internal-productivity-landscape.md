---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/the-internal-productivity-landscape.html
---

# Internal productivity applications
<a name="the-internal-productivity-landscape"></a>

These applications operate with a mix of internal data and web sources, creating a need to establish a secure environment for innovation while respecting the boundaries of corporate information security. They represent the foundation upon which many organizations build their AI capabilities, and can be categorized as:
+ Simple chatbots, which answer questions based on internal and public knowledge
+ Personal AI assistants, which use an agentic workflow to act, not just provide answers
+ Autonomous team agents, which work on your tasks in the background

## Simple chatbot
<a name="simple-chatbot"></a>

Whether accessed through an internal web page, via a plugin, or in a desktop app, this company chatbot should be your team's go-to tool for securely rewriting text, conducting research, or searching internal knowledge bases. Accessibility, integration with the local environment, knowledge depth, and ease of use are the key factors driving adoption. Examples uses:
+ Summarize a document
+ Rewrite raw notes into meeting minutes
+ Find specific information from internal knowledge bases

## Personal AI assistant
<a name="personal-ai-assistant"></a>

Consider having a digital assistant focused entirely on your individual needs – a tireless companion that helps manage your tasks, organizes your schedule, and retrieves information exactly when you need it. These assistants represent the most personal form of AI integration in the workplace, working alongside you throughout your day to handle the routine cognitive tasks that can distract from higher-value work.

These assistants integrate seamlessly with your email, calendar, and personal document management systems, adapting to your preferences and patterns over time. They can draft responses to routine emails, suggest optimal meeting times based on your schedule and priorities, summarize long email threads, and quickly locate the document that you saved months ago but can't quite remember where.

Access rights are tied to each individual user – your assistant only accesses information you're authorized to see, and doesn't inadvertently access information meant for others.

Examples:
+ Send a personalized email to a large audience
+ Log your customer relationship management (CRM) activities
+ Create a ticket
+ Automate the "copy paste" of data from one system to another by extracting, formatting and submitting it in appropriate formats
+ Interact with browser-based applications and populate web forms

## Autonomous team agent
<a name="autonomous-team-agent"></a>

Autonomous team agents are designed to handle complete workflows for specific organizational roles. These agents guide business processes in the background while keeping humans in control at critical decision points.

Examples:
+ Autonomous supply chain management agent, which monitors sales and inventory while factoring in supply chain variables such supplier delays, geopolitical events, and minimum batch quantities. Based on this data, the agent predicts out-of-stock and overstocking risks and can propose placing purchase orders directly in your enterprise resource planning (ERP) system.
+ Request for quotation (RFQ) agent, which scans your team folders to find previous quotation requests, then anonymizes and shares with your team your answers, thus capitalizing on existing knowledge.
+ Agent that auto-enriches project tasks with relevant ERP data (budgets, suppliers, costs, lead-time).
+ Autonomous compliance agent for document tagging and classification, including export control and sensitivity labeling.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
