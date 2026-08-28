---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-storagelensgrouplevel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens StorageLensGroupLevel
<a name="aws-properties-s3-storagelens-storagelensgrouplevel"></a>

This resource determines the scope of Storage Lens group data that is displayed in the Storage Lens dashboard.

## Syntax
<a name="aws-properties-s3-storagelens-storagelensgrouplevel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-storagelensgrouplevel-syntax.json"></a>

```
{
  "[StorageLensGroupSelectionCriteria](#cfn-s3-storagelens-storagelensgrouplevel-storagelensgroupselectioncriteria)" : {{StorageLensGroupSelectionCriteria}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-storagelensgrouplevel-syntax.yaml"></a>

```
  [StorageLensGroupSelectionCriteria](#cfn-s3-storagelens-storagelensgrouplevel-storagelensgroupselectioncriteria): {{
    StorageLensGroupSelectionCriteria}}
```

## Properties
<a name="aws-properties-s3-storagelens-storagelensgrouplevel-properties"></a>

`StorageLensGroupSelectionCriteria`  <a name="cfn-s3-storagelens-storagelensgrouplevel-storagelensgroupselectioncriteria"></a>
This property indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation. If this value is left null, then all Storage Lens groups are selected.
*Required*: No
*Type*: [StorageLensGroupSelectionCriteria](aws-properties-s3-storagelens-storagelensgroupselectioncriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
