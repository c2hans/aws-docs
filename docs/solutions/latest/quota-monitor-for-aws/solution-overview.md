---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/solution-overview.html
---

# Monitor resource usage and send notifications when approaching quotas
<a name="solution-overview"></a>

Publication date: *September 2016*. Visit the [CHANGELOG.md](https://github.com/aws-solutions/automations-for-aws-firewall-manager/blob/main/CHANGELOG.md) in our GitHub repository to track version-specific improvements and fixes.

The Quota Monitor for AWS solution proactively monitors resource utilization to avoid unexpectedly reaching [quota limits](https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/). It sends notifications when your Amazon Web Services (AWS) service quotas (previously known as limits) are approaching their maximum value. This solution uses [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates to automate the deployment by provisioning the infrastructure resources (also known as the *stack*) automatically.

The solution leverages [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/) and [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) to monitor resource utilization against quotas for specific AWS services. The solution can send you notifications via email or your existing Slack channel, requesting to increase quotas or to shut down resources before the quota is reached. For more information, refer to [Quotas](quotas.md) later in this document.

This implementation guide provides an overview of the Quota Monitor for AWS solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the AWS Cloud. It is intended for solution architects, DevOps engineers, AWS account administrators, and cloud professionals who want to implement Quota Monitor for AWS in their environment.

You can use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions this solution supports. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation templates included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation templates](aws-cloudformation-templates.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/quota-monitor-for-aws/)  |
