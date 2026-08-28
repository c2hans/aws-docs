---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-multicastsourcecreaterequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MulticastSourceCreateRequest
<a name="aws-properties-medialive-input-multicastsourcecreaterequest"></a>

A pair of multicast URL and source IP address (optional) that make up a multicast source.

The parent of this entity is MulticastSettingsCreateRequest.

## Syntax
<a name="aws-properties-medialive-input-multicastsourcecreaterequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-multicastsourcecreaterequest-syntax.json"></a>

```
{
  "[SourceIp](#cfn-medialive-input-multicastsourcecreaterequest-sourceip)" : {{String}},
  "[Url](#cfn-medialive-input-multicastsourcecreaterequest-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-multicastsourcecreaterequest-syntax.yaml"></a>

```
  [SourceIp](#cfn-medialive-input-multicastsourcecreaterequest-sourceip): {{String}}
  [Url](#cfn-medialive-input-multicastsourcecreaterequest-url): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-multicastsourcecreaterequest-properties"></a>

`SourceIp`  <a name="cfn-medialive-input-multicastsourcecreaterequest-sourceip"></a>
The IP address of the device sending the multicast stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-input-multicastsourcecreaterequest-url"></a>
The customer's source URL where the multicast stream is pulled from.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
