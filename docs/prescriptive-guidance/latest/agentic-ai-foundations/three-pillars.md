---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/three-pillars.html
---

# The three pillars of modern software agents
<a name="three-pillars"></a>

In the context of today's AI-powered platforms, microservice architectures, and event-driven systems, software agents can be defined by three interdependent principles that distinguish them from standard services or automation scripts: autonomy, asynchronicity, and agency. In the following illustration and in subsequent diagrams, the triangle represents these three pillars of modern software agents.

![Three pillars of modern sofware agents: agency, autonomy, asynchronicity.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/images/guide-img/bf0cde42-baef-4bee-8fff-ca482667d2b6/images/b911214a-d0f4-439d-9741-38ea4eae9813.png)

## Autonomy
<a name="autonomy"></a>

Modern agents operate independently. They make decisions based on internal state and environmental context without requiring human prompts. This enables them to react to data in real-time, manage their own lifecycle, and adjust their behavior based on goals and situational inputs.

Autonomy is the foundation of agent behavior. It allows agents to function without continuous supervision or hardcoded control flows.

## Asynchronicity
<a name="asynchronicity"></a>

Agents are fundamentally asynchronous. This means that they respond to events, signals, and stimuli as they occur, without relying on blocking calls or linear workflows. This characteristic enables scalable, non-blocking communication, responsiveness in distributed environments, and loose coupling between components.

Through asynchronicity, agents can participate in real-time systems and coordinate with other services or agents fluidly and efficiently.

## Agency as the defining principle
<a name="agency"></a>

Autonomy and asynchronicity are necessary, but these features alone aren't sufficient to make a system a true software agent. The critical differentiator is agency, which introduces:
+ Goal-directed behavior: Agents pursue objectives and evaluate progress toward them.
+ Decision-making: Agents assess options and choose actions based on rules, models, or learned policies.
+ Delegated intent: Agents act on behalf of a person, system, or organization and have an embedded sense of purpose.
+ Contextual reasoning: Agents incorporate memory or models of their environment to guide behavior intelligently.

A system that is autonomous and asynchronous might still be a reactive service. What makes it a software agent is its ability to act with intention and purpose, to be *agentic*.

## Agency with purpose
<a name="agency-purpose"></a>

The principles of autonomy, asynchronicity, and agency enable systems to operate intelligently, adaptively, and independently across distributed environments. These principles are rooted in decades of conceptual and architectural evolution, and now underpin many of the most advanced AI systems being built today.

In this new era of generative AI, goal-oriented orchestration, and multi-agent collaboration, it's essential to understand what makes a software agent truly agentic. Recognizing agency as the defining characteristic helps us move beyond automation and into the realm of autonomous intelligence with purpose.
