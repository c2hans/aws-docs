---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-multicastsettingscreaterequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MulticastSettingsCreateRequest
<a name="aws-properties-medialive-input-multicastsettingscreaterequest"></a>

Multicast input settings.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-multicastsettingscreaterequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-multicastsettingscreaterequest-syntax.json"></a>

```
{
  "[Sources](#cfn-medialive-input-multicastsettingscreaterequest-sources)" : {{[ MulticastSourceCreateRequest, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-input-multicastsettingscreaterequest-syntax.yaml"></a>

```
  [Sources](#cfn-medialive-input-multicastsettingscreaterequest-sources): {{
    - MulticastSourceCreateRequest}}
```

## Properties
<a name="aws-properties-medialive-input-multicastsettingscreaterequest-properties"></a>

`Sources`  <a name="cfn-medialive-input-multicastsettingscreaterequest-sources"></a>
The list of multicast sources for this input. Each source is a pair of a multicast URL and an optional source IP address.
*Required*: No
*Type*: Array of [MulticastSourceCreateRequest](aws-properties-medialive-input-multicastsourcecreaterequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
