---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-mediaitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace MediaItem
<a name="aws-properties-connect-workspace-mediaitem"></a>

Contains information about a media asset used in a workspace.

## Syntax
<a name="aws-properties-connect-workspace-mediaitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-mediaitem-syntax.json"></a>

```
{
  "[Source](#cfn-connect-workspace-mediaitem-source)" : {{String}},
  "[Type](#cfn-connect-workspace-mediaitem-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-mediaitem-syntax.yaml"></a>

```
  [Source](#cfn-connect-workspace-mediaitem-source): {{String}}
  [Type](#cfn-connect-workspace-mediaitem-type): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-mediaitem-properties"></a>

`Source`  <a name="cfn-connect-workspace-mediaitem-source"></a>
The source URL or data for the media asset.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `533333`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-workspace-mediaitem-type"></a>
The type of media. Valid values are: `IMAGE_LOGO_FAVICON` and `IMAGE_LOGO_HORIZONTAL`.
*Required*: Yes
*Type*: String
*Allowed values*: `IMAGE_LOGO_LIGHT_FAVICON | IMAGE_LOGO_DARK_FAVICON | IMAGE_LOGO_LIGHT_HORIZONTAL | IMAGE_LOGO_DARK_HORIZONTAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
