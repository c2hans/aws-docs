---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-ndisourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow NdiSourceSettings
<a name="aws-properties-mediaconnect-flow-ndisourcesettings"></a>

 The settings for the NDI® source. This includes the exact name of the upstream NDI sender that you want to connect to your source.

## Syntax
<a name="aws-properties-mediaconnect-flow-ndisourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-ndisourcesettings-syntax.json"></a>

```
{
  "[SourceName](#cfn-mediaconnect-flow-ndisourcesettings-sourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-ndisourcesettings-syntax.yaml"></a>

```
  [SourceName](#cfn-mediaconnect-flow-ndisourcesettings-sourcename): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-ndisourcesettings-properties"></a>

`SourceName`  <a name="cfn-mediaconnect-flow-ndisourcesettings-sourcename"></a>
 The exact name of an existing NDI sender that's registered with your discovery server. If included, the format of this name must be `MACHINENAME (ProgramName)`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
