---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-patchbaseline-patchfiltergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::PatchBaseline PatchFilterGroup
<a name="aws-properties-ssm-patchbaseline-patchfiltergroup"></a>

The `PatchFilterGroup` property type specifies a set of patch filters for an AWS Systems Manager patch baseline, typically used for approval rules for a Systems Manager patch baseline.

`PatchFilterGroup` is the property type for the `GlobalFilters` property of the [AWS::SSM::PatchBaseline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html) resource and the `PatchFilterGroup` property of the [Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html) property type.

## Syntax
<a name="aws-properties-ssm-patchbaseline-patchfiltergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-patchbaseline-patchfiltergroup-syntax.json"></a>

```
{
  "[PatchFilters](#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters)" : {{[ PatchFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-patchbaseline-patchfiltergroup-syntax.yaml"></a>

```
  [PatchFilters](#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters): {{
    - PatchFilter}}
```

## Properties
<a name="aws-properties-ssm-patchbaseline-patchfiltergroup-properties"></a>

`PatchFilters`  <a name="cfn-ssm-patchbaseline-patchfiltergroup-patchfilters"></a>
The set of patch filters that make up the group.
*Required*: No
*Type*: Array of [PatchFilter](aws-properties-ssm-patchbaseline-patchfilter.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
