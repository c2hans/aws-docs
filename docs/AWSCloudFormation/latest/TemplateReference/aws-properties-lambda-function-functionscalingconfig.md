---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-functionscalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function FunctionScalingConfig
<a name="aws-properties-lambda-function-functionscalingconfig"></a>

Configuration that defines the scaling behavior for a Lambda Managed Instances function, including the minimum and maximum number of execution environments that can be provisioned.

## Syntax
<a name="aws-properties-lambda-function-functionscalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-functionscalingconfig-syntax.json"></a>

```
{
  "[MaxExecutionEnvironments](#cfn-lambda-function-functionscalingconfig-maxexecutionenvironments)" : {{Integer}},
  "[MinExecutionEnvironments](#cfn-lambda-function-functionscalingconfig-minexecutionenvironments)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-function-functionscalingconfig-syntax.yaml"></a>

```
  [MaxExecutionEnvironments](#cfn-lambda-function-functionscalingconfig-maxexecutionenvironments): {{Integer}}
  [MinExecutionEnvironments](#cfn-lambda-function-functionscalingconfig-minexecutionenvironments): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-function-functionscalingconfig-properties"></a>

`MaxExecutionEnvironments`  <a name="cfn-lambda-function-functionscalingconfig-maxexecutionenvironments"></a>
The maximum number of execution environments that can be provisioned for the function.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinExecutionEnvironments`  <a name="cfn-lambda-function-functionscalingconfig-minexecutionenvironments"></a>
The minimum number of execution environments to maintain for the function.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
