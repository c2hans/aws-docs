---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/integration-vpc-lattice.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable secure cross-cluster connectivity with Amazon VPC Lattice
<a name="integration-vpc-lattice"></a>

Amazon VPC Lattice is a fully managed application networking service built directly into the AWS networking infrastructure that you can use to connect, secure, and monitor your services across multiple accounts and Virtual Private Clouds (VPCs). With Amazon EKS, you can leverage Amazon VPC Lattice through the use of the AWS Gateway API Controller, an implementation of the Kubernetes [Gateway API](https://gateway-api.sigs.k8s.io/). Using Amazon VPC Lattice, you can set up cross-cluster connectivity with standard Kubernetes semantics in a simple and consistent manner. To get started using Amazon VPC Lattice with Amazon EKS see the [AWS Gateway API Controller User Guide](https://www.gateway-api-controller.eks.aws.dev/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
