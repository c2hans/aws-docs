---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket UnreferencedFileRemoval
<a name="aws-properties-s3tables-tablebucket-unreferencedfileremoval"></a>

The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the [https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html).

## Syntax
<a name="aws-properties-s3tables-tablebucket-unreferencedfileremoval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-unreferencedfileremoval-syntax.json"></a>

```
{
  "[NoncurrentDays](#cfn-s3tables-tablebucket-unreferencedfileremoval-noncurrentdays)" : {{Integer}},
  "[Status](#cfn-s3tables-tablebucket-unreferencedfileremoval-status)" : {{String}},
  "[UnreferencedDays](#cfn-s3tables-tablebucket-unreferencedfileremoval-unreferenceddays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-unreferencedfileremoval-syntax.yaml"></a>

```
  [NoncurrentDays](#cfn-s3tables-tablebucket-unreferencedfileremoval-noncurrentdays): {{Integer}}
  [Status](#cfn-s3tables-tablebucket-unreferencedfileremoval-status): {{String}}
  [UnreferencedDays](#cfn-s3tables-tablebucket-unreferencedfileremoval-unreferenceddays): {{Integer}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-unreferencedfileremoval-properties"></a>

`NoncurrentDays`  <a name="cfn-s3tables-tablebucket-unreferencedfileremoval-noncurrentdays"></a>
The number of days an object can be noncurrent before Amazon S3 deletes it.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-s3tables-tablebucket-unreferencedfileremoval-status"></a>
The status of the unreferenced file removal configuration for your table bucket.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnreferencedDays`  <a name="cfn-s3tables-tablebucket-unreferencedfileremoval-unreferenceddays"></a>
The number of days an object must be unreferenced by your table before Amazon S3 marks the object as noncurrent.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
