---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-prompt-chaining.html
---

# Workflow for prompt chaining
<a name="workflow-for-prompt-chaining"></a>

Prompt chaining decomposes complex tasks into a sequence of steps, where each step is a discrete LLM invocation that processes or builds upon the output of the previous one.

![Workflow for prompt chaining.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/80105fdd-60a1-490e-a114-b8220676cf43.png)

The prompt chaining workflow is suited for scenarios where tasks can be logically divided into sequential reasoning steps, and where intermediate outputs inform the next stage. It excels in workflows that require structured thinking, progressive transformation, or layered analysis, such as document review, code generation, knowledge extraction, and content refinement.

## Description
<a name="description.fed89350-4472-562d-881f-c040eb6437ea"></a>
+ The complexity of the task exceeds the context window or reasoning depth of a single LLM call.
+ Outputs from one step (for example, analysis, summarization, or planning) become inputs for a follow-up decision or generation phase.
+ You need transparency and control across reasoning stages (for example, auditable intermediate results).
+ You want to plug in external validation, filtering, or enrichment logic between steps.
+ It's ideal for agents operating in pipeline-style reasoning loops, such as research agents, editorial assistants, planning systems, and multistage copilots.

## Capabilities
<a name="capabilities.1c9f2c40-df61-5b40-acee-2ab65dde6a9f"></a>
+ Linear or branching chains of LLM calls
+ Intermediate results passed as structured input or embedded into follow-up prompts
+ Can be orchestrated with AWS Step Functions, AWS Lambda, or agent-specific runners

## Common use cases
<a name="common-use-cases.0a8a02d1-c741-5973-ab98-255c9826794d"></a>
+ Multistep reasoning tasks (for example, "summarize critique rewrite")
+ Research assistants synthesizing layered outputs (for example, "search extract facts answer question")
+ Code generation pipelines ("generate plan write code test code explain output")

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
