---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/trace-the-execution.html
---

# Trace the execution of the remediation
<a name="trace-the-execution"></a>

To understand better how the solution works, you can trace the execution of the remediation.

## EventBridge rule
<a name="eventbridge-rule"></a>

In the admin account, locate an EventBridge rule named **Remediate\_with\_ASR\_CustomAction**. This rule matches the finding you sent from Security Hub and sends it to the Orchestrator Step Functions.

## Step Functions execution
<a name="step-function-execution"></a>

In the admin account, locate the AWS Step Functions named "**SO0111-ASR-Orchestrator**". This step function calls the SSM Automation document in the target account and Region. You can trace the execution of the remediation in the execution history of this AWS Step Functions.

## SSM Automation
<a name="ssm-automation"></a>

In the member account, navigate to the SSM Automation console. You will find two executions of a document named "ASR-SC\_2.0.0\_Lambda.1" and one execution of a document named "ASR-RemoveLambdaPublicAccess".

The first execution is from the orchestrator step function in the target account. The second execution occurs in the target Region, which may not be the Region from which the finding originated. The final execution is the remediation that revokes the public access policy from the Lambda Function.

## CloudWatch Log Group
<a name="cloudwatch-log-group"></a>

In the admin account, navigate to the CloudWatch Logs console and locate a Log Group named "**SO0111-ASR**". This log group is the destination for high-level logs from the Orchestrator Step Functions.
