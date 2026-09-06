---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-storagelenstabledestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens StorageLensTableDestination
<a name="aws-properties-s3-storagelens-storagelenstabledestination"></a>

This resource configures your S3 Storage Lens reports to export to read-only S3 table buckets. With this resource, you can store your Storage Lens metrics in S3 Tables that are created in a read-only S3 table bucket called aws-s3.

## Syntax
<a name="aws-properties-s3-storagelens-storagelenstabledestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-storagelenstabledestination-syntax.json"></a>

```
{
  "[Encryption](#cfn-s3-storagelens-storagelenstabledestination-encryption)" : {{Encryption}},
  "[IsEnabled](#cfn-s3-storagelens-storagelenstabledestination-isenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-storagelenstabledestination-syntax.yaml"></a>

```
  [Encryption](#cfn-s3-storagelens-storagelenstabledestination-encryption): {{
    Encryption}}
  [IsEnabled](#cfn-s3-storagelens-storagelenstabledestination-isenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-s3-storagelens-storagelenstabledestination-properties"></a>

`Encryption`  <a name="cfn-s3-storagelens-storagelenstabledestination-encryption"></a>
This resource configures your data encryption settings for Storage Lens metrics in read-only S3 table buckets.
*Required*: No
*Type*: [Encryption](aws-properties-s3-storagelens-encryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsEnabled`  <a name="cfn-s3-storagelens-storagelenstabledestination-isenabled"></a>
This property indicates whether the export to read-only S3 table buckets is enabled for your S3 Storage Lens configuration. When set to true, Storage Lens reports are automatically exported to tables in addition to other configured destinations.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
