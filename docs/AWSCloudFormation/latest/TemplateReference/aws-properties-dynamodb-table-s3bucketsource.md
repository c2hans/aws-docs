---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-s3bucketsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table S3BucketSource
<a name="aws-properties-dynamodb-table-s3bucketsource"></a>

 The S3 bucket that is being imported from.

## Syntax
<a name="aws-properties-dynamodb-table-s3bucketsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-s3bucketsource-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-dynamodb-table-s3bucketsource-s3bucket)" : {{String}},
  "[S3BucketOwner](#cfn-dynamodb-table-s3bucketsource-s3bucketowner)" : {{String}},
  "[S3KeyPrefix](#cfn-dynamodb-table-s3bucketsource-s3keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-s3bucketsource-syntax.yaml"></a>

```
  [S3Bucket](#cfn-dynamodb-table-s3bucketsource-s3bucket): {{String}}
  [S3BucketOwner](#cfn-dynamodb-table-s3bucketsource-s3bucketowner): {{String}}
  [S3KeyPrefix](#cfn-dynamodb-table-s3bucketsource-s3keyprefix): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-table-s3bucketsource-properties"></a>

`S3Bucket`  <a name="cfn-dynamodb-table-s3bucketsource-s3bucket"></a>
 The S3 bucket that is being imported from.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3BucketOwner`  <a name="cfn-dynamodb-table-s3bucketsource-s3bucketowner"></a>
 The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional.
*Required*: No
*Type*: String
*Pattern*: `[0-9]{12}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3KeyPrefix`  <a name="cfn-dynamodb-table-s3bucketsource-s3keyprefix"></a>
 The key prefix shared by all S3 Objects that are being imported.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
