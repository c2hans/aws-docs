---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/introduction.html
---

# Increasing resilience and improving customer experience by using chaos engineering on AWS
<a name="introduction"></a>

*Laurent Domb, Amazon Web Services*

Chaos engineering is the discipline of experimenting on an application in order to build confidence in your organization's and application's capability to withstand turbulent conditions in production. It is a proactive approach to resilience, with the goal to verify if your application and organization are able to absorb, adapt to, and eventually recover from service impairments by introducing controlled failures across people, processes, and technology. The intent is also to identify and eliminate weaknesses before they can cause outages or other disruptions in production.

At Amazon, we understand that failure is inevitable in distributed systems, to the point that functioning despite the presence of failures is a normal mode of operation. Because interactions between services are bound to fail, you need to understand how your services react during various failure modes and build services that are resilient to key vulnerabilities such as dependency failures, retry storms, impaired Availability Zones, and host resource exhaustion.

Let's take the example of a retry storm. A localized failure in a client can impact multiple services significantly. This is commonly referred as the *butterfly effect*. A *retry storm* is a manifestation of the butterfly effect where a failing dependency triggers clients, and clients of those clients, to retry the failed operation, leading to an exponential growth in traffic. Services become overloaded because they must respond to regular traffic in addition to retry traffic while handling a degradation in performance.

Chaos engineering has emerged as a response to the increasing complexity of distributed systems. It is a multidisciplinary approach that combines principles from chaos theory, systems thinking, and engineering to design and manage complex systems that are resilient to unexpected events and behaviors. At its core, chaos engineering is concerned with understanding and managing the behavior of complex systems under conditions of uncertainty and unpredictability. It recognizes that traditional approaches to engineering, which rely on predicting and controlling outcomes, are often insufficient for dealing with the complex and dynamic nature of distributed systems. As these systems grow, they often exceed the scope of understanding of any single individual.

Chaos engineering provides concepts, techniques, and tools to intentionally inject failures into systems to uncover weaknesses before they manifest in production. This proactive approach allows organizations to build confidence that their systems will perform under stressful conditions. Although chaos engineering is still an evolving practice, it represents a fundamental shift toward designing, managing, and operating modern computing systems to be resilient in the face of increasing complexity and interconnectedness.

The following sections of this guide discuss the benefits of chaos engineering, explain how to conduct chaos engineering experiments, and describe the approaches you can take to implement chaos engineering at scale in your organization. Also included are sample experiment planning and experiment result documents that you can use as templates for your chaos engineering experiments.
+ [Overview](overview.md)
+ [Getting started with chaos engineering](getting-started.md)
+ [Implementing chaos engineering on AWS](implementation.md)
+ [Continuous chaos engineering experiment lifecycle](lifecycle.md)
+ [Scaling chaos engineering across your organization](scaling.md)
+ [Conclusion](conclusion.md)
+ [Resources](resources.md)
+ [Appendix: Sample documents](appendix.md)

The next section explores how the characteristics of chaos engineering differ from traditional resilience testing such as unit, smoke, or integration tests.
