---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/control-plane-vs.-application-plane.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Control plane vs. application plane
<a name="control-plane-vs.-application-plane"></a>

 The previous diagram provides a conceptual view of the core SaaS architecture concepts. Now let’s drill down into that deeper, and better define how your SaaS environment decomposed into distinct layers. Having this clearer picture of the boundaries between SaaS concepts will make it easier to describe the moving parts of a SaaS solution.

 The following diagram divides your SaaS environment into two distinct planes. On the right side is the control plane. This side of the diagram includes all the functionality and services that are used to onboard, authenticate, manage, operate, and analyze a multi-tenant environment.

![A diagram depciting control plane vs. application plane.](http://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/control-vs-application.png)

 This control plane is foundational to any multi-tenant SaaS model. Every SaaS solution—regardless of application deployment and isolation scheme—must include those services that give you the ability to manage and operate your tenants through a single, unified experience.

 Within the control plane, we have further broken this down into two distinct elements. The core services here represent the collection of services that are used to orchestrate your multi-tenant experience. We’ve included some of the common examples of services that are typically part of the core, acknowledging that the core services could vary some for each SaaS solution.

 You’ll also notice that we show a separate administration application. This represents the application (a web application, a command line interface, or an API) that might be used by a SaaS provider to manage their multi-tenant environment.

 An important caveat is that the control plane and its services are not actually multi-tenant. The functionality is not providing the actual functional attributes of your SaaS application (which does need to be multi-tenant). If you look inside any one of the core services, for example, you won’t find tenant isolation and the other constructs that are part of your multi-tenant application functionality. These services are global to all tenants.

 The left side of the diagram references the application plane of a SaaS environment. This is where the multi-tenant functionality of your application resides. What appears in the diagram needs to remain somewhat vague, because each solution can be deployed and decomposed differently based on the needs of your domain, footprint of your technology, and so on.

 The application domain is separated into two elements. There is the SaaS application that represents the tenant experience/application for your solution. This is the surface that tenants touch to interact with your SaaS application. Then there are the backend services that represent business logic and functional elements of a SaaS solution. These could be microservices, or some other packaging of your application services.

 You’ll also note that we’ve broken out provisioning. This is done to highlight the fact that any provisioning of resources for tenants during onboarding would be part of this application domain. Some could argue that this belongs in the control plane. However, we’ve placed it in the application domain, because the resources it must provision and configure are more directly connected to services that are created and configured in the application plane.

 Breaking this down into distinct planes makes it easier to think about the overall landscape of a SaaS architecture. More importantly, it highlights the need for a set of services that are entirely outside the scope of your application functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
