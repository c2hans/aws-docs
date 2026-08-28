---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-globalcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::GlobalCluster
<a name="aws-resource-rds-globalcluster"></a>

The `AWS::RDS::GlobalCluster` resource creates or updates an Amazon Aurora global database spread across multiple AWS Regions.

The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.

You can create a global database that is initially empty, and then add a primary cluster and a secondary cluster to it.

For information about Aurora global databases, see [ Working with Amazon Aurora Global Databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-resource-rds-globalcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-globalcluster-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::GlobalCluster",
  "Properties" : {
      "[DeletionProtection](#cfn-rds-globalcluster-deletionprotection)" : {{Boolean}},
      "[Engine](#cfn-rds-globalcluster-engine)" : {{String}},
      "[EngineLifecycleSupport](#cfn-rds-globalcluster-enginelifecyclesupport)" : {{String}},
      "[EngineVersion](#cfn-rds-globalcluster-engineversion)" : {{String}},
      "[GlobalClusterIdentifier](#cfn-rds-globalcluster-globalclusteridentifier)" : {{String}},
      "[SourceDBClusterIdentifier](#cfn-rds-globalcluster-sourcedbclusteridentifier)" : {{String}},
      "[StorageEncrypted](#cfn-rds-globalcluster-storageencrypted)" : {{Boolean}},
      "[Tags](#cfn-rds-globalcluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-globalcluster-syntax.yaml"></a>

```
Type: AWS::RDS::GlobalCluster
Properties:
  [DeletionProtection](#cfn-rds-globalcluster-deletionprotection): {{Boolean}}
  [Engine](#cfn-rds-globalcluster-engine): {{String}}
  [EngineLifecycleSupport](#cfn-rds-globalcluster-enginelifecyclesupport): {{String}}
  [EngineVersion](#cfn-rds-globalcluster-engineversion): {{String}}
  [GlobalClusterIdentifier](#cfn-rds-globalcluster-globalclusteridentifier): {{String}}
  [SourceDBClusterIdentifier](#cfn-rds-globalcluster-sourcedbclusteridentifier): {{String}}
  [StorageEncrypted](#cfn-rds-globalcluster-storageencrypted): {{Boolean}}
  [Tags](#cfn-rds-globalcluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-globalcluster-properties"></a>

`DeletionProtection`  <a name="cfn-rds-globalcluster-deletionprotection"></a>
Specifies whether to enable deletion protection for the new global database cluster. The global database can't be deleted when deletion protection is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-rds-globalcluster-engine"></a>
The database engine to use for this global database cluster.
Valid Values: `aurora-mysql | aurora-postgresql`
Constraints:
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the engine of the source DB cluster.
*Required*: Conditional
*Type*: String
*Allowed values*: `aurora | aurora-mysql | aurora-postgresql`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineLifecycleSupport`  <a name="cfn-rds-globalcluster-enginelifecyclesupport"></a>
The lifecycle type for this global database cluster.
By default, this value is set to `open-source-rds-extended-support`, which enrolls your global cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, creating the global cluster will fail if the DB major version is past its end of standard support date.
This setting only applies to Aurora PostgreSQL-based global databases.
You can use this setting to enroll your global cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your global cluster past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide*.
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`
Default: `open-source-rds-extended-support`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EngineVersion`  <a name="cfn-rds-globalcluster-engineversion"></a>
The engine version to use for this global database cluster.
Constraints:
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the engine version of the source DB cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-rds-globalcluster-globalclusteridentifier"></a>
The cluster identifier for this global database cluster. This parameter is stored as a lowercase string.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDBClusterIdentifier`  <a name="cfn-rds-globalcluster-sourcedbclusteridentifier"></a>
The Amazon Resource Name (ARN) to use as the primary cluster of the global database.
If you provide a value for this parameter, don't specify values for the following settings because Amazon Aurora uses the values from the specified source DB cluster:
+  `DatabaseName`
+  `Engine`
+  `EngineVersion`
+  `StorageEncrypted`
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageEncrypted`  <a name="cfn-rds-globalcluster-storageencrypted"></a>
Specifies whether to enable storage encryption for the new global database cluster.
Constraints:
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the setting from the source DB cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-globalcluster-tags"></a>
Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-globalcluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-globalcluster-return-values"></a>

### Ref
<a name="aws-resource-rds-globalcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the global database cluster.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-globalcluster-return-values-fn--getatt"></a>

## Examples
<a name="aws-resource-rds-globalcluster--examples"></a>

**Topics**
+ [Creating a Global Database cluster for Aurora MySQL](#aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_MySQL)
+ [Creating a Global Database cluster for Aurora PostgreSQL](#aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_PostgreSQL)
+ [Adding a Region to an Aurora database cluster](#aws-resource-rds-globalcluster--examples--Adding_a_Region_to_an_Aurora_database_cluster)
+ [Adding a DB cluster to a Global Database cluster](#aws-resource-rds-globalcluster--examples--Adding_a_DB_cluster_to_a_Global_Database_cluster)

### Creating a Global Database cluster for Aurora MySQL
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_MySQL"></a>

The following example creates a global database cluster with an Aurora MySQL DB cluster and DB instance.

#### JSON
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_MySQL--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "GlobalClusterIdentifier": {
          "Type": "String",
          "Description": "Identifier used for global database cluster",
          "AllowedPattern": "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$"
        },
        "username": {
            "NoEcho": "true",
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "password": {
            "NoEcho": "true",
            "Description": "Password for MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "GlobalCluster": {
            "Type": "AWS::RDS::GlobalCluster",
            "Properties": {
                "GlobalClusterIdentifier": {
                    "Ref": "GlobalClusterIdentifier"
                },
                "SourceDBClusterIdentifier": {
                    "Ref": "RDSCluster"
                }
            }
        },
        "RDSCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "MasterUsername": {
                    "Ref": "username"
                },
                "MasterUserPassword": {
                    "Ref": "password"
                },
                "DBClusterParameterGroupName": "default.aurora-mysql5.7",
                "Engine": "aurora-mysql"
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "Engine": "aurora-mysql",
                "DBClusterIdentifier": {
                    "Ref": "RDSCluster"
                },
                "DBParameterGroupName": "default.aurora-mysql5.7",
                "PubliclyAccessible": "true",
                "DBInstanceClass": "db.r5.xlarge"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_MySQL--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  GlobalClusterIdentifier:
    Type: String
    Description: Identifier used for global database cluster
    AllowedPattern: '^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$'
  username:
    NoEcho: 'true'
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  password:
    NoEcho: 'true'
    Description: Password for MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  GlobalCluster:
    Type: 'AWS::RDS::GlobalCluster'
    Properties:
      GlobalClusterIdentifier: !Ref GlobalClusterIdentifier
      SourceDBClusterIdentifier: !Ref RDSCluster
  RDSCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      MasterUsername: !Ref username
      MasterUserPassword: !Ref password
      DBClusterParameterGroupName: default.aurora-mysql5.7
      Engine: aurora-mysql
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      Engine: aurora-mysql
      DBClusterIdentifier: !Ref RDSCluster
      DBParameterGroupName: default.aurora-mysql5.7
      PubliclyAccessible: 'true'
      DBInstanceClass: db.r5.xlarge
```

### Creating a Global Database cluster for Aurora PostgreSQL
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_PostgreSQL"></a>

The following example creates a global database cluster with an Aurora PostgreSQL DB cluster and DB instance.

#### JSON
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_PostgreSQL--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "GlobalClusterIdentifier": {
          "Type": "String",
          "Description": "Identifier used for global database cluster",
          "AllowedPattern": "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$"
        },
        "username": {
            "NoEcho": "true",
            "Description": "Username for PostgreSQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "password": {
            "NoEcho": "true",
            "Description": "Password for PostgreSQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "GlobalCluster": {
            "Type": "AWS::RDS::GlobalCluster",
            "Properties": {
                "GlobalClusterIdentifier": {
                    "Ref": "GlobalClusterIdentifier"
                },
                "SourceDBClusterIdentifier": {
                    "Ref": "RDSCluster"
                }
            }
        },
        "RDSCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "MasterUsername": {
                    "Ref": "username"
                },
                "MasterUserPassword": {
                    "Ref": "password"
                },
                "DBClusterParameterGroupName": "default.aurora-postgresql11",
                "Engine": "aurora-postgresql"
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "Engine": "aurora-postgresql",
                "DBClusterIdentifier": {
                    "Ref": "RDSCluster"
                },
                "DBParameterGroupName": "default.aurora-postgresql11",
                "PubliclyAccessible": "true",
                "DBInstanceClass": "db.r5.xlarge"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-globalcluster--examples--Creating_a_Global_Database_cluster_for_Aurora_PostgreSQL--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  GlobalClusterIdentifier:
    Type: String
    Description: Identifier used for global database cluster
    AllowedPattern: '^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$'
  username:
    NoEcho: 'true'
    Description: Username for PostgreSQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  password:
    NoEcho: 'true'
    Description: Password for PostgreSQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  GlobalCluster:
    Type: 'AWS::RDS::GlobalCluster'
    Properties:
      GlobalClusterIdentifier: !Ref GlobalClusterIdentifier
      SourceDBClusterIdentifier: !Ref RDSCluster
  RDSCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      MasterUsername: !Ref username
      MasterUserPassword: !Ref password
      DBClusterParameterGroupName: default.aurora-postgresql11
      Engine: aurora-postgresql
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      Engine: aurora-postgresql
      DBClusterIdentifier: !Ref RDSCluster
      DBParameterGroupName: default.aurora-postgresql11
      PubliclyAccessible: 'true'
      DBInstanceClass: db.r5.xlarge
```

### Adding a Region to an Aurora database cluster
<a name="aws-resource-rds-globalcluster--examples--Adding_a_Region_to_an_Aurora_database_cluster"></a>

The following example creates a new Aurora DB cluster, attaches it to a global database cluster as a read-only secondary cluster, and then adds a DB instance to the new DB cluster.

Specify the `GlobalClusterIdentifier` of a global database cluster with the primary DB cluster in a separate AWS Region.

#### JSON
<a name="aws-resource-rds-globalcluster--examples--Adding_a_Region_to_an_Aurora_database_cluster--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "GlobalClusterIdentifier": {
          "Type": "String",
          "Description": "Identifier used for global database cluster",
          "AllowedPattern": "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$"
        }
    },
    "Resources": {
        "RDSCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "GlobalClusterIdentifier": {
                    "Ref": "GlobalClusterIdentifier"
                },
                "DBClusterParameterGroupName": "default.aurora-mysql5.7",
                "Engine": "aurora-mysql"
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "Engine": "aurora-mysql",
                "DBClusterIdentifier": {
                    "Ref": "RDSCluster"
                },
                "DBParameterGroupName": "default.aurora-mysql5.7",
                "PubliclyAccessible": "true",
                "DBInstanceClass": "db.r5.xlarge"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-globalcluster--examples--Adding_a_Region_to_an_Aurora_database_cluster--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  GlobalClusterIdentifier:
    Type: String
    Description: Identifier used for global database cluster
    AllowedPattern: '^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$'
Resources:
  RDSCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      GlobalClusterIdentifier: !Ref GlobalClusterIdentifier
      DBClusterParameterGroupName: default.aurora-mysql5.7
      Engine: aurora-mysql
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      Engine: aurora-mysql
      DBClusterIdentifier: !Ref RDSCluster
      DBParameterGroupName: default.aurora-mysql5.7
      PubliclyAccessible: 'true'
      DBInstanceClass: db.r5.xlarge
```

### Adding a DB cluster to a Global Database cluster
<a name="aws-resource-rds-globalcluster--examples--Adding_a_DB_cluster_to_a_Global_Database_cluster"></a>

The following example adds a DB cluster to a global database cluster.

The example includes the template that was used to create the DB cluster. After the DB cluster created by the first template exists, the second template in the example adds the DB cluster to a global database cluster.

#### JSON
<a name="aws-resource-rds-globalcluster--examples--Adding_a_DB_cluster_to_a_Global_Database_cluster--json"></a>

```
The following template was used to create DB cluster that you want to add to the global database cluster.
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "username": {
            "NoEcho": "true",
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
         },
         "password": {
             "NoEcho": "true",
             "Description": "Password MySQL database access",
             "Type": "String",
             "MinLength": "8",
             "MaxLength": "41",
             "AllowedPattern": "[a-zA-Z0-9]*",
             "ConstraintDescription": "must contain only alphanumeric characters."
         }
    },
    "Resources": {
        "RDSCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "MasterUsername": {
                    "Ref": "username"
                },
                "MasterUserPassword": {
                    "Ref": "password"
                },
                "DBClusterParameterGroupName": "default.aurora-mysql8.0",
                "Engine": "aurora-mysql",
                "EngineVersion": "8.0.mysql_aurora.8.0.30"
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
                "Properties": {
                    "Engine": "aurora-mysql",
                    "DBClusterIdentifier": {
                        "Ref": "RDSCluster"
                },
                "DBParameterGroupName": "default.aurora-mysql8.0",
                "PubliclyAccessible": "true",
                "DBInstanceClass": "db.r5.xlarge"
            }
        }
    }
}

