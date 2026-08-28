---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/australian-sec-compliance.html
---

# Australian security and compliance
<a name="australian-sec-compliance"></a>

Many organizations in Australia use the AWS Cloud to store confidential data, process sensitive transactions, and build critical services.

Although this guide discusses how to adapt the Essential Eight framework for the cloud, AWS also provides the following certifications and models to help you meet your organization's security and compliance requirements:
+ [Information Security Registered Assessors Program](#irap)
+ [Hosting Certification Framework](#hcf)
+ [AWS shared responsibility model](#shared-model)
+ [AWS Well-Architected Framework](#well-architected)

## Information Security Registered Assessors Program
<a name="irap"></a>

AWS services have been assessed under the Australian Cyber Security Centre (ACSC) [Information Security Registered Assessors Program (IRAP)](https://www.cyber.gov.au/irap) at the PROTECTED level. An independent Australian Signals Directorate (ASD) certified IRAP assessor completed the IRAP assessment of AWS. This assessment provides assurance that, with respect to AWS products and services, applicable controls are implemented for PROTECTED level workloads.

The AWS IRAP PROTECTED package is available through [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html). The IRAP report was developed using the [ACSC Cloud security guidance](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/cloud-security-guidance) (ACSC website). For a complete list of AWS services that are in scope, see [AWS services in scope: IRAP](https://aws.amazon.com/compliance/services-in-scope/IRAP/).

## Hosting Certification Framework
<a name="hcf"></a>

The Australian [Hosting Certification Framework](https://www.dta.gov.au/our-projects/hosting-strategy/hosting-certification-framework) was developed to support the secure management of government systems and data. This framework is intended to help organizations mitigate supply chain and data centre ownership risks. AWS was granted certification at the Certified Strategic level. This helps government agencies continue to innovate at a rapid pace, knowing that AWS meets government requirements.

## AWS shared responsibility model
<a name="shared-model"></a>

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) defines how you share responsibility with AWS for security and compliance in the cloud. AWS secures the infrastructure that runs all of the services offered in the AWS Cloud, and you are responsible for securing your use of those services, such as your data and applications.

This shared model can help relieve your compliance and operational burden because AWS operates, manages, and controls many components, from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. You assume responsibility for managing the guest operating system (including updates and security patches) and other associated application software. You also assume responsibility for configuring the security group firewall that AWS provides.

It is critical that you understand the AWS shared responsibility model when you approach Essential Eight maturity on AWS. Your responsibilities vary depending on the services used, the integration of those services into your IT environment, and applicable laws and regulations.

## AWS Well-Architected Framework
<a name="well-architected"></a>

AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) provides architectural best practices that help you design, build, and operate systems on AWS. This framework is built around six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

AWS also provides a service for reviewing your workloads. The [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) helps you review and assess your architecture by using the AWS Well-Architected Framework. It provides recommendations for making your workloads more reliable, secure, efficient, and cost-effective.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
