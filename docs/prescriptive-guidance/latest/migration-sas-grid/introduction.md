---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/introduction.html
---

# Migrating SAS Grid to the AWS Cloud
<a name="introduction"></a>

*Battulga Purevragchaa, Amazon Web Services*

This guide provides prescriptive steps to streamline the migration of SAS Grid software to Amazon Web Services (AWS).

SAS customers migrate their applications from on-premises data centers to AWS to gain access to cloud-based data lakes and data warehouses. Their goals are to increase the agility, security, and reliability of their applications, to lower costs, and to improve data analytics capabilities. Moving a SAS software deployment to a new location is a multi-step process that involves tasks that must be identified, planned, implemented, and tested.

This guide is intended for organizations that want to rehost or replatform their current SAS Grid installations from on premises or privately hosted environments to AWS. This migration enables organizations to evolve analytics capabilities, minimize rehosting or replatforming risks, and standardize governance and management of the statistical computing environment on AWS. The target audience is IT professionals who have both SAS and AWS expertise.

## SAS Grid migration at a glance
<a name="migration-at-a-glance"></a>

|  |  |
| --- |--- |
| Workload | Source workload | + SAS Grid Manager for Platform<br />+ SAS Grid Manager |
| --- |--- |--- |
| Source environment | + Unix, Linux<br />+ On-premises/co-location/non-AWS environment |
| Destination workload | + SAS Grid Manager<br />+ Deployment: SAS Intelligence Platform software on a multi-machine host |
| Destination environment | + AWS<br />+ Operating model: customer/MSP (ISV) |
| **Migration** | Migration strategy (7 Rs) | Rehost/replatform |
| Is this an upgrade in workload version? | No |
| Is the source workload different from the ISV workload? | No |
| Migration duration | Varies by customer |
| **Cost** | Cost of running ISV workload on AWS | [Cost and licensing](licensing.md) |
| Cost of running ISV associated workload that is being migrated to AWS | No |
| **Assumptions and prerequisites** | System limitations (minimum/maximum requirements) | [SAS System Requirements](https://support.sas.com/en/documentation/system-requirements.html) |
| Service-level agreements (SLAs) | [SAS Technical Support Services and Policies](https://support.sas.com/en/technical-support/services-policies.html) |
| Recovery time objective (RTO) | [SAS 9.4 Disaster Recovery Policy](https://support.sas.com/en/technical-support/services-policies/disaster-recovery-policy.html) |
| Recovery point objective (RPO) | [SAS 9.4 Disaster Recovery Policy](https://support.sas.com/en/technical-support/services-policies/disaster-recovery-policy.html) |
| Licensing and operating model for the target AWS account | + Bring Your Own License (BYOL)<br />+ Managed services |
| Migration tooling | + [SAS Migration Utility](https://documentation.sas.com/doc/en/bicdc/9.4/bimig/n08001intelplatform00migrate.htm)<br />+ [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) |
| AWS services used | + [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/)<br />+ [FSx for Lustre](https://aws.amazon.com/fsx/lustre/)<br />+ [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)<br />+ [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/)NAT gatewayInternet gateway<br />+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)<br />+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) |
| Benchmarks | Contact the SAS Enterprise Excellence Center for benchmark information relevant to your site. |
| **Compliance** | Security and compliance requirements | [SAS 9.4 Intelligence Platform: Security Administration Guide](https://documentation.sas.com/doc/en/bicdc/9.4/bisecag/titlepage.htm) |
| Other [compliance certifications](https://aws.amazon.com/compliance/programs) | [SAS Governance and Compliance Manager](https://support.sas.com/documentation/prod-p/gcm/index.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
