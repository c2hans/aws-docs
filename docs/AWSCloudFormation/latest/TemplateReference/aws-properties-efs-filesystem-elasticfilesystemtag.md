---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-elasticfilesystemtag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem ElasticFileSystemTag
<a name="aws-properties-efs-filesystem-elasticfilesystemtag"></a>

A tag is a key-value pair attached to a file system. Allowed characters in the `Key` and `Value` properties are letters, white space, and numbers that can be represented in UTF-8, and the following characters:` + - = . _ : /`

## Syntax
<a name="aws-properties-efs-filesystem-elasticfilesystemtag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-elasticfilesystemtag-syntax.json"></a>

```
{
  "[Key](#cfn-efs-filesystem-elasticfilesystemtag-key)" : {{String}},
  "[Value](#cfn-efs-filesystem-elasticfilesystemtag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-elasticfilesystemtag-syntax.yaml"></a>

```
  [Key](#cfn-efs-filesystem-elasticfilesystemtag-key): {{String}}
  [Value](#cfn-efs-filesystem-elasticfilesystemtag-value): {{String}}
```

## Properties
<a name="aws-properties-efs-filesystem-elasticfilesystemtag-properties"></a>

`Key`  <a name="cfn-efs-filesystem-elasticfilesystemtag-key"></a>
The tag key (String). The key can't start with `aws:`.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-efs-filesystem-elasticfilesystemtag-value"></a>
The value of the tag key.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
