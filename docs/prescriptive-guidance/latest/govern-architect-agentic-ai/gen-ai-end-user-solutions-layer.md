---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/gen-ai-end-user-solutions-layer.html
---

# Applications layer – generative AI end-user solutions
<a name="gen-ai-end-user-solutions-layer"></a>

This layer includes user-facing applications that enable interaction with agentic AI systems. The components within this layer serve as the primary interface between end users and the underlying agentic infrastructure, providing conversational interfaces for natural language interaction, productivity features that augment workflows with AI assistance, and no-code tools that allow business users to create and deploy custom agents. They also provide interfaces to schedule and monitor the execution of agents.

![Architecture diagram generative AI end-user solutions](http://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/273e816d-d871-4c5e-af86-932c5ab0e0bf.png)

## Purpose and characteristics
<a name="purpose-and-characteristics"></a>

The generative AI End-User Solutions Component provides capabilities that include:
+ Conversational interfaces – enable natural language interaction with AI agents through chat (text or multimodal) and voice experiences.
+ Productivity augmentation – integrate AI capabilities directly into daily workflows and productivity tools to enhance efficiency. Examples include code assistants, meeting summarization tools, and document generation assistants.
+ Citizen developer enablement – provide no-code/low-code platforms for creating custom agents or defining AI augmented workflows without specialized technical skills.

## AWS solutions for this layer
<a name="aws-solutions-for-this-layer"></a>

Organizations can implement this layer using these AWS solutions:

### Amazon Quick
<a name="9999999999999999qslong-.2ddf6fc2-62fe-5862-a6d4-46f365326843"></a>

[ Amazon Quick](https://aws.amazon.com/quick/getting-started/) provides a unified productivity platform that delivers:
+ Enterprise-wide AI-powered search and knowledge management across structured and unstructured company data
+ No-code/low-code agent creation capabilities enabling citizen developers to build custom agents
+ Integrated workflows and automation through Quick Flows
+ Deep research capabilities (Quick Research) for comprehensive analysis and long-form report generation
+ Collaboration tools including Spaces for organizing files, dashboards, and knowledge bases
+ Extensibility through integration with internal and external tools, via MCP and connectorsKiro

[Kiro](https://kiro.dev/) serves as an AI-powered code assistant that:
+ Transforms natural language requirements into comprehensive technical specifications through its spec mode
+ Accelerates software development workflows through intelligent code generation
+ Generates comprehensive project deliverables including functional specifications, design documents, documentation, and test cases
+ Can create custom agents powered by MCP tools to interact with internal systems

### Claude Code with Amazon Bedrock
<a name="claude-code-with-amazon-bedrock.779963c7-08aa-58e2-994a-d1f0d6cc653e"></a>

[Claude Code with Amazon Bedrock](https://aws.amazon.com/solutions/guidance/claude-code-with-amazon-bedrock/) brings Anthropic's AI-powered coding assistant to enterprises with the security and enterprise-grade capabilities of Amazon Bedrock. This solution integrates directly with developer terminals and IDEs, enabling natural language interaction for code generation, review, and modification while leveraging Bedrock's fully managed infrastructure for strict security controls, compliance features, and scalability.

[AWS provides guidance](https://aws.amazon.com/solutions/guidance/claude-code-with-amazon-bedrock/) that demonstrates how organizations can implement Claude Code with secure enterprise authentication using industry-standard protocols and AWS services. The solution enables terminal-integrated development through conversational commands, replaces long-term access keys with temporary session-based credentials through standardized federation protocols, supports Model Context Protocol (MCP) for connecting external tools and data sources, and provides observability into developer productivity patterns and usage metrics.

### Custom-built solutions
<a name="custom-built-solutions.9330c18c-6d2c-53bc-96ee-19c987836e20"></a>

Organizations requiring tailored implementations can leverage:
+ AWS Bedrock Chat ([https://github.com/aws-samples/bedrock-chat](https://aws.amazon.com/solutions/guidance/claude-code-with-amazon-bedrock/)) as an open-source foundation for self-managed deployments
+ Custom enterprise portals integrated with existing systems using AWS services
+ Bespoke applications built on Amazon Bedrock for domain-specific requirements leveraging 3rd party frontend solutions such as [v0 AI SDK](https://ai-sdk.dev/docs/introduction), [CopilotKit](https://webflow.copilotkit.ai/), and [Open WebUI.](https://github.com/open-webui/open-webui)

## Integration patterns
<a name="integration-patterns"></a>

End-user solutions in this layer integrate with the underlying architecture through:
+ Connector based integration – Pre-built and custom connectors that enable seamless integration with third-party applications and data sources without custom code development. For instance, Quick Suite provides connectors to collaboration platforms (Slack, Microsoft Teams), productivity tools (Asana, Jira), cloud storage services (OneDrive, SharePoint, Google Drive), and more. Similarly, a bespoke application could use Bedrock Knowledge Bases, which provides connectors to enterprise data sources including Confluence, SharePoint, Salesforce, and web crawlers for authorized public web pages.
+ API-based integration – RESTful and WebSocket APIs for real-time communication with enterprise systems
+ Agent-to-system protocols – Standardized protocols (such as MCP) for connecting AI applications with external data sources and tools, enabling agents to access enterprise resources through unified interfaces
+ Event-driven patterns – Webhook and event subscriptions using Amazon EventBridge for asynchronous workflows
+ Embedded experiences – Widgets and iframes for seamless integration into existing applications
+ Identity federation – Single sign-on (SSO) through AWS IAM Identity Center, OIDC and OAuth 2.0 with integration with enterprise identity providers for secure end-user access control

## Implementation approaches
<a name="implementation-approaches"></a>

Organizations can choose between two primary approaches:
+ Off-the-shelf solutions – Platforms like [ Amazon Quick](https://aws.amazon.com/quick/getting-started/) , [Kiro](https://kiro.dev/), and [Claude Code with Amazon Bedrock](https://aws.amazon.com/solutions/guidance/claude-code-with-amazon-bedrock/) that provide immediate productivity gains with minimal configuration
+ Custom applications – Tailored implementations to meet specific organizational requirements

This modular approach allows organizations to balance speed of deployment with customization needs, selecting the right solution based on their technical capabilities, timeline, and specific use case requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
