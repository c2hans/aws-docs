---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyTargetGroupAttributes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyTargetGroupAttributes` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyTargetGroupAttributes_section"></a>

The following code examples show how to use `ModifyTargetGroupAttributes`.

------
#### [ CLI ]

**AWS CLI**
**To modify the deregistration delay timeout**
This example sets the deregistration delay timeout to the specified value for the specified target group.
Command:

```
aws elbv2 modify-target-group-attributes --target-group-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067}} --attributes {{Key=deregistration_delay.timeout_seconds,Value=600}}
```
Output:

```
{
  "Attributes": [
      {
          "Value": "false",
          "Key": "stickiness.enabled"
      },
      {
          "Value": "600",
          "Key": "deregistration_delay.timeout_seconds"
      },
      {
          "Value": "lb_cookie",
          "Key": "stickiness.type"
      },
      {
          "Value": "86400",
          "Key": "stickiness.lb_cookie.duration_seconds"
      }
  ]
}
```
+  For API details, see [ModifyTargetGroupAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group-attributes.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example modifies the deregistration\_delay attribute of the specified Target Group.**

```
Edit-ELB2TargetGroupAttribute -TargetGroupArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/test-tg/a4e04b3688be1970' -Attribute @{Key = 'deregistration_delay.timeout_seconds'; Value = 600}
```
**Output:**

```
Key                                   Value
---                                   -----
stickiness.enabled                    false
deregistration_delay.timeout_seconds  600
stickiness.type                       lb_cookie
stickiness.lb_cookie.duration_seconds 86400
slow_start.duration_seconds           0
load_balancing.algorithm.type         round_robin
```
+  For API details, see [ModifyTargetGroupAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example modifies the deregistration\_delay attribute of the specified Target Group.**

```
Edit-ELB2TargetGroupAttribute -TargetGroupArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/test-tg/a4e04b3688be1970' -Attribute @{Key = 'deregistration_delay.timeout_seconds'; Value = 600}
```
**Output:**

```
Key                                   Value
---                                   -----
stickiness.enabled                    false
deregistration_delay.timeout_seconds  600
stickiness.type                       lb_cookie
stickiness.lb_cookie.duration_seconds 86400
slow_start.duration_seconds           0
load_balancing.algorithm.type         round_robin
```
+  For API details, see [ModifyTargetGroupAttributes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
