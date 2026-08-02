---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-hooktimeoutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service HookTimeoutConfig
<a name="aws-properties-ecs-service-hooktimeoutconfig"></a>

<a name="aws-properties-ecs-service-hooktimeoutconfig-description"></a>The `HookTimeoutConfig` property type specifies Property description not available. for an [AWS::ECS::Service](aws-resource-ecs-service.md).

## Syntax
<a name="aws-properties-ecs-service-hooktimeoutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-hooktimeoutconfig-syntax.json"></a>

```
{
  "[Action](#cfn-ecs-service-hooktimeoutconfig-action)" : {{String}},
  "[TimeoutInMinutes](#cfn-ecs-service-hooktimeoutconfig-timeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-hooktimeoutconfig-syntax.yaml"></a>

```
  [Action](#cfn-ecs-service-hooktimeoutconfig-action): {{String}}
  [TimeoutInMinutes](#cfn-ecs-service-hooktimeoutconfig-timeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-hooktimeoutconfig-properties"></a>

`Action`  <a name="cfn-ecs-service-hooktimeoutconfig-action"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ROLLBACK | CONTINUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutInMinutes`  <a name="cfn-ecs-service-hooktimeoutconfig-timeoutinminutes"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `20160`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
