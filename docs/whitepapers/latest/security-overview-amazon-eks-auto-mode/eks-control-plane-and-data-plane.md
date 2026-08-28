---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/eks-control-plane-and-data-plane.html
---

# EKS control plane and data plane
<a name="eks-control-plane-and-data-plane"></a>

Amazon EKS operates a control plane that handles the AWS API calls responsible for high-level cluster management (such as `eks:CreateCluster` and `eks:UpdateClusterConfig`). That control plane is not covered in detail in this document; instead, this document focuses on the cluster-specific Kubernetes control plane and data plane. For information about securing the AWS APIs for cluster management, see the [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) guide.

![](http://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/images/image3.png)

**Topics**
+ [Amazon EKS control plane](amazon-eks-control-plane.md)
+ [EKS Auto Mode data plane](eks-auto-mode-data-plane.md)
+ [Workloads](workloads.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
