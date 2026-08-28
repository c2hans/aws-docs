---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-logging-alb-clb.html
---

# `AWSConfigRemediation-EnableLoggingForALBAndCLB`
<a name="automation-aws-enable-logging-alb-clb"></a>

 **Description**

 The `AWSConfigRemediation-EnableLoggingForALBAndCLB` runbook enables logging for the specified AWS Application Load Balancer or a Classic Load Balancer (CLB).

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableLoggingForALBAndCLB)

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
+ LoadBalancerId

  Type: String

  Description: (Required) The Classic Load Balancer name or the Application Load Balancer ARN.
+ S3BucketName

  Type: String

  Description: (Required) The Amazon S3 bucket name.
+ S3BucketPrefix

  Type: String

   Description: (Optional) The logical hierarchy you created for your Amazon Simple Storage Service (Amazon S3) bucket, for example `my-bucket-prefix/prod` . If the prefix is not provided, the log is placed at the root level of the bucket.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `elasticloadbalancing:DescribeLoadBalancerAttributes`
+  `elasticloadbalancing:ModifyLoadBalancerAttributes`

 **Document Steps**
+  `aws:executeScript` - Enables and verifies the logging for the Classic Load Balancer or the Application Load Balancer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
