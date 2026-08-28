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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
