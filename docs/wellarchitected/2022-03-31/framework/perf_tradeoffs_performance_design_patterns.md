---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_tradeoffs_performance_design_patterns.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF08-BP02 Learn about design patterns and services
<a name="perf_tradeoffs_performance_design_patterns"></a>

 Research and understand the various design patterns and services that help improve workload performance. As part of the analysis, identify what you could trade to achieve higher performance. For example, using a cache service can help to reduce the load placed on database systems. However, caching can introduce eventual consistency and requires engineering effort to implement within business requirements and customer expectations.

 **Desired outcome:** Researching design patterns will lead you to choosing an architecture design that will support the best performing system. Learn which performance configuration options are available to you and how they could impact the workload. Optimizing the performance of your workload depends on understanding how these options interact with your architecture and the impact they will have on both measured performance and the performance perceived by end users.

 **Common anti-patterns:**
+  You assume that all traditional IT workload performance strategies are best suited for cloud workloads.
+  You build and manage caching solutions instead of using managed services.
+  You use the same design pattern for all your workloads without evaluating which pattern would improve the workload performance.

 **Benefits of establishing this best practice:** By selecting the right design pattern and services for your workload you will be optimizing your performance, improving operational excellence and increasing reliability. The right design pattern will meet your current workload characteristics and help you scale for future growth or changes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Learn which performance configuration options are available and how they could impact the workload. Optimizing the performance of your workload depends on understanding how these options interact with your architecture, and the impact they have on measured performance and user-perceived performance.

 **Implementation steps:**

1. Evaluate and review design patterns that would improve your workload performance.

   1. The [Amazon Builders’ Library](https://aws.amazon.com/builders-library/) provides you with a detailed description of how Amazon builds and operates technology. These articles are written by senior engineers at Amazon and cover topics across architecture, software delivery, and operations.

   1. [AWS Solutions Library](https://aws.amazon.com/solutions/) is a collection of ready-to-deploy solutions that assemble services, code, and configurations. These solutions have been created by AWS and AWS Partners based on common use cases and design patterns grouped by industry or workload type. For example, you can set up a [distributed load testing solution](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) for your workload.

   1. [AWS Architecture Center](https://aws.amazon.com/architecture/) provides reference architecture diagrams grouped by design pattern, content type, and technology.

   1. [AWS samples](https://github.com/aws-samples) is a GitHub repository full of hands-on examples to help you explore common architecture patterns, solutions, and services. It is updated frequently with the newest services and examples.

1. Improve your workload to model the selected design patterns and use services and the service configuration options to improve your workload performance.

   1. Train your internal team with resources available at [AWS Skills Guild](https://aws.amazon.com/training/teams/aws-skills-guild/).

   1. Use the [AWS Partner Network](https://aws.amazon.com/partners/) to provide expertise quickly and to scale your ability to make improvements.

**Level of effort for the implementation plan:** To establish this best practice, you must be aware of the design patterns and services that could help improve your workload performance. After evaluating the design patterns, implementing the design patterns is a *high* level of effort.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Architecture Center](https://aws.amazon.com/architecture/)
+  [AWS Partner Network](https://aws.amazon.com/partners/)
+  [AWS Solutions Library](https://aws.amazon.com/solutions/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
+  [Amazon Builders’ Library](https://aws.amazon.com/builders-library/)
+  [Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/?did=ba_card&trk=ba_card)
+ [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/?did=ba_card&trk=ba_card)

 **Related videos:**
+  [Introducing The Amazon Builders’ Library (DOP328)](https://www.youtube.com/watch?v=sKRdemSirDM)
+  [This is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)

 **Related examples:**
+  [AWS Samples](https://github.com/aws-samples)
+  [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
