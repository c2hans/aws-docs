---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/employing-control-planes-in-agentic-environments.html
---

# Employing control planes in agentic environments
<a name="employing-control-planes-in-agentic-environments"></a>

Multi-tenant best practices often divide implementations into two distinct parts: a control plane and an application plane. The control plane provides a single pane of glass to access operational, management, and orchestration mechanisms that span the environment's tenants. The application plane is where the business logic, features, and functional capabilities reside.

This division of responsibility also applies to agentic models. A multi-tenant agent requires a degree of centralized management, operation, and insights, and it makes sense to continually address these needs through a control plane. The following diagram shows a conceptual view of how these planes are divided within an agent as a service (AaaS) environment.

![Control and application planes with agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/images/guide-img/2d1a9d67-004c-4c75-8cd2-68ceef9bbc6f/images/f1b75932-2da5-499a-810e-d177413646e6.png)

*Figure 16. Control and application planes with agents*

This diagram shows the traditional separation of control and application planes. What's new is that the control plane now manages the agents that make up an AaaS environment. The control plane interacts with all agents because we presume that the agents are built, managed, and deployed by one provider.

This model introduces additional layers of complexity, especially in agent lifecycle and third-party coordination, but retains the foundational separation of concerns. The control plane still provides the same core capabilities by orchestrating the configuration of agents, providing tenant and agent observability, collecting consumption and metering data for billing, and managing tenant policies.

This scenario becomes more complex if you consider a multi-agent system that incorporates agents from various providers. The following diagram shows an example of such a model.

![Control planes with agents from multiple providers](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/images/guide-img/2d1a9d67-004c-4c75-8cd2-68ceef9bbc6f/images/1fe29281-0a66-4adf-ad35-9de801d56d53.png)

*Figure 17. Control planes with agents from multiple providers*

This diagram depicts four agents from different providers that are part of multi-agentic system. Third-party providers still operate and deploy each agent, which are configured to enable authorized access from one or more providers. The agents, however, remain under the provider's control, so each agent maintains its own control plane.

Essentially, these multi-tenant agents behave as third-party services that integrate with other agents. As such, they must have their own control plane to provide the centralized operation, configuration, and management of an agent's capabilities.

We assume that agents are independent services that run in a provider-hosted experience. But this may be unclear in a scenario where an agent consumer imposes more constraints on how and where to host an agent.

## Onboarding tenants to agents
<a name="onboarding-tenants-to-agents.e8c619ab-0bf7-550e-af41-aa1300488547"></a>

Onboarding is typically a vital part of any AaaS environment. How you create, configure, and provision tenants often involves many moving parts, integrations, and tools. The agent onboarding experience may require the same services that are found in an AaaS control plane, which includes tenant identity, tiering, provisioning per-tenant resources, and configuring tenant policies.

Your approach to agent onboarding is influenced by the footprint and tenancy model of your agentic environment. Siloed and pooled agents each have their own nuances, and the choice of using either a single agent or multiple agents also affects the onboarding process. The following diagram shows a conceptual view of how onboarding affects an agent's configuration.

![Onboarding tenants to agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/images/guide-img/2d1a9d67-004c-4c75-8cd2-68ceef9bbc6f/images/9a622ddc-25e9-4c38-9e86-f4cfb92c2265.png)

*Figure 18. Onboarding tenants to agents*

Each time you onboard an agent, the control plane must take the necessary steps to enable the tenant to access the agent. How to introduce tenants varies based on the agent authorization model, but assume that you'll create a tenant identity that associates agent requests with individual tenants. This tenant context dictates the agent experience by applying it to routes, scopes, and control access.

Onboarding may also require you to configure any per-tenant resources that an agent uses. It's here that the control plane's tenant provisioning service connects your agent to tenant-specific data and resources that the agent consults.

If your system relies on integrating third-party agents, you must also address the needs of those agents during the onboarding process. How this works depends on the security and integration mechanisms for authorizing access between agents. Ideally, the required steps to orchestrate and configure agent-to-agent authentication and authorization are addressed through automated onboarding.
