---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/ml-cluster-configuration.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS cluster configuration for AI/ML workloads
<a name="ml-cluster-configuration"></a>

**Tip**
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section is designed to help you configure Amazon EKS clusters optimized for AI/ML workloads. You’ll find guidance on running GPU-accelerated containers using Linux and Windows optimized AMIs, setting up training clusters with Elastic Fabric Adapter (EFA) for high-performance networking, and creating inference clusters with AWS Inferentia instances, including prerequisites, step-by-step procedures, and deployment considerations.

**Topics**
+ [Use EKS-optimized accelerated AMIs for GPU instances](ml-eks-optimized-ami.md)
+ [Run GPU-accelerated containers (Windows on EC2 G-Series)](ml-eks-windows-optimized-ami.md)
+ [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md)
+ [Use AWS Inferentia instances with Amazon EKS for Machine Learning](inferentia-support.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
