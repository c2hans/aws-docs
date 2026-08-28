---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/introduction.html
---

# Best practices for streamlining Amazon EKS observability
<a name="introduction"></a>

*Ishwar Chauthaiwale, Pratap Kumar Nanda, and Naveen Suthar, Amazon Web Services*

Amazon Elastic Kubernetes Service (Amazon EKS) requires comprehensive observability solutions to monitor and troubleshoot containerized workloads effectively. Distributed systems and microservices have complex architectures in Amazon EKS environments, so implementing proper observability practices is crucial for maintaining reliable operations. Effective observability in Amazon EKS environments enables teams to gain deep insights into application performance, troubleshoot issues efficiently, and maintain optimal cluster health.

The challenge lies in navigating the vast ecosystem of tools and techniques available for Amazon EKS observability while adhering to best practices that align with organizational goals and industry standards. Effective observability strategies must balance comprehensive data collection with performance considerations, cost-effectiveness, and scalability.

This guide is designed to help organizations optimize their Amazon EKS observability across the following areas:
+ Establishing efficient **logging** mechanisms
+ Implementing robust **monitoring** solutions
+ Using distributed **tracing** for complex architectures
+ Implementing **alerting** and incident response strategies

By adopting these best practices, your organization can enhance their ability to gain deep insights into their Amazon EKS environment, which leads to improved reliability, performance, and operational efficiency. This streamlined approach to observability aids in troubleshooting and maintenance, and supports data-driven decision-making for continuous improvement of Kubernetes-based applications and infrastructure.

This guide dives deep into each aspect of Amazon EKS observability and explores the tools and strategies that you can tailor to meet the specific needs of your Amazon EKS deployments, from small-scale applications to large, complex microservices architectures. (For detailed information about Amazon EKS, see the [service documentation](https://docs.aws.amazon.com/eks/).)

In this guide:
+ [Logging in Amazon EKS](logging.md)
+ [Monitoring in Amazon EKS](monitoring.md)
+ [Tracing in Amazon EKS](tracing.md)
+ [Alerting in Amazon EKS](alerting.md)
+ [Resources](resources.md)
+ [Next steps](next-steps.md)

## Objectives
<a name="objectives"></a>

This guide can help you and your organization achieve the following business objectives:
+ **Enhanced operational visibility** – Achieve comprehensive insight into your Amazon EKS clusters and applications through effective observability practices.

  This objective emphasizes the importance of maintaining complete visibility across your Amazon EKS environment. Tools such as [AWS X-Ray](https://aws.amazon.com/xray/features/), [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), and[AWS Distro for OpenTelemetry ](https://aws.amazon.com/blogs/containers/metrics-and-traces-collection-using-amazon-eks-add-ons-for-aws-distro-for-opentelemetry/)help you understand system behavior, identify issues quickly, and maintain optimal performance.
+ **Improved troubleshooting efficiency** – Reduce mean time to detection (MTTD) and mean time to resolution (MTTR) through effective tracing and monitoring strategies.

  This objective focuses on implementing observability practices that enable quick identification and resolution of issues. Techniques such as distributed tracing, effective logging, and comprehensive metrics collection are key to achieving this objective.
+ **Proactive performance management** – Enable early detection of potential issues before they affect end users.

  Proactive monitoring is crucial for maintaining high service availability and performance. This objective addresses the importance of implementing proper alerting, trend analysis, and predictive monitoring to prevent service disruptions.
+ **Cost-effective observability** – Optimize observability costs while maintaining comprehensive system visibility.

  Cost optimization encompasses implementing efficient sampling strategies, appropriate data retention policies, and optimal instrumentation approaches. The goal is to balance observability needs with cost considerations while ensuring effective system monitoring.
+ **Scalable monitoring architecture** – Make sure that your observability solutions scale seamlessly with your Amazon EKS environment.

  This objective focuses on implementing monitoring solutions that can grow with your application. Whether you're running a single cluster or a multi-cluster, multi-Region deployment, your observability strategy should scale accordingly

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
