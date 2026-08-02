---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html
---

# Deploy a cloud foundation to support highly-regulated workloads and complex compliance requirements
<a name="solution-overview"></a>

The Landing Zone Accelerator on AWS (LZA) is architected to align with AWS best practices and in conformance with multiple, global compliance frameworks. We recommend customers deploy [AWS Control Tower](https://aws.amazon.com/controltower/) as the foundational landing zone and enhance their landing zone capabilities with Landing Zone Accelerator. These complementary capabilities provide a comprehensive no-code solution across 35\+ AWS services to manage and govern a multi-account environment built to support customers with highly-regulated workloads and complex compliance requirements. AWS Control Tower and Landing Zone Accelerator help you establish platform readiness with security, compliance, and operational capabilities.

We provide this solution as an open-source project that we built using the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK). You can install it directly into your environment, giving you full access to the infrastructure as code (IaC) solution. Through a simplified set of configuration files, you can:
+ Configure additional functionality, controls, and security services such as [AWS Config](https://aws.amazon.com/config/) Managed Rules and [AWS Security Hub](https://aws.amazon.com/security-hub/).
+ Manage your foundational networking topology such as [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/), and [AWS Network Firewall](https://aws.amazon.com/network-firewall/).
+ Generate additional workload accounts using the AWS Control Tower Account Factory.

There are no additional charges or upfront commitments required to use Landing Zone Accelerator on AWS. You pay only for AWS services turned on to set up your platform and operate your controls. This solution can also support non-standard AWS partitions, including the AWS GovCloud (US), AWS Secret, and AWS Top Secret Regions.

This implementation guide describes architectural considerations and configuration steps for deploying the Landing Zone Accelerator on AWS. It includes links to an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template synthesized from AWS CDK that launches and configures the AWS services required to deploy this solution using AWS best practices for security and availability.

Use this navigation table to quickly find answers to these questions:

| If you want to…​ | Read…​ |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution using AWS [sample configuration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config) with AWS Control Tower in the US East (N. Virginia) Region within a non-critical sandbox environment with no activity or workloads is approximately **$430.22 (USD) per month**. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions are supported for this solution. |  [Supported AWS Regions](plan-your-deployment.md#regional-deployments)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Deploy this solution in a configuration that supports a specific Region or industry. |  [Landing Zone Accelerator on AWS solution page](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/)  |
| Know how to troubleshoot common deployment errors. |  [Troubleshooting](troubleshooting.md)  |
| Use AWS Support to help you deploy, use, or troubleshoot the solution. |  [AWS Support](contact-aws-support.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/awslabs/landing-zone-accelerator-on-aws)  |

This guide is intended for solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who want to implement the Landing Zone Accelerator on AWS solution in their environment.

**Important**
This solution will not, by itself, make you compliant. It provides the foundational infrastructure from which additional complementary solutions can be integrated. The information contained in this solution implementation guide is not exhaustive. You must review, evaluate, assess, and approve the solution in compliance with your organization’s particular security features, tools, and configurations. It is the sole responsibility of you and your organization to determine which regulatory requirements are applicable and to ensure that you comply with all requirements. Although this solution discusses both the technical and administrative requirements, this solution does not help you comply with the non-technical administrative requirements.
