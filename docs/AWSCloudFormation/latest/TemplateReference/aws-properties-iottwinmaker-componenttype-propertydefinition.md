---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-propertydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType PropertyDefinition
<a name="aws-properties-iottwinmaker-componenttype-propertydefinition"></a>

PropertyDefinition is an object that maps strings to the property definitions in the component type.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-propertydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-propertydefinition-syntax.json"></a>

```
{
  "[Configurations](#cfn-iottwinmaker-componenttype-propertydefinition-configurations)" : {{{{{Key}}: {{Value}}, ...}}},
  "[DataType](#cfn-iottwinmaker-componenttype-propertydefinition-datatype)" : {{DataType}},
  "[DefaultValue](#cfn-iottwinmaker-componenttype-propertydefinition-defaultvalue)" : {{DataValue}},
  "[IsExternalId](#cfn-iottwinmaker-componenttype-propertydefinition-isexternalid)" : {{Boolean}},
  "[IsRequiredInEntity](#cfn-iottwinmaker-componenttype-propertydefinition-isrequiredinentity)" : {{Boolean}},
  "[IsStoredExternally](#cfn-iottwinmaker-componenttype-propertydefinition-isstoredexternally)" : {{Boolean}},
  "[IsTimeSeries](#cfn-iottwinmaker-componenttype-propertydefinition-istimeseries)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-propertydefinition-syntax.yaml"></a>

```
  [Configurations](#cfn-iottwinmaker-componenttype-propertydefinition-configurations): {{
    {{Key}}: {{Value}}}}
  [DataType](#cfn-iottwinmaker-componenttype-propertydefinition-datatype): {{
    DataType}}
  [DefaultValue](#cfn-iottwinmaker-componenttype-propertydefinition-defaultvalue): {{
    DataValue}}
  [IsExternalId](#cfn-iottwinmaker-componenttype-propertydefinition-isexternalid): {{Boolean}}
  [IsRequiredInEntity](#cfn-iottwinmaker-componenttype-propertydefinition-isrequiredinentity): {{Boolean}}
  [IsStoredExternally](#cfn-iottwinmaker-componenttype-propertydefinition-isstoredexternally): {{Boolean}}
  [IsTimeSeries](#cfn-iottwinmaker-componenttype-propertydefinition-istimeseries): {{Boolean}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-propertydefinition-properties"></a>

`Configurations`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-configurations"></a>
A mapping that specifies configuration information about the property.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-datatype"></a>

*Required*: No
*Type*: [DataType](aws-properties-iottwinmaker-componenttype-datatype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultValue`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-defaultvalue"></a>
A boolean value that specifies whether the property ID comes from an external data store.
*Required*: No
*Type*: [DataValue](aws-properties-iottwinmaker-componenttype-datavalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsExternalId`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-isexternalid"></a>
A Boolean value that specifies whether the property ID comes from an external data source.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsRequiredInEntity`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-isrequiredinentity"></a>
A boolean value that specifies whether the property is required in an entity.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsStoredExternally`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-isstoredexternally"></a>
A boolean value that specifies whether the property is stored externally.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsTimeSeries`  <a name="cfn-iottwinmaker-componenttype-propertydefinition-istimeseries"></a>
A boolean value that specifies whether the property consists of time series data.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
