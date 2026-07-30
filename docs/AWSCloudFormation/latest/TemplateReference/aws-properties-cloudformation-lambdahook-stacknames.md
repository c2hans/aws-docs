---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-stacknames.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::LambdaHook StackNames
<a name="aws-properties-cloudformation-lambdahook-stacknames"></a>

Specifies the stack names for the `StackFilters` property type to include or exclude specific stacks from Hook invocations.

For more information, see [CloudFormation Hooks stack level filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-stack-level-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-lambdahook-stacknames-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-lambdahook-stacknames-syntax.json"></a>

```
{
  "[Exclude](#cfn-cloudformation-lambdahook-stacknames-exclude)" : {{[ String, ... ]}},
  "[Include](#cfn-cloudformation-lambdahook-stacknames-include)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-lambdahook-stacknames-syntax.yaml"></a>

```
  [Exclude](#cfn-cloudformation-lambdahook-stacknames-exclude): {{
    - String}}
  [Include](#cfn-cloudformation-lambdahook-stacknames-include): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-lambdahook-stacknames-properties"></a>

`Exclude`  <a name="cfn-cloudformation-lambdahook-stacknames-exclude"></a>
The stack names to exclude. All stacks except those listed here will invoke the Hook.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Include`  <a name="cfn-cloudformation-lambdahook-stacknames-include"></a>
The stack names to include. Only the stacks specified in this list will invoke the Hook.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
