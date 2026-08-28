---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-accesscontroltranslation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket AccessControlTranslation
<a name="aws-properties-s3-bucket-accesscontroltranslation"></a>

Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.

## Syntax
<a name="aws-properties-s3-bucket-accesscontroltranslation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-accesscontroltranslation-syntax.json"></a>

```
{
  "[Owner](#cfn-s3-bucket-accesscontroltranslation-owner)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-accesscontroltranslation-syntax.yaml"></a>

```
  [Owner](#cfn-s3-bucket-accesscontroltranslation-owner): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-accesscontroltranslation-properties"></a>

`Owner`  <a name="cfn-s3-bucket-accesscontroltranslation-owner"></a>
Specifies the replica ownership. For default and valid values, see [PUT bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) in the *Amazon S3 API Reference*.
*Required*: Yes
*Type*: String
*Allowed values*: `Destination`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
