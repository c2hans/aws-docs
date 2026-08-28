---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel AssetModelProperty
<a name="aws-properties-iotsitewise-assetmodel-assetmodelproperty"></a>

Contains information about an asset model property.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-assetmodelproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-assetmodelproperty-syntax.json"></a>

```
{
  "[DataType](#cfn-iotsitewise-assetmodel-assetmodelproperty-datatype)" : {{String}},
  "[DataTypeSpec](#cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec)" : {{String}},
  "[ExternalId](#cfn-iotsitewise-assetmodel-assetmodelproperty-externalid)" : {{String}},
  "[Id](#cfn-iotsitewise-assetmodel-assetmodelproperty-id)" : {{String}},
  "[LogicalId](#cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid)" : {{String}},
  "[Name](#cfn-iotsitewise-assetmodel-assetmodelproperty-name)" : {{String}},
  "[Type](#cfn-iotsitewise-assetmodel-assetmodelproperty-type)" : {{PropertyType}},
  "[Unit](#cfn-iotsitewise-assetmodel-assetmodelproperty-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-assetmodelproperty-syntax.yaml"></a>

```
  [DataType](#cfn-iotsitewise-assetmodel-assetmodelproperty-datatype): {{String}}
  [DataTypeSpec](#cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec): {{String}}
  [ExternalId](#cfn-iotsitewise-assetmodel-assetmodelproperty-externalid): {{String}}
  [Id](#cfn-iotsitewise-assetmodel-assetmodelproperty-id): {{String}}
  [LogicalId](#cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid): {{String}}
  [Name](#cfn-iotsitewise-assetmodel-assetmodelproperty-name): {{String}}
  [Type](#cfn-iotsitewise-assetmodel-assetmodelproperty-type): {{
    PropertyType}}
  [Unit](#cfn-iotsitewise-assetmodel-assetmodelproperty-unit): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-assetmodelproperty-properties"></a>

`DataType`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-datatype"></a>
The data type of the asset model property.
The `VIDEO`, `ANNOTATION`, and `JSON` data types aren't supported for asset model properties. These types are used only by time series that store data for datasets in a workspace.
If you specify `STRUCT`, you must also specify `dataTypeSpec` to identify the type of the structure for this property.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataTypeSpec`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec"></a>
The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.
*Required*: No
*Type*: String
*Allowed values*: `AWS/ALARM_STATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-externalid"></a>
The external ID of the asset property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
One of `ExternalId` or `LogicalId` must be specified.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-id"></a>
The ID of the property.
This is a return value and can't be set.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid"></a>
The `LogicalID` of the asset model property.
One of `ExternalId` or `LogicalId` must be specified.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-name"></a>
The name of the asset model property.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-type"></a>
Contains a property type, which can be one of `attribute`, `measurement`, `metric`, or `transform`.
*Required*: Yes
*Type*: [PropertyType](aws-properties-iotsitewise-assetmodel-propertytype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperty-unit"></a>
The unit of the asset model property, such as `Newtons` or `RPM`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