The following template adds the DB cluster created by the previous template to a global database cluster.
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "GlobalClusterIdentifier": {
            "Description": "Global cluster identifier",
            "Type": "String"
        },
        "username": {
            "NoEcho": "true",
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "password": {
            "NoEcho": "true",
            "Description": "Password MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "GlobalCluster": {
            "Type": "AWS::RDS::GlobalCluster",
            "Properties": {
                "GlobalClusterIdentifier": {
                    "Ref": "GlobalClusterIdentifier"
                },
                "SourceDBClusterIdentifier": {
                    "Ref": "RDSCluster"
                }
            }
        },
        "RDSCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "MasterUsername": {
                    "Ref": "username"
                },
                "MasterUserPassword": {
                    "Ref": "password"
                },
                "DBClusterParameterGroupName": "default.aurora-mysql8.0",
                "Engine": "aurora-mysql",
                "EngineVersion": "8.0.mysql_aurora.8.0.30"
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "Engine": "aurora-mysql",
                "DBClusterIdentifier": {
                    "Ref": "RDSCluster"
                },
                "DBParameterGroupName": "default.aurora-mysql8.0",
                "PubliclyAccessible": "true",
                "DBInstanceClass": "db.r5.xlarge"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-globalcluster--examples--Adding_a_DB_cluster_to_a_Global_Database_cluster--yaml"></a>

