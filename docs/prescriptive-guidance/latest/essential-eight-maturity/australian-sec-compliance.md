---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/australian-sec-compliance.html
---

# Australian security and compliance
<a name="australian-sec-compliance"></a>

Many organizations in Australia use the AWS Cloud to store confidential data, process sensitive transactions, and build critical services.

This guide explains how to adapt the Essential Eight framework for the cloud. AWS also supports the following programs, frameworks, and models to help you address your organization's security and compliance requirements:
+ [Information Security Registered Assessors Program](#irap)
+ [Hosting Certification Framework](#hcf)
+ [AWS shared responsibility model](#shared-model)
+ [AWS Well-Architected Framework](#well-architected)

## Information Security Registered Assessors Program
<a name="irap"></a>

An independent Australian Signals Directorate (ASD) certified IRAP assessor assessed AWS services under the Australian Cyber Security Centre (ACSC) [Information Security Registered Assessors Program (IRAP)](https://www.cyber.gov.au/irap) at the PROTECTED level. This assessment helps you verify that, with respect to AWS products and services, AWS has implemented applicable controls for PROTECTED level workloads.

The AWS IRAP PROTECTED package is available through [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html). The assessor used the [ACSC Cloud security guidance](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/cloud-security-guidance) (ACSC website) to develop the IRAP report. For a complete list of AWS services that are in scope, see [AWS services in scope: IRAP](https://aws.amazon.com/compliance/services-in-scope/IRAP/).

## Hosting Certification Framework
<a name="hcf"></a>

The Australian [Hosting Certification Framework](https://www.dta.gov.au/our-projects/hosting-strategy/hosting-certification-framework) supports the secure management of government systems and data. This framework helps organizations mitigate supply chain and data center ownership risks. AWS received Strategic Hosting Provider certification. This certification helps government agencies continue to innovate, knowing that AWS completed an assessment against the framework's requirements.

## AWS shared responsibility model
<a name="shared-model"></a>

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) defines how you share responsibility with AWS for security and compliance in the cloud. AWS is responsible for protecting the infrastructure that runs the services offered in the AWS Cloud, and you are responsible for securing your use of those services, such as your data and applications.

This shared model can help relieve your compliance and operational burden because AWS operates, manages, and controls many components, from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. You assume responsibility for managing the guest operating system (including updates and security patches) and other associated application software. You also assume responsibility for configuring the security group firewall that AWS provides.

Understand the AWS shared responsibility model when you work toward Essential Eight maturity on AWS. Your responsibilities vary depending on the services you use, how you integrate those services into your IT environment, and applicable laws and regulations.

## AWS Well-Architected Framework
<a name="well-architected"></a>

AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) provides architectural best practices that help you design, build, and operate systems on AWS. This framework is built around six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

AWS also provides a service for reviewing your workloads. The [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) helps you review and assess your architecture by using the AWS Well-Architected Framework. It provides recommendations for making your workloads more reliable, secure, efficient, and cost-effective.
