---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-headertagaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link HeaderTagAction
<a name="aws-properties-rtbfabric-link-headertagaction"></a>

Describes the header tag for a bid action.

## Syntax
<a name="aws-properties-rtbfabric-link-headertagaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-headertagaction-syntax.json"></a>

```
{
  "[Name](#cfn-rtbfabric-link-headertagaction-name)" : {{String}},
  "[Value](#cfn-rtbfabric-link-headertagaction-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-headertagaction-syntax.yaml"></a>

```
  [Name](#cfn-rtbfabric-link-headertagaction-name): {{String}}
  [Value](#cfn-rtbfabric-link-headertagaction-value): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-link-headertagaction-properties"></a>

`Name`  <a name="cfn-rtbfabric-link-headertagaction-name"></a>
The name of the bid action.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rtbfabric-link-headertagaction-value"></a>
The value of the bid action.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
