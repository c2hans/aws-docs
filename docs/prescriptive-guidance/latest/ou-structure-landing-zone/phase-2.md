---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/phase-2.html
---

# OU design: phase 2
<a name="phase-2"></a>

The pharmaceutical company in our example accelerated into a new phase of cloud maturity by deploying qualified production workloads into the existing OUs. This initiated a review of the initial design, and the phase 1 structure was challenged as more workloads migrated to the regulated AWS landing zone.

The following new requirements and insights became important:
+ The company implemented data sharing model workloads, so applications acquired a multi-purpose nature that could no longer be assigned to separate OUs such as Clinical or Manufacturing.
+ Qualification (in particular, ongoing qualification) became a vital aspect of many workloads. These workloads had to be integrated into operational processes so they could follow security best practices more easily. Qualified workloads required more stringent AWS controls, which were set at the OU level in phase 1.
+ Nested OU functionality became available in AWS Control Tower.
+ Upskilling and experience resulted in a better understanding of which specific policies were relevant for workloads.
+ The company defined and agreed on an operational model that was based on responsibility alignment.
+ Workload segmentation and structuring blueprints matured and were adopted for workload migrations.

As a result of these, a new design was implemented in phase 2 and AWS accounts migrated to that new structure. This new structure includes the OUs described in the following sections.

## Architecture design
<a name="p2-arch-design"></a>

The following diagram shows the OU architecture for phase 2.

![Architecture design for phase 2 of the OU structure](https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/images/guide-img/dc8c0d6d-2fd2-4887-a8d0-2a424cc8ffb8/images/ce36cc11-de9b-4cb1-a017-abd9279bdfe6.png)

## Security OU
<a name="p2-security"></a>

The Security OU contains AWS accounts related broadly to security functionality and uses two accounts (Audit and Log Archive) to store security operational data for central logging and auditing access to the environment. AWS core security services such as Amazon GuardDuty and AWS Security Hub reside in the audit account. This OU remains unchanged from the original design.

## Infrastructure Platform OU
<a name="p2-infra"></a>

The Infrastructure Platform OU contains foundational infrastructure accounts such as networking and shared automation across the AWS landing zone. This OU remains unchanged from the original design.

## Qualified OU
<a name="p2-qualified"></a>

The Qualified OU contains workloads that require a qualified infrastructure such as stringent change management, qualification, and validation.

## Non-qualified OU
<a name="p2-non-qualified"></a>

The Non-Qualified OU contains workloads that don't have GxP requirements or aren't business-critical.

## Automations OU
<a name="p2-automations"></a>

The Automations OU contains shared resources for workload automation, such as continuous integration and continuous delivery (CI/CD) pipelines for infrastructure management. Depending on requirements, automation can either be split across environments or hosted in a single AWS account.

## Exceptions OU
<a name="p2-exceptions"></a>

The Exceptions OU contains workloads that require special treatment that would otherwise be prevented by policies. For example, widely accessible and readable Amazon Simple Storage Service (Amazon S3) buckets would belong in the Exceptions OU.

## Graveyard OU
<a name="p2-graveyard"></a>

The Graveyard OU contains AWS accounts for workloads that will be deleted. Policies in these accounts should be removed for effective and simple administrative access until the account expires or is deleted.
