---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-routing.html
---

# Workflow for routing
<a name="workflow-for-routing"></a>

In the routing pattern, a classifier or router agent uses an LLM to interpret the intent or category of a query, then routes the input to a specialized downstream task or agent.

![Workflow for routing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/52fbdfab-504f-4221-967e-ca873f963a00.png)

The Routing workflow is used in scenarios where an agent must quickly classify input intent, task type, or domain, and then delegate the request to a specialized subagent, tool, or workflow. It is especially useful in capability agents, such as those that serve as general assistants, front doors to enterprise functions, or user-facing AI interfaces that span domains.

Routing is particularly effective when:
+ Triaging requests across a variety of tasks (for example, search, summarization, booking, calculations).
+ Inputs must be preprocessed or normalized before entering more specialized workflows.
+ Different input types (for example, images vs. text, structured vs. unstructured queries) require custom handling.
+ An agent is acting as a conversational switchboard, delegating tasks to specialized agents or microservices.
+ This workflow is common in domain-specific copilots, customer-support bots, enterprise service routers, and multimodal agents, where intelligent dispatching determines both the quality and efficiency of agent behavior.

## Capabilities
<a name="capabilities.7ed924be-9dba-56b2-8b6a-2f3cd758921b"></a>
+ A first-pass LLM acts as a dispatcher
+ Routes can invoke distinct workflows or even other agent patterns
+ Supports modular expansion of capabilities

## Common use cases
<a name="common-use-cases.a56e7754-8b02-5d82-8186-b9f4e3c0d9ac"></a>
+ Multidomain assistants ("is this a legal, medical, or financial question?")
+ Decision trees enhanced with LLM reasoning
+ Dynamic tool selection (for example, search vs. code generation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
