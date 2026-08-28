---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-evaluators-and-reflect-refine-loops.html
---

# Workflow for evaluators and reflect-refine loops
<a name="workflow-for-evaluators-and-reflect-refine-loops"></a>

This workflow provides a feedback loop where one LLM generates a result, and another evaluates or critiques the result. This promotes self-reflection, optimization, and iterative improvements.

![Workflow for evaluator.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/1afcc739-ce67-41c9-aad2-a197bb0058bb.png)

The evaluator workflow is ideal for scenarios where output quality, accuracy, and alignment are important and where single-pass generation is unreliable or insufficient. This workflow excels when agents must self-critique, iterate, and refine their outputs—either to meet a higher standard of correctness or to explore improved alternatives based on feedback.

This workflow is particularly effective when:
+ The output involves subjective quality metrics (for example, style, tone, and readability) or objective criteria (for example, correctness, safety, and performance).
+ The agent must reason through trade-offs, evaluate constraints, or optimize toward a goal.
+ You require built-in redundancy and quality assurance, especially in regulated, customer-facing, or creative domains.
+ Human-in-the-loop review is expensive or unavailable, and autonomous validation is desired.

This workflow is used for content generation, code synthesis and review, policy enforcement, alignment checking, instruction tuning, and RAG postprocessing. It is also useful for self-improving agents, where continuous feedback helps shape better responses over time to build trustworthy, autonomous decision loops.

## Common use cases
<a name="common-use-cases.9af7a9ff-35a2-55a9-b0da-1ad5329dd630"></a>
+ Red-team agents compared to blue-team agents
+ Agents that generate, evaluate, and revise code or plans
+ Quality assurance, hallucination detection, and style enforcement

## Capabilities
<a name="capabilities.3d882a17-6368-5437-97d2-7bb693166b2a"></a>
+ Supports decoupled generation and evaluation using different models (for example, Claude for generation and Mistral for evaluation)
+ Feedback is structured and used to prompt revised outputs
+ Supports multiple iterations or convergence thresholds

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
