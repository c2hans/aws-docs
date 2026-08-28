---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/coding-agents.html
---

# Coding agents
<a name="coding-agents"></a>

Coding agents can reason about programming tasks, generate or modify code, and interact with developer environments, such as IDEs and CLIs. These agents combine natural-language understanding with structured reasoning to assist, augment, and automate software development, ranging from function generation to bug fixing and test authoring.

Unlike autocomplete tools, coding agents actively interpret user goals, query the development environment for context (for example, it opens files and traces errors), identify requirements, and then propose and perform actions.

## Architecture
<a name="architecture.f9afcb94-8586-537a-881c-4e77440f4240"></a>

A coding-agent pattern is shown in the following diagram:

![Coding agent.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/400980fd-a223-479b-b82b-0957743b19b6.png)

## Description
<a name="description.792d7b53-13aa-57f1-85e2-41ed3eb6f67a"></a>

1. Receives query
   + The user provides natural-language instructions through a command palette, chat window, or CLI (for example, "Add logging to this function" or "Refactor for readability").

1. Extracts environment context
   + The agent gathers context from the IDE, including active files, cursor position, code snippets and symbol tables.
   + It outputs error messages, test results, and outputs from other agents.

1. LLM reasoning
   + The agent sends a prompt, including the query and environmental context, to an LLM.
     + The LLM performs a reasoning pass to determine the following:
     + What needs to change
     + How to generate a solution
     + Any refactoring, rewriting, or coding steps

1. Executes actions
   + The LLM returns the output to the agent and imports it into the IDE or runtime environment.
   + This may include inserting or modifying code, generating comments or documentation, and triggering downstream build, test, and linting tasks.

## Capabilities
<a name="capabilities.ad946f20-628d-592c-b073-6d3c2a70241f"></a>
+ High-contextual awareness (for example, IDE state, cursor, and syntax tree)
+ Iterative reasoning of goals and feedback
+ Optional code planning and action separation (for example, first reason and then act)
+ Works in synchronous or asynchronous developer workflows

## Common use cases
<a name="common-use-cases.640fed29-4354-5558-88ff-95ed02d107d2"></a>
+ Code generation from task descriptions
+ Code refactoring and optimization
+ Test-case generation and validation
+ Error explanations and debugging
+ Documentation assistants
+ Paired programming copilots

## Implementation guidance
<a name="implementation-guidance.0df07ead-e069-5b3f-89e7-b0ca3675dae9"></a>
+ You can build this pattern using the following tools and AWS services:
+ Amazon Bedrock for LLM-driven generation and reasoning
+ Amazon Q Developer for coding suggestions and completions
+ AWS Lambda or Amazon Elastic Container Service (Amazon ECS) for running and testing sandbox environments
+ AWS Cloud9, VS Code extensions, or custom IDE integrations to host and evaluate context
+ Amazon Simple Storage Service (Amazon S3) for storing intermediate prompts, responses, and revision history

## Summary
<a name="summary.4c4ff110-962f-5566-ab8b-29b0fd36eaff"></a>

Coding agents are new AI-powered development tools that are capable of interpreting natural language, analyzing context, generating multistep code changes, and integrating with the software development lifecycle.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
