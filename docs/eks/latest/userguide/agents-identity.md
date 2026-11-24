---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents-identity.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Agent identity and authorization on Amazon EKS

Every action an agent takes runs with some identity’s authority, and for an agent, two identities are involved. The agent’s own identity decides what the agent can reach on AWS, how the gateway and its callers recognize it, and what an audit record attributes to it. A person’s identity, carried through the agent’s calls, decides whose authority those calls run with when the agent acts for that person.

Every agent needs its own identity. Add the person’s identity whenever that person’s authority should scope what the agent can reach and do in downstream systems. That includes a service that holds per-person data, and any downstream system that already authorizes people, such as a source repository, a ticketing system, a data warehouse, or an internal API with its own access rules. Each system then enforces the person’s existing permissions, so the agent can’t use broader access of its own to read data or take actions that the person couldn’t, and a prompt that steers the agent toward something the person isn’t allowed to touch is refused downstream.

The two identities work together. The person’s identity says whose authority a call carries, and the agent’s identity says who decided to make the call. Design the effective access as the intersection of what the person may do, what the agent is allowed to do, and what the target system accepts, so that delegating work to an agent can only narrow access, never widen it. OAuth 2.0 token exchange (RFC 8693) can express both in one token, with the person as the subject and the agent in an `act` claim. On the open source path, the reference sample can issue that token. See [Delegated token on the open source path](agents-identity-acting-for.md#agents-identity-acting-for-delegated). Keeping the agent’s identity on every delegated call is also what lets an audit record show that an agent acted rather than the person directly, and lets you revoke one agent without affecting the people who use it.

A third-party API outside AWS adds one more question, which is what credential the API accepts and who holds it. The gateway holds that credential and attaches it to the calls of the agent it belongs to, so the agent’s pod never holds it.

The following table compares them.

| Identity | What it decides | Page |
| --- | --- | --- |
| Agent | The agent’s AWS permissions through its own IAM role, the token that names it to the gateway, and which callers may reach it |  [Give each agent its own identity with EKS Pod Identity](agents-identity-agent.md)  |
| Person | Whose authority a call carries when the agent acts for a person. A downstream tool or AWS enforces the person’s permissions from a credential the identity provider signed, not the agent or the model |  [Act on behalf of a user with an agent on Amazon EKS](agents-identity-acting-for.md)  |
| Person and agent | What the agent may do for this person. The downstream system decides on both identities at once: the tool verifies the agent’s token and the person’s token, or one delegated token with the person as the subject and the agent in `act`, and IAM scopes an on-behalf-of role session to one person and one agent |  [How a request carries the person](agents-identity-acting-for.md#agents-identity-acting-for-flows)  |
| Third-party API | Which agent may use a credential for an API outside AWS, such as a personal access token or a token from a person’s OAuth consent. The gateway holds it, not the pod |  [Call third-party APIs from agents without giving them credentials](agents-third-party-credentials.md)  |
