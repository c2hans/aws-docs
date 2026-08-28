---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-thesaurus-s3path.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Thesaurus S3Path
<a name="aws-properties-kendra-thesaurus-s3path"></a>

Information required to find a specific file in an Amazon S3 bucket.

## Syntax
<a name="aws-properties-kendra-thesaurus-s3path-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-thesaurus-s3path-syntax.json"></a>

```
{
  "[Bucket](#cfn-kendra-thesaurus-s3path-bucket)" : {{String}},
  "[Key](#cfn-kendra-thesaurus-s3path-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-thesaurus-s3path-syntax.yaml"></a>

```
  [Bucket](#cfn-kendra-thesaurus-s3path-bucket): {{String}}
  [Key](#cfn-kendra-thesaurus-s3path-key): {{String}}
```

## Properties
<a name="aws-properties-kendra-thesaurus-s3path-properties"></a>

`Bucket`  <a name="cfn-kendra-thesaurus-s3path-bucket"></a>
The name of the S3 bucket that contains the file.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-kendra-thesaurus-s3path-key"></a>
The name of the file.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
