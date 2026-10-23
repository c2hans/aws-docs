---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html
---

# What is the Agent Toolkit for AWS?
<a name="what-is-agent-toolkit"></a>

The Agent Toolkit for AWS gives AI coding agents the tools, knowledge, and guardrails they need to build, deploy, and manage applications on AWS. It works with the coding agents that developers already use, such as Kiro, Claude Code, Cursor, and Codex. You don't need to switch tools or learn a new workflow.

The Agent Toolkit for AWS is not itself an AI coding agent. It has no chat interface and no model of its own. It is the AWS-facing layer that your agent connects to: it provides the tools your agent calls to work in your AWS account, the current AWS documentation it reads, and the IAM-governed path it takes to reach AWS. To install it for your agent, see [Getting started](quick-start.md). To decide whether it fits what you are trying to do, see [When to use the Agent Toolkit for AWS](#agent-toolkit-when-to-use).

AI coding agents can handle common AWS tasks like creating an Amazon S3 bucket or launching an Amazon EC2 instance. However, they often struggle with complex, multi-step workflows. They choose the wrong service for a use case, misconfigure resources, or repeatedly retry operations on newer services they were not trained on. The Agent Toolkit for AWS addresses these gaps. It gives agents secure access to AWS services, current documentation, and step-by-step guidance.

**Topics**
+ [When to use the Agent Toolkit for AWS](#agent-toolkit-when-to-use)
+ [Common tasks and where to start](#agent-toolkit-common-tasks)
+ [Components](#agent-toolkit-components)
+ [How the Agent Toolkit for AWS works](#how-agent-toolkit-works)
+ [Pricing](#agent-toolkit-pricing)

## When to use the Agent Toolkit for AWS
<a name="agent-toolkit-when-to-use"></a>

Use the Agent Toolkit for AWS when you already work with an AI coding agent and you want that agent to work in your AWS account. You keep the agent, editor, and workflow you have. The Agent Toolkit for AWS adds the AWS-facing layer that the agent connects to.

Adding the Agent Toolkit for AWS to an agent gives you the following:
+ **Build, deploy, and operate** – Your agent creates AWS infrastructure, writes application code, and deploys it, guided by skills for service selection, configuration, and deployment. Skills also cover the operational work that follows, such as reading CloudWatch logs and metrics and checking CloudFormation stack status. See [Available skills](skills.md#available-skills).
+ **AWS access that IAM governs** – Your agent reaches AWS with your existing IAM credentials, so the permissions you already maintain decide what it can do. The AWS MCP Server adds the `aws:ViaAWSMCPService` and `aws:CalledViaAWSMCP` condition keys to every request, so you can write policies that apply only to agent-initiated calls, and CloudTrail records the calls. See [Identity and access management for AWS MCP Server](security-iam.md).
+ **Current AWS information instead of training data** – Your agent searches and reads AWS documentation and checks AWS Region and service availability at the time it needs the answer, rather than relying on what its model was trained on. See [AWS Knowledge Tools](understanding-mcp-server-tools.md#aws-knowledge-tools).
+ **Procedures that AWS publishes and maintains** – Skills give your agent step-by-step procedures, decision guides, and reference material for a specific AWS task, so it follows a tested path instead of improvising. See [Skills](skills.md).
+ **Task-specific toolsets for operational work** – A capability groups helper functions that handle one kind of AWS task. For example, the serverless capability inspects a running Lambda function and its connected resources, read-only, to explain why the function is failing. See [Capabilities](capabilities.md).
+ **One integration for the agents you use** – The same AWS MCP Server endpoint works with Claude Code, Cursor, Codex, Devin, Kiro, Visual Studio Code, GitHub Copilot, Windsurf, Cline, and any other agent that supports the Model Context Protocol, so you do not build and maintain a separate AWS integration for each agent. See [Getting started](quick-start.md).
+ **No additional charge** – You pay only for the AWS resources your agent provisions or interacts with. See [Pricing](#agent-toolkit-pricing).

### What the Agent Toolkit for AWS does not do
<a name="agent-toolkit-what-it-is-not"></a>

The following boundaries help you place the Agent Toolkit for AWS in your setup:
+ **It is not an agent, and it includes no model** – The Agent Toolkit for AWS does not decide what to build or write code on its own. Your agent does that, and calls the Agent Toolkit for AWS when it needs to reach AWS.
+ **It does not replace your agent, editor, or IDE** – Installing the Agent Toolkit for AWS adds an AWS MCP Server connection and a set of skills to the agent you already run. Your projects, prompts, and workflow continue to work as before.
+ **It does not add permissions** – An agent that uses the Agent Toolkit for AWS can do only what the IAM identity behind your credentials is allowed to do. If your policies deny a call, the Agent Toolkit for AWS does not work around the denial. Requests that only search documentation or discover skills need no credentials at all.
+ **It does not keep your data** – The AWS MCP Server is a stateless proxy that runs AWS API calls on your behalf. It does not use persistent storage for customer content. See [Data protection in AWS MCP Server](data-protection.md).

## Common tasks and where to start
<a name="agent-toolkit-common-tasks"></a>

You use the Agent Toolkit for AWS by asking your agent for the outcome you want, in the agent you already use. You do not call the tools yourself. The agent selects the skill, capability, or tool that fits your request, runs it through the AWS MCP Server, and reports back. The following table lists tasks the Agent Toolkit for AWS supports, what handles each task, and where each one is documented.

| Task | What handles it, and where to start |
| --- | --- |
| Connect the agent you already use to AWS. | Install the `aws-core` plugin for your agent, add the AWS MCP Server to your MCP configuration, or run the AWS CLI setup wizard. See [Getting started](quick-start.md). |
| Find out why a running Lambda function is failing or slow, or what changed before it broke. For example, "Why is my checkout function timing out?" | The serverless capability inspects the function and its connected resources, read-only, through the `diagnose`, `search_logs`, `get_live_config`, `get_recent_changes`, and `get_trace_summary` helper functions. See [Serverless capability](capabilities.md#aws-serverless-capability). |
| Check what AWS documents today for a service or API, instead of what your agent remembers. For example, "Look up the current request parameters for this API." | The `aws___search_documentation` and `aws___read_documentation` knowledge tools search AWS documentation and return page content to your agent. These tools require no credentials. See [AWS Knowledge Tools](understanding-mcp-server-tools.md#aws-knowledge-tools). |
| Confirm that a service or feature is available where you plan to deploy. For example, "Is this feature available in the AWS Region I use?" | The `aws___list_regions` and `aws___get_regional_availability` knowledge tools return AWS Region information and availability for services, features, SDK APIs, and CloudFormation resources. See [AWS Knowledge Tools](understanding-mcp-server-tools.md#aws-knowledge-tools). |
| Run an AWS operation that takes several API calls. For example, "List the Amazon S3 buckets in this account that do not have versioning enabled." | The `aws___run_script` API tool runs Python with AWS API access in a sandboxed environment, using your IAM credentials. Use it for listing resources, parallel calls, cross-service checks, and multi-step workflows. See [AWS API Tools](understanding-mcp-server-tools.md#aws-api-tools). |
| Have your agent follow an AWS procedure for a task instead of improvising. For example, "Configure a least-privilege IAM policy for this function." | Skills provide the steps, decision guides, and reference material for the task. Your agent retrieves them at runtime with `aws___retrieve_skill`, or uses skills that a plugin installed locally. See [Skills](skills.md). |
| Work in more than one AWS account in the same session. For example, "Compare this setting between my dev and prod accounts." | Configure more than one credential profile for the MCP Proxy for AWS, using SigV4 authentication. Your agent then routes individual requests to the profile you name. OAuth sessions are bound to a single IAM role and cannot switch profiles. See [Multi-profile support](multi-account-access.md). |
| Restrict what your agent can do in your account, for example to keep it read-only. | Scope down the IAM role that your agent uses, and write policies on the `aws:ViaAWSMCPService` and `aws:CalledViaAWSMCP` condition keys to allow or deny agent-initiated calls. See [Identity-based policy examples for AWS MCP Server](security_iam_id-based-policy-examples.md). |
| Review what agents have done in your account. | The AWS MCP Server publishes CloudWatch metrics for tool invocations, and CloudTrail logs the API calls it makes on your behalf. See [Monitoring AWS MCP Server](monitoring-overview.md). |

## Components
<a name="agent-toolkit-components"></a>

The Agent Toolkit for AWS includes four components that work together:
+ **AWS MCP Server** – A managed server that gives agents access to AWS through the Model Context Protocol (MCP). Kiro, Claude Code, Cursor, Codex, Devin, and other MCP-compatible agents connect to this server. Agents can search AWS documentation and get service information without authentication. To run API calls, execute Python scripts, or follow curated skills, agents authenticate with your existing AWS Identity and Access Management (IAM) credentials. A single endpoint provides all these capabilities, with CloudWatch metrics and IAM-based access controls.
+ **Agent skills** – Curated packages of instructions, code scripts, and reference materials that help agents complete specific AWS tasks. Agents load skills on demand. They discover and retrieve only the skills relevant to the current task, so they do not consume unnecessary context. Skills cover service selection, step-by-step procedures, troubleshooting, and SDK best practices.
+ **Plugins** – Single-install packages for Claude Code, Codex, and Devin that bundle the AWS MCP Server configuration and a curated set of agent skills. After you install a plugin, your agent is ready to work with AWS. Kiro connects to the AWS MCP Server directly and does not require a plugin.
+ **Rules files** – Project-level configuration files that set guardrails and preferences for how agents work in your project. Rules files tell agents how to use AWS most effectively and securely. For example, they direct agents to use the AWS MCP Server, discover available skills, or search documentation before acting.

## How the Agent Toolkit for AWS works
<a name="how-agent-toolkit-works"></a>

The Agent Toolkit for AWS helps your AI coding agent build on AWS in three ways:
+ **Skills provide structured guidance** – Your agent uses skills installed locally through a plugin or discovers them at runtime through the AWS MCP Server. Skills contain step-by-step instructions, decision guides, and reference materials. These guide your agent through complex procedures while following AWS best practices.
+ **Knowledge tools provide current information** – When your agent needs up-to-date information, it can search AWS documentation and retrieve API references. It can also check regional availability and access the latest AWS service information.
+ **API tools execute authenticated actions** – The AWS MCP Server translates requests into properly formatted AWS API calls, handles authentication with your IAM credentials, and returns detailed feedback about results and errors. For complex multi-step operations, your agent can write and run Python scripts in an isolated sandbox using the `aws___run_script` tool. For the full list of tools, see [Understanding the MCP Server tools](understanding-mcp-server-tools.md).

The AWS MCP Server automatically adds two global condition context keys (`aws:ViaAWSMCPService` and `aws:CalledViaAWSMCP`) to all requests. These keys let you differentiate MCP-initiated actions from direct API calls in your IAM policies. CloudTrail logs all API calls for audit visibility.

Authentication and authorization use your existing AWS IAM roles and policies, so you maintain full control over what your agent can access and do. You can authenticate using SigV4 credentials through the MCP Proxy for AWS, or use OAuth 2.1 through AWS Sign-in for a direct connection without local proxy software. See [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md) for OAuth setup.

**Note**
We recommend scoping down IAM roles to the minimum permissions that your agent needs to perform its task.

## Pricing
<a name="agent-toolkit-pricing"></a>

You can use the Agent Toolkit for AWS at no additional charge. You pay only for the AWS resources your agent provisions or interacts with, at standard AWS pricing. For more information about AWS pricing, see [AWS Pricing](https://aws.amazon.com/pricing/). If you are new to AWS, you can get started with many services for free. For more information, see [AWS Free Tier](https://aws.amazon.com/free/).
