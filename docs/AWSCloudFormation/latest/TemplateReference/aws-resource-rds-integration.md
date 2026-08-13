---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::Integration
<a name="aws-resource-rds-integration"></a>

A zero-ETL integration with Amazon Redshift.

## Syntax
<a name="aws-resource-rds-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-integration-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::Integration",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-rds-integration-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[DataFilter](#cfn-rds-integration-datafilter)" : {{String}},
      "[Description](#cfn-rds-integration-description)" : {{String}},
      "[IntegrationName](#cfn-rds-integration-integrationname)" : {{String}},
      "[KMSKeyId](#cfn-rds-integration-kmskeyid)" : {{String}},
      "[SourceArn](#cfn-rds-integration-sourcearn)" : {{String}},
      "[Tags](#cfn-rds-integration-tags)" : {{[ Tag, ... ]}},
      "[TargetArn](#cfn-rds-integration-targetarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-rds-integration-syntax.yaml"></a>

```
Type: AWS::RDS::Integration
Properties:
  [AdditionalEncryptionContext](#cfn-rds-integration-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [DataFilter](#cfn-rds-integration-datafilter): {{String}}
  [Description](#cfn-rds-integration-description): {{String}}
  [IntegrationName](#cfn-rds-integration-integrationname): {{String}}
  [KMSKeyId](#cfn-rds-integration-kmskeyid): {{String}}
  [SourceArn](#cfn-rds-integration-sourcearn): {{String}}
  [Tags](#cfn-rds-integration-tags): {{
    - Tag}}
  [TargetArn](#cfn-rds-integration-targetarn): {{String}}
```

## Properties
<a name="aws-resource-rds-integration-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-rds-integration-additionalencryptioncontext"></a>
An optional set of non-secret key–value pairs that contains additional contextual information about the data. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *AWS Key Management Service Developer Guide*.
You can only include this parameter if you specify the `KMSKeyId` parameter.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataFilter`  <a name="cfn-rds-integration-datafilter"></a>
Data filters for the integration. These filters determine which tables from the source database are sent to the target Amazon Redshift data warehouse.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_ "\\\-$,*.:?+\/]*`
*Minimum*: `1`
*Maximum*: `25600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-rds-integration-description"></a>
A description of the integration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationName`  <a name="cfn-rds-integration-integrationname"></a>
The name of the integration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSKeyId`  <a name="cfn-rds-integration-kmskeyid"></a>
The AWS Key Management System (AWS KMS) key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, RDS uses a default AWS owned key.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceArn`  <a name="cfn-rds-integration-sourcearn"></a>
The Amazon Resource Name (ARN) of the database to use as the source for replication.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:rds(-[a-z]*)?:[a-z0-9\-]*:[0-9]*:(cluster|db):[a-z][a-z0-9]*(-[a-z0-9]+)*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-integration-tags"></a>
An optional array of key-value pairs to apply to this integration.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-integration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-rds-integration-targetarn"></a>
The ARN of the Redshift data warehouse to use as the target for replication.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-integration-return-values"></a>

### Ref
<a name="aws-resource-rds-integration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the integration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-integration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rds-integration-return-values-fn--getatt-fn--getatt"></a>

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time when the integration was created, in Universal Coordinated Time (UTC).

`IntegrationArn`  <a name="IntegrationArn-fn::getatt"></a>
The ARN of the integration.

## Examples
<a name="aws-resource-rds-integration--examples"></a>

**Topics**
+ [Create an Aurora zero-ETL integration using an AWS owned KMS key](#aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_an_owned_KMS_key)
+ [Create an Aurora zero-ETL integration using a customer managed KMS key](#aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_a_customer_managed_KMS_key)
+ [Create an RDS zero-ETL integration using an AWS owned KMS key](#aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_an_owned_KMS_key)
+ [Create an RDS zero-ETL integration using a customer managed KMS key](#aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_a_customer_managed_KMS_key)

### Create an Aurora zero-ETL integration using an AWS owned KMS key
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_an_owned_KMS_key"></a>

The following example creates an Amazon Aurora MySQL DB cluster, Redshift provisioned cluster, and a zero-ETL integration between the two clusters encrypted with an AWS owned KMS key. For more information, see [Working with Aurora zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) in the *Amazon Aurora User Guide*.

#### JSON
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_an_owned_KMS_key--json"></a>

```
{
    "Parameters": {
        "Username": {
            "Description": "Username for Aurora MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "bevelvoerder",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "Password": {
            "NoEcho": "true",
            "Description": "Password for Aurora MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Passw0rd",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        },
        "RSUsername": {
            "Description": "Username for Redshift cluster access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "bevelvoerder",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "RSPassword": {
            "NoEcho": "true",
            "Description": "Password for Redshift cluster access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Passw0rd",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "RDSDBClusterParameterGroup": {
            "Type": "AWS::RDS::DBClusterParameterGroup",
            "Properties": {
                "Description": "Enables enhanced binlog",
                "Family": "aurora-mysql8.0",
                "Parameters": {
                    "aurora_enhanced_binlog": "1",
                    "binlog_format": "ROW",
                    "binlog_backup": "0",
                    "binlog_replication_globaldb": "0",
                    "binlog_row_metadata": "full",
                    "binlog_row_image": "full"
                }
            }
        },
        "RDSDBCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "DBClusterParameterGroupName": {
                    "Ref": "RDSDBClusterParameterGroup"
                },
                "Engine": "aurora-mysql",
                "EngineVersion": "8.0.mysql_aurora.3.05.1",
                "MasterUsername": {
                    "Ref": "Username"
                },
                "MasterUserPassword": {
                    "Ref": "Password"
                }
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBClusterIdentifier": {
                    "Ref": "RDSDBCluster"
                },
                "DBInstanceClass": "db.r5.large",
                "Engine": "aurora-mysql",
                "PubliclyAccessible": true
            }
        },
        "RSClusterParameterGroup": {
            "Type": "AWS::Redshift::ClusterParameterGroup",
            "Properties": {
                "Description": "Enables case sensitivity",
                "ParameterGroupFamily": "redshift-1.0",
                "Parameters": [
                    {
                        "ParameterName": "enable_case_sensitive_identifier",
                        "ParameterValue": "true"
                    }
                ]
            }
        },
        "RSCluster": {
            "Type": "AWS::Redshift::Cluster",
            "Properties": {
                "ClusterParameterGroupName": {
                    "Ref": "RSClusterParameterGroup"
                },
                "ClusterType": "multi-node",
                "DBName": "dev",
                "Encrypted": true,
                "MasterUsername": {
                    "Ref": "RSUsername"
                },
                "MasterUserPassword": {
                    "Ref": "RSPassword"
                },
                "NodeType": "ra3.xlplus",
                "NumberOfNodes": 2,
                "NamespaceResourcePolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "redshift:AuthorizeInboundIntegration",
                            "Condition": {
                                "StringEquals": {
                                    "aws:SourceArn": {
                                        "Fn::GetAtt": [
                                            "RDSDBCluster",
                                            "DBClusterArn"
                                        ]
                                    }
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "redshift:CreateInboundIntegration"
                        }
                    ]
                }
            }
        },
        "Integration": {
            "Type": "AWS::RDS::Integration",
            "Properties": {
                "SourceArn": {
                    "Fn::GetAtt": [
                        "RDSDBCluster",
                        "DBClusterArn"
                    ]
                },
                "TargetArn": {
                    "Fn::GetAtt": [
                        "RSCluster",
                        "ClusterNamespaceArn"
                    ]
                }
            }
        }
    },
    "Outputs": {
        "IntegrationARN": {
            "Description": "Integration ARN",
            "Value": {
                "Ref": "Integration"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_an_owned_KMS_key--yaml"></a>

```
Parameters:
  Username:
    Description: Username for Aurora MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: "bevelvoerder"
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  Password:
    NoEcho: 'true'
    Description: Password for Aurora MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: "Passw0rd"
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
  RSUsername:
    Description: Username for Redshift cluster access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: "bevelvoerder"
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  RSPassword:
    NoEcho: 'true'
    Description: Password for Redshift cluster access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: "Passw0rd"
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  RDSDBClusterParameterGroup:
    Type: 'AWS::RDS::DBClusterParameterGroup'
    Properties:
      Description: Enables enhanced binlog
      Family: aurora-mysql8.0
      Parameters:
        aurora_enhanced_binlog: '1'
        binlog_format: ROW
        binlog_backup: '0'
        binlog_replication_globaldb: '0'
        binlog_row_metadata: full
        binlog_row_image: full
  RDSDBCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      DBClusterParameterGroupName: !Ref RDSDBClusterParameterGroup
      Engine: aurora-mysql
      EngineVersion: 8.0.mysql_aurora.3.05.1
      MasterUsername: !Ref Username
      MasterUserPassword: !Ref Password
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      DBClusterIdentifier: !Ref RDSDBCluster
      DBInstanceClass: db.r5.large
      Engine: aurora-mysql
      PubliclyAccessible: true
  RSClusterParameterGroup:
    Type: 'AWS::Redshift::ClusterParameterGroup'
    Properties:
      Description: Enables case sensitivity
      ParameterGroupFamily: redshift-1.0
      Parameters:
        - ParameterName: enable_case_sensitive_identifier
          ParameterValue: 'true'
  RSCluster:
    Type: 'AWS::Redshift::Cluster'
    Properties:
      ClusterParameterGroupName: !Ref RSClusterParameterGroup
      ClusterType: multi-node
      DBName: dev
      Encrypted: true
      MasterUsername: !Ref RSUsername
      MasterUserPassword: !Ref RSPassword
      NodeType: ra3.xlplus
      NumberOfNodes: 2
      NamespaceResourcePolicy:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: redshift:AuthorizeInboundIntegration
            Condition:
              StringEquals:
                aws:SourceArn: !GetAtt RDSDBCluster.DBClusterArn
          - Effect: Allow
            Principal:
              AWS: !Join [":", ["arn", !Ref AWS::Partition, "iam", "", !Ref AWS::AccountId, "root"]]
            Action: redshift:CreateInboundIntegration
  Integration:
    Type: 'AWS::RDS::Integration'
    Properties:
      SourceArn: !GetAtt RDSDBCluster.DBClusterArn
      TargetArn: !GetAtt RSCluster.ClusterNamespaceArn
Outputs:
  IntegrationARN:
    Description: Integration ARN
    Value: !Ref Integration
```

### Create an Aurora zero-ETL integration using a customer managed KMS key
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_a_customer_managed_KMS_key"></a>

The following example creates an Amazon Aurora MySQL DB cluster, Redshift provisioned cluster, and a zero-ETL integration between the two clusters encrypted with a customer managed KMS key. For more information, see [Working with Aurora zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) in the *Amazon Aurora User Guide*.

#### JSON
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_a_customer_managed_KMS_key--json"></a>

```
{
    "Parameters": {
        "Username": {
            "Description": "Username for Aurora MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "bevelvoerder",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "Password": {
            "NoEcho": "true",
            "Description": "Password for Aurora MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Passw0rd",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        },
        "RSUsername": {
            "Description": "Username for Redshift cluster access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "bevelvoerder",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "RSPassword": {
            "NoEcho": "true",
            "Description": "Password for Redshift cluster access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Passw0rd",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "kmsKey": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "Description": "Key used to encrypt the zero-ETL integration.",
                "KeyPolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Sid": "statement1",
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "kms:CreateGrant",
                            "Resource": "*"
                        },
                        {
                            "Sid": "statement2",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "kms:*",
                            "Resource": "*"
                        }
                    ]
                }
            }
        },
        "RDSDBClusterParameterGroup": {
            "Type": "AWS::RDS::DBClusterParameterGroup",
            "Properties": {
                "Description": "Enables enhanced binlog",
                "Family": "aurora-mysql8.0",
                "Parameters": {
                    "aurora_enhanced_binlog": "1",
                    "binlog_format": "ROW",
                    "binlog_backup": "0",
                    "binlog_replication_globaldb": "0",
                    "binlog_row_metadata": "full",
                    "binlog_row_image": "full"
                }
            }
        },
        "RDSDBCluster": {
            "Type": "AWS::RDS::DBCluster",
            "Properties": {
                "DBClusterParameterGroupName": {
                    "Ref": "RDSDBClusterParameterGroup"
                },
                "Engine": "aurora-mysql",
                "EngineVersion": "8.0.mysql_aurora.3.05.1",
                "MasterUsername": {
                    "Ref": "Username"
                },
                "MasterUserPassword": {
                    "Ref": "Password"
                }
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBClusterIdentifier": {
                    "Ref": "RDSDBCluster"
                },
                "DBInstanceClass": "db.r5.large",
                "Engine": "aurora-mysql",
                "PubliclyAccessible": true
            }
        },
        "RSClusterParameterGroup": {
            "Type": "AWS::Redshift::ClusterParameterGroup",
            "Properties": {
                "Description": "Enables case sensitivity",
                "ParameterGroupFamily": "redshift-1.0",
                "Parameters": [
                    {
                        "ParameterName": "enable_case_sensitive_identifier",
                        "ParameterValue": "true"
                    }
                ]
            }
        },
        "RSCluster": {
            "Type": "AWS::Redshift::Cluster",
            "Properties": {
                "ClusterParameterGroupName": {
                    "Ref": "RSClusterParameterGroup"
                },
                "ClusterType": "multi-node",
                "DBName": "dev",
                "Encrypted": true,
                "MasterUsername": {
                    "Ref": "RSUsername"
                },
                "MasterUserPassword": {
                    "Ref": "RSPassword"
                },
                "NodeType": "ra3.xlplus",
                "NumberOfNodes": 2,
                "NamespaceResourcePolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "redshift:AuthorizeInboundIntegration",
                            "Condition": {
                                "StringEquals": {
                                    "aws:SourceArn": {
                                        "Fn::GetAtt": [
                                            "RDSDBCluster",
                                            "DBClusterArn"
                                        ]
                                    }
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "redshift:CreateInboundIntegration"
                        }
                    ]
                }
            }
        },
        "Integration": {
            "Type": "AWS::RDS::Integration",
            "Properties": {
                "SourceArn": {
                    "Fn::GetAtt": [
                        "RDSDBCluster",
                        "DBClusterArn"
                    ]
                },
                "TargetArn": {
                    "Fn::GetAtt": [
                        "RSCluster",
                        "ClusterNamespaceArn"
                    ]
                },
                "KMSKeyId": {
                    "Fn::GetAtt": [
                        "kmsKey",
                        "Arn"
                    ]
                },
                "AdditionalEncryptionContext": {
                    "custom-context-1": "custom-context-value-1",
                    "custom-context-2": "custom-context-value-2"
                }
            }
        }
    },
    "Outputs": {
        "IntegrationARN": {
            "Description": "Integration ARN",
            "Value": {
                "Ref": "Integration"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-integration--examples--Create_an_Aurora_zero-ETL_integration_using_a_customer_managed_KMS_key--yaml"></a>

```
Parameters:
  Username:
    Description: Username for Aurora MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: "bevelvoerder"
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  Password:
    NoEcho: 'true'
    Description: Password for Aurora MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: "Passw0rd"
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
  RSUsername:
    Description: Username for Redshift cluster access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: "bevelvoerder"
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  RSPassword:
    NoEcho: 'true'
    Description: Password for Redshift cluster access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: "Passw0rd"
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  kmsKey:
    Type: 'AWS::KMS::Key'
    Properties:
      Description: Key used to encrypt the zero-ETL integration.
      KeyPolicy:
        Version: 2012-10-17
        Statement:
          - Sid: statement1
            Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: "kms:CreateGrant"
            Resource: "*"
          - Sid: statement2
            Effect: Allow
            Principal:
              AWS: !Join [":", ["arn", !Ref AWS::Partition, "iam", "", !Ref AWS::AccountId, "root"]]
            Action: "kms:*"
            Resource: "*"
  RDSDBClusterParameterGroup:
    Type: 'AWS::RDS::DBClusterParameterGroup'
    Properties:
      Description: Enables enhanced binlog
      Family: aurora-mysql8.0
      Parameters:
        aurora_enhanced_binlog: '1'
        binlog_format: ROW
        binlog_backup: '0'
        binlog_replication_globaldb: '0'
        binlog_row_metadata: full
        binlog_row_image: full
  RDSDBCluster:
    Type: 'AWS::RDS::DBCluster'
    Properties:
      DBClusterParameterGroupName: !Ref RDSDBClusterParameterGroup
      Engine: aurora-mysql
      EngineVersion: 8.0.mysql_aurora.3.05.1
      MasterUsername: !Ref Username
      MasterUserPassword: !Ref Password
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      DBClusterIdentifier: !Ref RDSDBCluster
      DBInstanceClass: db.r5.large
      Engine: aurora-mysql
      PubliclyAccessible: true
  RSClusterParameterGroup:
    Type: 'AWS::Redshift::ClusterParameterGroup'
    Properties:
      Description: Enables case sensitivity
      ParameterGroupFamily: redshift-1.0
      Parameters:
        - ParameterName: enable_case_sensitive_identifier
          ParameterValue: 'true'
  RSCluster:
    Type: 'AWS::Redshift::Cluster'
    Properties:
      ClusterParameterGroupName: !Ref RSClusterParameterGroup
      ClusterType: multi-node
      DBName: dev
      Encrypted: true
      MasterUsername: !Ref RSUsername
      MasterUserPassword: !Ref RSPassword
      NodeType: ra3.xlplus
      NumberOfNodes: 2
      NamespaceResourcePolicy:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: redshift:AuthorizeInboundIntegration
            Condition:
              StringEquals:
                aws:SourceArn: !GetAtt RDSDBCluster.DBClusterArn
          - Effect: Allow
            Principal:
              AWS: !Join [":", ["arn", !Ref AWS::Partition, "iam", "", !Ref AWS::AccountId, "root"]]
            Action: redshift:CreateInboundIntegration
  Integration:
    Type: 'AWS::RDS::Integration'
    Properties:
      SourceArn: !GetAtt RDSDBCluster.DBClusterArn
      TargetArn: !GetAtt RSCluster.ClusterNamespaceArn
      KMSKeyId: !GetAtt kmsKey.Arn
      AdditionalEncryptionContext:
        custom-context-1: custom-context-value-1
        custom-context-2: custom-context-value-2
Outputs:
  IntegrationARN:
    Description: Integration ARN
    Value: !Ref Integration
```

### Create an RDS zero-ETL integration using an AWS owned KMS key
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_an_owned_KMS_key"></a>

The following example creates an Amazon RDS MySQL DB instance, Redshift provisioned cluster, and a zero-ETL integration between them encrypted with an AWS owned key. For more information, see [Working with RDS zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_an_owned_KMS_key--json"></a>

```
{
    "Parameters": {
        "Username": {
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "Password": {
            "NoEcho": "true",
            "Description": "Password for MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        },
        "RSUsername": {
            "Description": "Username for Redshift cluster access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "RSPassword": {
            "NoEcho": "true",
            "Description": "Password for Redshift cluster access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Sqladmin2024",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
        "RDSDBParameterGroup": {
            "Type": "AWS::RDS::DBParameterGroup",
            "Properties": {
            	"DBParameterGroupName": "zeroetl-mysql-parameter-group",
                "Description": "Enables enhanced binlog",
                "Family": "mysql8.0",
                "Parameters": {
                    "binlog_checksum": "NONE",
                    "binlog_format": "ROW",
                    "binlog_row_image": "FULL"
                }
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
            	"DBInstanceIdentifier": "zeroetl-mysql-source",
                "DBParameterGroupName": {
                    "Ref": "RDSDBParameterGroup"
                },
                "Engine": "mysql",
                "EngineVersion": "8.0.33",
                "MasterUsername": {
                    "Ref": "Username"
                },
                "MasterUserPassword": {
                    "Ref": "Password"
                },
                "DBInstanceClass": "db.r5.large",
                "BackupRetentionPeriod": 1,
                "StorageType": "gp2",
                "AllocatedStorage": "100"
            }
        },
        "RSClusterParameterGroup": {
            "Type": "AWS::Redshift::ClusterParameterGroup",
            "Properties": {
            	"ParameterGroupName": "zeroetl-redshift-cluster-parameter-group",
                "Description": "Enables case sensitivity",
                "ParameterGroupFamily": "redshift-1.0",
                "Parameters": [
                    {
                        "ParameterName": "enable_case_sensitive_identifier",
                        "ParameterValue": "true"
                    }
                ]
            }
        },
        "RSCluster": {
            "Type": "AWS::Redshift::Cluster",
            "Properties": {
            	"ClusterIdentifier": "zeroetl-redshift-cluster",
                "ClusterParameterGroupName": {
                    "Ref": "RSClusterParameterGroup"
                },
                "ClusterType": "multi-node",
                "DBName": "sqladmin",
                "MaintenanceTrackName": "PREVIEW_2023",
                "Encrypted": true,
                "MasterUsername": {
                    "Ref": "RSUsername"
                },
                "MasterUserPassword": {
                    "Ref": "RSPassword"
                },
                "NodeType": "ra3.xlplus",
                "NumberOfNodes": 2,
                "NamespaceResourcePolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "redshift:AuthorizeInboundIntegration",
                            "Condition": {
                                "StringEquals": {
                                    "aws:SourceArn": {
                                        "Fn::GetAtt": [
                                            "RDSDBInstance",
                                            "DBInstanceArn"
                                        ]
                                    }
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "redshift:CreateInboundIntegration"
                        }
                    ]
                }
            }
        },
        "Integration": {
            "Type": "AWS::RDS::Integration",
            "Properties": {
            	"IntegrationName": "zeroetl-integration-from-mysql-to-redshift",
                "SourceArn": {
                    "Fn::GetAtt": [
                        "RDSDBInstance",
                        "DBInstanceArn"
                    ]
                },
                "TargetArn": {
                    "Fn::GetAtt": [
                        "RSCluster",
                        "ClusterNamespaceArn"
                    ]
                }
            }
        }
    },
    "Outputs": {
    	"IntegrationCreateTime": {
    		"Description": "Integration Creation Time",
    		"Value": {
    			"Fn::GetAtt": [
    				"Integration",
    				"CreateTime"
    			]
    		}
    	},
        "IntegrationARN": {
            "Description": "Integration ARN",
            "Value": {
                "Ref": "Integration"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_an_owned_KMS_key--yaml"></a>

```
Parameters:
  Username:
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  Password:
    NoEcho: 'true'
    Description: Password for MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
  RSUsername:
    Description: Username for Redshift cluster access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  RSPassword:
    NoEcho: 'true'
    Description: Password for Redshift cluster access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: Sqladmin2024
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  RDSDBParameterGroup:
    Type: 'AWS::RDS::DBParameterGroup'
    Properties:
      DBParameterGroupName: zeroetl-mysql-parameter-group
      Description: Enables enhanced binlog
      Family: mysql8.0
      Parameters:
        binlog_checksum: NONE
        binlog_format: ROW
        binlog_row_image: FULL
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      DBInstanceIdentifier: zeroetl-mysql-source
      DBParameterGroupName: !Ref RDSDBParameterGroup
      Engine: mysql
      EngineVersion: 8.0.33
      MasterUsername: !Ref Username
      MasterUserPassword: !Ref Password
      DBInstanceClass: db.r5.large
      BackupRetentionPeriod: 1
      StorageType: gp2
      AllocatedStorage: '100'
  RSClusterParameterGroup:
    Type: 'AWS::Redshift::ClusterParameterGroup'
    Properties:
      ParameterGroupName: zeroetl-redshift-cluster-parameter-group
      Description: Enables case sensitivity
      ParameterGroupFamily: redshift-1.0
      Parameters:
        - ParameterName: enable_case_sensitive_identifier
          ParameterValue: 'true'
  RSCluster:
    Type: 'AWS::Redshift::Cluster'
    Properties:
      ClusterIdentifier: zeroetl-redshift-cluster
      ClusterParameterGroupName: !Ref RSClusterParameterGroup
      ClusterType: multi-node
      DBName: sqladmin
      MaintenanceTrackName: PREVIEW_2023
      Encrypted: true
      MasterUsername: !Ref RSUsername
      MasterUserPassword: !Ref RSPassword
      NodeType: ra3.xlplus
      NumberOfNodes: 2
      NamespaceResourcePolicy:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: 'redshift:AuthorizeInboundIntegration'
            Condition:
              StringEquals:
                'aws:SourceArn': !GetAtt
                  - RDSDBInstance
                  - DBInstanceArn
          - Effect: Allow
            Principal:
              AWS: !Join
                - ':'
                - - arn
                  - !Ref 'AWS::Partition'
                  - iam
                  - ''
                  - !Ref 'AWS::AccountId'
                  - root
            Action: 'redshift:CreateInboundIntegration'
  Integration:
    Type: 'AWS::RDS::Integration'
    Properties:
      IntegrationName: zeroetl-integration-from-mysql-to-redshift
      SourceArn: !GetAtt
        - RDSDBInstance
        - DBInstanceArn
      TargetArn: !GetAtt
        - RSCluster
        - ClusterNamespaceArn
Outputs:
  IntegrationCreateTime:
    Description: Integration Creation Time
    Value: !GetAtt
      - Integration
      - CreateTime
  IntegrationARN:
    Description: Integration ARN
    Value: !Ref Integration
```

### Create an RDS zero-ETL integration using a customer managed KMS key
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_a_customer_managed_KMS_key"></a>

The following example creates an Amazon RDS MySQL DB instance, Redshift provisioned cluster, and a zero-ETL integration between them encrypted with a customer managed KMS key. For more information, see [Working with RDS zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html) in the *Amazon RDS User Guide*.

#### JSON
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_a_customer_managed_KMS_key--json"></a>

```
{
    "Parameters": {
        "Username": {
            "Description": "Username for MySQL database access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "Password": {
            "NoEcho": "true",
            "Description": "Password for MySQL database access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        },
        "RSUsername": {
            "Description": "Username for Redshift cluster access",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "16",
            "Default": "sqladmin",
            "AllowedPattern": "[a-zA-Z][a-zA-Z0-9]*",
            "ConstraintDescription": "must begin with a letter and contain only alphanumeric characters."
        },
        "RSPassword": {
            "NoEcho": "true",
            "Description": "Password for Redshift cluster access",
            "Type": "String",
            "MinLength": "8",
            "MaxLength": "41",
            "Default": "Sqladmin2024",
            "AllowedPattern": "[a-zA-Z0-9]*",
            "ConstraintDescription": "must contain only alphanumeric characters."
        }
    },
    "Resources": {
    	"kmsKey": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "Description": "Key used to encrypt the zero-ETL integration.",
                "KeyPolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Sid": "statement1",
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "kms:CreateGrant",
                            "Resource": "*"
                        },
                        {
                            "Sid": "statement2",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "kms:*",
                            "Resource": "*"
                        }
                    ]
                }
            }
        },
        "RDSDBParameterGroup": {
            "Type": "AWS::RDS::DBParameterGroup",
            "Properties": {
            	"DBParameterGroupName": "zeroetl-mysql-parameter-group",
                "Description": "Enables enhanced binlog",
                "Family": "mysql8.0",
                "Parameters": {
                    "binlog_checksum": "NONE",
                    "binlog_format": "ROW",
                    "binlog_row_image": "FULL"
                }
            }
        },
        "RDSDBInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
            	"DBInstanceIdentifier": "zeroetl-mysql-source",
                "DBParameterGroupName": {
                    "Ref": "RDSDBParameterGroup"
                },
                "Engine": "mysql",
                "EngineVersion": "8.0.33",
                "MasterUsername": {
                    "Ref": "Username"
                },
                "MasterUserPassword": {
                    "Ref": "Password"
                },
                "DBInstanceClass": "db.r5.large",
                "BackupRetentionPeriod": 1,
                "StorageType": "gp2",
                "AllocatedStorage": "100"
            }
        },
        "RSClusterParameterGroup": {
            "Type": "AWS::Redshift::ClusterParameterGroup",
            "Properties": {
            	"ParameterGroupName": "zeroetl-redshift-cluster-parameter-group",
                "Description": "Enables case sensitivity",
                "ParameterGroupFamily": "redshift-1.0",
                "Parameters": [
                    {
                        "ParameterName": "enable_case_sensitive_identifier",
                        "ParameterValue": "true"
                    }
                ]
            }
        },
        "RSCluster": {
            "Type": "AWS::Redshift::Cluster",
            "Properties": {
            	"ClusterIdentifier": "zeroetl-redshift-cluster",
                "ClusterParameterGroupName": {
                    "Ref": "RSClusterParameterGroup"
                },
                "ClusterType": "multi-node",
                "DBName": "sqladmin",
                "MaintenanceTrackName": "PREVIEW_2023",
                "Encrypted": true,
                "MasterUsername": {
                    "Ref": "RSUsername"
                },
                "MasterUserPassword": {
                    "Ref": "RSPassword"
                },
                "NodeType": "ra3.xlplus",
                "NumberOfNodes": 2,
                "NamespaceResourcePolicy": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "redshift.amazonaws.com"
                            },
                            "Action": "redshift:AuthorizeInboundIntegration",
                            "Condition": {
                                "StringEquals": {
                                    "aws:SourceArn": {
                                        "Fn::GetAtt": [
                                            "RDSDBInstance",
                                            "DBInstanceArn"
                                        ]
                                    }
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        ":",
                                        [
                                            "arn",
                                            {
                                                "Ref": "AWS::Partition"
                                            },
                                            "iam",
                                            "",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            "root"
                                        ]
                                    ]
                                }
                            },
                            "Action": "redshift:CreateInboundIntegration"
                        }
                    ]
                }
            }
        },
        "Integration": {
            "Type": "AWS::RDS::Integration",
            "Properties": {
            	"IntegrationName": "zeroetl-integration-from-mysql-to-redshift",
                "SourceArn": {
                    "Fn::GetAtt": [
                        "RDSDBInstance",
                        "DBInstanceArn"
                    ]
                },
                "TargetArn": {
                    "Fn::GetAtt": [
                        "RSCluster",
                        "ClusterNamespaceArn"
                    ]
                },
                "KMSKeyId": {
                    "Fn::GetAtt": [
                        "kmsKey",
                        "Arn"
                    ]
                },
                "AdditionalEncryptionContext": {
                    "integrationName": "zeroetl-integration-from-mysql-to-redshift"
                }
            }
        }
    },
    "Outputs": {
    	"IntegrationCreateTime": {
    		"Description": "Integration Creation Time",
    		"Value": {
    			"Fn::GetAtt": [
    				"Integration",
    				"CreateTime"
    			]
    		}
    	},
        "IntegrationARN": {
            "Description": "Integration ARN",
            "Value": {
                "Ref": "Integration"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-integration--examples--Create_an_RDS_zero-ETL_integration_using_a_customer_managed_KMS_key--yaml"></a>

```
Parameters:
  Username:
    Description: Username for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  Password:
    NoEcho: 'true'
    Description: Password for MySQL database access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
  RSUsername:
    Description: Username for Redshift cluster access
    Type: String
    MinLength: '1'
    MaxLength: '16'
    Default: sqladmin
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric characters.
  RSPassword:
    NoEcho: 'true'
    Description: Password for Redshift cluster access
    Type: String
    MinLength: '8'
    MaxLength: '41'
    Default: Sqladmin2024
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
Resources:
  kmsKey:
    Type: 'AWS::KMS::Key'
    Properties:
      Description: Key used to encrypt the zero-ETL integration.
      KeyPolicy:
        Version: 2012-10-17
        Statement:
          - Sid: statement1
            Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: 'kms:CreateGrant'
            Resource: '*'
          - Sid: statement2
            Effect: Allow
            Principal:
              AWS: !Join
                - ':'
                - - arn
                  - !Ref 'AWS::Partition'
                  - iam
                  - ''
                  - !Ref 'AWS::AccountId'
                  - root
            Action: 'kms:*'
            Resource: '*'
  RDSDBParameterGroup:
    Type: 'AWS::RDS::DBParameterGroup'
    Properties:
      DBParameterGroupName: zeroetl-mysql-parameter-group
      Description: Enables enhanced binlog
      Family: mysql8.0
      Parameters:
        binlog_checksum: NONE
        binlog_format: ROW
        binlog_row_image: FULL
  RDSDBInstance:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      DBInstanceIdentifier: zeroetl-mysql-source
      DBParameterGroupName: !Ref RDSDBParameterGroup
      Engine: mysql
      EngineVersion: 8.0.33
      MasterUsername: !Ref Username
      MasterUserPassword: !Ref Password
      DBInstanceClass: db.r5.large
      BackupRetentionPeriod: 1
      StorageType: gp2
      AllocatedStorage: '100'
  RSClusterParameterGroup:
    Type: 'AWS::Redshift::ClusterParameterGroup'
    Properties:
      ParameterGroupName: zeroetl-redshift-cluster-parameter-group
      Description: Enables case sensitivity
      ParameterGroupFamily: redshift-1.0
      Parameters:
        - ParameterName: enable_case_sensitive_identifier
          ParameterValue: 'true'
  RSCluster:
    Type: 'AWS::Redshift::Cluster'
    Properties:
      ClusterIdentifier: zeroetl-redshift-cluster
      ClusterParameterGroupName: !Ref RSClusterParameterGroup
      ClusterType: multi-node
      DBName: sqladmin
      MaintenanceTrackName: PREVIEW_2023
      Encrypted: true
      MasterUsername: !Ref RSUsername
      MasterUserPassword: !Ref RSPassword
      NodeType: ra3.xlplus
      NumberOfNodes: 2
      NamespaceResourcePolicy:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service: redshift.amazonaws.com
            Action: 'redshift:AuthorizeInboundIntegration'
            Condition:
              StringEquals:
                'aws:SourceArn': !GetAtt
                  - RDSDBInstance
                  - DBInstanceArn
          - Effect: Allow
            Principal:
              AWS: !Join
                - ':'
                - - arn
                  - !Ref 'AWS::Partition'
                  - iam
                  - ''
                  - !Ref 'AWS::AccountId'
                  - root
            Action: 'redshift:CreateInboundIntegration'
  Integration:
    Type: 'AWS::RDS::Integration'
    Properties:
      IntegrationName: zeroetl-integration-from-mysql-to-redshift
      SourceArn: !GetAtt
        - RDSDBInstance
        - DBInstanceArn
      TargetArn: !GetAtt
        - RSCluster
        - ClusterNamespaceArn
      KMSKeyId: !GetAtt
        - kmsKey
        - Arn
      AdditionalEncryptionContext:
        integrationName: zeroetl-integration-from-mysql-to-redshift
Outputs:
  IntegrationCreateTime:
    Description: Integration Creation Time
    Value: !GetAtt
      - Integration
      - CreateTime
  IntegrationARN:
    Description: Integration ARN
    Value: !Ref Integration
```
