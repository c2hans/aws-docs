---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalyticsv2-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application
<a name="aws-resource-kinesisanalyticsv2-application"></a>

Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see [Creating an Application](https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html).

## Syntax
<a name="aws-resource-kinesisanalyticsv2-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesisanalyticsv2-application-syntax.json"></a>

```
{
  "Type" : "AWS::KinesisAnalyticsV2::Application",
  "Properties" : {
      "[ApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration)" : {{ApplicationConfiguration}},
      "[ApplicationDescription](#cfn-kinesisanalyticsv2-application-applicationdescription)" : {{String}},
      "[ApplicationMaintenanceConfiguration](#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration)" : {{ApplicationMaintenanceConfiguration}},
      "[ApplicationMode](#cfn-kinesisanalyticsv2-application-applicationmode)" : {{String}},
      "[ApplicationName](#cfn-kinesisanalyticsv2-application-applicationname)" : {{String}},
      "[RunConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration)" : {{RunConfiguration}},
      "[RuntimeEnvironment](#cfn-kinesisanalyticsv2-application-runtimeenvironment)" : {{String}},
      "[ServiceExecutionRole](#cfn-kinesisanalyticsv2-application-serviceexecutionrole)" : {{String}},
      "[Tags](#cfn-kinesisanalyticsv2-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesisanalyticsv2-application-syntax.yaml"></a>

```
Type: AWS::KinesisAnalyticsV2::Application
Properties:
  [ApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration): {{
    ApplicationConfiguration}}
  [ApplicationDescription](#cfn-kinesisanalyticsv2-application-applicationdescription): {{String}}
  [ApplicationMaintenanceConfiguration](#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration): {{
    ApplicationMaintenanceConfiguration}}
  [ApplicationMode](#cfn-kinesisanalyticsv2-application-applicationmode): {{String}}
  [ApplicationName](#cfn-kinesisanalyticsv2-application-applicationname): {{String}}
  [RunConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration): {{
    RunConfiguration}}
  [RuntimeEnvironment](#cfn-kinesisanalyticsv2-application-runtimeenvironment): {{String}}
  [ServiceExecutionRole](#cfn-kinesisanalyticsv2-application-serviceexecutionrole): {{String}}
  [Tags](#cfn-kinesisanalyticsv2-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesisanalyticsv2-application-properties"></a>

`ApplicationConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration"></a>
Use this parameter to configure the application.
*Required*: No
*Type*: [ApplicationConfiguration](aws-properties-kinesisanalyticsv2-application-applicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationDescription`  <a name="cfn-kinesisanalyticsv2-application-applicationdescription"></a>
The description of the application.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationMaintenanceConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration"></a>
Specifies the maintenance window parameters for a Kinesis Data Analytics application.
*Required*: No
*Type*: [ApplicationMaintenanceConfiguration](aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationMode`  <a name="cfn-kinesisanalyticsv2-application-applicationmode"></a>
To create a Kinesis Data Analytics Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.
*Required*: No
*Type*: String
*Allowed values*: `INTERACTIVE | STREAMING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ApplicationName`  <a name="cfn-kinesisanalyticsv2-application-applicationname"></a>
The name of the application.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunConfiguration`  <a name="cfn-kinesisanalyticsv2-application-runconfiguration"></a>
Describes the starting parameters for an Managed Service for Apache Flink application.
*Required*: No
*Type*: [RunConfiguration](aws-properties-kinesisanalyticsv2-application-runconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeEnvironment`  <a name="cfn-kinesisanalyticsv2-application-runtimeenvironment"></a>
The runtime environment for the application.
*Required*: Yes
*Type*: String
*Allowed values*: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceExecutionRole`  <a name="cfn-kinesisanalyticsv2-application-serviceexecutionrole"></a>
Specifies the IAM role that the application uses to access external resources.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kinesisanalyticsv2-application-tags"></a>
A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesisanalyticsv2-application-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-kinesisanalyticsv2-application--examples"></a>

**Topics**
+ [Creating an Amazon Kinesis Data Analytics Application using Apache Flink](#aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Application_using_Apache_Flink)
+ [Creating an Amazon Kinesis Data Analytics Studio Application](#aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Studio_Application)

### Creating an Amazon Kinesis Data Analytics Application using Apache Flink
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Application_using_Apache_Flink"></a>

The following example shows how to create a simple application by using a deployment package from Amazon S3. You must add permissions to the IAM role to access any streams that your code requires.

#### JSON
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Application_using_Apache_Flink--json"></a>

```
{
    "Description": "Simple KDA Flink application",
    "Parameters": {
        "CodeBucketArn": {
            "Type": "String"
        },
        "CodeKey": {
            "Type": "String"
        }
    },
    "Resources": {
        "MyApplication": {
            "Type": "AWS::KinesisAnalyticsV2::Application",
            "Properties": {
                "RuntimeEnvironment": "FLINK-1_15",
                "ServiceExecutionRole": {
                    "Fn::GetAtt": [
                        "ServiceExecutionRole",
                        "Arn"
                    ]
                },
                "ApplicationConfiguration": {
                    "ApplicationCodeConfiguration": {
                        "CodeContent": {
                            "S3ContentLocation": {
                                "BucketARN": {
                                    "Ref": "CodeBucketArn"
                                },
                                "FileKey": {
                                    "Ref": "CodeKey"
                                }
                            }
                        },
                        "CodeContentType": "ZIPFILE"
                    }
                }
            }
        },
        "ServiceExecutionRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "kinesisanalytics.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "s3-code-access",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "${CodeBucketArn}/${CodeKey}"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Application_using_Apache_Flink--yaml"></a>

```
Description: Simple KDA Flink application
Parameters:
  CodeBucketArn:
    Type: String
  CodeKey:
    Type: String
​
Resources:
  MyApplication:
    Type: AWS::KinesisAnalyticsV2::Application
    Properties:
      RuntimeEnvironment: FLINK-1_15
      ServiceExecutionRole: !GetAtt ServiceExecutionRole.Arn
      ApplicationConfiguration:
        ApplicationCodeConfiguration:
          CodeContent:
            S3ContentLocation:
              BucketARN: !Ref CodeBucketArn
              FileKey: !Ref CodeKey
          CodeContentType: 'ZIPFILE'
​
  ServiceExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service: kinesisanalytics.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: s3-code-access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                Resource:
                  - !Sub "${CodeBucketArn}/${CodeKey}"
```

### Creating an Amazon Kinesis Data Analytics Studio Application
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Studio_Application"></a>

The following example shows how to create a simple Studio application with an Amazon Glue database. You must add permissions to the IAM role to create or access any streams you require, and any that already exist must be added to the Glue database.

#### JSON
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Studio_Application--json"></a>

```
{
    "Description": "KDA Studio application",
    "Parameters": {
        "GlueDatabaseName": {
            "Type": "String"
        }
    },
    "Resources": {
        "MyApplication": {
            "Type": "AWS::KinesisAnalyticsV2::Application",
            "Properties": {
                "ApplicationMode": "INTERACTIVE",
                "RuntimeEnvironment": "ZEPPELIN-FLINK-3_0",
                "ServiceExecutionRole": {
                    "Fn::GetAtt": [
                        "ServiceExecutionRole",
                        "Arn"
                    ]
                },
                "ApplicationConfiguration": {
                    "FlinkApplicationConfiguration": {
                        "ParallelismConfiguration": {
                            "Parallelism": 4,
                            "ConfigurationType": "CUSTOM"
                        }
                    },
                    "ZeppelinApplicationConfiguration": {
                        "CatalogConfiguration": {
                            "GlueDataCatalogConfiguration": {
                                "DatabaseARN": {
                                    "Fn::Sub": "arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${GlueDatabase}"
                                }
                            }
                        },
                        "CustomArtifactsConfiguration": [
                            {
                                "ArtifactType": "DEPENDENCY_JAR",
                                "MavenReference": {
                                    "GroupId": "org.apache.flink",
                                    "ArtifactId": "flink-sql-connector-kinesis",
                                    "Version": "1.15.4"
                                }
                            },
                            {
                                "ArtifactType": "DEPENDENCY_JAR",
                                "MavenReference": {
                                    "GroupId": "org.apache.flink",
                                    "ArtifactId": "flink-connector-kafka",
                                    "Version": "1.15.4"
                                }
                            },
                            {
                                "ArtifactType": "DEPENDENCY_JAR",
                                "MavenReference": {
                                    "GroupId": "software.amazon.msk",
                                    "ArtifactId": "aws-msk-iam-auth",
                                    "Version": "1.1.6"
                                }
                            }
                        ]
                    }
                }
            }
        },
        "GlueDatabase": {
            "Type": "AWS::Glue::Database",
            "Properties": {
                "CatalogId": {
                    "Ref": "AWS::AccountId"
                },
                "DatabaseInput": {
                    "Name": {
                        "Ref": "GlueDatabaseName"
                    },
                    "Description": "My glue database"
                }
            }
        },
        "ServiceExecutionRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "kinesisanalytics.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "glue-access",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "glue:GetConnection",
                                        "glue:GetTable",
                                        "glue:GetTables",
                                        "glue:CreateTable",
                                        "glue:UpdateTable",
                                        "glue:GetDatabases",
                                        "glue:GetUserDefinedFunction"
                                    ],
                                    "Resource": [
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:connection/*"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:table/*"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:database/${GlueDatabase}/*"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:catalog"
                                        },
                                        {
                                            "Fn::Sub": "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:userDefinedFunction/*"
                                        }
                                    ]
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "glue:GetDatabase"
                                    ],
                                    "Resource": [
                                        "*"
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-kinesisanalyticsv2-application--examples--Creating_an_Amazon_Kinesis_Data_Analytics_Studio_Application--yaml"></a>

```
Description: KDA Studio application
Parameters:
  GlueDatabaseName:
    Type: String

Resources:
  MyApplication:
    Type: AWS::KinesisAnalyticsV2::Application
    Properties:
      ApplicationMode: INTERACTIVE
      RuntimeEnvironment: ZEPPELIN-FLINK-3_0
      ServiceExecutionRole: !GetAtt ServiceExecutionRole.Arn
      ApplicationConfiguration:
        FlinkApplicationConfiguration:
          ParallelismConfiguration:
            Parallelism: 4
            ConfigurationType: CUSTOM
        ZeppelinApplicationConfiguration:
          CatalogConfiguration:
            GlueDataCatalogConfiguration:
              DatabaseARN: !Sub "arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${GlueDatabase}"
          CustomArtifactsConfiguration:
            - ArtifactType: DEPENDENCY_JAR
              MavenReference:
                GroupId: org.apache.flink
                ArtifactId: flink-sql-connector-kinesis
                Version: 1.15.4
            - ArtifactType: DEPENDENCY_JAR
              MavenReference:
                GroupId: org.apache.flink
                ArtifactId: flink-connector-kafka
                Version: 1.15.4
            - ArtifactType: DEPENDENCY_JAR
              MavenReference:
                GroupId: software.amazon.msk
                ArtifactId: aws-msk-iam-auth
                Version: 1.1.6

  GlueDatabase:
    Type: AWS::Glue::Database
    Properties:
      CatalogId: !Ref AWS::AccountId
      DatabaseInput:
        Name: !Ref GlueDatabaseName
        Description: My glue database

  ServiceExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service: kinesisanalytics.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: glue-access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - glue:GetConnection
                  - glue:GetTable
                  - glue:GetTables
                  - glue:CreateTable
                  - glue:UpdateTable
                  - glue:GetDatabases
                  - glue:GetUserDefinedFunction
                Resource:
                  - !Sub "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:connection/*"
                  - !Sub "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:table/*"
                  - !Sub "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:database/${GlueDatabase}/*"
                  - !Sub "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:catalog"
                  - !Sub "arn:${AWS::Partition}:glue:${AWS::Region}:${AWS::AccountId}:userDefinedFunction/*"
              - Effect: Allow
                Action:
                  - glue:GetDatabase
                Resource:
                  - "*"
```

## See also
<a name="aws-resource-kinesisanalyticsv2-application--seealso"></a>
+ [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html) in the *Amazon Kinesis Data Analytics API Reference*
