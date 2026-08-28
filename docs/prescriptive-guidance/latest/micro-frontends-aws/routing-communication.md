---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/routing-communication.html
---

# Routing and communication across micro-frontends
<a name="routing-communication"></a>

Routing options depend on the composition approach. Communication can be optimized by reducing coupling between front-end components.

## Routing
<a name="routing"></a>

Applications that use client-side composition with vertical split can use server-side routing (multipage application) or client-side routing (single-page application). If they use a mixed split for the UI composition, client-side routing is necessary to support deeper routing hierarchies of micro-frontends on a page.

Applications that use edge-side composition and server-side composition align better with server-side routing, or routing with edge compute such as Lambda@Edge with Amazon CloudFront.

## Communication between micro-frontends
<a name="communication"></a>

With micro-frontend architectures, we recommend reducing the coupling between frontend components. One approach to reduce coupling is to move away from synchronous function calls to asynchronous messaging.

Browser runtimes and user interactions are asynchronous by nature. Events can be exchanged between producers and consumers through messages. The events provide a well-defined interface for communication across micro-frontends.

If you follow DDD practices to identify your bounded contexts for micro-frontends, the next step is to identify events that must be communicated across the boundaries.

The messaging mechanism for events can be native DOM events (`CustomEvents`), JavaScript event emitters, or reactive stream libraries provided by the platform teams. Micro-frontends publish events and subscribe to events relevant for their bounded context. With this method, the publishers and subscribers don't need to be aware of each other. The contract is the event definition. For a visual representation of this, see the *Communicate with events* section of the [Bounded context with event architectures diagram](https://eda-visuals.boyney.io/visuals/bounded-context-with-event-architectures).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
