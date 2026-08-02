---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/phase-1.html
---

# OU design: phase 1
<a name="phase-1"></a>

For the multinational pharmaceutical company in our example, the initial design of the organizations and OUs in AWS Organizations closely followed AWS recommendations for setting up AWS Control Tower. For an example, see the [Landing Zone Accelerator on AWS for Healthcare](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config-healthcare). AWS Control Tower initially provisioned a simple OU structure with common foundational OUs, as described in the blog post [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/?org_product_gs_bp_OUBlog), including the Security OU, the Platform Infrastructure OU, and company-specific OUs.

## Architecture design
<a name="p1-arch-design"></a>

The following diagram shows the initial OU architecture.

![Architecture design for phase 1 of the OU structure](http://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/images/guide-img/dc8c0d6d-2fd2-4887-a8d0-2a424cc8ffb8/images/816de7e8-f5fa-4d89-9cda-b234c107cf73.png)

## Security OU
<a name="p1-security"></a>

The Security OU broadly groups AWS accounts related to security functionality together and uses two accounts (Audit and Log Archive) to store security operational data for central logging and auditing access to the environment. AWS core security services such as Amazon GuardDuty and AWS Security Hub reside in the Audit account.

## Infrastructure Platform OU
<a name="p1-infra"></a>

The Infrastructure Platform OU groups together AWS accounts that provide the infrastructure foundation. Initially deployed within this OU are the AWS accounts for the central networking components (gateways, firewalls, central networking hub, and similar services).

## Additional OUs
<a name="p1-additional"></a>

Other, company-specific OUs (such as a Clinical OU) augment the foundational OUs within a low-level hierarchy. Workloads are implemented with a multi-account structure and with separate environments within those OUs.

Several considerations drove this initial design:
+ Nested OUs were not available at that time in AWS Control Tower and required extensive customization.
+ Initial workloads designated for the cloud focused on particular aspects of the company such as clinical trials or manufacturing equipment analytics (functional views).
+ The company differentiates between five workload environments (development, validation, integration, training, and production). The company needed a playground for developing applications without the strict governance by AWS controls that production workloads required. Development OUs such as the Manufacturing-Dev OU were assigned for this purpose.
+ Workload automation was part of each application's ecosystem and did not need separation.
+ Infrastructure qualification (IQ) and GxP compliance processes did not require a distinction of AWS controls at the OU level.
