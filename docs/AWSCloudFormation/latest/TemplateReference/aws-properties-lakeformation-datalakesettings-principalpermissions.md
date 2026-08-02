---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-datalakesettings-principalpermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::DataLakeSettings PrincipalPermissions
<a name="aws-properties-lakeformation-datalakesettings-principalpermissions"></a>

Permissions granted to a principal.

## Syntax
<a name="aws-properties-lakeformation-datalakesettings-principalpermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-datalakesettings-principalpermissions-syntax.json"></a>

```
{
  "[Permissions](#cfn-lakeformation-datalakesettings-principalpermissions-permissions)" : {{[ String, ... ]}},
  "[Principal](#cfn-lakeformation-datalakesettings-principalpermissions-principal)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-datalakesettings-principalpermissions-syntax.yaml"></a>

```
  [Permissions](#cfn-lakeformation-datalakesettings-principalpermissions-permissions): {{
    - String}}
  [Principal](#cfn-lakeformation-datalakesettings-principalpermissions-principal): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-datalakesettings-principalpermissions-properties"></a>

`Permissions`  <a name="cfn-lakeformation-datalakesettings-principalpermissions-permissions"></a>
The permissions that are granted to the principal.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-lakeformation-datalakesettings-principalpermissions-principal"></a>
The principal who is granted permissions.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
