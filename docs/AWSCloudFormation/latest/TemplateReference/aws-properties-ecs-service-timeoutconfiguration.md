---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-timeoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service TimeoutConfiguration
<a name="aws-properties-ecs-service-timeoutconfiguration"></a>

An object that represents the timeout configurations for Service Connect.

**Note**
If `idleTimeout` is set to a time that is less than `perRequestTimeout`, the connection will close when the `idleTimeout` is reached and not the `perRequestTimeout`.

## Syntax
<a name="aws-properties-ecs-service-timeoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-timeoutconfiguration-syntax.json"></a>

```
{
  "[IdleTimeoutSeconds](#cfn-ecs-service-timeoutconfiguration-idletimeoutseconds)" : {{Integer}},
  "[PerRequestTimeoutSeconds](#cfn-ecs-service-timeoutconfiguration-perrequesttimeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-timeoutconfiguration-syntax.yaml"></a>

```
  [IdleTimeoutSeconds](#cfn-ecs-service-timeoutconfiguration-idletimeoutseconds): {{Integer}}
  [PerRequestTimeoutSeconds](#cfn-ecs-service-timeoutconfiguration-perrequesttimeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-timeoutconfiguration-properties"></a>

`IdleTimeoutSeconds`  <a name="cfn-ecs-service-timeoutconfiguration-idletimeoutseconds"></a>
The amount of time in seconds a connection will stay active while idle. A value of `0` can be set to disable `idleTimeout`.
The `idleTimeout` default for `HTTP`/`HTTP2`/`GRPC` is 5 minutes.
The `idleTimeout` default for `TCP` is 1 hour.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerRequestTimeoutSeconds`  <a name="cfn-ecs-service-timeoutconfiguration-perrequesttimeoutseconds"></a>
The amount of time waiting for the upstream to respond with a complete response per request. A value of `0` can be set to disable `perRequestTimeout`. `perRequestTimeout` can only be set if Service Connect `appProtocol` isn't `TCP`. Only `idleTimeout` is allowed for `TCP``appProtocol`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-timeoutconfiguration--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
