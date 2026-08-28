---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/ct-appsync-pv-1.html
---

# [CT.APPSYNC.PV.1] Require an AWS AppSync GraphQL API to be configured with private visibility
<a name="ct-appsync-pv-1"></a>

This control disallows creation of public AWS AppSync APIs by requiring APIs to be configured with private visibility.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **AWS AppSync

**Control metadata**
+ **Control objective: **Limit network access
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::AppSync::GraphQLApi`

**Usage considerations**
This control requires AppSync GraphQL APIs to be created with a private API configuration to ensure that the API is accessible only from a VPC.
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTAPPSYNCPV1",
            "Effect": "Deny",
            "Action": "appsync:CreateGraphqlApi",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "appsync:Visibility": "PRIVATE"
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
