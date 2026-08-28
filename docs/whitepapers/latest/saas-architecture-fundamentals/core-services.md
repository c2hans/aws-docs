---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/core-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Core services
<a name="core-services"></a>

 The control plane referenced previously mentions a series of core services that represent the typical services that are used to onboard, manage, and operate a SaaS environment. It may be helpful to further highlight the role of some of these services to highlight their scope and purpose in a SaaS environment. The following provides a brief summary of each of these services:
+  **Onboarding** – Every SaaS solution must provide a frictionless mechanism for introducing new tenants into your SaaS environment. This can be a self-service sign-up page or an internally managed experience. Either way, a SaaS solution should do all that it can remove internal and external friction from this experience and ensure stability, efficiency, and repeatability for this process. It plays an essential role in supporting the growth and scale of a SaaS business. Generally, this service orchestrates other services to create users, tenant, isolation policies, provision, and per-tenant resources.
+  **Tenant** – The tenant service provides a way to centralize the policies, attributes, and state of tenants. The key is that tenants are not individual users. In fact, a tenant is likely associated with many users.
+  **Identity** – SaaS systems need a clear way to connect users to tenants that will bring tenant context to the authentication and authorization experience of their solutions. This influences both the onboarding experience and the overall management of user profiles.
+  **Billing** – As part of adopting SaaS, organizations often embrace new billing models. They may also explore integration with third-party billing providers. This core service is largely focused on supporting the onboarding of new tenants, and collecting consumption and activity data that is used to generate bills for tenants.
+  **Metrics** – SaaS teams rely heavily on their ability to capture and analyze rich metric data that brings more visibility to how tenants use their system, how they consume resources, and how their tenants engage their systems. This data is used to shape operational, product, and business strategies.
+  **Admin user management** – SaaS systems must support both tenant users and admin users. The admin users represent the administrators of a SaaS provider. They will log into your operational experience to monitor and manage your SaaS environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
