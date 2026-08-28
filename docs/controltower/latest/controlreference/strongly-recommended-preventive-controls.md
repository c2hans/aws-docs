---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-preventive-controls.html
---

# Strongly recommended controls with preventive behavior
<a name="strongly-recommended-preventive-controls"></a>

The following strongly recommended controls have preventive behavior.

**Topics**
+ [[AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS] Disallow creation of access keys for the root user](#disallow-root-access-keys)
+ [[AWS-GR\_RESTRICT\_ROOT\_USER] Disallow actions as a root user](#disallow-root-auser-actions)

## [AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS] Disallow creation of access keys for the root user
<a name="disallow-root-access-keys"></a>

Secure your AWS accounts by disallowing creation of access keys for the root user, which will allow unrestricted access to all resources in the account. We recommend that you instead create access keys for an AWS Identity and Access Management (IAM) user for everyday interaction with your AWS account.

This is a preventive control with strongly-recommended guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **AWS Identity and Access Management (IAM)

**Control metadata**
+ **Control objective: **Enforce least privilege
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::::Account`, `AWS::IAM::AccessKey`

**Usage considerations**
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTROOTUSERACCESSKEYS",
            "Effect": "Deny",
            "Action": "iam:CreateAccessKey",
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:*:iam::*:root"
                    ]
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}
```

## [AWS-GR\_RESTRICT\_ROOT\_USER] Disallow actions as a root user
<a name="disallow-root-auser-actions"></a>

Secure your AWS accounts by disallowing account access with root user credentials, which are credentials of the account owner and allow unrestricted access to all resources in the account. We recommend that you instead create AWS Identity and Access Management (IAM) users for everyday interaction with your AWS account.

This is a preventive control with strongly-recommended guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **AWS Identity and Access Management (IAM)

**Control metadata**
+ **Control objective: **Enforce least privilege
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::::Account`

**Usage considerations**
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**, **ExemptAssumeRoot**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTROOTUSER",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:*:iam::*:root"
                    ]
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}{% if ExemptAssumeRoot %},
                "Null": {
                    "aws:AssumedRoot": "true"
                }{% endif %}
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
