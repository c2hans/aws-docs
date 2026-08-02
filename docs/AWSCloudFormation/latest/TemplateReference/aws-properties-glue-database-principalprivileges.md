---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-database-principalprivileges.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Database PrincipalPrivileges
<a name="aws-properties-glue-database-principalprivileges"></a>

the permissions granted to a principal

## Syntax
<a name="aws-properties-glue-database-principalprivileges-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-database-principalprivileges-syntax.json"></a>

```
{
  "[Permissions](#cfn-glue-database-principalprivileges-permissions)" : {{[ String, ... ]}},
  "[Principal](#cfn-glue-database-principalprivileges-principal)" : {{DataLakePrincipal}}
}
```

### YAML
<a name="aws-properties-glue-database-principalprivileges-syntax.yaml"></a>

```
  [Permissions](#cfn-glue-database-principalprivileges-permissions): {{
    - String}}
  [Principal](#cfn-glue-database-principalprivileges-principal): {{
    DataLakePrincipal}}
```

## Properties
<a name="aws-properties-glue-database-principalprivileges-properties"></a>

`Permissions`  <a name="cfn-glue-database-principalprivileges-permissions"></a>
The permissions that are granted to the principal.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-glue-database-principalprivileges-principal"></a>
The principal who is granted permissions.
*Required*: No
*Type*: [DataLakePrincipal](aws-properties-glue-database-datalakeprincipal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
