---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-backup-pv-3.html
---

# [CT.BACKUP.PV.3] Disallow modification of an AWS Backup resource that AWS Control Tower manages
<a name="ct-backup-pv-3"></a>

This control limits creation or modification of AWS Backup resources that AWS Control Tower manages.

This is a preventive control with elective guidance. By default, this control is not enabled. Although you can see the control in the console, you can enable it only by activating AWS Backup capabilities for your landing zone.

**AWS service: **AWS Backup

**Control metadata**
+ **Control objective: **Protect configurations
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control group: **
+ **Resource types: **`AWS::Backup::BackupPlan`, `AWS::Backup::BackupVault`

**Usage considerations**
AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.
If you apply a tag with the key `aws-control-tower` to an AWS Backup resource created independently of AWS Control Tower, the resource becomes subject to this SCP.

 The artifact for this control is the following service control policy (SCP).

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "CTBACKUPPV3",
        "Effect": "Deny",
        "Action": [
          "backup:CreateBackupPlan",
          "backup:CreateBackupSelection",
          "backup:CreateBackupVault",
          "backup:CreateLogicallyAirGappedBackupVault",
          "backup:DeleteBackupPlan",
          "backup:DeleteBackupSelection",
          "backup:DeleteBackupVault",
          "backup:DeleteBackupVaultAccessPolicy",
          "backup:DeleteBackupVaultLockConfiguration",
          "backup:DeleteBackupVaultSharingPolicy",
          "backup:PutBackupVaultAccessPolicy",
          "backup:PutBackupVaultLockConfiguration",
          "backup:PutBackupVaultSharingPolicy",
          "backup:UpdateBackupPlan"
        ],
        "Resource": [
          "arn:*:backup:*:*:backup-plan:*",
          "arn:*:backup:*:*:backup-vault:*"
        ],
        "Condition": {
          "ArnNotLike": {
            "aws:PrincipalARN": "arn:*:iam::*:role/AWSControlTowerExecution"
          },
          "Null": {
            "aws:ResourceTag/aws-control-tower": false
          }
        }
      }
    ]
  }
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
