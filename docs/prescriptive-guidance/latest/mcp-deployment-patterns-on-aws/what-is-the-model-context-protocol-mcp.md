---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/what-is-the-model-context-protocol-mcp.html
---

# What is the Model Context Protocol (MCP)?
<a name="what-is-the-model-context-protocol-mcp"></a>

## Overview
<a name="overview.5da40455-4dbf-5184-ba4b-b19db1536bfc"></a>

The Model Context Protocol (MCP) is an open protocol introduced by Anthropic that enables seamless integration between LLM applications and external data sources and tools to access real-time information. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

## Why MCP Matters
<a name="why-mcp-matters.4bde6f1f-8c84-5d8c-8ab6-0221a4534483"></a>

Traditional AI applications operate in isolation, lacking access to organization-specific data, internal APIs, and business tools. Each integration requires custom development, creating fragmentation and maintenance overhead. MCP addresses this challenge by providing a standardized protocol for AI applications to discover and interact with contextual resources through three core primitives:

1. Resources, which expose data and content such as files, databases, and APIs to AI applications

1. Tools, which enable LLM's to run actions like creating tickets, running queries, or calling APIs; and

1. Prompts, which provide reusable prompt templates with dynamic context.

## Key Benefits
<a name="key-benefits.df9e2345-6759-5991-92db-2b1639a89325"></a>

MCP delivers several significant advantages for organizations building AI-powered applications.
+ Standardization through a single protocol eliminates the need for custom integrations for each AI-to-system connection.
+ Discoverability allows AI applications to automatically discover available capabilities without manual configuration.
+ Security is enhanced through centralized authentication and authorization at the protocol level.
+ Maintainability improves as you can update integration logic once and benefit all connected AI applications.
+ The protocol's extensibility enables adding new data sources and tools without modifying AI applications.

### Common use cases
<a name="common-use-cases"></a>

Organizations deploy MCP servers to enhance AI applications across various domains:
+ AI Development Tools: Organizations deploy MCP servers to connect with AI-powered development tools like Kiro, Claude Code, Codex, Cursor, or custom AI coding assistants with version control repositories, enabling real-time code analysis and context-aware suggestions. These integrations provide access to internal code documentation, API references, and sandboxed development environment ,  helping coding agents understand project structure and dependencies while limiting tool and filesystem access. The MCP server exposes organization-specific context and approved development operations to the AI assistant, enabling repository-aware analysis, user-directed code changes, access to internal libraries and documentation, and controlled CI/CD actions.  This approach significantly accelerates development workflows by providing AI with a comprehensive understanding of the codebase and organizational coding standards.
+ Enterprise Knowledge Access: Enterprise knowledge management becomes significantly more accessible when MCP servers connect AI assistants to document management systems, databases, wikis, and internal knowledge bases. Employees can query organizational information conversationally, asking natural language questions that retrieve relevant documentation, technical specifications, and historical decisions. The MCP server provides secure access to customer documentation, support articles, product catalogs, and technical specifications, enabling AI assistants to ground responses and improve accuracy.
+ Workflow Automation: MCP servers enable AI to interact directly with business process tools, creating a powerful automation layer for routine tasks. AI assistants can create and update tickets in project management systems like Jira or Asana, interact with CRM platforms to access and update customer data, and trigger business process automation workflows based on conversational requests. This integration streamlines operations by reducing context switching between tools and enabling voice-driven or chat-driven workflow execution.
+ Data Analysis: MCP servers enable AI assistants to generate reports, create visualizations, and summarize business metrics by providing access to data warehouses, business intelligence tools, and analytics platforms without writing SQL queries or navigating complex dashboard interfaces.
+ Customer Support: Customer support operations benefit significantly from MCP servers that provide AI assistants with a comprehensive customer context. Support agents and AI chatbots gain access to customer databases, order history, product catalogs, and inventory systems through standardized MCP interfaces. AI assistants can provide personalized recommendations based on customer preferences and past behavior, resolve common issues by referencing similar cases, and if required, escalating complex problems with full context to human agents. The result is faster resolution times, improved customer satisfaction, and reduced operational overhead for support teams.
