---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens StorageLensExpandedPrefixesDataExport
<a name="aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport"></a>

This resource specifies the properties of your S3 Storage Lens Expanded Prefixes metrics export.

## Syntax
<a name="aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport-syntax.json"></a>

```
{
  "[S3BucketDestination](#cfn-s3-storagelens-storagelensexpandedprefixesdataexport-s3bucketdestination)" : {{S3BucketDestination}},
  "[StorageLensTableDestination](#cfn-s3-storagelens-storagelensexpandedprefixesdataexport-storagelenstabledestination)" : {{StorageLensTableDestination}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport-syntax.yaml"></a>

```
  [S3BucketDestination](#cfn-s3-storagelens-storagelensexpandedprefixesdataexport-s3bucketdestination): {{
    S3BucketDestination}}
  [StorageLensTableDestination](#cfn-s3-storagelens-storagelensexpandedprefixesdataexport-storagelenstabledestination): {{
    StorageLensTableDestination}}
```

## Properties
<a name="aws-properties-s3-storagelens-storagelensexpandedprefixesdataexport-properties"></a>

`S3BucketDestination`  <a name="cfn-s3-storagelens-storagelensexpandedprefixesdataexport-s3bucketdestination"></a>
This property specifies the general purpose bucket where the S3 Storage Lens Expanded Prefixes metrics export files are located. At least one export destination must be specified.
*Required*: No
*Type*: [S3BucketDestination](aws-properties-s3-storagelens-s3bucketdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageLensTableDestination`  <a name="cfn-s3-storagelens-storagelensexpandedprefixesdataexport-storagelenstabledestination"></a>
This property configures S3 Storage Lens Expanded Prefixes metrics report to read-only S3 table buckets.
*Required*: No
*Type*: [StorageLensTableDestination](aws-properties-s3-storagelens-storagelenstabledestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
