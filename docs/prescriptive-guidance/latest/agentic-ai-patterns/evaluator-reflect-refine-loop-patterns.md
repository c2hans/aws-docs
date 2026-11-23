---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html
---

# Evaluator reflect-refine loop patterns

Tasks such as code generation, summarization, or autonomous decision-making benefit greatly from runtime feedback, enabling the system to evolve through observation and refinement. To operationalize this, the reflect–refine cycle can be implemented as an event-driven feedback control loop – a pattern inspired by systems engineering, adapted for autonomous, intelligent workflows.

The following diagram is an example of an evaluator reflect-refine feedback loop:

![Evaluator reflect-refine feedback loop.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/b1826ee2-d50a-450a-85c6-9167096e061e.png)

## Feedback control loop
<a name="feedback-control-loop.7b9dbc8d-1081-5efe-a338-aaf0fed5bcd3"></a>

A feedback control loop is a pattern that monitors its own outputs and behaviors, evaluates them against defined criteria or a desired state, and then adjusts its actions accordingly. This architecture is inspired by control theory and is foundational in domains such as automation, continuous integration and continuous delivery (CI/CD) pipelines, and machine learning operations.

The following diagram is an AWS architectural example of a feedback control loop:

![Feedback control loop.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/edfd6ee6-bac9-43d4-a6fe-7ab774577464.png)

1. A deployment pipeline emits a buildComplete event.

1. The event triggers an automated test or evaluation job that validates the build.

1. If validation fails (for example, due to failing tests, security issues, or a policy violation), the system:
   + Emits a buildComplete event
   + Logs the issue or sends a notification
   + Triggers a remediation or corrective action, such as rollback, patching, or retry

The loop continues until it produces an acceptable outcome or escalation, or a time out occurs. This pattern is commonly used for the following:
+ Amazon EventBridge rules to route events to evaluation or remediation tasks
+ AWS Step Functions for iterative retry logic and branching on evaluation outcomes
+ Amazon Simple Notification Service (Amazon SNS) or Amazon CloudWatch alarms for feedback triggers and alerts
+ AWS Lambda functions or containerized workers to apply corrective actions

## Feedback control loop (evaluator)
<a name="feedback-control-loop--evaluator-.5382de76-b6bb-588b-8bba-9d343d3b627a"></a>

An evaluator workflow is a cognitive feedback loop that's powered by LLMs or reasoning agents. The process consists of the following:

1. A generator agent or LLM produces an output (for example, a plan, answer, or draft).

1. An evaluator agent reviews the result using a critique prompt or evaluation rubric.

1. Based on the feedback, the original agent or a new optimizer agent revises the output.

The loop repeats until the result meets a set of criteria, is approved, or reaches a retry limit.

## Evaluator
<a name="evaluator.d2079fbd-9ddf-5d2d-be87-77d396a796b4"></a>

1. A user asks an agent to write a policy summary.

1. The generator agent drafts it.

1. An evaluator agent checks coverage, tone, and legal correctness.

1. If the response is inadequate, it's refined and resubmitted until the feedback loop converges.

This enables self-assessment, iterative refinement, and adaptive output control—all without human input.

The following diagram is an AWS architectural example of a feedback control loop (evaluator):

![Feedback control loop (evaluator).](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/752b849e-6c1e-44e0-8162-686878792464.png)

1. A user issues a task (for example, draft a business strategy).

1. An Amazon Bedrock agent generates an initial draft using an LLM.

1. A second agent (or a follow-up prompt) performs a structured evaluation (for example, "rate this output by clarity, completeness, and tone").

1. If the rating falls below a threshold, the response is revised by:
   + Reinvoking the generator with an embedded critique
   + Sending the feedback to a specialized refiner agent
   + Iterating until an acceptable response is reached

Optional components like AWS Lambda controllers or AWS Step Functions can manage feedback thresholds, retries, and fallback strategies.

## Takeaways
<a name="takeaways.a3db31e6-4fde-51eb-8ff1-94102231eb06"></a>

Where traditional feedback control loops use events, metrics, and remediation logic to validate and adjust system behavior, agentic evaluator loops use reasoning agents to evaluate, reflect, and revise output dynamically.

In both paradigms:
+ Output is evaluated after it's generated
+ Corrective or refining actions are triggered based on feedback
+ System continuously adapts toward a target quality or goal

The agentic version transforms static validation into semantic reflection, enabling self-improving agents that evaluate their own effectiveness.
