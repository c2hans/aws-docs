---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/architecture.html
---

# Red Hat OpenShift architecture on AWS
<a name="architecture"></a>

At a high level, the Red Hat OpenShift infrastructure runs on AWS, and the cluster is registered on the Red Hat Portal. When you create a cluster, you provide your Red Hat account details. This generates a token that helps identify your Red Hat account. The following diagram illustrates the high-level process, regardless of the implementation method you choose:

1. Create a Red Hat account.

1. Generate a token from the account.

1. Use the token to provision a cluster on AWS.

1. Administer the cluster by using the Red Hat console.

The entire infrastructure, including the control plane, user nodes, and Network Load Balancer, runs on AWS.

![Red Hat OpenShift architecture and high-level implementation process](http://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/images/guide-img/bcbfa5c1-b077-4a7c-9aab-f667a34c404d/images/5e105ac5-4b09-425f-a345-40fe10190799.png)

## Infrastructure requirements
<a name="infrastructure"></a>

Because Red Hat OpenShift uses Kubernetes for container orchestration, it requires infrastructure components such as a virtual private cloud (VPC), subnets, and Amazon Route 53 on AWS. These requirements can change depending on the topology, but the following core components are always required:
+ Kubernetes and Red Hat OpenShift Container Platform control plane services that run on master nodes
+ The default router
+ The container image registry
+ The cluster metrics collection or monitoring service
+ Cluster-aggregated logging
+ Service brokers

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