```
The following template created the DB cluster that you want to add to the global database cluster.
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  username:
    NoEcho: 'true'
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  password:
    NoEcho: 'true'
    Description: Password MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  RDSCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      MasterUsername: !Ref username
      MasterUserPassword: !Ref password
      DBClusterParameterGroupName: default.aurora-mysql8.0
      Engine: aurora-mysql
      EngineVersion: 8.0.mysql_aurora.8.0.30
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      Engine: aurora-mysql
      DBClusterIdentifier: !Ref RDSCluster
      DBParameterGroupName: default.aurora-mysql8.0
      PubliclyAccessible: 'true'
      DBInstanceClass: db.r5.xlarge

The following template adds the DB cluster created by the previous template to a global database cluster.
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  GlobalClusterIdentifier:
    Description: Global cluster identifier
    Type: String
  username:
    NoEcho: 'true'
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  password:
    NoEcho: 'true'
    Description: Password MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  GlobalCluster:
    Type: 'AWS::RDS::GlobalCluster'
    Properties:
      GlobalClusterIdentifier: !Ref GlobalClusterIdentifier
      SourceDBClusterIdentifier: !Ref RDSCluster
  RDSCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      MasterUsername: !Ref username
      MasterUserPassword: !Ref password
      DBClusterParameterGroupName: default.aurora-mysql8.0
      Engine: aurora-mysql
      EngineVersion: 8.0.mysql_aurora.8.0.30
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      Engine: aurora-mysql
      DBClusterIdentifier: !Ref RDSCluster
      DBParameterGroupName: default.aurora-mysql8.0
      PubliclyAccessible: 'true'
      DBInstanceClass: db.r5.xlarge
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
