---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/architectural-decisions.html
---

# Architectural decisions in micro-frontends
<a name="architectural-decisions"></a>

Teams that apply a micro-frontend architecture pattern for their applications must make several decisions about architecture early on:
+ [Identification of micro-frontends and definition of boundaries](micro-frontend-boundaries.md)
+ [Composing pages and views with micro-frontends](composition-approaches.md)
+ [Routing, state management, and communication across micro-frontends](routing-communication.md)
+ [Managing dependencies for cross-cutting concerns](manage-dependencies.md)

The following sections cover these topics in more depth.

When making architecture decisions, it's essential to have the correct metrics and to understand the usage patterns application characteristics, and trade-offs. For example, an e-commerce site has different characteristics and usage patterns compared with a video-editing tool or observability dashboards.

Public-facing applications with high traffic and short session depth can be optimized for initial page load metrics such as Time to Interactive (TTI) and First Contentful Paint (FCP). In contrast, an application to which users log in at the start of their day and keep interacting with throughout the day might be optimized for the in-application experience. The application team might optimize for the First Input Delay (FID) metric after each navigation instead of initial page load.

Public websites must cater to various browser environments. Enterprise applications with known constraints on the client environment can optimize their micro-frontend composition according to their constraints.

There is no single right choice for the architecture decisions. Understand the trade-offs, the context where business operates, usage patterns, and metrics to guide decisions that are suitable for each individual application.
