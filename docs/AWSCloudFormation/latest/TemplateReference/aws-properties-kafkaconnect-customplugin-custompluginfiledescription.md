---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-customplugin-custompluginfiledescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::CustomPlugin CustomPluginFileDescription
<a name="aws-properties-kafkaconnect-customplugin-custompluginfiledescription"></a>

Details about a custom plugin file.

## Syntax
<a name="aws-properties-kafkaconnect-customplugin-custompluginfiledescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-customplugin-custompluginfiledescription-syntax.json"></a>

```
{
  "[FileMd5](#cfn-kafkaconnect-customplugin-custompluginfiledescription-filemd5)" : {{String}},
  "[FileSize](#cfn-kafkaconnect-customplugin-custompluginfiledescription-filesize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-customplugin-custompluginfiledescription-syntax.yaml"></a>

```
  [FileMd5](#cfn-kafkaconnect-customplugin-custompluginfiledescription-filemd5): {{String}}
  [FileSize](#cfn-kafkaconnect-customplugin-custompluginfiledescription-filesize): {{Integer}}
```

## Properties
<a name="aws-properties-kafkaconnect-customplugin-custompluginfiledescription-properties"></a>

`FileMd5`  <a name="cfn-kafkaconnect-customplugin-custompluginfiledescription-filemd5"></a>
The hex-encoded MD5 checksum of the custom plugin file. You can use it to validate the file.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSize`  <a name="cfn-kafkaconnect-customplugin-custompluginfiledescription-filesize"></a>
The size in bytes of the custom plugin file. You can use it to validate the file.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
