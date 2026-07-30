---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-stackfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::LambdaHook StackFilters
<a name="aws-properties-cloudformation-lambdahook-stackfilters"></a>

The `StackFilters` property type specifies stack level filters for a Hook.

The `StackNames` or `StackRoles` properties are optional. However, you must specify at least one of these properties.

For more information, see [CloudFormation Hooks stack level filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-stack-level-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-lambdahook-stackfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-lambdahook-stackfilters-syntax.json"></a>

```
{
  "[FilteringCriteria](#cfn-cloudformation-lambdahook-stackfilters-filteringcriteria)" : {{String}},
  "[StackNames](#cfn-cloudformation-lambdahook-stackfilters-stacknames)" : {{StackNames}},
  "[StackRoles](#cfn-cloudformation-lambdahook-stackfilters-stackroles)" : {{StackRoles}}
}
```

### YAML
<a name="aws-properties-cloudformation-lambdahook-stackfilters-syntax.yaml"></a>

```
  [FilteringCriteria](#cfn-cloudformation-lambdahook-stackfilters-filteringcriteria): {{String}}
  [StackNames](#cfn-cloudformation-lambdahook-stackfilters-stacknames): {{
    StackNames}}
  [StackRoles](#cfn-cloudformation-lambdahook-stackfilters-stackroles): {{
    StackRoles}}
```

## Properties
<a name="aws-properties-cloudformation-lambdahook-stackfilters-properties"></a>

`FilteringCriteria`  <a name="cfn-cloudformation-lambdahook-stackfilters-filteringcriteria"></a>
The filtering criteria.
+ All stack names and stack roles (`All`): The Hook will only be invoked when all specified filters match.
+ Any stack names and stack roles (`Any`): The Hook will be invoked if at least one of the specified filters match.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackNames`  <a name="cfn-cloudformation-lambdahook-stackfilters-stacknames"></a>
Includes or excludes specific stacks from Hook invocations.
*Required*: No
*Type*: [StackNames](aws-properties-cloudformation-lambdahook-stacknames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackRoles`  <a name="cfn-cloudformation-lambdahook-stackfilters-stackroles"></a>
Includes or excludes specific stacks from Hook invocations based on their associated IAM roles.
*Required*: No
*Type*: [StackRoles](aws-properties-cloudformation-lambdahook-stackroles.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
