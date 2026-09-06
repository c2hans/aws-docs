---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/core-modules.html
---

# Core building blocks of software agents
<a name="core-modules"></a>

The following diagram presents the key functional modules found in most intelligent agents. Each component contributes to the agent's ability to operate autonomously in complex environments.

![Key functional modules and submodules in intelligent agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/images/guide-img/bf0cde42-baef-4bee-8fff-ca482667d2b6/images/b97920fd-1170-4545-bab9-e099b15f597b.png)

In the context of the perceive, reason, act loop, an agent's reasoning capability is distributed across both its cognitive and learning modules. Through the integration of memory and learning, the agent develops adaptive reasoning grounded in past experience. As the agent acts within its environment, it creates an emergent feedback loop: Each action influences future perceptions, and the resulting experience is incorporated into memory and internal models through the learning module. This continuous loop of perception, reasoning, and action enables the agent to improve over time and completes the full perceive, reason, act cycle.

## Perception module
<a name="perception"></a>

The perception module enables the agent to interface with its environment through diverse input modalities such as text, audio, and sensors. These inputs form the raw data that all reasoning and action are based on. Text inputs might include natural language prompts, structured commands, or documents. Audio inputs encompass spoken instructions or environmental sounds. Sensor inputs include physical data such as visual feeds, motion signals, or GPS coordinates. The core function of perception is to extract meaningful features and representations from this raw data. This allows the agent to construct an accurate and actionable understanding of its current context. The process might involve feature extraction, object or event recognition, and semantic interpretation, and forms the critical first step in the perceive, reason, act loop. Effective perception ensures that downstream reasoning and decision-making are grounded in relevant, up-to-date situational awareness.

## Cognitive module
<a name="cognitive"></a>

The cognitive module serves as the deliberative core of the software agent. It is responsible for interpreting perceptions, forming intent, and guiding purposeful behavior through goal-driven planning and decision-making. This module transforms inputs into structured reasoning processes, which enables the agent to operate intentionally rather than reactively. These processes are managed through three key submodules: goals, planning, and decision-making.

### Goals submodule
<a name="goals-submodule.ed04e169-d236-530d-8148-2e87fbe5e162"></a>

The goals submodule defines the agent's intent and direction. Goals can be explicit (for example, "navigate to a location" or "submit a report") or implicit (for example, "maximize user engagement" or "minimize latency"). They are central to the agent's reasoning cycle, and provide a target state for its planning and decisions.

The agent continuously evaluates progress toward its goals and might reprioritize or regenerate goals based on new perceptions or learning. This goal awareness keeps the agent adaptable in dynamic environments.

### Planning submodule
<a name="planning-submodule.63af2055-2a04-592d-ac6c-007f5b5cdf69"></a>

The planning submodule constructs strategies to achieve the agent's current goals. It generates action sequences, decomposes tasks hierarchically, and selects from predefined or dynamically generated plans.

To operate effectively in non-deterministic or changing environments, planning is not static. Modern agents can generate chain-of-thought sequences, introduce subgoals as intermediate steps, and revise plans in real time when conditions shift.

This submodule connects closely with memory and learning, and allows the agent to refine its planning over time based on past outcomes.

### Decision-making submodule
<a name="decision-making-submodule.8c2d3427-441f-51ae-93ac-44386d5f1b9c"></a>

The decision-making submodule evaluates available plans and actions to select the most appropriate next step. It integrates input from perception, the current plan, the agent's goals, and environmental context.

Decision-making accounts for:
+ Trade-offs between conflicting goals
+ Confidence thresholds (for example, uncertainty in perception)
+ Consequences of actions
+ The agent's learned experience

Depending on the architecture, agents might rely on symbolic reasoning, heuristics, reinforcement learning, or language models (LLMs) to make informed decisions. This process keeps the agent's behavior context-aware, goal-aligned, and adaptive.

## Action module
<a name="action"></a>

The action module is responsible for executing the agent's selected decisions and interfacing with the external world or internal systems to produce meaningful effects. It represents the Act phase of the perceive, reason, act loop, where intent is transformed into behavior.

When the cognitive module selects an action, the action module coordinates execution through specialized submodules, where each submodule aligns with the agent's integrated environment:
+ Physical actuation: For agents that are embedded in robotic systems or IoT devices, this submodule translates decisions into real-world physical movements or hardware-level instructions.

  Examples: steering a robot, triggering a valve, turning on a sensor.
+ Integrated interaction: This submodule handles non-physical but externally visible actions such as interacting with software systems, platforms, or APIs.

  Examples: sending a command to a cloud service, updating a database, submitting a report by calling an API.
+ Tool invocation: Agents often extend their capabilities by using specialized tools to accomplish sub-tasks such as the following:
  + Search: querying structured or unstructured knowledge sources
  + Summarization: compressing large text inputs into high-level overviews
  + Calculation: performing logical, numerical, or symbolic computation

  Tool invocation enables complex behavior composition through modular, callable skills.

## Learning module
<a name="learning"></a>

The learning module enables agents to adapt, generalize, and improve over time based on experience. It supports the reasoning process by continuously refining the agent's internal models, strategies, and decision policies by using feedback from perception and action.

This module operates in coordination with both short-term and long-term memory:
+ Short-term memory: Stores transient context, such as dialogue state, current task information, and recent observations. It helps the agent maintain continuity within interactions and tasks.
+ Long-term memory: Encodes persistent knowledge from past experiences, including previously encountered goals, outcomes of actions, and environmental states. Long-term memory enables the agent to recognize patterns, reuse strategies, and avoid repeating mistakes.

### Learning modes
<a name="learning-modes.704c78ec-2164-5001-a560-8913da6023d1"></a>

The learning module supports a range of paradigms, such as supervised, unsupervised, and reinforcement learning, which support different environments and agent roles:
+ Supervised learning: Updates internal models based on labeled examples, often from human feedback or training datasets.

  Example: learning to classify user intent based on previous conversations.
+ Unsupervised learning: Identifies hidden patterns or structures in data without explicit labels.

  Example: clustering environmental signals to detect anomalies.
+ Reinforcement learning: Optimizes behavior through trial and error by maximizing cumulative reward in interactive environments.

  Example: learning which strategy leads to the fastest task completion.

Learning integrates tightly with the agent's cognitive module. It refines planning strategies based on past outcomes, enhances decision-making through the evaluation of historical success, and continuously improves the mapping between perception and action. Through this closed learning and feedback loop, agents evolve beyond reactive execution to become self-improving systems that are capable of adapting to new goals, conditions, and contexts over time.
