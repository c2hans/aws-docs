---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/introduction.html
---

# Designing for high availability and resiliency in Amazon EKS applications
<a name="introduction"></a>

*Haofei Feng, Frank Fan, and Rus Kalakutskiy, Amazon Web Services*

Ensuring high availability (HA) and resiliency in application design is crucial for achieving near-zero recovery point objective (RPO) and recovery time objective (RTO). As organizations increasingly migrate and modernize their applications to Kubernetes environments, the demand for robust and scalable solutions continues to increase. Amazon Elastic Kubernetes Service (Amazon EKS) helps you to efficiently manage containerized applications at scale.

This guide delves into a set of widely recognized recommendations and best practices for designing and managing Amazon EKS microservice applications. Based on extensive experience and real-world deployments, these insights offer valuable guidance for architects and developers. Implement these recommendations for high performance, reliability, and scalability of your Kubernetes-based applications to achieve robust operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
