---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/saga-orchestration-patterns.html
---

# Saga orchestration patterns

As workflows driven by LLMs become increasingly complex, spanning prompt chains, data processing steps, tool invocations, and agent collaboration, the need for intelligent orchestration becomes essential. Rather than relying on tightly coupled scripts or static predetermined execution flows, these workflows can be implemented as event-driven orchestration patterns, enabling LLM-based systems to dynamically coordinate, monitor, and adapt multi-step tasks across autonomous agents.

The following diagram is an example of an orchestrator:

![Orhestrator.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/83993753-1ff8-4b63-815c-263b81018ecc.png)

## Event orchestration
<a name="event-orchestration.2f170177-e72d-5b7c-82df-536834087509"></a>

In traditional distributed systems, event orchestration refers to a pattern in which a central coordinator manages a complex workflow by explicitly directing the flow of control across multiple services or tasks. Unlike event choreography (where each service reacts independently), orchestration provides centralized logic, visibility, and control over the entire process.

This is typically implemented using the following tools:
+ **AWS Step Functions** – Define and execute stateful workflows
+ **AWS Lambda** – Carry out discrete tasks within the orchestrated flow
+ **Amazon SQS** or **Amazon EventBridge** – Triggers asynchronous steps or responses

The following diagram is an AWS architectural example of saga orchestration:

![Saga orchestration.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/aa6fa06e-c007-4707-90a3-e9e7e14b90e8.png)

An AWS Step Functions workflow manages a customer order process:

1. Create order (AWS Lambda)

1. Update inventory (AWS Lambda)

1. Make payment (AWS Lambda)

The orchestrator coordinates each step by managing retries, parallel branches, timeouts, and failures.

## Role-based agent system (orchestrator)
<a name="role-based-agent-system--orchestrator-.018ee74e-20d7-53b4-94df-7ef9b17cc074"></a>

In agentic systems, the orchestrator pattern mirrors event orchestration but distributes the logic across multiple reasoning agents, each with a defined role or specialization. A central orchestrator agent interprets the overall task, decomposes it into subtasks, and delegates those to worker agents, each optimized for a particular domain (for example, research, coding, summarization, review).

## Supervisor
<a name="supervisor.c002baf6-7e6f-599d-b60e-23476591c671"></a>

1. A user submits the query "Create a project brief and summarize the top 5 competitors."

1. The orchestrator agent does the following:
   + Assigns a research agent to find competitor data
   + Sends the raw findings to a summarization agent
   + Passes results to a brief-writer agent
   + Compiles the final output for the user

Each agent operates independently, but the orchestrator coordinates the tasks. This is like a Lambda function that handles workflow tasks.

The following diagram an AWS architectural example of a supervisor:

![Supervisor.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/4b9fdd79-a451-45af-a3d3-be3ec59093ec.png)

1. A user submits a task to an Amazon Bedrock supervisor agent.

1. The supervisor agent parses the request into subtasks for each agent collaborator.

1. Each subtask is assigned to a collaborator agent with role-specific prompts or toolchains.

1. Worker agents call external APIs or tools through an action group.

1. Each worker agent returns the output in a structured format.

1. When all workers return their results, the supervisor evaluates, synthesizes, and returns the final response.

This structure allows for modularity, adaptability, and introspection across complex multistep agent workflows.

## Takeaways
<a name="takeaways.15aa4743-1db1-5a57-aae9-f4c74a2658b6"></a>

Where event orchestration uses centralized control (for example, AWS Step Functions) to direct service execution, role-based agent systems use an LLM-powered orchestrator agent to reason about the goal, delegate subtasks to worker agents, and synthesize the final output.

In both paradigms, the orchestrator does the following:
+ Maintains context and execution flow
+ Handles branching, sequencing, and error handling
+ Produces a unified result from distributed components

Agentic orchestration, however, adds reasoning, adaptability, and semantic delegation. This makes it well-suited to open-ended, ambiguous, and evolving tasks.
