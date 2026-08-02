---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-principalpermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog PrincipalPermissions
<a name="aws-properties-glue-catalog-principalpermissions"></a>

Permissions granted to a principal.

## Syntax
<a name="aws-properties-glue-catalog-principalpermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-principalpermissions-syntax.json"></a>

```
{
  "[Permissions](#cfn-glue-catalog-principalpermissions-permissions)" : {{[ String, ... ]}},
  "[Principal](#cfn-glue-catalog-principalpermissions-principal)" : {{DataLakePrincipal}}
}
```

### YAML
<a name="aws-properties-glue-catalog-principalpermissions-syntax.yaml"></a>

```
  [Permissions](#cfn-glue-catalog-principalpermissions-permissions): {{
    - String}}
  [Principal](#cfn-glue-catalog-principalpermissions-principal): {{
    DataLakePrincipal}}
```

## Properties
<a name="aws-properties-glue-catalog-principalpermissions-properties"></a>

`Permissions`  <a name="cfn-glue-catalog-principalpermissions-permissions"></a>
The permissions that are granted to the principal.
*Required*: No
*Type*: Array of String
*Allowed values*: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-glue-catalog-principalpermissions-principal"></a>
The principal who is granted permissions.
*Required*: No
*Type*: [DataLakePrincipal](aws-properties-glue-catalog-datalakeprincipal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
