---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html
---

# 1. System design and security recommendations for agentic AI systems
<a name="best-practices-system-design"></a>

System design decisions can support the development of agentic AI systems with strong protections against well-documented large language model (LLM) application threats. Adoption of risk-aligned design patterns helps drive an outcome is in line with your business needs.

**This section contains the following best practices:**
+ [1.1 Use deterministic execution logic unless AI is needed (AI-specific)](#best-practices-1-deterministic-execution-logic)
+ [1.2 Determine agent scoping (AI-specific)](#best-practices-1-agent-scoping)
+ [1.3 Implement shared memory management (AI-specific)](#best-practices-1-shared-memory)
+ [1.4 Isolate sessions (General)](#best-practices-1-isolate-sessions)

## 1.1 Use deterministic execution logic unless AI is needed (AI-specific)
<a name="best-practices-1-deterministic-execution-logic"></a>

Implement coded logic for deterministic execution. Use AI functionality where it provides value that deterministic code cannot.

The following image shows an agent with internal logic flow. Standard programming logic is used instead of prompting the LLM for validation, normalization, or user communication tasks. This is a clear example of perceive, reason, and act. The perceive layer gathers and normalizes the input, the reason layer (LLM inference) summarizes content, and then the act layer sends the email back to the user.

![An agent that follows the perceive, reason, and act logic flow.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/images/guide-img/562fab0c-abe0-4a40-a738-87a61cbd8d2a/images/8eb433ee-9204-460e-8cff-f6e932d83bee.png)

This approach limits the impact of prompt injection attacks by reducing the scope of the system prompt and what the LLM response is used for. It reduces the attack surface by treating the LLM interaction similar to how a system might interact with a public user. The prompt to the LLM is normalized and prepared before inference, and the LLM response has guardrails applied to it before output.

Minimizing the scope of AI use within an agent offers the following advantages:
+ Larger percentage of coded logic results in faster agent execution
+ Lower cost of agent execution
+ Improved testability of agent outcomes
+ Simplified threat modeling and risk management

If you use AI to drive the agent behavior, you might observe the following advantages:
+ Simplified agent coding due to decisions being handled by AI rather than coded by logic
+ Implementation of behaviors not possible with coded logic

Where an LLM response is used to drive tool selection or interface with another system, use an allow list. This helps you ensure that interactions not specifically needed for normal operation are not accessed. Allowing unrestricted access to tools and interactions can lead to unexpected interactions. This might lead to data exfiltration or [confused deputy](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-service-confused-deputy-prevention.html) (privilege escalation) scenarios.

## 1.2 Determine agent scoping (AI-specific)
<a name="best-practices-1-agent-scoping"></a>

Consider the scope of agent and tool interactions that each agent is directly responsible for. Consider the following example, where two agents are responsible for four tools. The left side of the image shows a *super agent* approach, and the right side shows a *disparate worker agent* approach. While both approaches are reasonable, there are several factors that you should consider during system design.

![Two approaches to agent system design: super agent and disparate worker agents.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/images/guide-img/562fab0c-abe0-4a40-a738-87a61cbd8d2a/images/186426f7-f4b6-4b98-a545-ab3ba88ec117.png)

The disparate worker approach typically has the following advantages:
+ Reduces risk of second-tier agent performing actions that the orchestrator agent didn't intend
+ Enforces[ access control](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_data_rest_access_control.html) of user permissions against a smaller exposure point
+ Reduces the scope of impact if a single agent is compromised
+ Improves agent explainability and behavior observation due to reduced agent responsibilities
+ Supports organizations with a lower tolerance for risk

The super agent approach allows the following:
+ Simplifies agent development and entitlements management
+ Accelerates coordination for tasks that interact with the second-tier agents
+ Reduces the number of orchestrator-to-second-tier-agent interactions, which reduces system load

## 1.3 Implement shared memory management (AI-specific)
<a name="best-practices-1-shared-memory"></a>

Shared memory management can be challenging if multiple agents require access to a single shared resource. Examples of a shared memory resource include shared knowledge bases, conversation histories, learned patterns, and intermediate reasoning states. Unlike traditional microservices that typically operate on well-defined data contracts and well-known interaction patterns, agentic AI systems manage dynamic, contextual information that evolves through agent interactions and reasoning processes. This shared memory often contains unstructured data, such as natural language conversations, embeddings, and probabilistic reasoning chains, that cannot be easily partitioned or validated using conventional database constraints. This can create dependencies between agents that can lead to inconsistent worldviews or conflicting decision-making processes.

Strong access controls that enforce least privilege or read-only permissions can significantly reduce the number of agents that can modify shared memory resources. However, authorized agents with write access still represent a potential threat vector that requires additional safeguards. Given this inherent risk, shared memory resources should be treated as partially trusted components. The retrieved information must undergo validation or grounding processes before being acted upon, particularly in systems with a low risk tolerance. The most effective mitigation strategy involves implementing a single deterministic tool that serves as a coordinating proxy for shared memory access. It incorporates filters and logic to detect memory corruption, validate content integrity, and make sure that all memory operations conform to established security policies before propagation to dependent agents.

Implementing a deterministic tool as shared memory gateway offers the following advantages:
+ Provides centralized validation and content integrity checking before memory propagation
+ Implements consistent security policies and filters for all memory operations across agents
+ Enables detection and prevention of memory corruption through coordinated proxy logic
+ Enforces uniform access controls and audit trails for all shared memory interactions
+ Allows grounding processes to validate information reliability before agent consumption
+ Creates a single point of control for memory security policies without modifying individual agents

Advantages of not implementing shared memory:
+ Removes complex access control requirements and potential write-access threat vectors
+ Prevents memory corruption risks from compromised agents that affect the entire system
+ Simplifies system architecture by avoiding unstructured data partitioning challenges
+ Eliminates cascading failures where corrupted shared memory impacts multiple agents

## 1.4 Isolate sessions (General)
<a name="best-practices-1-isolate-sessions"></a>

Make sure that each user maintains their own distinct context and state without interference from other concurrent sessions. This architectural pattern prevents data leakage between users, maintains conversation coherence, and enables personalized agent behavior. Implementing effective session isolation requires careful management of the session lifecycle, proper cleanup of temporary resources, and strategic use of session-scoped storage mechanisms. For more information, see the [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Developers should implement session timeouts to prevent resource exhaustion, use cryptographically secure session identifiers to prevent session hijacking, and make sure that agent memory and context are properly partitioned by using session boundaries.

[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) implements session isolation through unique session identifiers that encapsulate conversation history, retrieved knowledge, and intermediate reasoning states. This helps prevent sensitive information from one user's interaction from inadvertently influencing another user's experience and helps protect data privacy.
