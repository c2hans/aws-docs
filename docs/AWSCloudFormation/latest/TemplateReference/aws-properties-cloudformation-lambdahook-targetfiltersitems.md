---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-targetfiltersitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::LambdaHook TargetFiltersItems
<a name="aws-properties-cloudformation-lambdahook-targetfiltersitems"></a>

Specifies the resource types, actions, and invocation points to target for the `TargetFilters` property type.

For more information, see [CloudFormation Hook target filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-target-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-lambdahook-targetfiltersitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-lambdahook-targetfiltersitems-syntax.json"></a>

```
{
  "[Actions](#cfn-cloudformation-lambdahook-targetfiltersitems-actions)" : {{[ String, ... ]}},
  "[InvocationPoints](#cfn-cloudformation-lambdahook-targetfiltersitems-invocationpoints)" : {{[ String, ... ]}},
  "[TargetNames](#cfn-cloudformation-lambdahook-targetfiltersitems-targetnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-lambdahook-targetfiltersitems-syntax.yaml"></a>

```
  [Actions](#cfn-cloudformation-lambdahook-targetfiltersitems-actions): {{
    - String}}
  [InvocationPoints](#cfn-cloudformation-lambdahook-targetfiltersitems-invocationpoints): {{
    - String}}
  [TargetNames](#cfn-cloudformation-lambdahook-targetfiltersitems-targetnames): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-lambdahook-targetfiltersitems-properties"></a>

`Actions`  <a name="cfn-cloudformation-lambdahook-targetfiltersitems-actions"></a>
The actions to target.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationPoints`  <a name="cfn-cloudformation-lambdahook-targetfiltersitems-invocationpoints"></a>
The invocation points to target.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetNames`  <a name="cfn-cloudformation-lambdahook-targetfiltersitems-targetnames"></a>
The resource types to target, such as `AWS::S3::Bucket` or `AWS::DynamoDB::Table`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
