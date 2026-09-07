---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/computer-use-agents.html
---

# Computer-use agents
<a name="computer-use-agents"></a>

Computer-use agents can simulate or control digital environments like browsers, terminals, file systems, and applications. These agents interpret user intent, interact with visual and text interfaces, and perform goal-directed actions by combining LLM reasoning, visual language models (VLMs), and tool servers that execute commands or simulate input events.

This pattern is important for practical AI automations, where the agent functions not just as an assistant but also as a proxy that performs actions as a human would, often by using the same tools and environments.

## Architecture
<a name="architecture.59f5fe2d-ce76-5d4e-b5c7-18732e9b41f5"></a>

A computer-use agent pattern is shown in the following diagram:

![Computer-use agent.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/e56a2cef-9d10-4284-befb-fcf75f025f0a.png)

## Description
<a name="description.56d4c193-a6f1-54f3-abca-0b0f4ba08931"></a>

1. Receives a query
   + A task or request is provided through a UI, API, or natural language interface.

1. Accesses memory
   + The agent retrieves short-term and long-term memory to recall past commands, goals, and system states.

1. Analyzes the visual context
   + A VLM observes the computer screen, system state, or UI elements to understand a given context and identify actionable items.

1. Reasons through an LLM
   + The LLM combines the query, memory state, tool, and server response to determine the next action.

1. Interacts with tool server
   + The agent invokes tools that are hosted on a server, which may include the following:
     + Browsers (for example, headless Chrome) and shell environments
     + Text and code editors
     + Custom script interfaces

1. Updates visual inputs
   + If the system UI changes or further observation is needed, the VLM may reanalyze the screen state or text buffers.

1. Updates memory
   + New insights, system states, or user feedback are written to short-term and long-term memory.

1. Formulates final decisions and explanations
   + The LLM synthesizes results or recommends actions based on the query and tool output.

1. Returns a response
   + The agent returns results to the interface (for example, a completed task, confirmation, or generated content).

## Capabilities
<a name="capabilities.21110e24-c2f9-5b5e-883d-c60f2042810a"></a>
+ Multimodal reasoning with visual and textual inputs
+ Control over applications through simulated or API-driven inputs
+ Memory management for persistent state
+ Autonomy in sequence execution (multistep flows)

## Common use cases
<a name="common-use-cases.8d45463a-6488-57d1-b1d6-ef9c093b561f"></a>
+ AI developers that write and run code in IDEs
+ Computer-use agents for repetitive digital workflows
+ Simulated users for software testing and quality assurance
+ Accessibility agents for navigating UIs through voice or high-level instructions
+ Smart robotic process automation (RPA) that's enhanced with reasoning

## Implementation guidance
<a name="implementation-guidance.d54bb973-2db6-50ff-9bcf-b87c136c736f"></a>
+ You can build this pattern using the following AWS services:
+ Amazon Bedrock for LLM-based planning and reasoning
+ Amazon Elastic Compute Cloud (Amazon EC2), AWS Lambda, or Amazon SageMaker notebooks to run tool servers with simulated UI environments
+ Amazon Simple Storage Service (Amazon S3) or Amazon DynamoDB for memory persistence
+ Amazon Rekognition (or custom models) for UI image analysis in hybrid scenarios
+ Amazon CloudWatch Logs or AWS X-Ray for observability and audit trails

## Summary
<a name="summary.b78a4880-3c9b-5f63-b127-ee3cff7b02c8"></a>

Computer-use agents act as autonomous digital operators, bridging the gap between human-computer interactions and AI-driven actions. By incorporating memory, tool orchestration, and VLMs, these agents can adaptively interact with systems designed for humans, execute actions, update files, navigate menus, and generate responses.
