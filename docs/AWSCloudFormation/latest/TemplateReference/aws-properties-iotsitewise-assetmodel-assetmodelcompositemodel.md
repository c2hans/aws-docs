---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel AssetModelCompositeModel
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel"></a>

Contains information about a composite model in an asset model. This object contains the asset property definitions that you define in the composite model.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel-syntax.json"></a>

```
{
  "[ComposedAssetModelId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-composedassetmodelid)" : {{String}},
  "[CompositeModelProperties](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties)" : {{[ AssetModelProperty, ... ]}},
  "[Description](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description)" : {{String}},
  "[ExternalId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-externalid)" : {{String}},
  "[Id](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-id)" : {{String}},
  "[Name](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name)" : {{String}},
  "[ParentAssetModelCompositeModelExternalId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-parentassetmodelcompositemodelexternalid)" : {{String}},
  "[Path](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-path)" : {{[ String, ... ]}},
  "[Type](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel-syntax.yaml"></a>

```
  [ComposedAssetModelId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-composedassetmodelid): {{String}}
  [CompositeModelProperties](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties): {{
    - AssetModelProperty}}
  [Description](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description): {{String}}
  [ExternalId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-externalid): {{String}}
  [Id](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-id): {{String}}
  [Name](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name): {{String}}
  [ParentAssetModelCompositeModelExternalId](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-parentassetmodelcompositemodelexternalid): {{String}}
  [Path](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-path): {{
    - String}}
  [Type](#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel-properties"></a>

`ComposedAssetModelId`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-composedassetmodelid"></a>
The ID of a component model which is reused to create this composite model.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompositeModelProperties`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties"></a>
The asset property definitions for this composite model.
*Required*: No
*Type*: Array of [AssetModelProperty](aws-properties-iotsitewise-assetmodel-assetmodelproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description"></a>
The description of the composite model.
If the composite model is a `component-model-based` composite model, the description is inherited from the `COMPONENT_MODEL` asset model and cannot be changed.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-externalid"></a>
The external ID of a composite model on this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
One of `ExternalId` or `Path` must be specified.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-id"></a>
 The ID of the asset model composite model.
This is a return value and can't be set.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name"></a>
The name of the composite model.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentAssetModelCompositeModelExternalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-parentassetmodelcompositemodelexternalid"></a>
The external ID of the parent composite model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-path"></a>
The structured path to the property from the root of the asset using property names. Path is used as the ID if the asset model is a derived composite model.
One of `ExternalId` or `Path` must be specified.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type"></a>
The type of the composite model. For alarm composite models, this type is `AWS/ALARM`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples"></a>

**Topics**
+ [Create an alarm model](#aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_an_alarm_model)
+ [Create a `component-model-based` composite model](#aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_a_component-model-based_composite_model)

### Create an alarm model
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_an_alarm_model"></a>

You can modify the following example to create an alarm model.

**Note**
Replace `TestAlarmModel` with the name of your alarm model.

#### YAML
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_an_alarm_model--yaml"></a>

```
Resources: AssetModelWithAlarmCompositeModel: Type:
                AWS::IoTSiteWise::AssetModel Properties: AssetModelName:
                AssetModelWithValidAlarmCompositeModel AssetModelDescription:
                AssetModelWithValidAlarmCompositeModel AssetModelCompositeModels: - Description:
                compositeModel created by cfn Name: TestAlarmCompositeModel Type: AWS/ALARM
                CompositeModelProperties: - LogicalId: MyLogicalId_for_ALARM_TYPE_1 Name:
                AWS/ALARM_TYPE DataType: STRING Type: TypeName: Attribute Attribute: DefaultValue:
                IOT_EVENTS - LogicalId: MyLogicalId_for_ALARM_SOURCE_1 Name: AWS/ALARM_SOURCE
                DataType: STRING Type: TypeName: Attribute Attribute: DefaultValue: Fn::Sub:
                "arn:${AWS::Partition}:iotevents:${AWS::Region}:${AWS::AccountId}:alarmModel/TestAlarmModel"
                - LogicalId: MyLogicalId_for_ALARM_STATE_1 Name: AWS/ALARM_STATE DataType: STRUCT
                DataTypeSpec: AWS/ALARM_STATE Type: TypeName: Measurement
```

### Create a `component-model-based` composite model
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_a_component-model-based_composite_model"></a>

You can modify the following example to create a `component-model-based` composite model.

#### YAML
<a name="aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel--examples--Create_a_component-model-based_composite_model--yaml"></a>

```
Resources: MainAssetModel: Type: AWS::IoTSiteWise::AssetModel
                Properties: AssetModelExternalId: AssetModelName: AssetModelWithCustomComposites
                AssetModelDescription: Asset model with custom composite models
                AssetModelProperties: - Name: metric_property ExternalId:
                metric_property_external_id DataType: DOUBLE Type: TypeName: Transform Transform:
                Expression: abs(avgtemp) Variables: - Name: avgtemp Value: PropertyPath: - Name:
                AssetModelWithCustomComposites - Name: CompositeModel3 - Name:
                ComponentModel1CompositeModel - Name: ComponentModel2Property
                AssetModelCompositeModels: - ExternalId: CompositeModelExternalId1 Type: CUSTOM
                Name: CompositeModel1 CompositeModelProperties: - Name: CompositeModel1Property
                ExternalId: CompositeModel1PropertyExternalId DataType: DOUBLE Type: TypeName:
                Measurement - ExternalId: CompositeModelExternalId2 Type: CUSTOM Name:
                CompositeModel2 ParentAssetModelCompositeModelExternalId: CompositeModelExternalId1
                CompositeModelProperties: - Name: CompositeModel2Property ExternalId:
                CompositeModel2PropertyExternalId DataType: DOUBLE Type: TypeName: Measurement -
                ExternalId: CompositeModelExternalId3 Type: CUSTOM Name: CompositeModel3
                ComposedAssetModelId: !Ref ComponentModel1 - Path: - AssetModelWithCustomComposites
                - CompositeModel3 - ComponentModel1CompositeModel ExternalId:
                DerivedCompositeExternalId Type: CUSTOM Name: ComponentModel1CompositeModel
                CompositeModelProperties: - Name: ComponentModel2Property ExternalId:
                DerivedCompositePropertyExternalId DataType: DOUBLE Type: TypeName: Measurement
                ComponentModel1: Type: AWS::IoTSiteWise::AssetModel Properties:
                AssetModelExternalId: ComponentModel1ExternalId AssetModelType: COMPONENT_MODEL
                AssetModelName: ComponentModel1 AssetModelCompositeModels: - ExternalId:
                ComponentModel1CompositeModel ComposedAssetModelId: !Ref ComponentModel2 Name:
                ComponentModel1CompositeModel Type: CUSTOM ComponentModel2: Type:
                AWS::IoTSiteWise::AssetModel Properties: AssetModelExternalId:
                ComponentModel2ExternalId AssetModelType: COMPONENT_MODEL AssetModelName:
                ComponentModel2 AssetModelProperties: - Name: ComponentModel2Property ExternalId:
                ComponentModel2PropertyExternalId DataType: DOUBLE Type: TypeName: Measurement
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
