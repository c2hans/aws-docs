---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-elb-protection.html
---

# `AWSConfigRemediation-EnableELBDeletionProtection`
<a name="automation-aws-enable-elb-protection"></a>

 **Description**

 The `AWSConfigRemediation-EnableELBDeletionProtection` runbook enables deletion protection for the elastic load balancer (ELB) you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableELBDeletionProtection)

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
+ LoadBalancerArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the ELB that you want to enable deletion protection on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `elasticloadbalancing:DescribeLoadBalancerAttributes`
+  `elasticloadbalancing:DescribeLoadBalancers`
+  `elasticloadbalancing:ModifyLoadBalancerAttributes`

 **Document Steps**
+  `aws:executeScript` - Enables deletion protection on the ELB you specify in the `LoadBalancerArn` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
