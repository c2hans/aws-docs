---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-databaseresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions DatabaseResource
<a name="aws-properties-lakeformation-principalpermissions-databaseresource"></a>

A structure for the database object.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-databaseresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-databaseresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-principalpermissions-databaseresource-catalogid)" : {{String}},
  "[Name](#cfn-lakeformation-principalpermissions-databaseresource-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-databaseresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-principalpermissions-databaseresource-catalogid): {{String}}
  [Name](#cfn-lakeformation-principalpermissions-databaseresource-name): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-databaseresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-principalpermissions-databaseresource-catalogid"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-principalpermissions-databaseresource-name"></a>
The name of the database resource. Unique to the Data Catalog.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
