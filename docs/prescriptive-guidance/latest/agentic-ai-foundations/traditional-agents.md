---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/traditional-agents.html
---

# Traditional agent architecture: perceive, reason, act
<a name="traditional-agents"></a>

The following diagram illustrates how the building blocks discussed in the [previous section](core-modules.md) operate under the perceive, reason, act cycle.

![How the core building blocks apply to traditional agent architecture.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/images/guide-img/bf0cde42-baef-4bee-8fff-ca482667d2b6/images/7b6527c6-7a5a-4e01-9062-39992917838e.png)

## Perceive module
<a name="perceive"></a>

The perceive module acts as the agent's sensory interface with the external world. It transforms raw environmental input into structured representations that inform reasoning. This includes handling multimodal data such as text, audio, or sensor signals.
+ Text input may come from user commands, documents, or dialogue.
+ Audio input includes spoken instructions or environmental sounds.
+ Sensor input captures real-world signals such as motion, visual feeds, or GPS.

When the raw input has been ingested, the perception process performs feature extraction, followed by object or event recognition and semantic interpretation to create a meaningful model of the current situation. These outputs provide structured context for downstream decision-making and anchor the agent's reasoning in real-world observations.

## Reason module
<a name="reason"></a>

The reason module is the cognitive core of the agent. It evaluates context, formulates intent, and determines appropriate actions. This module orchestrates goal-driven behavior by using both learned knowledge and reasoning.

The reason module consists of tightly integrated submodules:
+ Memory: Maintains dialogue state, task context, and episodic history in both short-term and long-term formats.
+ Knowledge base: Provides access to symbolic rules, ontologies, or learned models (such as embeddings, facts, and policies).
+ Goals and plans: Defines desired outcomes and constructs action strategies to achieve them. Goals can be dynamically updated and plans can be adaptively modified based on feedback.
+ Decision-making: Acts as the central arbitration engine by weighing options, evaluating trade-offs, and selecting the next action. This submodule factors in confidence thresholds, goal alignment, and contextual constraints.

Together, these components allow the agent to reason about its environment, update beliefs, select paths, and behave in a coherent, adaptive manner. The reason module closes the gap between perception and behavior.

## Act module
<a name="act"></a>

The act module executes the agent's selected decision by interfacing with either the digital or the physical environment to carry out tasks. This is where intention becomes action.

This module includes three functional channels:
+ Actuators: For agents that have a physical presence (such as robots and IoT devices), controls hardware-level interactions such as movement, manipulation, or signaling.
+ Execution: Handles software-based actions, including invoking APIs, dispatching commands, and updating systems.
+ Tools: Enables functional capabilities such as search, summarization, code execution, calculation, and document handling. These tools are often dynamic and context-aware, which extends the agent's utility.

The outputs of the act module feed back into the environment and close the loop. These outcomes are perceived by the agent again. They update the agent's internal state and inform future decisions, thus completing the perceive, reason, act cycle.
