---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign Tag
<a name="aws-properties-connectcampaignsv2-campaign-tag"></a>

The tag of the campaign.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-tag-syntax.json"></a>

```
{
  "[Key](#cfn-connectcampaignsv2-campaign-tag-key)" : {{String}},
  "[Value](#cfn-connectcampaignsv2-campaign-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-tag-syntax.yaml"></a>

```
  [Key](#cfn-connectcampaignsv2-campaign-tag-key): {{String}}
  [Value](#cfn-connectcampaignsv2-campaign-tag-value): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-tag-properties"></a>

`Key`  <a name="cfn-connectcampaignsv2-campaign-tag-key"></a>
The tag keys.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connectcampaignsv2-campaign-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
