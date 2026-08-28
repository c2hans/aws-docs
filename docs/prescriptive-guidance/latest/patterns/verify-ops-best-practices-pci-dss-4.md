---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/verify-ops-best-practices-pci-dss-4.html
---

# Verify operational best practices for PCI DSS 4.0 by using AWS Config
<a name="verify-ops-best-practices-pci-dss-4"></a>

*Tala Qraitem and Alex Goff, Amazon Web Services*

## Summary
<a name="verify-ops-best-practices-pci-dss-4-summary"></a>

The [Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/standards/pci-dss/) outlines essential technical and operational protocols to help safeguard payment data. PCI DSS was developed to encourage and enhance data security for payment card accounts. It also facilitates the global adoption of consistent security measures. Although it’s specifically designed for environments with payment card account data, you can use PCI DSS to help protect against threats and secure other elements in the payment ecosystem.

PCI DSS version 4.0 was released to address evolving requirements, provide clarification or additional guidance, and improve the structure and format of the standard. For more information about the changes, see [Summary of changes from PCI DSS version 3.2.1 to 4.0](https://listings.pcisecuritystandards.org/documents/PCI-DSS-Summary-of-Changes-v3_2_1-to-v4_0.pdf).

An AWS Config [conformance pack](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) is a collection of AWS Config rules and remediation actions that help you create security, operational, or cost-optimization governance checks. You can deploy a conformance pack as a single entity in an AWS account and AWS Region, or you can deploy across an organization in AWS Organizations.

The conformance packs for PCI DSS version 4.0 augment and build upon the conformance pack for version 3.2.1. The rules in the conformance pack map to the rules in the standard. For more information, see the mapping provided in the *Attachments* section. You can choose between two versions of this conformance pack: one that includes [global resource types](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all) and one that excludes them.

**Important**
Conformance packs are not designed to fully ensure compliance with a specific governance or compliance standard. You are responsible for making your own assessment of whether usage meets applicable legal and regulatory requirements.

## Prerequisites and limitations
<a name="verify-ops-best-practices-pci-dss-4-prereqs"></a>

**Prerequisites**
+ Have an active AWS account.
+ [Set up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html).
+ Meet the [prerequisites for conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/cpack-prerequisites.html).
+ Deploy the [PCI DSS version 3.2.1 conformance pack](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-PCI-DSS.yaml).
+ Have permissions to  access AWS Config and manage conformance packs. For an example policy, see the [Additional information](#verify-ops-best-practices-pci-dss-4-additional) section of this pattern.

**Limitations**
+ Your AWS account has default quotas, formerly referred to as *limits*, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, but not all quotas can be increased. Make sure that you are familiar with the [AWS Config service limits](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html), including the limits for single account conformance packs and organization conformance packs.
+ The version of this conformance pack that includes global resource types is intended for deployment only in the `us-east-1` Region.
+ The version of this conformance pack that excludes global resources types is intended for deployment only in the following Regions:
  + `ap-east-1`
  + `ap-south-1`
  + `ap-northeast-2`
  + `ap-southeast-1`
  + `ap-southeast-2`
  + `ap-northeast-1`
  + `ca-central-1`
  + `eu-central-1`
  + `eu-west-1`
  + `eu-west-2`
  + `eu-west-3`
  + `eu-north-1`
  + `sa-east-1`
  + `us-east-2`
  + `us-west-1`
  + `us-west-2`

## Tools
<a name="verify-ops-best-practices-pci-dss-4-tools"></a>

**AWS services**
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

**Code repository**

The conformance packs are located in the [AWS Config conformance packs](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs) GitHub repository. This repository contains the following templates related to PCI DSS version 4.0:
+ [Operational-Best-Practices-for-PCI-DSS-v4.0-including-global-resourcetypes.yaml](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-PCI-DSS-v4.0-including-global-resourcetypes.yaml)
+ [Operational-Best-Practices-for-PCI-DSS-v4.0-excluding-global-resourcetypes.yaml](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-PCI-DSS-v4.0-excluding-global-resourcetypes.yaml)

## Epics
<a name="verify-ops-best-practices-pci-dss-4-epics"></a>

### Deploy and manage the conformance pack
<a name="deploy-and-manage-the-conformance-pack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the conformance pack. | If you're deploying the conformance pack in the `us-east-1` Region, download the [Operational-Best-Practices-for-PCI-DSS-v4.0-including-global-resourcetypes.yaml](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-PCI-DSS-v4.0-including-global-resourcetypes.yaml) template.<br />If you're deploying the conformance pack in a different Region, download the [Operational-Best-Practices-for-PCI-DSS-v4.0-excluding-global-resourcetypes.yaml](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-PCI-DSS-v4.0-excluding-global-resourcetypes.yaml) template. | DevOps engineer |
| (Optional) Modify the conformance pack. | You can modify the conformance pack template for the unique needs of your organization. For example, you can create custom remediation actions. For more information about how to create and modify templates, see [Creating templates for custom conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/custom-conformance-pack.html) in the AWS Config documentation. | General AWS |
| Deploy the conformance pack. | If you're deploying in a target AWS account or AWS Region, follow the instructions in [Deploying conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-deploy.html) in the AWS Config documentation. You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI).<br />If you're deploying the conformance pack across an organization in AWS Organizations, follow the instructions in [Deploy AWS Config conformance pack using Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-cpack.html) in the AWS Systems Manager documentation. | General AWS |
| (Optional) Edit the conformance pack. | If you want to edit the conformance pack, follow the instructions in [Editing conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-edit.html) in the AWS Config documentation. You can use the AWS Management Console or the AWS CLI. | General AWS |
| (Optional) Delete the conformance pack. | If you want to delete the conformance pack, follow the instructions in [Deleting conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-delete.html) in the AWS Config documentation. You can use the AWS Management Console or the AWS CLI. | General AWS |

## Related resources
<a name="verify-ops-best-practices-pci-dss-4-resources"></a>

**AWS resources**
+ [Conformance packs for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) (AWS Config documentation)
+ [Deploy AWS Config conformance pack using Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-cpack.html) (Systems Manager documentation)
+ [PCI DSS compliance on AWS](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) (AWS website)
+ [PCI DSS version 4.0 on AWS](https://d1.awsstatic.com/whitepapers/compliance/pci-dss-compliance-on-aws-v4-102023.pdf) (Compliance guide)

**PCI DSS resources**
+ [PCI DSS version 4.0 Resource Hub](https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub)
+ [PCI Security Standards Council Document Library](https://www.pcisecuritystandards.org/document_library/)
+ [Summary of changes from PCI DSS version 3.2.1 to 4.0](https://listings.pcisecuritystandards.org/documents/PCI-DSS-Summary-of-Changes-v3_2_1-to-v4_0.pdf)

## Additional information
<a name="verify-ops-best-practices-pci-dss-4-additional"></a>

The following is a sample AWS Identity and Access Management (IAM) policy that allows the user to access AWS Config and manage conformance packs:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "config:PutConfigRule",
                "config:PutConformancePack",
                "config:DeleteConfigRule",
                "config:DeleteRemediationConfiguration",
                "config:DeleteConformancePack",
                "config:PutRemediationConfigurations",
                "config:BatchGetAggregateResourceConfig",
                "config:BatchGetResourceConfig",
                "config:Get*",
                "config:Describe*",
                "config:Deliver*",
                "config:List*",
                "config:Select*"
            ],
            "Resource": "*"
        }
    ]
}
```

## Attachments
<a name="attachments-7f4b4311-2606-44e9-b9a2-8c2472643008"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/7f4b4311-2606-44e9-b9a2-8c2472643008/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
