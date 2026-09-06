---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-stackroles.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GuardHook StackRoles
<a name="aws-properties-cloudformation-guardhook-stackroles"></a>

Specifies the stack roles for the `StackFilters` property type to include or exclude specific stacks from Hook invocations based on their associated IAM roles.

For more information, see [CloudFormation Hooks stack level filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-stack-level-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-guardhook-stackroles-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-guardhook-stackroles-syntax.json"></a>

```
{
  "[Exclude](#cfn-cloudformation-guardhook-stackroles-exclude)" : {{[ String, ... ]}},
  "[Include](#cfn-cloudformation-guardhook-stackroles-include)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-guardhook-stackroles-syntax.yaml"></a>

```
  [Exclude](#cfn-cloudformation-guardhook-stackroles-exclude): {{
    - String}}
  [Include](#cfn-cloudformation-guardhook-stackroles-include): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-guardhook-stackroles-properties"></a>

`Exclude`  <a name="cfn-cloudformation-guardhook-stackroles-exclude"></a>
The IAM role ARNs for stacks you want to exclude. The Hook will be invoked on all stacks except those initiated by the specified roles.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Include`  <a name="cfn-cloudformation-guardhook-stackroles-include"></a>
The IAM role ARNs to target stacks associated with these roles. Only stack operations initiated by these roles will invoke the Hook.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
