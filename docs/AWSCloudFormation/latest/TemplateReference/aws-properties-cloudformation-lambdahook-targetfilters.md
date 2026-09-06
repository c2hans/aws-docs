---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-targetfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::LambdaHook TargetFilters
<a name="aws-properties-cloudformation-lambdahook-targetfilters"></a>

The `TargetFilters` property type specifies the target filters for the Hook.

For more information, see [CloudFormation Hook target filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-target-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-lambdahook-targetfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-lambdahook-targetfilters-syntax.json"></a>

```
{
  "[TargetFiltersItems](#cfn-cloudformation-lambdahook-targetfilters-targetfiltersitems)" : {{TargetFiltersItems}}
}
```

### YAML
<a name="aws-properties-cloudformation-lambdahook-targetfilters-syntax.yaml"></a>

```
  [TargetFiltersItems](#cfn-cloudformation-lambdahook-targetfilters-targetfiltersitems): {{
    TargetFiltersItems}}
```

## Properties
<a name="aws-properties-cloudformation-lambdahook-targetfilters-properties"></a>

`TargetFiltersItems`  <a name="cfn-cloudformation-lambdahook-targetfilters-targetfiltersitems"></a>
The specific resource types, actions, and invocation points to target.
*Required*: No
*Type*: [TargetFiltersItems](aws-properties-cloudformation-lambdahook-targetfiltersitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
