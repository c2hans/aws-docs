---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/security-compliance.html
---

# Achieving security and compliance for semiconductor development environments on AWS
<a name="security-compliance"></a>

AWS has developed best practice guidance to implement security controls and published reference architectures to address semiconductor industry needs. This section discusses how to use the AWS recommended designs and reference architectures to help achieve security and compliance for your mission-critical workloads on AWS.

## Reducing compliance efforts with AWS
<a name="compliance-efforts"></a>

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes how responsibility for security and compliance is shared between AWS and the customer. AWS is responsible for security *of* the cloud, and the customer is responsible for security *in* the cloud. This can help companies reduce the effort necessary to achieve compliance with corporate and regulatory requirements by placing the responsibility for cloud infrastructure on AWS.

The following AWS services can help semiconductor companies demonstrate compliance with corporate and regulatory requirements:
+ [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides downloadable compliance reports for various compliance frameworks, including International Organization for Standardization (ISO), National Institute of Standards and Technology (NIST), and Federal Risk and Authorization Management Program (FedRAMP). You can combine AWS Artifact reports with corporate assessment of cloud resources to demonstrate compliance to auditors and help reduce the time and effort required to become compliant with regulations such as United States International Traffic in Arms Regulations (ITAR).
+ [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) can map your compliance requirements to AWS usage data by using prebuilt and custom frameworks and automated evidence collection.

By using these services and features, companies can achieve compliance with corporate and regulatory requirements more efficiently and effectively. For more information about whether an AWS service is in scope of AWS assurance programs, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/).

## Using provided reference architectures
<a name="using-reference-architectures"></a>

AWS develops prescriptive guidance and best practices based on thousands of deployments across various industries. These recommendations are included within the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc), [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/professional-services/CAF/), and [AWS Security Reference Architecture (AWS SRA).](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)

When architecting and designing your secure development environment, AWS provides semiconductor and electronics [reference architectures](https://aws.amazon.com/manufacturing/semiconductor-electronics/resources/#Reference_architectures) that are based on the aforementioned frameworks. These reference architectures are designed to protect data and workloads.

You can use the [AWS Security Maturity Model](https://maturitymodel.security.aws.dev/en/) to guide you through the backlog of security controls in a phased approach.

By utilizing these frameworks, models, and reference architectures, you can establish a robust security posture in the cloud and help protect critical assets.
