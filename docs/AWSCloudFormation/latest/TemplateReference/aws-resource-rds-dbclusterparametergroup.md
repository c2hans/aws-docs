---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbclusterparametergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBClusterParameterGroup
<a name="aws-resource-rds-dbclusterparametergroup"></a>

The `AWS::RDS::DBClusterParameterGroup` resource creates a new Amazon RDS DB cluster parameter group.

For information about configuring parameters for Amazon Aurora DB clusters, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.

**Note**
If you apply a parameter group to a DB cluster, then its DB instances might need to reboot. This can result in an outage while the DB instances are rebooting.
If you apply a change to parameter group associated with a stopped DB cluster, then the updated stack waits until the DB cluster is started.

## Syntax
<a name="aws-resource-rds-dbclusterparametergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbclusterparametergroup-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBClusterParameterGroup",
  "Properties" : {
      "[DBClusterParameterGroupName](#cfn-rds-dbclusterparametergroup-dbclusterparametergroupname)" : {{String}},
      "[Description](#cfn-rds-dbclusterparametergroup-description)" : {{String}},
      "[Family](#cfn-rds-dbclusterparametergroup-family)" : {{String}},
      "[Parameters](#cfn-rds-dbclusterparametergroup-parameters)" : {{Json}},
      "[Tags](#cfn-rds-dbclusterparametergroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbclusterparametergroup-syntax.yaml"></a>

```
Type: AWS::RDS::DBClusterParameterGroup
Properties:
  [DBClusterParameterGroupName](#cfn-rds-dbclusterparametergroup-dbclusterparametergroupname): {{String}}
  [Description](#cfn-rds-dbclusterparametergroup-description): {{String}}
  [Family](#cfn-rds-dbclusterparametergroup-family): {{String}}
  [Parameters](#cfn-rds-dbclusterparametergroup-parameters): {{Json}}
  [Tags](#cfn-rds-dbclusterparametergroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbclusterparametergroup-properties"></a>

`DBClusterParameterGroupName`  <a name="cfn-rds-dbclusterparametergroup-dbclusterparametergroupname"></a>
The name of the DB cluster parameter group.
Constraints:
+ Must not match the name of an existing DB cluster parameter group.
This value is stored as a lowercase string.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9])*$`
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-rds-dbclusterparametergroup-description"></a>
The description for the DB cluster parameter group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Family`  <a name="cfn-rds-dbclusterparametergroup-family"></a>
The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
 **Aurora MySQL**
Example: `aurora-mysql5.7`, `aurora-mysql8.0`
 **Aurora PostgreSQL**
Example: `aurora-postgresql14`
 **RDS for MySQL**
Example: `mysql8.0`
 **RDS for PostgreSQL**
Example: `postgres13`
To list all of the available parameter group families for a DB engine, use the following command:
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine <engine>`
For example, to list all of the available parameter group families for the Aurora PostgreSQL DB engine, use the following command:
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine aurora-postgresql`
The output contains duplicates.
The following are the valid DB engine values:
+  `aurora-mysql`
+  `aurora-postgresql`
+  `mysql`
+  `postgres`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-rds-dbclusterparametergroup-parameters"></a>
Provides a list of parameters for the DB cluster parameter group.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-dbclusterparametergroup-tags"></a>
Tags to assign to the DB cluster parameter group.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbclusterparametergroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbclusterparametergroup-return-values"></a>

### Ref
<a name="aws-resource-rds-dbclusterparametergroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the DB cluster parameter group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-rds-dbclusterparametergroup--examples"></a>

### Create a parameter group for an Aurora MySQL DB cluster
<a name="aws-resource-rds-dbclusterparametergroup--examples--Create_a_parameter_group_for_an_Aurora_MySQL_DB_cluster"></a>

The following example creates a DB cluster parameter group for an Aurora MySQL DB cluster and sets the `time_zone` and `character_set_database` parameters:

#### JSON
<a name="aws-resource-rds-dbclusterparametergroup--examples--Create_a_parameter_group_for_an_Aurora_MySQL_DB_cluster--json"></a>

```
"RDSDBClusterParameterGroup": {
        "Type": "AWS::RDS::DBClusterParameterGroup",
        "Properties": {
            "Description": "CloudFormation Sample Aurora Cluster Parameter Group",
            "Family": "aurora-mysql8.0",
            "Parameters": {
                "time_zone": "US/Eastern",
                "character_set_database": "utf32"
            }
        }
    }
```

#### YAML
<a name="aws-resource-rds-dbclusterparametergroup--examples--Create_a_parameter_group_for_an_Aurora_MySQL_DB_cluster--yaml"></a>

```
RDSDBClusterParameterGroup:
  Type: 'AWS::RDS::DBClusterParameterGroup'
  Properties:
    Description: CloudFormation Sample Aurora Cluster Parameter Group
    Family: aurora5.6
    Parameters:
      time_zone: US/Eastern
      character_set_database: utf32
```
