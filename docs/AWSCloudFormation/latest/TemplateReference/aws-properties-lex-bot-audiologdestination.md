---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-audiologdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AudioLogDestination
<a name="aws-properties-lex-bot-audiologdestination"></a>

The location of audio log files collected when conversation logging is enabled for a bot.

## Syntax
<a name="aws-properties-lex-bot-audiologdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-audiologdestination-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-lex-bot-audiologdestination-s3bucket)" : {{S3BucketLogDestination}}
}
```

### YAML
<a name="aws-properties-lex-bot-audiologdestination-syntax.yaml"></a>

```
  [S3Bucket](#cfn-lex-bot-audiologdestination-s3bucket): {{
    S3BucketLogDestination}}
```

## Properties
<a name="aws-properties-lex-bot-audiologdestination-properties"></a>

`S3Bucket`  <a name="cfn-lex-bot-audiologdestination-s3bucket"></a>
Specifies the Amazon S3 bucket where the audio files are stored.
*Required*: Yes
*Type*: [S3BucketLogDestination](aws-properties-lex-bot-s3bucketlogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
