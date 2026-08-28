---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputdevicesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputDeviceSettings
<a name="aws-properties-medialive-input-inputdevicesettings"></a>

Settings that apply only if the input is an Elemental Link input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-inputdevicesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputdevicesettings-syntax.json"></a>

```
{
  "[Id](#cfn-medialive-input-inputdevicesettings-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputdevicesettings-syntax.yaml"></a>

```
  [Id](#cfn-medialive-input-inputdevicesettings-id): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputdevicesettings-properties"></a>

`Id`  <a name="cfn-medialive-input-inputdevicesettings-id"></a>
The unique ID for the device.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
