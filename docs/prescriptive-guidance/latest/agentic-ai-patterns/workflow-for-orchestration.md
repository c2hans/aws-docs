---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-orchestration.html
---

# Workflow for orchestration
<a name="workflow-for-orchestration"></a>

A central orchestrator agent uses an LLM to plan, decompose, and delegate subtasks to specialized worker agents or models, each with a specific role or domain expertise. This mirrors human team structures and supports emergent behavior across multiple agents.

![Workflow for orchestration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/9b41d8cf-bd37-4aa8-8e13-80888c0b7c55.png)

The orchestration workflow is ideal for scenarios that are complex, hierarchical, or multidisciplinary, requiring structured decomposition and specialized execution. It is particularly well-suited to tasks that require division of labor, where different subcomponents of a task are best handled by agents with distinct capabilities, knowledge, or toolsets.

This workflow is particularly effective when:
+ Tasks can be divided into subtasks that vary in scope, type, or reasoning (for example, plan, research, implement, and test).
+ An LLM or meta-agent must coordinate other agents, monitor progress, and synthesize results.
+ You want to modularize agent responsibilities, enabling scalability, reuse, and specialized tuning.
+ The system requires role-based behavior, mimicking how human teams (for example, project managers, developers, and reviewers) operate in collaboration.

Orchestration is ideal for multiturn planning agents, software development copilots, enterprise process agents, and autonomous project executors. It is especially useful when implementing multi-agent systems that require centralized task breakdown but distributed execution logic, enabling extensibility and more explainable behavior across agent layers.

## Capabilities
<a name="capabilities.d4903c3a-5050-59b9-acd7-1fd66665da1c"></a>
+ Orchestrator performs goal meta-reasoning
+ Worker agents may include tool access, memory, or domain-specific prompting
+ Can be hierarchical (that is, multilevel task delegation)

## Common use cases
<a name="common-use-cases.cc5398ad-17e0-5972-9991-828d190f0609"></a>
+ Project managers, coordinating researchers, writers, and quality-assurance agents
+ Coding copilots that combine planning, executing, and testing
+ Agents that supervise toolchains or API access patterns

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
