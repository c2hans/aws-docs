---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiohlsrenditionselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioHlsRenditionSelection
<a name="aws-properties-medialive-channel-audiohlsrenditionselection"></a>

Selector for HLS audio rendition.

The parent of this entity is AudioSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiohlsrenditionselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiohlsrenditionselection-syntax.json"></a>

```
{
  "[GroupId](#cfn-medialive-channel-audiohlsrenditionselection-groupid)" : {{String}},
  "[Name](#cfn-medialive-channel-audiohlsrenditionselection-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiohlsrenditionselection-syntax.yaml"></a>

```
  [GroupId](#cfn-medialive-channel-audiohlsrenditionselection-groupid): {{String}}
  [Name](#cfn-medialive-channel-audiohlsrenditionselection-name): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-audiohlsrenditionselection-properties"></a>

`GroupId`  <a name="cfn-medialive-channel-audiohlsrenditionselection-groupid"></a>
Specifies the GROUP-ID in the \#EXT-X-MEDIA tag of the target HLS audio rendition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-channel-audiohlsrenditionselection-name"></a>
Specifies the NAME in the \#EXT-X-MEDIA tag of the target HLS audio rendition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
