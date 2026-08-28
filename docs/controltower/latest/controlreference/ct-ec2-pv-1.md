---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-1.html
---

# [CT.EC2.PV.1] Require an Amazon EBS snapshot to be created from an encrypted EC2 volume
<a name="ct-ec2-pv-1"></a>

This control disallows creation of new snapshots that are based on unencrypted EBS volumes.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon EC2

**Control metadata**
+ **Control objective: **Encrypt data at rest
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::::Account`

**Usage considerations**
This control does not prevent creation of unencrypted EBS snapshots that are created by means of the `CopySnapshot` operation. AWS Control Tower recommends that you enable EBS encryption by default, so that encryption is applied to copies of unencrypted snapshots. See [Encryption scenarios](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-examples) in the *Amazon EC2 User Guide for Linux Instances* for more information.
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV1",
            "Effect": "Deny",
            "Action": [
                "ec2:CreateSnapshot",
                "ec2:CreateSnapshots"
            ],
            "Resource": "arn:*:ec2:*:*:volume/*",
            "Condition": {
                "Bool": {
                    "ec2:Encrypted": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
