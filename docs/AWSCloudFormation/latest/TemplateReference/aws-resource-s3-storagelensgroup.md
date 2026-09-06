---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-storagelensgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup
<a name="aws-resource-s3-storagelensgroup"></a>

The `AWS::S3::StorageLensGroup` resource creates an S3 Storage Lens group. A Storage Lens group is a custom grouping of objects that include filters for prefixes, suffixes, object tags, object size, or object age. You can create an S3 Storage Lens group that includes a single filter or multiple filter conditions. To specify multiple filter conditions, you use `AND` or `OR` logical operators. For more information about S3 Storage Lens groups, see [Working with S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-overview.html).

## Syntax
<a name="aws-resource-s3-storagelensgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-storagelensgroup-syntax.json"></a>

```
{
  "Type" : "AWS::S3::StorageLensGroup",
  "Properties" : {
      "[Filter](#cfn-s3-storagelensgroup-filter)" : {{Filter}},
      "[Name](#cfn-s3-storagelensgroup-name)" : {{String}},
      "[Tags](#cfn-s3-storagelensgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3-storagelensgroup-syntax.yaml"></a>

```
Type: AWS::S3::StorageLensGroup
Properties:
  [Filter](#cfn-s3-storagelensgroup-filter): {{
    Filter}}
  [Name](#cfn-s3-storagelensgroup-name): {{String}}
  [Tags](#cfn-s3-storagelensgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3-storagelensgroup-properties"></a>

`Filter`  <a name="cfn-s3-storagelensgroup-filter"></a>
This property contains the criteria for the Storage Lens group data that is displayed
*Required*: Yes
*Type*: [Filter](aws-properties-s3-storagelensgroup-filter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-s3-storagelensgroup-name"></a>
This property contains the Storage Lens group name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3-storagelensgroup-tags"></a>
This property contains the AWS resource tags that you're adding to your Storage Lens group. This parameter is optional.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-storagelensgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3-storagelensgroup-return-values"></a>

### Ref
<a name="aws-resource-s3-storagelensgroup-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the S3 Storage Lens group name. For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3-storagelensgroup-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following are the available attributes and sample return values.

####
<a name="aws-resource-s3-storagelensgroup-return-values-fn--getatt-fn--getatt"></a>

`StorageLensGroupArn`  <a name="StorageLensGroupArn-fn::getatt"></a>
Property description not available.
