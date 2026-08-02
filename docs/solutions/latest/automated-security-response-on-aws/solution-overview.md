---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/solution-overview.html
---

# Automatically address security threats with predefined response and remediation actions in AWS Security Hub
<a name="solution-overview"></a>

This implementation guide provides an overview of the Automated Security Response on AWS solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the Automated Security Response on AWS solution to the Amazon Web Services (AWS) Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution |  [Cost](cost.md)  |
| Understand the security considerations for this solution |  [Security](security.md)  |
| Know how to plan for quotas for this solution |  [Quotas](quotas.md)  |
| Know which AWS Regions are supported for this solution |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution |  [AWS CloudFormation templates](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/automated-security-response-on-aws)  |

The continued evolution of security requires proactive steps to secure data which can make it difficult, expensive, and time-consuming for security teams to react. The Automated Security Response on AWS solution helps you quickly react to address security issues by providing predefined responses and remediation actions based on industry compliance standards and best practices.

Automated Security Response on AWS is an AWS Solution that works with [AWS Security Hub](https://aws.amazon.com/security-hub/) to improve your security and helps align your workloads to the Well-Architected Security pillar best practices ([SEC10](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-10.html)). This solution makes it easier for AWS Security Hub customers to resolve common security findings and improve their security posture in AWS.

You can select specific playbooks to deploy in your Security Hub primary account. Each playbook contains the necessary custom actions, [Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles, [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html), [AWS Systems Manager](https://aws.amazon.com/systems-manager/) automation documents, [AWS Lambda](https://aws.amazon.com/lambda/) functions, and [AWS Step Functions](https://aws.amazon.com/step-functions/) needed to start a remediation workflow within a single AWS account, or across multiple accounts. Remediations work from the Actions menu in AWS Security Hub and allow authorized users to remediate a finding across all of their AWS Security Hub-managed accounts with a single action. For example, you can apply recommendations from the Center for Internet Security (CIS) AWS Foundations Benchmark, a compliance standard for securing AWS resources, to ensure passwords expire within 90 days and enforce encryption of event logs stored in AWS.

**Note**
Remediation is intended for emergent situations that require immediate action. This solution makes changes to remediate findings only when initiated by you via the AWS Security Hub Management console, or when automated remediation has been enabled using the Remediation Configuration DynamoDB table. To revert these changes, you must manually put resources back in their original state.
When remediating AWS resources deployed as a part of the CloudFormation stack, be aware that this might cause a drift. When possible, remediate stack resources by modifying the code that defines the stack resources and updating the stack. For more information, refer to [What is drift?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html#what-is-drift) in the *AWS CloudFormation User Guide*.

Automated Security Response on AWS includes the playbook remediations for the security standards defined as part of the following:
+  [Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v2-standard)
+  [CIS AWS Foundations Benchmark v1.4.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v4-standard)
+  [CIS AWS Foundations Benchmark v3.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis3v0-standard)
+  [AWS Foundational Security Best Practices (FSBP) v.1.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html)
+  [Payment Card Industry Data Security Standard (PCI-DSS) v3.2.1](https://docs.aws.amazon.com/securityhub/latest/userguide/pci-standard.html)
+  [National Institute of Standards and Technology (NIST) SP 800-53 Rev. 5](https://docs.aws.amazon.com/securityhub/latest/userguide/nist-standard.html)

The solution also includes a Security Controls (SC) playbook for the [consolidated control findings feature](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#consolidated-control-findings) of AWS Security Hub. For more information, refer to [Playbooks](playbooks.md). We recommend using the SC playbook along with consolidated control findings in Security Hub.

This implementation guide discusses architectural considerations and configuration steps for deploying the Automated Security Response on AWS solution in the AWS Cloud. It includes links to [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates that launch, configure, and run the AWS compute, network, storage, and other services required to deploy this solution on AWS, using AWS best practices for security and availability.

The guide is intended for IT infrastructure architects, administrators, and DevOps professionals who have practical experience architecting in the AWS Cloud.
