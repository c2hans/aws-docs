---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-relationshipvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity RelationshipValue
<a name="aws-properties-iottwinmaker-entity-relationshipvalue"></a>

The entity relationship.

## Syntax
<a name="aws-properties-iottwinmaker-entity-relationshipvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-relationshipvalue-syntax.json"></a>

```
{
  "[TargetComponentName](#cfn-iottwinmaker-entity-relationshipvalue-targetcomponentname)" : {{String}},
  "[TargetEntityId](#cfn-iottwinmaker-entity-relationshipvalue-targetentityid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-relationshipvalue-syntax.yaml"></a>

```
  [TargetComponentName](#cfn-iottwinmaker-entity-relationshipvalue-targetcomponentname): {{String}}
  [TargetEntityId](#cfn-iottwinmaker-entity-relationshipvalue-targetentityid): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-relationshipvalue-properties"></a>

`TargetComponentName`  <a name="cfn-iottwinmaker-entity-relationshipvalue-targetcomponentname"></a>
The target component name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetEntityId`  <a name="cfn-iottwinmaker-entity-relationshipvalue-targetentityid"></a>
The target entity Id.
*Required*: No
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
