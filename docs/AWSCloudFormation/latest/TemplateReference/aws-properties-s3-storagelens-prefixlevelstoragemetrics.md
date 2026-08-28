---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens PrefixLevelStorageMetrics
<a name="aws-properties-s3-storagelens-prefixlevelstoragemetrics"></a>

This resource contains the details of the prefix-level storage metrics for Amazon S3 Storage Lens.

## Syntax
<a name="aws-properties-s3-storagelens-prefixlevelstoragemetrics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-prefixlevelstoragemetrics-syntax.json"></a>

```
{
  "[IsEnabled](#cfn-s3-storagelens-prefixlevelstoragemetrics-isenabled)" : {{Boolean}},
  "[SelectionCriteria](#cfn-s3-storagelens-prefixlevelstoragemetrics-selectioncriteria)" : {{SelectionCriteria}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-prefixlevelstoragemetrics-syntax.yaml"></a>

```
  [IsEnabled](#cfn-s3-storagelens-prefixlevelstoragemetrics-isenabled): {{Boolean}}
  [SelectionCriteria](#cfn-s3-storagelens-prefixlevelstoragemetrics-selectioncriteria): {{
    SelectionCriteria}}
```

## Properties
<a name="aws-properties-s3-storagelens-prefixlevelstoragemetrics-properties"></a>

`IsEnabled`  <a name="cfn-s3-storagelens-prefixlevelstoragemetrics-isenabled"></a>
This property identifies whether the details of the prefix-level storage metrics for S3 Storage Lens are enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionCriteria`  <a name="cfn-s3-storagelens-prefixlevelstoragemetrics-selectioncriteria"></a>
This property identifies whether the details of the prefix-level storage metrics for S3 Storage Lens are enabled.
*Required*: No
*Type*: [SelectionCriteria](aws-properties-s3-storagelens-selectioncriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
