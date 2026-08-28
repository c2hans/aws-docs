---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-boundaries.html
---

# Identifying micro-frontend boundaries
<a name="micro-frontend-boundaries"></a>

To improve team autonomy, the business capabilities provided by an application can be decomposed into several micro-frontends with minimal dependencies on each other.

Following the DDD methodology discussed previously, teams can break down an application domain into business subdomains and bounded contexts. Autonomous teams can then own the functionality of their bounded contexts and deliver those contexts as micro-frontends.

A well-defined bounded context should minimize functional overlap and the need for runtime communication across contexts. The required communication can be implemented with event-driven methods. This is no different from event-driven architecture for microservices development.

A well-architected application should also support the delivery of future extensions by new teams to provide a consistent experience for customers.

## How to slice a monolithic application into micro-frontends
<a name="monolith-slicing"></a>

The [Overview](introduction.md#overview) section included an example of identifying independent functional contexts on a web page. Several patterns for splitting the functionality on the user interface emerge.

For example, when the business domains form stages of a user journey, a vertical split on the frontend can be applied, where a collection of views in the user journey is delivered as micro-frontends. The following diagram shows a vertical split, where Catalog, Checkout, and Invoice steps are delivered by separate teams as separate micro-frontends.

![Each micro-frontend having a header, a catalog, subscription details, and a footer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/e84a18f8-6eac-4fbf-9cdd-9480cddfa896.png)

For some applications, vertical split alone might not be enough. For example, some functionality might need to be provided in many views. For these applications, you can apply a mixed split. The following diagram shows a mixed split solution in which micro-frontends for Station finder and Route explorer both use the Map view functionality.

![Station finder's Team Discover and Route explorer's Team Route both use Map view, owned by Team Map.](http://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/22fb54ac-a4b0-4dae-8447-ad6a2dcbb54f.png)

Portal-type or dashboard-type applications typically bring frontend capabilities together in a single view. In these types of applications, each widget can be delivered as a micro-frontend, and the hosting application defines the constraints and interfaces that the micro-frontends should implement.

This approach provides a mechanism for micro-frontends to handle concerns such as viewport sizing, authentication providers, configuration settings, and metadata. These types of applications optimize for extensibility. New features can be developed by new teams to scale the dashboard capabilities.

The following diagram shows a dashboard application developed by three individual teams that are part of Team Dashboard.

![Current multiple-team dashboard application, with the possibility of new features by future teams.](http://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/9411fe52-3855-4fd4-8f9c-9d224361a6c2.png)

In the diagram, the future view represents new features developed by new teams to scale Team Dashboard and the dashboard capabilities.

Portal and dashboard applications usually compose functionality by using a mixed split in the UI. The micro-frontends are configurable with well-defined settings, including position and size constraints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
