---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/team.html
---

# Security and compliance workstream and team structure
<a name="team"></a>

AWS offers the [AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/). This program separates the [migration process](https://aws.amazon.com/cloud-migration/how-to-migrate/) into three phases: assess, mobilize, and migrate and modernize. As part of the mobilize phase, you create a migration plan and refine your business case. You address gaps in your organization's readiness that were uncovered in the assess phase. You also focus on building your landing zone, driving operational readiness, and developing cloud skills. A key part of the mobilize phase is create a *security and compliance workstream* that plans and addresses security, risk, and compliance requirements for the migration. As shown in the following image, the security and compliance workstream is part of the platform perspective of this migration methodology.

![Security and compliance in the mobilize phase of the migration process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/images/guide-img/c77d8a62-e667-4282-8232-e9d9bafb3db2/images/fb37e1a3-007f-4191-bb2d-b3eda15fd0a6.png)

During the mobilize phase, it's important to discover and plan your security and compliance requirements. Evaluate your requirements through the lenses of tools, people, and process. There are five key domains for the security and compliance workstream during the mobilize phase:
+ Security discovery and alignment
+ Security framework mapping
+ Security implementation, integration, validation
+ Security documentation
+ Security and compliance cloud operations

These activities are discussed in detail in the [Domains of the security and compliance workstream](domains.md) chapter of this guide. First, it's important to understand the composition and structure of the teams that support the security and compliance workstream. These teams perform or facilitate the activities in the security and compliance workstream.

## Security and compliance team structure
<a name="security-and-compliance-team-structure"></a>

The first step for effective security and compliance mobilization is to set up or form two teams that can support, complete, and govern the five key activities in the framework. The following image shows the recommended team structure and resource requirements. The security and compliance workstream is primarily composed of individuals from the quality assurance (QA) team and the planning and delivery team.

![Recommended team structure for the security and compliance team.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/images/guide-img/c77d8a62-e667-4282-8232-e9d9bafb3db2/images/4f8a9e4b-4cb0-4011-b1d5-5f75972a5a69.png)

The planning and delivery team is responsible for the following in the security and compliance workstream:
+ Understanding the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
+ Understanding AWS security and compliance services at the 300–400 level
+ Understanding compliance architectures design and setup on AWS
+ Collecting security and compliance requirements by using defined tooling or mechanisms in place
+ Mapping security requirements, policies, configurations, controls, and guardrails to service configurations on AWS (This is known as *security framework mapping*)
+ Providing at least two individuals who are certified in AWS security
+ Creating security documentation

The QA team is responsible for the following in the security and compliance workstream:
+ Providing a total of 3–5 individuals, and at least two of them must have AWS security certifications
+ Understanding compliance architecture design and setup on AWS
+ Understanding and experience completing five or more [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) reviews
+ Validating that the AWS infrastructure and resources comply with AWS security and compliance best practices
+ Creating and presenting a security validation report

The requirements for each team vary depending on the migration size and security and compliance complexity. It is also important to note that the team structure and requirements are limited to the following scope:
+ Operation of the security and compliance workstream in the mobilize phase
+ Security and compliance validation of the migration and modernization

After the migration, we recommend that you establish a dedicated Security Operations Center (SOC) to continuously monitor and govern security and compliance in the AWS Cloud.
