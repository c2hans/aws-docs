---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-confluencedocumentresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace ConfluenceDocumentResource
<a name="aws-properties-securityagent-agentspace-confluencedocumentresource"></a>

A Confluence document (page) integrated as a resource.

## Syntax
<a name="aws-properties-securityagent-agentspace-confluencedocumentresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-confluencedocumentresource-syntax.json"></a>

```
{
  "[Name](#cfn-securityagent-agentspace-confluencedocumentresource-name)" : {{String}},
  "[PageId](#cfn-securityagent-agentspace-confluencedocumentresource-pageid)" : {{String}},
  "[SpaceKey](#cfn-securityagent-agentspace-confluencedocumentresource-spacekey)" : {{String}},
  "[SpaceTitle](#cfn-securityagent-agentspace-confluencedocumentresource-spacetitle)" : {{String}},
  "[Title](#cfn-securityagent-agentspace-confluencedocumentresource-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-confluencedocumentresource-syntax.yaml"></a>

```
  [Name](#cfn-securityagent-agentspace-confluencedocumentresource-name): {{String}}
  [PageId](#cfn-securityagent-agentspace-confluencedocumentresource-pageid): {{String}}
  [SpaceKey](#cfn-securityagent-agentspace-confluencedocumentresource-spacekey): {{String}}
  [SpaceTitle](#cfn-securityagent-agentspace-confluencedocumentresource-spacetitle): {{String}}
  [Title](#cfn-securityagent-agentspace-confluencedocumentresource-title): {{String}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-confluencedocumentresource-properties"></a>

`Name`  <a name="cfn-securityagent-agentspace-confluencedocumentresource-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageId`  <a name="cfn-securityagent-agentspace-confluencedocumentresource-pageid"></a>
The Confluence page identifier.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceKey`  <a name="cfn-securityagent-agentspace-confluencedocumentresource-spacekey"></a>
The Confluence space key containing the document.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceTitle`  <a name="cfn-securityagent-agentspace-confluencedocumentresource-spacetitle"></a>
The display title of the Confluence space.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-securityagent-agentspace-confluencedocumentresource-title"></a>
The display title of the Confluence page.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
