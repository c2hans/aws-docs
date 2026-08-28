---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/overview.html
---

# Overview
<a name="overview"></a>

This guide classifies AWS recommendations for the hybrid cloud into five pillars: networking, security, resiliency, capacity planning, and infrastructure management. It provides guidelines to help you improve your readiness and to develop a migration strategy by using an AWS hybrid edge service such as AWS Outposts or AWS Local Zones. We strongly recommend that you work with your AWS account team or AWS Partner to ensure that an AWS hybrid cloud specialist is available to assist you as you follow this guide and develop your process.

**Note**
Although AWS Outposts and Local Zones address similar problems, we recommend that you review use cases as well as the services and features available to decide which offering best suits your needs. For more information, see the AWS blog post [AWS Local Zones and AWS Outposts, choosing the right technology for your edge workload](https://aws.amazon.com/blogs/compute/aws-local-zones-and-aws-outposts-choosing-the-right-technology-for-your-edge-workload/).

## Hybrid cloud workshops
<a name="workshop"></a>

With the assistance of an AWS hybrid cloud subject matter expert (SME), you can run a hybrid cloud workshop to assess your company's maturity level in relation to the five pillars discussed in this guide.

The workshop focuses on internal areas within your organization, such as networking, security, compliance, DevOps, virtualization, and business units. It helps you design a hybrid cloud architecture that meets your organization's requirements and defines implementation details, following the steps in the [Hybrid cloud adoption process section](pillars.md) of this guide.

## PoCs
<a name="poc"></a>

If you have specific requirements, you can use proofs of concept (PoCs) to validate functionality in Local Zones and AWS Outposts against those requirements.

AWS uses PoCs to help you test the workloads you want to move to an Outpost or Local Zone, to determine whether the workloads will be functional under the test architectures. To access a Local Zone for testing, follow the instructions in the [Local Zones documentation](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html). To test your workload on AWS Outposts, work with your AWS account team or AWS Partner to access an AWS Outposts test laboratory and receive guidance from AWS solutions architects. In all scenarios, the development of a PoC requires you to generate a test document that contains:
+ AWS services to use, such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Block Store (Amazon EBS), Amazon Virtual Private Cloud (Amazon VPC), and Amazon Elastic Kubernetes Service (Amazon EKS)
+ Size and number of instances to consume (for example, `m5.xlarge` or `c5.2xlarge`)
+ Test architecture diagram
+ Test success criteria
+ Details and objectives of each test to runIf you have specific requirements, you can use proofs of concept (PoCs) to validate functionality in Local Zones and AWS Outposts against those requirements.

## Pillars
<a name="pillars-about"></a>

The next section covers [prerequisites and limitations](requirements.md) for using the architectures discussed in this guide. The sections after that cover the details of each pillar so that the recommendations document that you create during the hybrid cloud workshop can reflect the design details required for implementation.
+ [Networking at the edge](networking.md)
+ [Security at the edge](security.md)
+ [Resiliency at the edge](resiliency.md)
+ [Capacity planning at the edge](capacity-planning.md)
+ [Edge infrastructure management](infrastructure-mgmt.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
