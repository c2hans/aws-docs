---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-parallelization.html
---

# Workflow for parallelization
<a name="workflow-for-parallelization"></a>

This workflow involves breaking down a task into independent subtasks that can be handled concurrently by multiple LLM calls or agents. Outputs are then programmatically aggregated and synthesized into a result.

![Workflow for parallelization.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/45fbbe3d-abc6-4f0c-8855-1a2b4fbd596e.png)

The Parallelization workflow is used when a task can be divided into independent, nonsequential subtasks that can be processed simultaneously, significantly improving efficiency, throughput, and scalability. It is especially powerful in data-heavy, batch-oriented, or multiperspective problem spaces where the agent must analyze or generate content across multiple inputs.

Parallelization is particularly effective when:
+ Subtasks do not depend on each other's intermediate results, allowing them to run in parallel without coordination.
+ A task involves repeating the same reasoning process across many items (for example, summarizing multiple documents or evaluating a list of options).
+ Multiple hypotheses or perspectives are explored in parallel to promote diversity, creativity, or robustness.
+ You need to reduce latency for high-volume or high-frequency requests through concurrent LLM execution.
+ This workflow is commonly used in document processing agents, survey or comparison engines, batch summarizers, multi-agent brainstormers, and scalable classification or labeling tasks, especially where rapid, parallel reasoning is a performance advantage.

## Capabilities
<a name="capabilities.93e8a3dc-cce6-5294-a17b-5b1e9b461f8a"></a>
+ Parallel execution of LLM tasks (by using AWS Lambda, AWS Fargate, or an AWS Step Functions map state)
+ Requires result alignment, validation, or deduplication at the synthesis stage
+ Well-suited for stateless agent loops

## Common use cases
<a name="common-use-cases.f2470db6-a2ef-5b11-8cf8-4aeb76552966"></a>
+ Analyzing multiple documents or perspectives in parallel
+ Generating diverse drafts, summaries, or plans
+ Accelerating throughput across batch jobs
