---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Using service-linked roles for Amazon EKS
<a name="using-service-linked-roles"></a>

Amazon Elastic Kubernetes Service uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon EKS. Service-linked roles are predefined by Amazon EKS and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles for Amazon EKS clusters](using-service-linked-roles-eks.md)
+ [Using roles for Amazon EKS node groups](using-service-linked-roles-eks-nodegroups.md)
+ [Using roles for Amazon EKS Fargate profiles](using-service-linked-roles-eks-fargate.md)
+ [Using roles to connect a Kubernetes cluster to Amazon EKS](using-service-linked-roles-eks-connector.md)
+ [Using roles for Amazon EKS local clusters on Outpost](using-service-linked-roles-eks-outpost.md)
+ [Using roles for Amazon EKS Dashboard](using-service-linked-roles-eks-dashboard.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
