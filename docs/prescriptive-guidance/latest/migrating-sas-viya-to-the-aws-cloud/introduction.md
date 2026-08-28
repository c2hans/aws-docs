---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/introduction.html
---

# Migrating SAS Viya to the AWS Cloud
<a name="introduction"></a>

*Battulga Purevragchaa and Dilip Rajan, Amazon Web Services*

SAS Viya is a cloud-enabled, in-memory analytics engine that provides quick, accurate, and reliable analytical insights. It uses elastic, scalable, and fault-tolerant processing that addresses complex analytical challenges while scaling for future use cases. SAS Viya has the following benefits:
+ Fast processing for large-scale data and complex analytics, which includes machine learning, deep learning, and artificial intelligence.
+ A standardized code base that supports programming in SAS and other languages, such as Python, R, Java, and Lua.
+ Support for cloud, on-site, and hybrid environments. SAS Viya deploys to any infrastructure or application ecosystem.

This guide describes how to migrate SAS Viya to Amazon Web Service (AWS) and modernize your SAS workloads by using Amazon Elastic Kubernetes Service (Amazon EKS). It also discusses other architectural and design considerations in terms of costs, licenses, and best practices. The guide is intended for IT professionals who have both SAS and AWS expertise.

## SAS Viya migration at a glance
<a name="migration-at-a-glace"></a>

|
|
| **Category** | **Attribute** | **Value** |
| --- |--- |--- |
| **Workload** | Source workload | SAS Viya 3.x |
| Source environment | Unix, Linux<br />On-premises/colocation |
| Destination workload | SAS Viya |
| Destination environment | AWS |
| **Migration** | Migration strategy (7 Rs) | Refactor/rearchitect<br />  |
| Is this a workload version upgrade? | Yes |
| Migration duration | Varies by customer |
| **Assumptions and prerequisites** | System limitations (minimum/maximum requirements) | [ SAS System Requirements](https://support.sas.com/en/documentation/system-requirements.html) |
| Service-level agreements (SLAs) | [ SAS Technical Support Services and Policies](https://support.sas.com/en/technical-support/services-policies.html) |
| Recovery time objective (RTO) | [Backup and Restore: Recover from a Disaster](https://go.documentation.sas.com/?cdcId=sasadmincdc&cdcVersion=v_001LTS&docsetId=calbr&docsetTarget=n019z9ma0dvhdyn126dz4gedvaf0.htm&locale=en) |
| Recovery point objective (RPO) |
| Licensing and operating model for the target AWS account | [Bring Your Own License (BYOL)](https://aws.amazon.com/windows/faq/#byol) |
| Migration tools | + [Full-System Migration and Content Migration](https://documentation.sas.com/doc/en/sasadmincdc/v_012/promigwlcm/home.htm)<br />+ [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) |
| AWS services used | + [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks) (Amazon EKS)<br />+ [Amazon Elastic File System](https://aws.amazon.com/efs) (Amazon EFS)<br />+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/)<br />+ [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC)<br />+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)<br />+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) |
| Benchmarks | Contact the SAS Enterprise Excellence Center for benchmark information relevant to your site. |
| **Compliance** | Security and compliance requirements | [Security Administration](https://go.documentation.sas.com/?cdcId=sasadmincdc&cdcVersion=v_001LTS&docsetId=calsecwlcm&docsetTarget=home.htm&locale=en) |
| [AWS Compliance Programs](https://aws.amazon.com/compliance/programs) | [SAS Governance and Compliance Manager](https://support.sas.com/documentation/prod-p/gcm/index.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
