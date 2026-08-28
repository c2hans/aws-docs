---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-accesspoint-accesspointtag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::AccessPoint AccessPointTag
<a name="aws-properties-s3files-accesspoint-accesspointtag"></a>

A key-value pair to associate with the access point.

## Syntax
<a name="aws-properties-s3files-accesspoint-accesspointtag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-accesspoint-accesspointtag-syntax.json"></a>

```
{
  "[Key](#cfn-s3files-accesspoint-accesspointtag-key)" : {{String}},
  "[Value](#cfn-s3files-accesspoint-accesspointtag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3files-accesspoint-accesspointtag-syntax.yaml"></a>

```
  [Key](#cfn-s3files-accesspoint-accesspointtag-key): {{String}}
  [Value](#cfn-s3files-accesspoint-accesspointtag-value): {{String}}
```

## Properties
<a name="aws-properties-s3files-accesspoint-accesspointtag-properties"></a>

`Key`  <a name="cfn-s3files-accesspoint-accesspointtag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3files-accesspoint-accesspointtag-value"></a>
The value for the tag. You can specify a value that's 1 to 256 characters in length.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
