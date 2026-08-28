---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enablekinesisstreamencryption.html
---

# `AWS-EnableKinesisStreamEncryption`
<a name="aws-enablekinesisstreamencryption"></a>

 **Description**

 The `AWS-EnableKinesisStreamEncryption` runbook enables encryption on an Amazon Kinesis Data Streams (Kinesis Data Streams). Producer applications writing to an encrypted stream will encounter errors if they do not have access to the AWS Key Management Service (AWS KMS) key.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableKinesisStreamEncryption)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ KinesisStreamName

  Type: String

  Description: (Required) The name of the stream you want to enable encryption on.
+ KeyId

  Type: String

  Default: alias/aws/kinesis

  Description: (Required) The customer-managed AWS KMS key you want to use for encryption. This value can be a globally unique identifier, an ARN to either an alias or a key, or an alias name prefixed by "alias/". You can also use the AWS managed key by using the default value for the parameter.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:GetAutomationExecution`
+ `ssm:StartAutomationExecution`
+ `kinesis:DescribeStream`
+ `kinesis:StartStreamEncryption`
+ `kms:DescribeKey`

 **Document Steps**
+ VerifyKinesisStreamStatus (`aws:waitforAwsResourceProperty`) - Checks the status of the Kinesis Data Streams.
+ EnableKinesisStreamEncryption (`aws:executeAwsApi`) - Enables encryption for the Kinesis Data Streams.
+ VerifyKinesisStreamUpdateComplete (`aws:waitForAwsResourceProperty`) - Waits for the Kinesis Data Streams status to return to `ACTIVE`.
+ VerifyKinesisStreamEncryption (`aws:assertAwsResourceProperty`) - Verifies encryption is enabled for the Kinesis Data Streams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
