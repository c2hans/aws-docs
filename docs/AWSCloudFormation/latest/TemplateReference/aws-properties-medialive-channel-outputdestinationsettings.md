---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-outputdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel OutputDestinationSettings
<a name="aws-properties-medialive-channel-outputdestinationsettings"></a>

The configuration information for this output.

The parent of this entity is OutputDestination.

## Syntax
<a name="aws-properties-medialive-channel-outputdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-outputdestinationsettings-syntax.json"></a>

```
{
  "[PasswordParam](#cfn-medialive-channel-outputdestinationsettings-passwordparam)" : {{String}},
  "[StreamName](#cfn-medialive-channel-outputdestinationsettings-streamname)" : {{String}},
  "[Url](#cfn-medialive-channel-outputdestinationsettings-url)" : {{String}},
  "[Username](#cfn-medialive-channel-outputdestinationsettings-username)" : {{String}},
  "[VirtualSourceAddress](#cfn-medialive-channel-outputdestinationsettings-virtualsourceaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-outputdestinationsettings-syntax.yaml"></a>

```
  [PasswordParam](#cfn-medialive-channel-outputdestinationsettings-passwordparam): {{String}}
  [StreamName](#cfn-medialive-channel-outputdestinationsettings-streamname): {{String}}
  [Url](#cfn-medialive-channel-outputdestinationsettings-url): {{String}}
  [Username](#cfn-medialive-channel-outputdestinationsettings-username): {{String}}
  [VirtualSourceAddress](#cfn-medialive-channel-outputdestinationsettings-virtualsourceaddress): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-outputdestinationsettings-properties"></a>

`PasswordParam`  <a name="cfn-medialive-channel-outputdestinationsettings-passwordparam"></a>
The password parameter that holds the password for accessing the downstream system. This password parameter applies only if the downstream system requires credentials.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-medialive-channel-outputdestinationsettings-streamname"></a>
The stream name for the content. This applies only to RTMP outputs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-channel-outputdestinationsettings-url"></a>
The URL for the destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-medialive-channel-outputdestinationsettings-username"></a>
The user name to connect to the downstream system. This applies only if the downstream system requires credentials.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualSourceAddress`  <a name="cfn-medialive-channel-outputdestinationsettings-virtualsourceaddress"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
