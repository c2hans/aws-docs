---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-iam-pv-1.html
---

# [CT.IAM.PV.1] Disallow modification of an AWS IAM role that AWS Control Tower utilizes to manage AWS Backup resources
<a name="ct-iam-pv-1"></a>

This control limits modification of the AWS IAM role (aws-controltower-BackupRole) that AWS Control Tower utilizes for management of AWS Backup resources.

This is a preventive control with elective guidance. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **AWS Identity and Access Management (IAM)

**Control metadata**
+ **Control objective: **Protect configurations
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control group: **
+ **Resource types: **`AWS::IAM::Role`

**Usage considerations**
AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.

 The artifact for this control is the following service control policy (SCP).

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "CTIAMPV1",
        "Effect": "Deny",
        "Action": [
          "iam:AttachRolePolicy",
          "iam:CreateRole",
          "iam:DeleteRole",
          "iam:DeleteRolePermissionsBoundary",
          "iam:DeleteRolePolicy",
          "iam:DetachRolePolicy",
          "iam:PutRolePermissionsBoundary",
          "iam:PutRolePolicy",
          "iam:UpdateAssumeRolePolicy",
          "iam:UpdateRole"
        ],
        "Resource": "arn:*:iam::*:role/aws-controltower-BackupRole",
        "Condition": {
          "ArnNotLike": {
            "aws:PrincipalARN": "arn:*:iam::*:role/AWSControlTowerExecution"
          }
        }
      }
    ]
  }
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
