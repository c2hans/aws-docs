---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-definition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity Definition
<a name="aws-properties-iottwinmaker-entity-definition"></a>

The entity definition.

## Syntax
<a name="aws-properties-iottwinmaker-entity-definition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-definition-syntax.json"></a>

```
{
  "[Configuration](#cfn-iottwinmaker-entity-definition-configuration)" : {{{{{Key}}: {{Value}}, ...}}},
  "[DataType](#cfn-iottwinmaker-entity-definition-datatype)" : {{DataType}},
  "[DefaultValue](#cfn-iottwinmaker-entity-definition-defaultvalue)" : {{DataValue}},
  "[IsExternalId](#cfn-iottwinmaker-entity-definition-isexternalid)" : {{Boolean}},
  "[IsFinal](#cfn-iottwinmaker-entity-definition-isfinal)" : {{Boolean}},
  "[IsImported](#cfn-iottwinmaker-entity-definition-isimported)" : {{Boolean}},
  "[IsInherited](#cfn-iottwinmaker-entity-definition-isinherited)" : {{Boolean}},
  "[IsRequiredInEntity](#cfn-iottwinmaker-entity-definition-isrequiredinentity)" : {{Boolean}},
  "[IsStoredExternally](#cfn-iottwinmaker-entity-definition-isstoredexternally)" : {{Boolean}},
  "[IsTimeSeries](#cfn-iottwinmaker-entity-definition-istimeseries)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-definition-syntax.yaml"></a>

```
  [Configuration](#cfn-iottwinmaker-entity-definition-configuration): {{
    {{Key}}: {{Value}}}}
  [DataType](#cfn-iottwinmaker-entity-definition-datatype): {{
    DataType}}
  [DefaultValue](#cfn-iottwinmaker-entity-definition-defaultvalue): {{
    DataValue}}
  [IsExternalId](#cfn-iottwinmaker-entity-definition-isexternalid): {{Boolean}}
  [IsFinal](#cfn-iottwinmaker-entity-definition-isfinal): {{Boolean}}
  [IsImported](#cfn-iottwinmaker-entity-definition-isimported): {{Boolean}}
  [IsInherited](#cfn-iottwinmaker-entity-definition-isinherited): {{Boolean}}
  [IsRequiredInEntity](#cfn-iottwinmaker-entity-definition-isrequiredinentity): {{Boolean}}
  [IsStoredExternally](#cfn-iottwinmaker-entity-definition-isstoredexternally): {{Boolean}}
  [IsTimeSeries](#cfn-iottwinmaker-entity-definition-istimeseries): {{Boolean}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-definition-properties"></a>

`Configuration`  <a name="cfn-iottwinmaker-entity-definition-configuration"></a>
The configuration.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-iottwinmaker-entity-definition-datatype"></a>
The data type
*Required*: No
*Type*: [DataType](aws-properties-iottwinmaker-entity-datatype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultValue`  <a name="cfn-iottwinmaker-entity-definition-defaultvalue"></a>
The default value.
*Required*: No
*Type*: [DataValue](aws-properties-iottwinmaker-entity-datavalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsExternalId`  <a name="cfn-iottwinmaker-entity-definition-isexternalid"></a>
Displays if the entity has a external Id.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsFinal`  <a name="cfn-iottwinmaker-entity-definition-isfinal"></a>
Displays if the entity is final.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsImported`  <a name="cfn-iottwinmaker-entity-definition-isimported"></a>
Displays if the entity is imported.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsInherited`  <a name="cfn-iottwinmaker-entity-definition-isinherited"></a>
Displays if the entity is inherited.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsRequiredInEntity`  <a name="cfn-iottwinmaker-entity-definition-isrequiredinentity"></a>
Displays if the entity is a required entity.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsStoredExternally`  <a name="cfn-iottwinmaker-entity-definition-isstoredexternally"></a>
Displays if the entity is tored externally.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsTimeSeries`  <a name="cfn-iottwinmaker-entity-definition-istimeseries"></a>
Displays if the entity
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
