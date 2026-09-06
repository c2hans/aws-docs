---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/getting-started-with-a2-a.html
---

# Getting started with A2A
<a name="getting-started-with-a2-a"></a>

The Agent2Agent (A2A) protocol enables decentralized collaboration between agents through a shared semantic layer. Instead of routing all work through a central orchestrator, A2A allows agents to discover each other, advertise their capabilities, negotiate tasks, and share context using a lightweight JSON-based protocol. Each agent publishes a capability manifest.

The following example shows a simplified A2A capability manifest that advertises an agent's supported actions, required inputs, and operational metadata to enable discovery and task negotiation:

```
{
  "can": ["summarize.text", "extract.keywords"],
  "needs": ["document.input"],
  "meta": { "version": "1.0.3", "latencyMs": 120 }
}
```

This model enables dynamic capability matching, mid-task delegation, and cross-organizational collaboration. Agents can self-organize around tasks, form temporary working groups, and adapt as new capabilities enter or exit the system.

A2A supports interactions ranging from simple stateless requests to multi-step negotiation sessions. These include:
+ **Direct peer-to-peer messaging** for low-latency collaboration
+ **Semantic task negotiation**, where agents select the most suitable peer
+ **Capability-based discovery**, enabling emergent division of labor
+ **Session anchoring** for stateful multi-step interactions

By adopting open, agent-native protocols like A2A, organizations create AI systems that are modular, interoperable, and capable of cross-boundary collaboration. A2A ensures that agent ecosystems remain flexible and evolvable as new agents, teams, or external systems are introduced, without requiring rigid orchestration layers or prior coupling.

To implement the A2A protocol in your agent architecture, take the following actions:

1. **Review the A2A Protocol Specification** – Read the latest version of the [Agent2Agent (A2A) Protocol Specification](https://a2a-protocol.org/latest/specification/) to learn how capability manifests, negotiation flows, and the agent handshake operate.

1. **Explore A2A-compatible runtimes** – Evaluate frameworks such as the Strands Agents SDK, or custom runtime layers that support A2A-style capability manifests and peer-to-peer negotiation.

1. **Implement a capability manifest for your agents** – Define each agent's `can`, `needs`, and `meta` fields to enable discovery, matchmaking, and intent-level collaboration.

1. **Experiment with A2A negotiation patterns** – Use the request–offer–accept loop, structured capability queries, or gossip-based discovery to understand how agents reason about who should handle a task.

1. **Test A2A in a mixed infrastructure environment **– Combine A2A peer negotiation with event routing that's native to AWS through Amazon EventBridge to evaluate hybrid coordination patterns.

1. **Join the A2A community** – Engage with the [open working group](https://a2a-protocol.org/latest/community/) to stay up to date with extensions, security recommendations, and cross-vendor interoperability improvements, and [contribute to the development](https://github.com/a2aproject/A2A?tab=contributing-ov-file) of the protocol.
