---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-customconnectorsourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow CustomConnectorSourceProperties
<a name="aws-properties-appflow-flow-customconnectorsourceproperties"></a>

The properties that are applied when the custom connector is being used as a source.

## Syntax
<a name="aws-properties-appflow-flow-customconnectorsourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-customconnectorsourceproperties-syntax.json"></a>

```
{
  "[CustomProperties](#cfn-appflow-flow-customconnectorsourceproperties-customproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[DataTransferApi](#cfn-appflow-flow-customconnectorsourceproperties-datatransferapi)" : {{DataTransferApi}},
  "[EntityName](#cfn-appflow-flow-customconnectorsourceproperties-entityname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-customconnectorsourceproperties-syntax.yaml"></a>

```
  [CustomProperties](#cfn-appflow-flow-customconnectorsourceproperties-customproperties): {{
    {{Key}}: {{Value}}}}
  [DataTransferApi](#cfn-appflow-flow-customconnectorsourceproperties-datatransferapi): {{
    DataTransferApi}}
  [EntityName](#cfn-appflow-flow-customconnectorsourceproperties-entityname): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-customconnectorsourceproperties-properties"></a>

`CustomProperties`  <a name="cfn-appflow-flow-customconnectorsourceproperties-customproperties"></a>
Custom properties that are required to use the custom connector as a source.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\w]{1,2048}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataTransferApi`  <a name="cfn-appflow-flow-customconnectorsourceproperties-datatransferapi"></a>
The API of the connector application that Amazon AppFlow uses to transfer your data.
*Required*: No
*Type*: [DataTransferApi](aws-properties-appflow-flow-datatransferapi.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityName`  <a name="cfn-appflow-flow-customconnectorsourceproperties-entityname"></a>
The entity specified in the custom connector as a source in the flow.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
