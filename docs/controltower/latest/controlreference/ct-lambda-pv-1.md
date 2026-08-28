---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-lambda-pv-1.html
---

# [CT.LAMBDA.PV.1] Require an AWS Lambda function URL to use AWS IAM-based authentication
<a name="ct-lambda-pv-1"></a>

Require an AWS Lambda function URL to restrict access to authenticated users by using `AWS_IAM` based authentication.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **AWS Lambda

**Control metadata**
+ **Control objective: **Enforce least privilege
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::Lambda::Url`

**Usage considerations**
This control disallows creation and update of AWS Lambda function URL configurations. It does not prevent deletion of Lambda function URL configurations.
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTLAMBDAPV1",
            "Effect": "Deny",
            "Action": [
                "lambda:CreateFunctionUrlConfig",
                "lambda:UpdateFunctionUrlConfig"
            ],
            "Resource": "arn:*:lambda:*:*:function:*",
            "Condition": {
                "StringNotEquals": {
                    "lambda:FunctionUrlAuthType": "AWS_IAM"
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
