---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-botalias-audiologdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::BotAlias AudioLogDestination
<a name="aws-properties-lex-botalias-audiologdestination"></a>

Specifies the S3 bucket location where audio logs are stored.

## Syntax
<a name="aws-properties-lex-botalias-audiologdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-botalias-audiologdestination-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-lex-botalias-audiologdestination-s3bucket)" : {{S3BucketLogDestination}}
}
```

### YAML
<a name="aws-properties-lex-botalias-audiologdestination-syntax.yaml"></a>

```
  [S3Bucket](#cfn-lex-botalias-audiologdestination-s3bucket): {{
    S3BucketLogDestination}}
```

## Properties
<a name="aws-properties-lex-botalias-audiologdestination-properties"></a>

`S3Bucket`  <a name="cfn-lex-botalias-audiologdestination-s3bucket"></a>
The S3 bucket location where audio logs are stored.
*Required*: Yes
*Type*: [S3BucketLogDestination](aws-properties-lex-botalias-s3bucketlogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
