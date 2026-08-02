---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbparametergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBParameterGroup
<a name="aws-resource-rds-dbparametergroup"></a>

The `AWS::RDS::DBParameterGroup` resource creates a custom parameter group for an RDS database family.

This type can be declared in a template and referenced in the `DBParameterGroupName` property of an ` [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html) ` resource.

For information about configuring parameters for Amazon RDS DB instances, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.

For information about configuring parameters for Amazon Aurora DB instances, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.

**Note**
Applying a parameter group to a DB instance may require the DB instance to reboot, resulting in a database outage for the duration of the reboot.

## Syntax
<a name="aws-resource-rds-dbparametergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbparametergroup-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBParameterGroup",
  "Properties" : {
      "[DBParameterGroupName](#cfn-rds-dbparametergroup-dbparametergroupname)" : {{String}},
      "[Description](#cfn-rds-dbparametergroup-description)" : {{String}},
      "[Family](#cfn-rds-dbparametergroup-family)" : {{String}},
      "[Parameters](#cfn-rds-dbparametergroup-parameters)" : {{Json}},
      "[Tags](#cfn-rds-dbparametergroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbparametergroup-syntax.yaml"></a>

```
Type: AWS::RDS::DBParameterGroup
Properties:
  [DBParameterGroupName](#cfn-rds-dbparametergroup-dbparametergroupname): {{String}}
  [Description](#cfn-rds-dbparametergroup-description): {{String}}
  [Family](#cfn-rds-dbparametergroup-family): {{String}}
  [Parameters](#cfn-rds-dbparametergroup-parameters): {{Json}}
  [Tags](#cfn-rds-dbparametergroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbparametergroup-properties"></a>

`DBParameterGroupName`  <a name="cfn-rds-dbparametergroup-dbparametergroupname"></a>
The name of the DB parameter group.
Constraints:
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
If you don't specify a value for `DBParameterGroupName` property, a name is automatically created for the DB parameter group.
This value is stored as a lowercase string.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9])*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-rds-dbparametergroup-description"></a>
Provides the customer-specified description for this DB parameter group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Family`  <a name="cfn-rds-dbparametergroup-family"></a>
The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
To list all of the available parameter group families for a DB engine, use the following command:
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine <engine>`
For example, to list all of the available parameter group families for the MySQL DB engine, use the following command:
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine mysql`
The output contains duplicates.
The following are the valid DB engine values:
+  `aurora-mysql`
+  `aurora-postgresql`
+  `db2-ae`
+  `db2-ce`
+  `db2-se`
+  `mysql`
+  `oracle-ee`
+  `oracle-ee-cdb`
+  `oracle-se2`
+  `oracle-se2-cdb`
+  `postgres`
+  `sqlserver-ee`
+  `sqlserver-se`
+  `sqlserver-ex`
+  `sqlserver-web`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-rds-dbparametergroup-parameters"></a>
A mapping of parameter names and values for the parameter update. You must specify at least one parameter name and value.
For more information about parameter groups, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*, or [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.
AWS CloudFormation doesn't support specifying an apply method for each individual parameter. The default apply method for each parameter is used.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-dbparametergroup-tags"></a>
Tags to assign to the DB parameter group.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbparametergroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbparametergroup-return-values"></a>

### Ref
<a name="aws-resource-rds-dbparametergroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the DB parameter group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbparametergroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rds-dbparametergroup-return-values-fn--getatt-fn--getatt"></a>

`DBParameterGroupName`  <a name="DBParameterGroupName-fn::getatt"></a>
The name of the DB parameter group.

## Examples
<a name="aws-resource-rds-dbparametergroup--examples"></a>

### Create a parameter group for a MySQL DB instance
<a name="aws-resource-rds-dbparametergroup--examples--Create_a_parameter_group_for_a_MySQL_DB_instance"></a>

The following example creates a parameter group for a MySQL DB instance and sets the `sql_mode`, `max_allowed_packet`, and `innodb_buffer_pool_size` parameters.

#### JSON
<a name="aws-resource-rds-dbparametergroup--examples--Create_a_parameter_group_for_a_MySQL_DB_instance--json"></a>

```
"RDSDBParameterGroup": {
        "Type": "AWS::RDS::DBParameterGroup",
        "Properties": {
            "Description": "CloudFormation Sample MySQL Parameter Group",
            "Family": "mysql8.0",
            "Parameters": {
                "sql_mode": "IGNORE_SPACE",
                "max_allowed_packet": 1024,
                "innodb_buffer_pool_size": "{DBInstanceClassMemory*3/4}"
            }
        }
    }
```

#### YAML
<a name="aws-resource-rds-dbparametergroup--examples--Create_a_parameter_group_for_a_MySQL_DB_instance--yaml"></a>

```
RDSDBParameterGroup:
  Type: 'AWS::RDS::DBParameterGroup'
  Properties:
    Description: CloudFormation Sample MySQL Parameter Group
    Family: mysql8.0
    Parameters:
      sql_mode: IGNORE_SPACE
      max_allowed_packet: 1024
      innodb_buffer_pool_size: '{DBInstanceClassMemory*3/4}'
```
