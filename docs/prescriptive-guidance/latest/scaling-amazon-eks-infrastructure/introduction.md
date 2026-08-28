---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/scaling-amazon-eks-infrastructure/introduction.html
---

# Scaling Amazon EKS infrastructure to optimize compute, workloads, and network performance
<a name="introduction"></a>

*Aniket Dekate, Ishwar Chauthaiwale, and Aniket Kurzadkar, Amazon Web Services*

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service. With Amazon EKS, you can run Kubernetes pods in a containerized cloud environment without needing to install and operate your own control plane. With AWS managing the control plane, Amazon EKS reduces organizational operational management. Other benefits of using Amazon EKS include scaling, reliability, and security in the cloud environment.

This guide is designed to help organizations to optimize their Amazon EKS infrastructure across the following areas:
+ [Compute scaling](compute-scaling.md) is a critical component to application performance in a dynamic Kubernetes environment:
  + **Efficient resource allocation** – Learn about techniques for allocating computed resources dynamically to meet varying demand.
  + **Automation tools** – Get an overview of tools and services that automate compute scaling, reducing the need for manual intervention.
+ [Workload scaling](workload-scaling.md) helps to make sure that applications can handle varying workloads without performance degradation:
  + **Horizontal pod autoscaler** – Take an in-depth look at how an HPA helps in scaling workloads based on real-time metrics.
  + **Cluster Proportional Autoscaler** – Learn how CPA automatically scales and maintains a proportional relationship between nodes and replicas, scaling workloads up or down as the cluster size changes.
  + **Event-driven scaling** – Review strategies for scaling applications in response to specific events or triggers.
+ [Network scaling](network-scaling.md) helps to maintain seamless communication between services and efficient data flow in dynamic environments:
  + **Amazon VPC CNI plugin** – Learn how the VPC CNI plugin enables scalable networking within Amazon EKS clusters.
  + **Custom networking** - Review IP address management and network traffic segregation on Amazon EKS clusters.
  + **Prefix delegation** - Get an overview of streamlining IP management in large and scalable Amazon EKS clusters.
  + **Amazon VPC Lattice** – Get an overview of how VPC Lattice can manage cross-VPC and service-to-service networking for seamless scaling.
+ [Cost optimization](cost-optimization.md) helps businesses see where their resources are being spent and appropriately assign expenses to departments or projects:
  + **Right-sizing resources** – Consider techniques for sizing cloud resources appropriately for the workload.
  + **Cost monitoring and control** – Review tools and best practices for tracking and optimizing cloud expenses.

Each section focuses on particular goals that are necessary to create a reliable, effective, and affordable cloud environment.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization achieve the following business objectives:
+ **Enhanced resource efficiency** – Achieve optimal resource utilization by dynamically scaling compute, workloads, and network resources based on real-time demands.

  This objective emphasizes the importance of scaling resources up and down in response to actual usage patterns. Tools such as horizontal pod autoscalers and the Amazon VPC CNI plugin help organizations only use the resources that they need, minimizing waste and maximizing performance.
+ **Improved application performance** – Maintain high performance and responsiveness of applications, even under fluctuating workloads and traffic patterns.

  This objective focuses on strategies to help make sure that applications can handle peak traffic and heavy workloads without compromising performance. Techniques such as event-driven workload scaling, efficient compute allocation, and scalable network architectures are key to achieving this objective.
+ **Seamless scalability** – Enable smooth scaling of infrastructure components, allowing for effortless growth and adaptation to changing business needs.

  Seamless scalability is crucial for organizations that anticipate growth or experience varying traffic levels. This objective addresses the importance of implementing scalable solutions across compute, workload, and network resources, so that scaling can be automatic, efficient, and transparent.
+ **Cost optimization** – Minimize cloud costs while maintaining or improving performance and scalability.

  Cost optimization can encompass reducing expenses, such as right-sizing resources, using cost-effective scaling solutions, and monitoring spending. The goal is to balance cost savings with the need for high performance and scalability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
