---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-copysnapshot.html
---

# `AWS-CopySnapshot`
<a name="automation-aws-copysnapshot"></a>

 **Description**

Copies a point-in-time snapshot of an Amazon Elastic Block Store (Amazon EBS) volume. You can copy the snapshot within the same AWS Region or from one Region to another. Copies of encrypted Amazon EBS snapshots remain encrypted. Copies of unencrypted snapshots remain unencrypted. To copy an encrypted snapshot that was shared from another account, you must have permissions for the KMS key used to encrypt the snapshot. Snapshots created by copying another snapshot have an arbitrary volume ID that should not be used for any purpose.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CopySnapshot)

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
+ Description

  Type: String

  Description: (Optional) A description for the Amazon EBS snapshot.
+ SnapshotId

  Type: String

  Description: (Required) The ID of the Amazon EBS snapshot to copy.
+ SourceRegion

  Type: String

  Description: (Required) The Region where the source snapshot currently exists.

 **Document Steps**

copySnapshot - Copies a snapshot of an Amazon EBS volume.

 **Outputs**

copySnapshot.SnapshotId - The ID of the new snapshot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
