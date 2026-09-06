---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html
---

# Building multi-tenant architectures for agentic AI on AWS
<a name="introduction"></a>

*Aaron Sempf and Tod Golding, Amazon Web Services*

Agentic AI represents a disruptive paradigm shift that requires organizations to rethink how to build, deliver, and operate their systems. The agentic model has teams exploring new ways to decompose systems into one or more agents that create new paths, possibilities, and values.

Much of the agentic discussion centers around the tools, frameworks, and patterns that are used to build and implement agents. We must not only adopt good tools to create agents but also new integration protocols, authentication strategies, and discovery mechanisms that can serve as the basis of agentic architectures.

While the number of agentic tools grows, teams must also consider how their agents address more traditional architecture challenges. Scale, noisy neighbor, resilience, cost, and operational efficiency are fundamental topics that must be evaluated when you're designing, building, and deploying agents. Regardless of how autonomous and smart agents might be, we must also ensure that they achieve economies of scale, efficiency, and agility that align with business needs.

This guide's goal is to explore various dimensions of agentic footprints. This includes reviewing various agent deployment and consumption patterns and highlighting different strategies for creating agents that address architectural goals. It also means looking at how agents might be consumed in a multi-tenant environment by introducing internal constructs that are typically required in a multi-tenant setting.

## Intended audience
<a name="intended-audience"></a>

This guide is for architects, developers, and technology leaders who want to build AI-driven multi-tenant systems.

## Objectives
<a name="objectives"></a>

This guide helps you do the following:
+ Understand multi-tenant agent deployments, exploring both siloed and pooled models, and how tenant context affects agent implementation
+ Explore agent management, including onboarding, tenant isolation, and resource management across single- and multi-provider environments
+ Evaluate aspects of multi-tenant agents, including data ownership, monitoring, and testing

## About this content series
<a name="about-this-content-series"></a>

This guide is part of a series about agentic AI on AWS. For more information and to view the other guides in this series, see [Agentic AI](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) on the AWS Prescriptive Guidance website.
