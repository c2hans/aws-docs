---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/security-overview-amazon-eks-auto-mode.html
---

# Abstract and introduction
<a name="security-overview-amazon-eks-auto-mode"></a>

**First published September 18, 2025**

*Last updated September 18, 2025*

This paper is intended for existing and potential Amazon EKS customers who are using or considering EKS Auto Mode. It provides a comprehensive security overview of Auto Mode, which is helpful for new adopters and deepens understanding of Auto Mode for current customers.

## Introduction
<a name="introduction"></a>

Since its introduction in 2018, [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks) has provided a managed Kubernetes control plane integrated with existing AWS services, where [Amazon Web Services (AWS)](https://aws.amazon.com/) is responsible for the health, scaling, and patching of the control plane. Amazon EKS Auto Mode represents a significant evolution in Kubernetes infrastructure management, combining secure and scalable cluster infrastructure with integrated Kubernetes capabilities managed by AWS. We have extended the AWS managed portion of the control plane to include the worker nodes, their components and core cluster capabilities.

The result is a production-ready, Kubernetes-conformant cluster that is ready to host workloads out of the box. Customers who have previously used managed node groups (MNG) or [Karpenter](https://karpenter.sh/) can transition to EKS Auto Mode, so they can focus on deploying their applications while Auto Mode handles the rest. This makes it an ideal solution for those who want to use Kubernetes without having to manage its underlying complexity.

To make this transition seamless, EKS Auto Mode has been designed to be compatible with existing clusters and their compute management. This allows transitioning the entirety or a subset of workloads to Auto Mode managed compute to minimize disruption.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
