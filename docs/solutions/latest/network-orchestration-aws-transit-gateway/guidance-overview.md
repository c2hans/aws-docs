---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/guidance-overview.html
---

# Automate setting up and managing your transit networks with AWS Transit Gateway
<a name="guidance-overview"></a>

The Network Orchestration for AWS Transit Gateway solution automates the process of setting up and managing transit networks in multi-account AWS environments. The solution creates a web user interface (UI) to help you control, audit, and approve or reject transit network changes. This solution supports both [AWS Organizations](https://aws.amazon.com/organizations/) and standalone AWS accounts, and you can use the solution to visualize your transit network across multiple AWS Regions. You can use this solution with the default deployment template or customize it to meet your specific use case.

You can use [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) to attach [Amazon Virtual Private Clouds](https://aws.amazon.com/vpc/) (Amazon VPCs) in the same AWS Region, and to route traffic between them. With this solution, you can connect your VPCs across multiple accounts by tagging the VPCs. It also connects your transit gateway across multiple AWS Regions by tagging the transit gateway. You can set rules to automatically approve or reject, or manually approve, the network changes.

This implementation guide provides an overview of the Network Orchestration for AWS Transit Gateway solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud.

The intended audience for implementing this solution in their environment includes solution architects, networking professionals, business decision makers and cloud professionals. To deploy and use this solution, you should have an understanding of Amazon VPC, route tables, subnets, transit gateways, and network protocols. For additional training about these topics, see [AWS Networking Basics](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12439/aws-networking-basics), [Understanding AWS Networking Gateways](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/1377/understanding-aws-networking-gateways), and [Advanced Architecting on AWS](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/3214/advanced-architecting-on-aws-amazon).

Use this navigation table to quickly find answers to these questions:

| If you want to …​ | Read …​ |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution in the US East (N. Virginia) Region is USD $85.22 per month. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know the supported AWS Regions for this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-templates.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/network-orchestration-for-aws-transit-gateway)  |
