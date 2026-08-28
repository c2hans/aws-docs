---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-plugin-s3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin S3
<a name="aws-properties-qbusiness-plugin-s3"></a>

Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.

## Syntax
<a name="aws-properties-qbusiness-plugin-s3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-plugin-s3-syntax.json"></a>

```
{
  "[Bucket](#cfn-qbusiness-plugin-s3-bucket)" : {{String}},
  "[Key](#cfn-qbusiness-plugin-s3-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-plugin-s3-syntax.yaml"></a>

```
  [Bucket](#cfn-qbusiness-plugin-s3-bucket): {{String}}
  [Key](#cfn-qbusiness-plugin-s3-key): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-plugin-s3-properties"></a>

`Bucket`  <a name="cfn-qbusiness-plugin-s3-bucket"></a>
The name of the S3 bucket that contains the file.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-qbusiness-plugin-s3-key"></a>
The name of the file.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
