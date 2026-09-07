---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/organization-account-structure.html
---

# AWS Organizations and the dedicated account structure
<a name="organization-account-structure"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

[AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you centrally manage and govern multiple AWS accounts. Use of AWS Organizations is the basis of a well-architected, multi-account AWS environment. For more information, see [Establishing your best practice AWS environment](https://aws.amazon.com/organizations/getting-started/best-practices/).

The following diagram shows the high-level account and organizational unit (OU) structure of the AWS PRA. For the most part, the organizational structure of the AWS PRA matches the [organizational structure of the AWS SRA](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html).

![The AWS Privacy Reference Architecture (AWS PRA) account structure in AWS Organizations.](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/3419edeb-2b5b-4d49-b531-362393bb7405.png)

The deviations from the AWS SRA organization include:
+ The AWS PRA adds the Personal Data (PD) OU, which is dedicated for collecting, storing, and processing personal data. This structural separation provides flexibility so that you can define specific, fine-grained controls to help protect personal data from unintended disclosure.
+ In the Infrastructure OU, the AWS PRA doesn't currently include additional guidance for the [Shared Services account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/shared-services.html) that is described in the AWS SRA.
+ The AWS PRA doesn't currently include additional guidance for the [Workloads OU](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/application.html) that is described in the AWS SRA. Applications that collect or process personal data are located in dedicated accounts in the PD OU.

You can use [AWS Control Tower](https://aws.amazon.com/controltower/) for overall foundational governance and automated deployment of security and privacy controls across your organization. If AWS Control Tower isn't in use today in your organization, you can still deploy many of the security and privacy controls in AWS Control Tower, such as service control policies and AWS Config rules, in their respective services.

You might find it helpful to consider the processing of personal data when you plan your account and OU structure, including an account segmentation strategy. You might need to consider the types of data you are processing for their unique use cases and applicable laws and regulations. For example, cardholder data is protected under the Payment Card Industry Data Security Standard (PCI DSS), and protected health information might be subject to the Health Insurance Portability and Accountability Act (HIPAA). You might want to review which environments contain personal data and plan your segmentation strategy heavily on that. A typical account segmentation strategy can include dedicated AWS accounts that align to the software development lifecycle (SDLC), such as dedicated accounts for development, staging or quality assurance (QA), and production. A segmentation strategy such as this can be a critical component in the overall design discussion, and your OUs might need to align to your specific regulatory requirements.

Some multi-account AWS environments require dedicated application accounts per AWS Region, or they might require multi-account landing zones. In this case, you require additional segmentation to meet the unique data sovereignty requirements for your customers and regulators. For more information, see [Strategizing for global expansion](global-expansion.md) in this guide.
