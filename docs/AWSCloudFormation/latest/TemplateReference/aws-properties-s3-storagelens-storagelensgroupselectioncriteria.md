---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-storagelensgroupselectioncriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens StorageLensGroupSelectionCriteria
<a name="aws-properties-s3-storagelens-storagelensgroupselectioncriteria"></a>

This resource indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation. You can only attach Storage Lens groups to your dashboard if they're included in your Storage Lens group aggregation. If this value is left null, then all Storage Lens groups are selected.

## Syntax
<a name="aws-properties-s3-storagelens-storagelensgroupselectioncriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-storagelensgroupselectioncriteria-syntax.json"></a>

```
{
  "[Exclude](#cfn-s3-storagelens-storagelensgroupselectioncriteria-exclude)" : {{[ String, ... ]}},
  "[Include](#cfn-s3-storagelens-storagelensgroupselectioncriteria-include)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-storagelensgroupselectioncriteria-syntax.yaml"></a>

```
  [Exclude](#cfn-s3-storagelens-storagelensgroupselectioncriteria-exclude): {{
    - String}}
  [Include](#cfn-s3-storagelens-storagelensgroupselectioncriteria-include): {{
    - String}}
```

## Properties
<a name="aws-properties-s3-storagelens-storagelensgroupselectioncriteria-properties"></a>

`Exclude`  <a name="cfn-s3-storagelens-storagelensgroupselectioncriteria-exclude"></a>
This property indicates which Storage Lens group ARNs to exclude from the Storage Lens group aggregation.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Include`  <a name="cfn-s3-storagelens-storagelensgroupselectioncriteria-include"></a>
This property indicates which Storage Lens group ARNs to include in the Storage Lens group aggregation.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
