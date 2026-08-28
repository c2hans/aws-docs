---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/bedrock-agents.html
---

# Amazon Bedrock Agents
<a name="bedrock-agents"></a>

Amazon Bedrock Agents is a fully managed service that enables you to build and configure autonomous agents in your applications. It can orchestrate interactions between foundation models, data sources, software applications, and user conversations. Its streamlined approach to creating agents doesn't require you to provision capacity, manage infrastructure, or write custom code.

## Key features of Amazon Bedrock Agents
<a name="key-features-of-9999999999999999br--agents.dc9263bf-3a18-58e1-8847-b616923700e3"></a>

Amazon Bedrock Agents includes the following key features:
+ **Fully managed service** – Complete infrastructure management with no need to provision capacity or manage underlying systems. For more information, see [Automate tasks in your application using AI agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) in the Amazon Bedrock documentation.
+ **API-driven development** – Define and run agents through simple API calls by specifying models, instructions, tools, and configuration parameters. For more information, see [Create and configure agent manually](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html) in the Amazon Bedrock documentation.
+ **Action groups** – Define specific actions your agent can perform by creating action groups with API schemas. For more information, see [Use action groups to define actions for your agent to perform](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html) in the Amazon Bedrock documentation.
+ **Knowledge base integration** – Seamlessly connect to Amazon Bedrock Knowledge Bases to augment agent responses with your organization's data. For more information, see [Augment response generation for your agent with knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-add.html) in the Amazon Bedrock documentation.
+ **Advanced prompt templates** – Customize agent behavior through prompt templates for pre-processing, orchestration, knowledge base response generation, and post-processing. For more information, see [Enhance agent's accuracy using advanced prompt templates in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html) in the Amazon Bedrock documentation.
+ **Tracing and observability** – Track the agent's step-by-step reasoning process using built-in tracing capabilities. For more information, see [Track agent's step-by-step reasoning process using trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) in the Amazon Bedrock documentation.
+ **Versioning and aliases** – Create multiple versions of your agent and deploy them through aliases for controlled rollouts. For more information, see [Deploy and use an Amazon Bedrock agent in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-deploy.html) in the Amazon Bedrock documentation.

## When to use Amazon Bedrock Agents
<a name="when-to-use-9999999999999999br--agents.f90153d1-8087-5dbc-86a3-689ca12f45d4"></a>

Amazon Bedrock Agents is particularly well-suited for autonomous agent scenarios including:
+ Organizations that want a fully managed experience for building and deploying agents without managing infrastructure
+ Projects that require rapid development and deployment of agents through configuration rather than code
+ Use cases that benefit from tight integration with other Amazon Bedrock capabilities like Knowledge Bases and Guardrails
+ Teams without the in-house resources to build agents from scratch but need production-ready autonomous capabilities

## Implementation approach for Amazon Bedrock Agents
<a name="implementation-approach-for-9999999999999999br--agents.6f47d3be-fa6e-55b3-a774-634b5e5feed9"></a>

Amazon Bedrock Agents provides a configuration-based implementation approach for business stakeholders. The service enables organizations to:
+ Define agents through the AWS Management Console or API calls without writing complex code.
+ Create action groups that specify the APIs and operations that the agent can perform.
+ Connect knowledge bases to provide domain-specific information to the agent.
+ Test and iterate on agent behavior through a visual interface.

This managed approach allows business teams to rapidly develop and deploy autonomous agents without deep technical expertise in AI model development or infrastructure management.

## Real-world example of Amazon Bedrock Agents
<a name="real-world-example-of-9999999999999999br--agents.bab755c0-30bd-5ec1-9f16-a76d2b8b5d39"></a>

A financial operations (FinOps) solution described in this AWS blog post uses the Amazon Bedrock multi-agent framework to create an AI-driven cloud cost management assistant. The cost-effective Amazon Nova foundation model powers the solution where a central FinOps Supervisor agent delegates tasks to specialized agents. These agents fetch and analyze AWS spend data by using AWS Cost Explorer and generate cost-saving recommendations by using AWS Trusted Advisor.

The system includes secure user access through Amazon Cognito, a front-end hosted on AWS Amplify, and AWS Lambda action groups for real-time analysis and forecasting. Finance teams can ask natural language queries such as "What were my costs in February 2025?" The system responds with detailed breakdowns, optimization suggestions, and forecasts—all within a scalable, serverless architecture deployed by using AWS CloudFormation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
