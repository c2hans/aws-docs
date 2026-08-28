---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/org-management-account.html
---

# Org Management account
<a name="org-management-account"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

The Org Management account is primarily used to manage resource configuration drift for the foundational privacy controls across all of the accounts in your organization, which is managed by AWS Organizations. This account is also where you can deploy new member accounts consistently, with many of the same security and privacy controls. For more information about this account, see the [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html). The following diagram illustrates the AWS security and privacy services that are configured in the Org Management account.

![AWS services deployed in the Org Management account](http://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/604c8fa7-4814-46fe-a1be-7de672f43b4a.png)

This section provides more detailed information about the following AWS services that are used in this account:
+ [AWS Artifact](#aws-artifact)
+ [AWS Control Tower](#aws-control-tower)
+ [AWS Organizations](#aws-organizations)

## AWS Artifact
<a name="aws-artifact"></a>

[AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) can help you with audits by providing on-demand downloads of AWS security and compliance documents. For more information about how this service is used in a security context, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html#mgmt-artifact).

This AWS service helps you understand the controls that you inherit from AWS and determine what controls may be remaining for you to implement in your environment. AWS Artifact provides access to AWS security and compliance reports, such as System and Organization Controls (SOC) reports and payment card industry (PCI) reports. It also provides access to certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS controls. Using AWS Artifact, you can provide the AWS audit artifacts to your auditors or regulators as evidence of AWS security and privacy controls. The following reports might be useful to demonstrate the effectiveness of AWS privacy controls:
+ **SOC 2 Type 2 Privacy report** – This report demonstrates the effectiveness of AWS controls for how personal data is collected, used, retained, disclosed, and disposed of. There is also a [SOC 3 Privacy report](https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf), which is a less detailed description of the SOC 2 privacy controls. For more information, see the [SOC FAQ](https://aws.amazon.com/compliance/soc-faqs/).
+ **Cloud Computing Compliance Controls Catalog (C5)** – This report was created by Germany's national cybersecurity authority, Bundesamt für Sicherheit in der Informationstechnik (BSI). It details the security controls that AWS implemented in order to meet the C5 requirements. It also includes additional control requirements for privacy relating to data location, service provisioning, place of jurisdiction, and information disclosure obligations.
+ **ISO/IEC 27701:2019 certification report** ­–[ISO/IEC 27701:2019](https://aws.amazon.com/compliance/iso-27701-faqs/?refid=sl_card) describes requirements and guidelines to establish and continuously improve a privacy information management system (PIMS). This report details the scope of this certification and can serve as proof of AWS certification. For more information about this standard, see [ISO/IEC 27701:2019](https://www.iso.org/standard/71670.html) (ISO website).

## AWS Control Tower
<a name="aws-control-tower"></a>

[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment that follows prescriptive security recommended practices. For more information about how this service is used in a security context, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html#mgmt-tower).

In AWS Control Tower, you can also automate the deployment of many proactive, preventative, and detective controls, also known as *guardrails*, that align to your data privacy requirements, specifically for data residency and sovereignty. For example, you can specify guardrails that limit the transfer of data to only approved AWS Regions. For even more granular control, you can choose from more than 17 guardrails that are designed to control data residency, such as *Disallow Amazon Virtual Private Network (VPN) connections*, *Disallow internet access for an Amazon VPC instance*, and *Deny access to AWS based on the requested AWS Region*. These guardrails consist of a number of AWS CloudFormation hooks, service control policies, and AWS Config rules that can be uniformly deployed across your organization. For more information, see [Controls that enhance data residency protection](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-controls.html) in the AWS Control Tower documentation.

For data sovereignty, AWS Control Tower currently provides preventative controls, such as *Require that an attached Amazon EBS volume is configured to encrypt data at rest *and *Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services*. Sovereignty controls are broader than just data residency controls. They help prevent actions that might violate data residency, granular access restriction, encryption, and resilience requirements. For more information, see [Preventive controls that assist with digital sovereignty](https://docs.aws.amazon.com/controltower/latest/controlreference/ds-preventive-controls.html) in the AWS Control Tower documentation.

If you need to deploy privacy guardrails beyond data residency and sovereignty controls, AWS Control Tower includes a number of [mandatory controls](https://docs.aws.amazon.com/controltower/latest/userguide/mandatory-controls.html). These controls are deployed by default across every OU when you set up your landing zone. Many of these are preventative controls that are designed to protect logs, such as *Disallow Deletion of Log Archive* and *Enable Integrity Validation for CloudTrail Log File*.

AWS Control Tower is also integrated with AWS Security Hub CSPM to provide detective controls. These controls are known as [Service-Managed Standard: AWS Control Tower](https://docs.aws.amazon.com/securityhub/latest/userguide/service-managed-standard-aws-control-tower.html). You can use these controls to monitor for configuration drift of privacy-supporting controls, such as encryption at rest for Amazon Relational Database Service (Amazon RDS) database instances.

## AWS Organizations
<a name="aws-organizations"></a>

The AWS PRA uses AWS Organizations to centrally manage all accounts within the architecture. For more information, see [AWS Organizations and the dedicated account structure](organization-account-structure.md) in this guide. In AWS Organizations, you can use service control policies (SCPs) and [management policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_management_policies.html) to help protect personal data and privacy.

### Service control policies (SCPs)
<a name="service-control-policies--scps-.b7c0e855-29b6-57db-985c-80fef0c67045"></a>

[Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) are a type of organization policy that you can use to manage permissions in your organization. They provide centralized control over the maximum available permissions for AWS Identity and Access Management (IAM) roles and users in the target account, organization unit (OU), or entire organization. You can create and apply SCPs from the Org Management account.

You can use AWS Control Tower to deploy SCPs uniformly across your accounts. For more information about the data residency controls you can apply through AWS Control Tower, see [AWS Control Tower](#aws-control-tower) in this guide. AWS Control Tower includes a full complement of preventative SCPs. If AWS Control Tower isn't currently used in your organization, you can also deploy these controls manually.

#### Using SCPs to address data residency requirements
<a name="using-scps-to-address-data-residency-requirements.f1b5093c-c74d-5bdb-abfe-df980a4fbad8"></a>

It's common to manage personal data residency requirements by storing and processing data within a specific geographic region. In order to verify that a jurisdiction's unique data residency requirements are met, we recommend that you work closely with your regulatory team to confirm your requirements. When these requirements have been determined, there are a number of AWS foundational privacy controls that can help support. For example, you can use SCPs to limit which AWS Regions can be used to process and store data. For a sample policy, see [Restrict data transfers across AWS Regions](restrict-data-transfers-across-regions.md) in this guide.

#### Using SCPs to restrict high-risk API calls
<a name="using-scps-to-restrict-high-risk-api-calls.40d02bcc-9a0c-576b-a8d4-e27a54781811"></a>

It is important to understand which security and privacy controls AWS is responsible for and which ones you are responsible for. For example, you are responsible for the results of API calls that could be made against the AWS services that you use. You are also responsible for understanding which of those calls could result in changes to your security or privacy posture. If you are concerned about maintaining a certain security and privacy posture, you can enable SCPs that deny certain API calls. These API calls may have implications, such as unintended disclosure of personal data or violations of specific cross-border data transfer. For example, you might want to prohibit the following API calls:
+ Enabling public access to Amazon Simple Storage Service (Amazon S3) buckets
+ Disabling Amazon GuardDuty or creating suppression rules for data exfiltration findings, such as the [Trojan:EC2/DNSDataExfiltration](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dnsdataexfiltration) finding
+ Deleting AWS WAF data exfiltration rules
+ Sharing Amazon Elastic Block Store (Amazon EBS) snapshots publicly
+ Removing a member account from the organization
+ Disassociating Amazon CodeGuru Reviewer from a repository

### Management policies
<a name="management-policies.689f51be-72b2-59b5-854a-e9d985b0d6f4"></a>

[Management policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_management_policies.html) in AWS Organizations can help you centrally configure and manage AWS services and their features. The types of management policy you choose determine how policies affect the OUs and accounts that inherit them. [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) are an example of a management policy in AWS Organizations that directly relates to privacy.

#### Using tag policies
<a name="using-tag-policies.bdba6ed2-b6c0-5a14-9717-6982b495fb6f"></a>

[Tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) are key value pairs that help you manage, identify, organize, search for, and filter AWS resources. It can be useful to apply tags that distinguish the resources in your organization that handle personal data. The use of tags supports many of the privacy solutions in this guide. For example, you might want to apply a tag that indicates the general data classification of the data being processed or stored within the resource. You can write attribute-based access control (ABAC) policies that limit access to resources that have a particular tag or set of tags. For example, your policy might specify that the `SysAdmin` role can't access resources that have the `dataclassification:4` tag. For more information and a tutorial, see [Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the IAM documentation. In addition, if your organization uses [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) to apply data retention policies broadly across your backups in many accounts, you can apply a tag that puts that resource within scope for that backup policy.

[Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) help you maintain consistent tags throughout your organization. In a tag policy, you specify rules that apply to resources when they are tagged. For example, you can require resources to be tagged with specific keys, such as `DataClassification` or `DataSteward`, and you can specify valid case treatments or values for keys. You can also use [enforcement](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-enforcement.html) to prevent noncompliant tagging requests from completing.

When using tags as a core component of your privacy control strategy, consider the following:
+ Consider the implications of placing personal data or other types of sensitive data within tag keys or values. When you contact AWS for technical assistance, AWS might analyze tags and other resource identifiers to help resolve the issue. Tag data is not encrypted, and AWS services, such as AWS Billing and Cost Management, can read them. Therefore, you might want to deidentify tag values and then reidentify them by using a system that you control, such as an IT service management (ITSM) system. AWS recommends not including personally identifiable information in tags.
+ Consider that some tag values need to be made immutable (unmodifiable) to prevent circumvention of technical controls, such as ABAC conditions that rely on tags.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
