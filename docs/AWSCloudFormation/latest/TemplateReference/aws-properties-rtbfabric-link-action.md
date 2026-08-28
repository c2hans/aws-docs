---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link Action
<a name="aws-properties-rtbfabric-link-action"></a>

Describes a bid action.

## Syntax
<a name="aws-properties-rtbfabric-link-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-action-syntax.json"></a>

```
{
  "[HeaderTag](#cfn-rtbfabric-link-action-headertag)" : {{HeaderTagAction}},
  "[NoBid](#cfn-rtbfabric-link-action-nobid)" : {{NoBidAction}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-action-syntax.yaml"></a>

```
  [HeaderTag](#cfn-rtbfabric-link-action-headertag): {{
    HeaderTagAction}}
  [NoBid](#cfn-rtbfabric-link-action-nobid): {{
    NoBidAction}}
```

## Properties
<a name="aws-properties-rtbfabric-link-action-properties"></a>

`HeaderTag`  <a name="cfn-rtbfabric-link-action-headertag"></a>
Describes the header tag for a bid action.
*Required*: No
*Type*: [HeaderTagAction](aws-properties-rtbfabric-link-headertagaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoBid`  <a name="cfn-rtbfabric-link-action-nobid"></a>
Describes the parameters of a no bid module.
*Required*: No
*Type*: [NoBidAction](aws-properties-rtbfabric-link-nobidaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
