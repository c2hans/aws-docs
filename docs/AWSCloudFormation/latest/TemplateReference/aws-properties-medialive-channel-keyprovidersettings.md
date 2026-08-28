---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-keyprovidersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel KeyProviderSettings
<a name="aws-properties-medialive-channel-keyprovidersettings"></a>

The configuration of key provider settings.

The parent of this entity is HlsGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-keyprovidersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-keyprovidersettings-syntax.json"></a>

```
{
  "[StaticKeySettings](#cfn-medialive-channel-keyprovidersettings-statickeysettings)" : {{StaticKeySettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-keyprovidersettings-syntax.yaml"></a>

```
  [StaticKeySettings](#cfn-medialive-channel-keyprovidersettings-statickeysettings): {{
    StaticKeySettings}}
```

## Properties
<a name="aws-properties-medialive-channel-keyprovidersettings-properties"></a>

`StaticKeySettings`  <a name="cfn-medialive-channel-keyprovidersettings-statickeysettings"></a>
The configuration of static key settings.
*Required*: No
*Type*: [StaticKeySettings](aws-properties-medialive-channel-statickeysettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
