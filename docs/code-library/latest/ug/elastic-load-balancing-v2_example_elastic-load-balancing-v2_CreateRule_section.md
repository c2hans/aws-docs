---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateRule_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateRule` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateRule_section"></a>

The following code examples show how to use `CreateRule`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To create a rule using a path condition and a forward action**
The following `create-rule` example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern.

```
aws elbv2 create-rule \
    --listener-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2}} \
    --priority {{5}} \
    --conditions {{file://conditions-pattern.json}} \
    --actions {{Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067}}
```
Contents of `conditions-pattern.json`:

```
[
    {
        "Field": "path-pattern",
        "PathPatternConfig": {
            "Values": ["/images/*"]
        }
    }
]
```
Output:

```
{
    "Rules": [
        {
            "RuleArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3",
            "Priority": "5",
            "Conditions": [
                {
                    "Field": "path-pattern",
                    "Values": [
                        "/images/*"
                    ],
                    "PathPatternConfig": {
                        "Values": [
                            "/images/*"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
                    "ForwardConfig": {
                        "TargetGroups": [
                            {
                                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
                                "Weight": 1
                            }
                        ],
                        "TargetGroupStickinessConfig": {
                            "Enabled": false
                        }
                    }
                }
            ],
            "IsDefault": false
        }
    ]
}
```
For more information, see [Add a listener rule for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/add-rule.html) in the *Application Load Balancers Guide*.
**Example 2: To create a rule using a host condition and a fixed response**
The following `create-rule` example creates a rule that provides a fixed response if the hostname in the host header matches the specified hostname.

```
aws elbv2 create-rule \
    --listener-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2}} \
    --priority {{10}} \
    --conditions {{file://conditions-host.json}} \
    --actions {{file://actions-fixed-response.json}}
```
Contents of `conditions-host.json`:

```
[
    {
        "Field": "host-header",
        "HostHeaderConfig": {
            "Values": ["*.example.com"]
        }
    }
]
```
Contents of `actions-fixed-response.json`:

```
[
    {
        "Type": "fixed-response",
        "FixedResponseConfig": {
            "MessageBody": "Hello world",
            "StatusCode": "200",
            "ContentType": "text/plain"
        }
    }
]
```
Output:

```
{
    "Rules": [
        {
            "RuleArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/a7e3b2c1d4f56789",
            "Priority": "10",
            "Conditions": [
                {
                    "Field": "host-header",
                    "Values": [
                        "*.example.com"
                    ],
                    "HostHeaderConfig": {
                        "Values": [
                            "*.example.com"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "fixed-response",
                    "FixedResponseConfig": {
                        "MessageBody": "Hello world",
                        "StatusCode": "200",
                        "ContentType": "text/plain"
                    }
                }
            ],
            "IsDefault": false
        }
    ]
}
```
For more information, see [Add a listener rule for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/add-rule.html) in the *Application Load Balancers Guide*.
**Example 3: To create a rule using a source IP address condition, an authenticate action, and a forward action**
The following `create-rule` example creates a rule that authenticates the user if the source IP address matches the specified IP address, and forwards the request to the specified target group if authentication is successful.

```
aws elbv2 create-rule \
    --listener-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2}} \
    --priority {{20}} \
    --conditions {{file://conditions-source-ip.json}} \
    --actions {{file://actions-authenticate.json}}
```
Contents of `conditions-source-ip.json`:

```
[
    {
        "Field": "source-ip",
        "SourceIpConfig": {
            "Values": ["192.0.2.0/24", "198.51.100.10/32"]
        }
    }
]
```
Contents of `actions-authenticate.json`:

```
[
    {
        "Type": "authenticate-oidc",
        "AuthenticateOidcConfig": {
            "Issuer": "https://idp-issuer.com",
            "AuthorizationEndpoint": "https://authorization-endpoint.com",
            "TokenEndpoint": "https://token-endpoint.com",
            "UserInfoEndpoint": "https://user-info-endpoint.com",
            "ClientId": "abcdefghijklmnopqrstuvwxyz123456789",
            "ClientSecret": "123456789012345678901234567890",
            "SessionCookieName": "my-cookie",
            "SessionTimeout": 3600,
            "Scope": "email",
            "AuthenticationRequestExtraParams": {
                "display": "page",
                "prompt": "login"
            },
            "OnUnauthenticatedRequest": "deny"
        },
        "Order": 1
    },
    {
        "Type": "forward",
        "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
        "Order": 2
    }
]
```
Output:

```
{
    "Rules": [
        {
            "RuleArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/b8f4c3d2e5a67890",
            "Priority": "20",
            "Conditions": [
                {
                    "Field": "source-ip",
                    "SourceIpConfig": {
                        "Values": [
                            "192.0.2.0/24",
                            "198.51.100.10/32"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "authenticate-oidc",
                    "AuthenticateOidcConfig": {
                        "Issuer": "https://idp-issuer.com",
                        "AuthorizationEndpoint": "https://authorization-endpoint.com",
                        "TokenEndpoint": "https://token-endpoint.com",
                        "UserInfoEndpoint": "https://user-info-endpoint.com",
                        "ClientId": "abcdefghijklmnopqrstuvwxyz123456789",
                        "SessionCookieName": "my-cookie",
                        "Scope": "email",
                        "SessionTimeout": 3600,
                        "AuthenticationRequestExtraParams": {
                            "display": "page",
                            "prompt": "login"
                        },
                        "OnUnauthenticatedRequest": "deny"
                    },
                    "Order": 1
                },
                {
                    "Type": "forward",
                    "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
                    "Order": 2,
                    "ForwardConfig": {
                        "TargetGroups": [
                            {
                                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
                                "Weight": 1
                            }
                        ],
                        "TargetGroupStickinessConfig": {
                            "Enabled": false
                        }
                    }
                }
            ],
            "IsDefault": false
        }
    ]
}
```
For more information, see [Add a listener rule for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/add-rule.html) in the *Application Load Balancers Guide*.
+  For API details, see [CreateRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-rule.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates new Listener rule with fixed-response action based on the customer header value for the specified Listener.**

```
$newRuleAction = [Amazon.ElasticLoadBalancingV2.Model.Action]@{
  "FixedResponseConfig" = @{
    "ContentType" = "text/plain"
    "MessageBody" = "Hello World"
    "StatusCode" = "200"
  }
  "Type" = [Amazon.ElasticLoadBalancingV2.ActionTypeEnum]::FixedResponse
}

$newRuleCondition = [Amazon.ElasticLoadBalancingV2.Model.RuleCondition]@{
  "httpHeaderConfig" = @{
    "HttpHeaderName" = "customHeader"
    "Values" = "header2","header1"
  }
  "Field" = "http-header"
}

New-ELB2Rule -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/testALB/3e2f03b558e19676/1c84f02aec143e80' -Action $newRuleAction -Condition $newRuleCondition -Priority 10
```
**Output:**

```
Actions    : {Amazon.ElasticLoadBalancingV2.Model.Action}
Conditions : {Amazon.ElasticLoadBalancingV2.Model.RuleCondition}
IsDefault  : False
Priority   : 10
RuleArn    : arn:aws:elasticloadbalancing:us-east-1:123456789012:listener-rule/app/testALB/3e2f03b558e19676/1c84f02aec143e80/f4f51dfaa033a8cc
```
+  For API details, see [CreateRule](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates new Listener rule with fixed-response action based on the customer header value for the specified Listener.**

```
$newRuleAction = [Amazon.ElasticLoadBalancingV2.Model.Action]@{
  "FixedResponseConfig" = @{
    "ContentType" = "text/plain"
    "MessageBody" = "Hello World"
    "StatusCode" = "200"
  }
  "Type" = [Amazon.ElasticLoadBalancingV2.ActionTypeEnum]::FixedResponse
}

$newRuleCondition = [Amazon.ElasticLoadBalancingV2.Model.RuleCondition]@{
  "httpHeaderConfig" = @{
    "HttpHeaderName" = "customHeader"
    "Values" = "header2","header1"
  }
  "Field" = "http-header"
}

New-ELB2Rule -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/testALB/3e2f03b558e19676/1c84f02aec143e80' -Action $newRuleAction -Condition $newRuleCondition -Priority 10
```
**Output:**

```
Actions    : {Amazon.ElasticLoadBalancingV2.Model.Action}
Conditions : {Amazon.ElasticLoadBalancingV2.Model.RuleCondition}
IsDefault  : False
Priority   : 10
RuleArn    : arn:aws:elasticloadbalancing:us-east-1:123456789012:listener-rule/app/testALB/3e2f03b558e19676/1c84f02aec143e80/f4f51dfaa033a8cc
```
+  For API details, see [CreateRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
