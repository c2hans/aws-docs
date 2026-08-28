---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-targetfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GuardHook TargetFilters
<a name="aws-properties-cloudformation-guardhook-targetfilters"></a>

The `TargetFilters` property type specifies the target filters for the Hook.

For more information, see [CloudFormation Hook target filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-target-filtering.html).

## Syntax
<a name="aws-properties-cloudformation-guardhook-targetfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-guardhook-targetfilters-syntax.json"></a>

```
{
  "[TargetFiltersItems](#cfn-cloudformation-guardhook-targetfilters-targetfiltersitems)" : {{TargetFiltersItems}}
}
```

### YAML
<a name="aws-properties-cloudformation-guardhook-targetfilters-syntax.yaml"></a>

```
  [TargetFiltersItems](#cfn-cloudformation-guardhook-targetfilters-targetfiltersitems): {{
    TargetFiltersItems}}
```

## Properties
<a name="aws-properties-cloudformation-guardhook-targetfilters-properties"></a>

`TargetFiltersItems`  <a name="cfn-cloudformation-guardhook-targetfilters-targetfiltersitems"></a>
The specific resource types, actions, and invocation points to target.
*Required*: No
*Type*: [TargetFiltersItems](aws-properties-cloudformation-guardhook-targetfiltersitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
