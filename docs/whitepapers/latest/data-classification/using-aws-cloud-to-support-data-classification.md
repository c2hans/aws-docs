---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using AWS Cloud to support data classification
<a name="using-aws-cloud-to-support-data-classification"></a>

 Cloud computing can offer customers the ability to secure their workloads. Organizations in highly regulated industries, public sector, enterprises, small and medium sized businesses, or startups, can work to meet their data classification policies and requirements in the cloud. Cloud service providers (CSPs), such as AWS, provide a standardized, utility-based service that is self-provisioned by customers. AWS does not have visibility into the type of data customers run in the cloud, which means AWS does not distinguish, for example, personal data from other customer data when providing cloud services. It is the customer’s responsibility to classify their data and implement appropriate controls within their cloud environment (for example, encryption). However, the security controls CSPs implement within their infrastructure and their service offerings can be used by customers to help meet the most sensitive data requirements.

## AWS Cloud security and compliance
<a name="aws-cloud-security-and-compliance"></a>

 AWS services offer the same high level of security to all customers, regardless of the type of content being stored. These services are then queued for certification against international security and compliance “gold” standards, which translates to customers benefiting from elevated levels of protection for customer data processed and stored in the cloud.

 The risk events and threat vectors of greatest concern are largely accounted for through foundational cyber hygiene disciplines (such as patching and configuring systems), which CSPs can demonstrate through widely adopted, internationally-recognized security certifications and assurance programs such as ISO 27001, Payment Card Industry Data Security Standard (PCI DSS), and Service Organization Controls (SOC).

 ISO 27001/27002 is a widely-adopted global security standard that sets out requirements and best practices for a systematic approach to managing company and customer information that’s based on periodic risk assessments appropriate to ever-changing threat scenarios.

 The Payment Card Industry Data Security Standard (also known as PCI DSS) is a proprietary information security standard administered by the [PCI Security Standards Council](https://www.pcisecuritystandards.org/), which was founded by American Express, Discover Financial Services, JCB International, MasterCard Worldwide and Visa Inc. PCI DSS applies to entities that store, process or transmit card data.

 Service Organization Controls reports (SOC 1, 2, 3) are intended to meet a broad range of financial auditing requirements for U.S. and international auditing bodies. The audit for this report is conducted in accordance with the International Standards for Assurance Engagements No. 3402 (ISAE 3402) and the American Institute of Certified Public Accountants (AICPA): AT 801 (formerly SSAE 16).

 Security and compliance reports such as SOC 1, PCI, FedRAMP are available to customers through [AWS Artifact](https://aws.amazon.com/artifact/getting-started/), a self-service portal for on-demand access to AWS’ security and compliance reports. You can use those documents to validate the implementation and operating effectiveness of AWS security controls. Those documents can also be used as guidelines to evaluate and assess the effectiveness of your company's internal controls. AWS customers are responsible for developing or obtaining documents that demonstrate the security and compliance of their workloads in the AWS Cloud. For more information, refer to the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

 In evaluating CSPs, organizations should leverage these existing CSP certifications so that they can appropriately determine whether a CSP (and services within the CSP’s offerings) can support their data classification requirements. AWS encourages organizations to implement a policy identifying which existing national, international, or sector-specific cloud certifications and attestations are acceptable for each level in the data classification scheme to streamline accreditation and accelerate migrating workloads to the cloud.

## AWS Well-Architected Framework and data protection best practices
<a name="aws-well-architected-framework-and-data-protection-best-practices"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected) helps you understand trade-offs for decisions you make while building workloads on AWS. The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) provides guidance to help you apply best practices and current recommendations in the design, delivery, and maintenance of secure AWS workloads.

 Two of the design principles given focus on data protection include:
+  **Protect data in transit and at rest** — Classify your data into sensitivity levels and use mechanisms, such as encryption, tokenization, and access control where appropriate.
+  **Keep people away from data** — Use mechanisms and tools to reduce or eliminate the need for direct access or manual processing of data. This reduces the risk of mishandling or modification and human error when handling sensitive data.

 In regard to data classification, the framework provides these additional recommendations:
+  **Identify the data within your workload** — Understand the type and classification of data your workload is processing, the associated business processes, data owner, applicable legal and compliance requirements, where it’s stored, and the resulting controls that are needed to be enforced.
+  **Define data protection controls** — Using resource tags, separate AWS accounts per sensitivity (and potentially also per caveat / enclave / community of interest), Identity and Access Management (IAM) policies, Organizations Service Control Policies (SCPs), [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS), and [AWS CloudHSM](https://aws.amazon.com/cloudhsm/), organizations can define and implement policies for data classification and protection.
+  **Define data lifecycle management** — Have a defined lifecycle strategy based on sensitivity level and legal and organizational requirements., Consider the duration for which your organization has to retain data, data destruction processes, data access management, data transformation, and data sharing.
+  **Automate identification and classification** — Automating the identification and classification of data, as opposed to directing access from an individual or team, reduces the risk of human error / exposure and helps implement the correct controls.

 For more in-depth guidance, refer to [Data Classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html).

## AWS services and features
<a name="aws-services-and-features"></a>

 AWS offers several services and features that can facilitate an organization’s implementation of a data classification scheme. For example, [Amazon Macie](https://aws.amazon.com/macie/) can help customers inventory and classify sensitive and business-critical data stored in AWS. Amazon Macie uses ML to automate the process of discovering, classifying, labeling, and applying protection rules to data. This helps customers better understand where sensitive information is stored and how it’s being accessed, including user authentications and access patterns.

 Another important feature supporting data classification and protection is [AWS resource tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). By assigning metadata to your AWS resources in the form of tags (with each tag being a label consisting of a user-defined key and value), you can manage, identify, organize, search for, and filter resources. Security tags can contain information on confidentiality, identifying specific data confidential level a resource supports, or compliance, like an identifier for workloads that must adhere to specific compliance requirements.

 Other AWS services and features that can support data classification include, but are not limited to:
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM) for managing user credentials, setting permissions, and authorizing access.
+  [AWS Organizations](https://aws.amazon.com/organizations/) helps you centrally govern your environment with automated account creation, account grouping to reflect your business needs, and policies to enforce governance. Policies can include required actions such as tagging of resources.
+  [AWS Glue](https://aws.amazon.com/glue/) to store data and discover associated metadata like table definition and schema, in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html). Once cataloged, your data is immediately searchable and available for ETL.
+  [Amazon Neptune](https://aws.amazon.com/neptune/), fully managed graph database, can give you insights into the relationships between different data sets. This can include identification and traceability of sensitive data through metadata analysis.
+  [AWS KMS](https://aws.amazon.com/kms/) or [AWS CloudHSM](https://aws.amazon.com/cloudhsm) for encryption; key management with AWS-generated keys, or bring your own key (BYOK) with Federal Information Processing Standards (FIPS) 140-2 validation.
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail) for extensive logging to track who, what, and when data was created, accessed, copied/ moved, modified, and deleted.
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to view and manage service operations such as patching, along with [AWS Inspector](https://aws.amazon.com/inspector/) to conduct vulnerability scans.
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) for intelligent threat detection, supporting nearly continuous monitoring requirements.
+  [AWS Config](https://aws.amazon.com/config/) to manage configuration changes and implement governance rules.
+  [AWS Web Application Firewall](https://aws.amazon.com/waf) (AWS WAF) and [AWS Shield](https://aws.amazon.com/) to help protect web applications from common attack vectors (such as SQL injection, cross-site scripting, and DDoS).

 For the entire list of AWS security services, refer to [Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security/).
