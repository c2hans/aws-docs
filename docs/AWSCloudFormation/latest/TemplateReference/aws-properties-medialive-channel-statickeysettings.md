---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-statickeysettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel StaticKeySettings
<a name="aws-properties-medialive-channel-statickeysettings"></a>

The static key settings.

The parent of this entity is KeyProviderSettings.

## Syntax
<a name="aws-properties-medialive-channel-statickeysettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-statickeysettings-syntax.json"></a>

```
{
  "[KeyProviderServer](#cfn-medialive-channel-statickeysettings-keyproviderserver)" : {{InputLocation}},
  "[StaticKeyValue](#cfn-medialive-channel-statickeysettings-statickeyvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-statickeysettings-syntax.yaml"></a>

```
  [KeyProviderServer](#cfn-medialive-channel-statickeysettings-keyproviderserver): {{
    InputLocation}}
  [StaticKeyValue](#cfn-medialive-channel-statickeysettings-statickeyvalue): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-statickeysettings-properties"></a>

`KeyProviderServer`  <a name="cfn-medialive-channel-statickeysettings-keyproviderserver"></a>
The URL of the license server that is used for protecting content.
*Required*: No
*Type*: [InputLocation](aws-properties-medialive-channel-inputlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticKeyValue`  <a name="cfn-medialive-channel-statickeysettings-statickeyvalue"></a>
The static key value as a 32 character hexadecimal string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
