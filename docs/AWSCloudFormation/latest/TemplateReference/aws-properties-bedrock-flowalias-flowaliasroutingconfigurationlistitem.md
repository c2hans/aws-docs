---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowAlias FlowAliasRoutingConfigurationListItem
<a name="aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem"></a>

Contains information about a version that the alias maps to.

## Syntax
<a name="aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem-syntax.json"></a>

```
{
  "[FlowVersion](#cfn-bedrock-flowalias-flowaliasroutingconfigurationlistitem-flowversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem-syntax.yaml"></a>

```
  [FlowVersion](#cfn-bedrock-flowalias-flowaliasroutingconfigurationlistitem-flowversion): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem-properties"></a>

`FlowVersion`  <a name="cfn-bedrock-flowalias-flowaliasroutingconfigurationlistitem-flowversion"></a>
The version that the alias maps to.
*Required*: No
*Type*: String
*Pattern*: `^(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
