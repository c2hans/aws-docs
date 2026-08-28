---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3tables-tablebucketpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucketPolicy
<a name="aws-resource-s3tables-tablebucketpolicy"></a>

Creates a new maintenance configuration or replaces an existing table bucket policy for a table bucket. For more information, see [Adding a table bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:PutTableBucketPolicy` permission to use this operation.

 AWS Cloud Development Kit (AWS CDK)
To use S3 Tables AWS CDK constructs, add the `@aws-cdk/aws-s3tables-alpha` dependency with one of the following options:
+ NPM: `npm i @aws-cdk/aws-s3tables-alpha`
+ Yarn:`yarn add @aws-cdk/aws-s3tables-alpha`

## Syntax
<a name="aws-resource-s3tables-tablebucketpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3tables-tablebucketpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3Tables::TableBucketPolicy",
  "Properties" : {
      "[ResourcePolicy](#cfn-s3tables-tablebucketpolicy-resourcepolicy)" : {{Json}},
      "[TableBucketARN](#cfn-s3tables-tablebucketpolicy-tablebucketarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3tables-tablebucketpolicy-syntax.yaml"></a>

```
Type: AWS::S3Tables::TableBucketPolicy
Properties:
  [ResourcePolicy](#cfn-s3tables-tablebucketpolicy-resourcepolicy): {{Json}}
  [TableBucketARN](#cfn-s3tables-tablebucketpolicy-tablebucketarn): {{String}}
```

## Properties
<a name="aws-resource-s3tables-tablebucketpolicy-properties"></a>

`ResourcePolicy`  <a name="cfn-s3tables-tablebucketpolicy-resourcepolicy"></a>
The bucket policy JSON for the table bucket.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableBucketARN`  <a name="cfn-s3tables-tablebucketpolicy-tablebucketarn"></a>
The Amazon Resource Name (ARN) of the table bucket.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3tables-tablebucketpolicy-return-values"></a>

### Ref
<a name="aws-resource-s3tables-tablebucketpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns some information about your table bucket policy.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
