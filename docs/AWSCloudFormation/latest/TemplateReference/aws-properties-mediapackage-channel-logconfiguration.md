---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-channel-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::Channel LogConfiguration
<a name="aws-properties-mediapackage-channel-logconfiguration"></a>

The access log configuration parameters for your channel.

## Syntax
<a name="aws-properties-mediapackage-channel-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-channel-logconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-mediapackage-channel-logconfiguration-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackage-channel-logconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-mediapackage-channel-logconfiguration-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-mediapackage-channel-logconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-mediapackage-channel-logconfiguration-loggroupname"></a>
Sets a custom Amazon CloudWatch log group name.
*Required*: No
*Type*: String
*Pattern*: `\A^(\/aws\/MediaPackage\/)[a-zA-Z0-9_-]+\Z`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
