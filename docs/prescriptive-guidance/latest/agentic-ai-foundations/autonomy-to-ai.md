---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/autonomy-to-ai.html
---

# From autonomy to distributed intelligence
<a name="autonomy-to-ai"></a>

Before the term *software agent* entered the mainstream, early computing research explored the idea of *autonomous digital entities*, which are systems that are capable of acting independently, reacting to inputs, and making decisions based on internal rules or objectives. These early ideas laid the conceptual groundwork for what would become the agent paradigm. (For a historical timeline, see the section [The evolution of software agents](evolution.md) later in this guide.)

## Early concepts of autonomy
<a name="early-concepts"></a>

The notion of machines or programs that act independently from human operators has intrigued system designers for decades. Early work in cybernetics, artificial intelligence, and control systems examined how software could exhibit self-regulating behavior, respond dynamically to changes, and operate without continuous human supervision.

These ideas introduced *autonomy* as a core attribute of intelligent systems and set the stage for the emergence of software that could *decide and act*, instead of only *reacting* or *executing*.

## The actor model and asynchronous execution
<a name="actor-model"></a>

In the 1970s, the *actor model*, which was introduced in the paper [A Universal Modular ACTOR Formalism for Artificial Intelligence](https://www.ijcai.org/Proceedings/73/Papers/027B.pdf) (Hewitt et al. 1973), provided a formal framework for thinking about decentralized, message-driven computation. In this model, actors are independent entities that communicate exclusively by passing asynchronous messages, and enable scalable, concurrent, and fault-tolerant systems.

The actor model emphasized three key attributes that continue to influence modern agent design:
+ Isolation of state and behavior
+ Asynchronous interaction between entities
+ Dynamic creation and delegation of tasks

These attributes aligned with the needs of distributed systems and prefigured the operational characteristics of software agents in cloud-native environments.

## Distributed intelligence and multi-agent systems
<a name="distributed-intelligence"></a>

As computing systems became more interconnected after the 1960s, researchers explored distributed artificial intelligence (DAI). This field focused on how multiple autonomous entities could work collaboratively or competitively across a system. DAI led to the development of multi-agent systems, where each agent has local goals, perception, and reasoning but also operates within a broader, interconnected environment.

This vision of distributed intelligence, where decision-making is decentralized and emergent behavior arises from agent interaction, remains central to how modern agent-based systems are conceived and built.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
