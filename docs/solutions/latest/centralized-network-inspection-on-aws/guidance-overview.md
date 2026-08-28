---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/guidance-overview.html
---

# Automate the process of provisioning a centralized AWS Network Firewall to inspect traffic between your Amazon VPCs
<a name="guidance-overview"></a>

 Centralized Network Inspection on AWS configures the Amazon Web Services (AWS) resources needed to filter network traffic. With this guidance, you can inspect hundreds or thousands of [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) environments and accounts in one place. This guidance saves you time by automating the process of provisioning a centralized [AWS Network Firewall](https://aws.amazon.com/network-firewall/) to inspect traffic between VPCs. You can also centrally configure and manage your firewall, firewall policies, and rule groups.

 This guidance uses Network Firewall to provide granular visibility and control of your network traffic. This allows you to accomplish network segmentation, egress domain filtering, and intrusion prevention through event-driven logging. You can use Network Firewall to filter network traffic at the perimeter of your VPCs. Network Firewall automatically scales with network traffic to provide high availability protections without the need to set up or maintain the underlying infrastructure. This guidance also helps you collaborate and manage the changes to the Network Firewall configuration by using a [GitOps workflow](https://about.gitlab.com/topics/gitops/gitops-workflow/).

 This implementation guide provides an overview of the Centralized Network Inspection on AWS guidance, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the guidance to the AWS Cloud.

 The intended audience for using this guidance's features and capabilities in their environment includes solution architects, DevOps engineers, security engineers, and cloud professionals.

 Use this navigation table to quickly find answers to these questions:

|  If you want to . . .  |  Read . . .  |
| --- | --- |
|  Know the cost for running this guidance. <br /> The estimated cost for running this guidance in the US East (N. Virginia) Region is USD $620.55 per month for AWS resources.  |  [Cost](cost.md)  |
|  Understand the security considerations for this guidance.  |  [Security](security.md)  |
|  Know how to plan for quotas for this guidance.  |  [Quotas](quotas.md)  |
|  Know which AWS Regions support this guidance.  |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the guidance. | [GitHub repository](https://github.com/aws-solutions/centralized-network-inspection-on-aws/) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
