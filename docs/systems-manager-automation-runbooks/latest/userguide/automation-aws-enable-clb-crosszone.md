---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-clb-crosszone.html
---

# `AWSConfigRemediation-EnableCLBCrossZoneLoadBalancing`
<a name="automation-aws-enable-clb-crosszone"></a>

 **Description**

 The `AWSConfigRemediation-EnableCLBCrossZoneLoadBalancing` runbook enables cross-zone load balancing for the Classic Load Balancer (CLB) you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCLBCrossZoneLoadBalancing)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ LoadBalancerName

  Type: String

  Description: (Required) The name of the CLB that you want to enable cross-zone load balancing on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `elb:DescribeLoadBalancerAttributes`
+  `elb:ModifyLoadBalancerAttributes`

 **Document Steps**
+  `aws:executeAwsApi` - Enables cross-zone load balancing for the CLB you specify in the `LoadBalancerName` parameter.
+  `aws:assertAwsResourceProperty` - Verifies cross-zone load balancing has been enabled on the CLB.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
