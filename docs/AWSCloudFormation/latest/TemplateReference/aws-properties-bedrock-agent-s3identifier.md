---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-s3identifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent S3Identifier
<a name="aws-properties-bedrock-agent-s3identifier"></a>

 The identifier information for an Amazon S3 bucket.

## Syntax
<a name="aws-properties-bedrock-agent-s3identifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-s3identifier-syntax.json"></a>

```
{
  "[S3BucketName](#cfn-bedrock-agent-s3identifier-s3bucketname)" : {{String}},
  "[S3ObjectKey](#cfn-bedrock-agent-s3identifier-s3objectkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-s3identifier-syntax.yaml"></a>

```
  [S3BucketName](#cfn-bedrock-agent-s3identifier-s3bucketname): {{String}}
  [S3ObjectKey](#cfn-bedrock-agent-s3identifier-s3objectkey): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-s3identifier-properties"></a>

`S3BucketName`  <a name="cfn-bedrock-agent-s3identifier-s3bucketname"></a>
 The name of the S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ObjectKey`  <a name="cfn-bedrock-agent-s3identifier-s3objectkey"></a>
 The S3 object key for the S3 resource.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
