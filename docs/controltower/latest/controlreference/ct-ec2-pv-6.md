---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-6.html
---

# [CT.EC2.PV.6] Disallow the use of deprecated Amazon EC2 RequestSpotFleet and RequestSpotInstances API actions
<a name="ct-ec2-pv-6"></a>

This control disallows usage of EC2 `RequestSpotFleet` and `RequestSpotInstances` APIs, because they are legacy APIs with no planned investment.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon EC2

**Control metadata**
+ **Control objective: **Enforce least privilege, Protect configurations
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::EC2::SpotFleet`

**Usage considerations**
This control denies `ec2:RequestSpotFleet` and `ec2:RequestSpotInstances` actions for all IAM principals. If you need to use these actions, do not enable this control.
This control does not prevent cancelling or modifying an existing spot fleet or spot instance request.

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV6",
            "Effect": "Deny",
            "Action": [
                "ec2:RequestSpotFleet",
                "ec2:RequestSpotInstances"
            ],
            "Resource": "*"{% if ExemptedPrincipalArns %},
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }
            }{% endif %}
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
