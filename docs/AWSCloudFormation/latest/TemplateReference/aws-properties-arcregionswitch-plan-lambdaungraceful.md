---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-lambdaungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan LambdaUngraceful
<a name="aws-properties-arcregionswitch-plan-lambdaungraceful"></a>

Configuration for handling failures when invoking Lambda functions.

## Syntax
<a name="aws-properties-arcregionswitch-plan-lambdaungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-lambdaungraceful-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-lambdaungraceful-behavior)" : {{}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-lambdaungraceful-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-lambdaungraceful-behavior): {{
    }}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-lambdaungraceful-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-lambdaungraceful-behavior"></a>
The ungraceful behavior for a Lambda function, which must be set to `skip`.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
