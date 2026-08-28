---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot S3Location
<a name="aws-properties-lex-bot-s3location"></a>

Defines an Amazon S3 bucket location.

## Syntax
<a name="aws-properties-lex-bot-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-s3location-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-lex-bot-s3location-s3bucket)" : {{String}},
  "[S3ObjectKey](#cfn-lex-bot-s3location-s3objectkey)" : {{String}},
  "[S3ObjectVersion](#cfn-lex-bot-s3location-s3objectversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-s3location-syntax.yaml"></a>

```
  [S3Bucket](#cfn-lex-bot-s3location-s3bucket): {{String}}
  [S3ObjectKey](#cfn-lex-bot-s3location-s3objectkey): {{String}}
  [S3ObjectVersion](#cfn-lex-bot-s3location-s3objectversion): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-s3location-properties"></a>

`S3Bucket`  <a name="cfn-lex-bot-s3location-s3bucket"></a>
The S3 bucket name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ObjectKey`  <a name="cfn-lex-bot-s3location-s3objectkey"></a>
The path and file name to the object in the S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ObjectVersion`  <a name="cfn-lex-bot-s3location-s3objectversion"></a>
The version of the object in the S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
