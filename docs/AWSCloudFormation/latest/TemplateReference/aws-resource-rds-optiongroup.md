---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-optiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::OptionGroup
<a name="aws-resource-rds-optiongroup"></a>

The `AWS::RDS::OptionGroup` resource creates or updates an option group, to enable and configure features that are specific to a particular DB engine.

## Syntax
<a name="aws-resource-rds-optiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-optiongroup-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::OptionGroup",
  "Properties" : {
      "[EngineName](#cfn-rds-optiongroup-enginename)" : {{String}},
      "[MajorEngineVersion](#cfn-rds-optiongroup-majorengineversion)" : {{String}},
      "[OptionConfigurations](#cfn-rds-optiongroup-optionconfigurations)" : {{[ OptionConfiguration, ... ]}},
      "[OptionGroupDescription](#cfn-rds-optiongroup-optiongroupdescription)" : {{String}},
      "[OptionGroupName](#cfn-rds-optiongroup-optiongroupname)" : {{String}},
      "[Tags](#cfn-rds-optiongroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-optiongroup-syntax.yaml"></a>

```
Type: AWS::RDS::OptionGroup
Properties:
  [EngineName](#cfn-rds-optiongroup-enginename): {{String}}
  [MajorEngineVersion](#cfn-rds-optiongroup-majorengineversion): {{String}}
  [OptionConfigurations](#cfn-rds-optiongroup-optionconfigurations): {{
    - OptionConfiguration}}
  [OptionGroupDescription](#cfn-rds-optiongroup-optiongroupdescription): {{String}}
  [OptionGroupName](#cfn-rds-optiongroup-optiongroupname): {{String}}
  [Tags](#cfn-rds-optiongroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-optiongroup-properties"></a>

`EngineName`  <a name="cfn-rds-optiongroup-enginename"></a>
Specifies the name of the engine that this option group should be associated with.
Valid Values:
+  `mariadb`
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

`MajorEngineVersion`  <a name="cfn-rds-optiongroup-majorengineversion"></a>
Specifies the major version of the engine that this option group should be associated with.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptionConfigurations`  <a name="cfn-rds-optiongroup-optionconfigurations"></a>
A list of all available options for an option group.
*Required*: Conditional
*Type*: Array of [OptionConfiguration](aws-properties-rds-optiongroup-optionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptionGroupDescription`  <a name="cfn-rds-optiongroup-optiongroupdescription"></a>
The description of the option group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptionGroupName`  <a name="cfn-rds-optiongroup-optiongroupname"></a>
The name of the option group to be created.
Constraints:
+ Must be 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `myoptiongroup`
If you don't specify a value for `OptionGroupName` property, a name is automatically created for the option group.
This value is stored as a lowercase string.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-optiongroup-tags"></a>
Tags to assign to the option group.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-optiongroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-optiongroup-return-values"></a>

### Ref
<a name="aws-resource-rds-optiongroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the option group.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-rds-optiongroup--examples"></a>

**Topics**
+ [Create an option group with multiple option configurations](#aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_configurations)
+ [Create an option group with multiple option settings](#aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_settings)
+ [Microsoft SQL Server native backup and restore option](#aws-resource-rds-optiongroup--examples--Microsoft_SQL_Server_native_backup_and_restore_option)

### Create an option group with multiple option configurations
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_configurations"></a>

The following example creates an option group with two option configurations (`OEM` and `APEX`). For more information about these options, see [Adding options to Oracle DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_configurations--json"></a>

```
{
    "OracleOptionGroup": {
        "Type": "AWS::RDS::OptionGroup",
        "Properties": {
            "EngineName": "oracle-ee",
            "MajorEngineVersion": "12.1",
            "OptionGroupDescription": "A test option group",
            "OptionConfigurations": [
                {
                    "OptionName": "OEM",
                    "DBSecurityGroupMemberships": [
                        "default"
                    ],
                    "Port": "5500"
                },
                {
                    "OptionName": "APEX"
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_configurations--yaml"></a>

```
---
OracleOptionGroup:
  Type: AWS::RDS::OptionGroup
  Properties:
    EngineName: oracle-ee
    MajorEngineVersion: "12.1"
    OptionConfigurations:
      -
        DBSecurityGroupMemberships:
          - default
        OptionName: OEM
        Port: "5500"
      -
        OptionName: APEX
    OptionGroupDescription: A test option group
```

### Create an option group with multiple option settings
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_settings"></a>

The following example creates an option group that specifies two option settings for the `MEMCACHED` option. For more information about this option, see [ MySQL memcached support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.memcached.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_settings--json"></a>

```
{
    "SQLOptionGroup": {
        "Type": "AWS::RDS::OptionGroup",
        "Properties": {
            "EngineName": "mysql",
            "MajorEngineVersion": "8.0",
            "OptionGroupDescription": "A test option group",
            "OptionConfigurations": [
                {
                    "OptionName": "MEMCACHED",
                    "VpcSecurityGroupMemberships": [
                        "sg-a1238db7"
                    ],
                    "Port": "1234",
                    "OptionSettings": [
                        {
                            "Name": "CHUNK_SIZE",
                            "Value": "32"
                        },
                        {
                            "Name": "BINDING_PROTOCOL",
                            "Value": "ascii"
                        }
                    ]
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-optiongroup--examples--Create_an_option_group_with_multiple_option_settings--yaml"></a>

```
---
SQLOptionGroup:
  Properties:
    EngineName: mysql
    MajorEngineVersion: "8.0"
    OptionConfigurations:
      -
        OptionName: MEMCACHED
        OptionSettings:
          -
            Name: CHUNK_SIZE
            Value: "32"
          -
            Name: BINDING_PROTOCOL
            Value: ascii
        Port: "1234"
        VpcSecurityGroupMemberships:
          - sg-a1238db7
    OptionGroupDescription: "A test option group"
  Type: AWS::RDS::OptionGroup
```

### Microsoft SQL Server native backup and restore option
<a name="aws-resource-rds-optiongroup--examples--Microsoft_SQL_Server_native_backup_and_restore_option"></a>

The following example creates an option group that specifies the Microsoft SQL Server native backup and restore option. For more information about this option, see [ Support for Native Backup and Restore in SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.BackupRestore.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-optiongroup--examples--Microsoft_SQL_Server_native_backup_and_restore_option--json"></a>

```
{
    "myOptionGroup": {
        "Type": "AWS::RDS::OptionGroup",
        "Properties": {
            "EngineName": "sqlserver-se",
            "MajorEngineVersion": "12.00",
            "OptionGroupDescription": "SQL Server Native Backup and Restore",
            "OptionConfigurations": [
                {
                    "OptionName": "SQLSERVER_BACKUP_RESTORE",
                    "OptionSettings": [
                        {
                            "Name": "IAM_ROLE_ARN",
                            "Value": "arn:aws:iam::333333333333333:role/service-role/sqlserverrestore"
                        }
                    ]
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-optiongroup--examples--Microsoft_SQL_Server_native_backup_and_restore_option--yaml"></a>

```
---
myOptionGroup:
  Type: 'AWS::RDS::OptionGroup'
  Properties:
    EngineName: sqlserver-se
    MajorEngineVersion: '12.00'
    OptionGroupDescription: SQL Server Native Backup and Restore
    OptionConfigurations:
      - OptionName: SQLSERVER_BACKUP_RESTORE
        OptionSettings:
          - Name: IAM_ROLE_ARN
            Value: 'arn:aws:iam::333333333333333:role/service-role/sqlserverrestore'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
