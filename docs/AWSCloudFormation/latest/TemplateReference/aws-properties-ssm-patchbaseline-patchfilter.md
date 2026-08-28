---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-patchbaseline-patchfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::PatchBaseline PatchFilter
<a name="aws-properties-ssm-patchbaseline-patchfilter"></a>

The `PatchFilter` property type defines a patch filter for an AWS Systems Manager patch baseline.

The `PatchFilters` property of the [PatchFilterGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html) property type contains a list of `PatchFilter` property types.

You can view lists of valid values for the patch properties by running the `DescribePatchProperties` command. For more information, see [DescribePatchProperties](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html) in the *AWS Systems Manager API Reference*.

## Syntax
<a name="aws-properties-ssm-patchbaseline-patchfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-patchbaseline-patchfilter-syntax.json"></a>

```
{
  "[Key](#cfn-ssm-patchbaseline-patchfilter-key)" : {{String}},
  "[Values](#cfn-ssm-patchbaseline-patchfilter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-patchbaseline-patchfilter-syntax.yaml"></a>

```
  [Key](#cfn-ssm-patchbaseline-patchfilter-key): {{String}}
  [Values](#cfn-ssm-patchbaseline-patchfilter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ssm-patchbaseline-patchfilter-properties"></a>

`Key`  <a name="cfn-ssm-patchbaseline-patchfilter-key"></a>
The key for the filter.
For information about valid keys, see [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) in the *AWS Systems Manager API Reference*.
*Required*: No
*Type*: String
*Allowed values*: `ADVISORY_ID | ARCH | BUGZILLA_ID | CLASSIFICATION | CVE_ID | EPOCH | MSRC_SEVERITY | NAME | PATCH_ID | PATCH_SET | PRIORITY | PRODUCT | PRODUCT_FAMILY | RELEASE | REPOSITORY | SECTION | SECURITY | SEVERITY | VERSION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ssm-patchbaseline-patchfilter-values"></a>
The value for the filter key.
For information about valid values for each key based on operating system type, see [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) in the *AWS Systems Manager API Reference*.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `64 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
