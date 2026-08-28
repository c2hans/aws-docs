---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ReplicationConfiguration
<a name="aws-properties-s3-bucket-replicationconfiguration"></a>

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication configuration is 2 MB. The latest version of the replication configuration XML is V2. For more information about XML V2 replication configurations, see [Replication configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-add-config.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-replicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-replicationconfiguration-syntax.json"></a>

```
{
  "[Role](#cfn-s3-bucket-replicationconfiguration-role)" : {{String}},
  "[Rules](#cfn-s3-bucket-replicationconfiguration-rules)" : {{[ ReplicationRule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-bucket-replicationconfiguration-syntax.yaml"></a>

```
  [Role](#cfn-s3-bucket-replicationconfiguration-role): {{String}}
  [Rules](#cfn-s3-bucket-replicationconfiguration-rules): {{
    - ReplicationRule}}
```

## Properties
<a name="aws-properties-s3-bucket-replicationconfiguration-properties"></a>

`Role`  <a name="cfn-s3-bucket-replicationconfiguration-role"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html) in the *Amazon S3 User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-s3-bucket-replicationconfiguration-rules"></a>
A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.
*Required*: Yes
*Type*: Array of [ReplicationRule](aws-properties-s3-bucket-replicationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-replicationconfiguration--examples"></a>

**Topics**
+ [Associate a replication configuration IAM role with an S3 bucket](#aws-properties-s3-bucket-replicationconfiguration--examples--Associate_a_replication_configuration_IAM_role_with_an_S3_bucket)
+ [Enable versioning and replicate objects](#aws-properties-s3-bucket-replicationconfiguration--examples--Enable_versioning_and_replicate_objects)

### Associate a replication configuration IAM role with an S3 bucket
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Associate_a_replication_configuration_IAM_role_with_an_S3_bucket"></a>

The following example creates an S3 bucket and grants it permission to write to a replication bucket by using an AWS Identity and Access Management (IAM) role. To avoid a circular dependency, the role's policy is declared as a separate resource. The bucket depends on the `WorkItemBucketBackupRole` role. If the policy is included in the role, the role also depends on the bucket.

#### JSON
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Associate_a_replication_configuration_IAM_role_with_an_S3_bucket--json"></a>

```
{
    "Resources": {
        "RecordServiceS3Bucket": {
            "Type": "AWS::S3::Bucket",
            "DeletionPolicy": "Retain",
            "Properties": {
                "ReplicationConfiguration": {
                    "Role": {
                        "Fn::GetAtt": [
                            "WorkItemBucketBackupRole",
                            "Arn"
                        ]
                    },
                    "Rules": [
                        {
                            "Destination": {
                                "Bucket": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:s3:::",
                                            {
                                                "Fn::Join": [
                                                    "-",
                                                    [
                                                        {
                                                            "Ref": "AWS::Region"
                                                        },
                                                        {
                                                            "Ref": "AWS::StackName"
                                                        },
                                                        "replicationbucket"
                                                    ]
                                                ]
                                            }
                                        ]
                                    ]
                                },
                                "StorageClass": "STANDARD"
                            },
                            "Id": "Backup",
                            "Prefix": "",
                            "Status": "Enabled"
                        }
                    ]
                },
                "VersioningConfiguration": {
                    "Status": "Enabled"
                }
            }
        },
        "WorkItemBucketBackupRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Statement": [
                        {
                            "Action": [
                                "sts:AssumeRole"
                            ],
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "s3.amazonaws.com"
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "BucketBackupPolicy": {
            "Type": "AWS::IAM::Policy",
            "Properties": {
                "PolicyDocument": {
                    "Statement": [
                        {
                            "Action": [
                                "s3:GetReplicationConfiguration",
                                "s3:ListBucket"
                            ],
                            "Effect": "Allow",
                            "Resource": [
                                {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:s3:::",
                                            {
                                                "Ref": "RecordServiceS3Bucket"
                                            }
                                        ]
                                    ]
                                }
                            ]
                        },
                        {
                            "Action": [
                                "s3:GetObjectVersion",
                                "s3:GetObjectVersionAcl"
                            ],
                            "Effect": "Allow",
                            "Resource": [
                                {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:s3:::",
                                            {
                                                "Ref": "RecordServiceS3Bucket"
                                            },
                                            "/*"
                                        ]
                                    ]
                                }
                            ]
                        },
                        {
                            "Action": [
                                "s3:ReplicateObject",
                                "s3:ReplicateDelete"
                            ],
                            "Effect": "Allow",
                            "Resource": [
                                {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:s3:::",
                                            {
                                                "Fn::Join": [
                                                    "-",
                                                    [
                                                        {
                                                            "Ref": "AWS::Region"
                                                        },
                                                        {
                                                            "Ref": "AWS::StackName"
                                                        },
                                                        "replicationbucket"
                                                    ]
                                                ]
                                            },
                                            "/*"
                                        ]
                                    ]
                                }
                            ]
                        }
                    ]
                },
                "PolicyName": "BucketBackupPolicy",
                "Roles": [
                    {
                        "Ref": "WorkItemBucketBackupRole"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Associate_a_replication_configuration_IAM_role_with_an_S3_bucket--yaml"></a>

```
Resources:
  RecordServiceS3Bucket:
    Type: 'AWS::S3::Bucket'
    DeletionPolicy: Retain
    Properties:
      ReplicationConfiguration:
        Role: !GetAtt
          - WorkItemBucketBackupRole
          - Arn
        Rules:
          - Destination:
              Bucket: !Join
                - ''
                - - 'arn:aws:s3:::'
                  - !Join
                    - '-'
                    - - !Ref 'AWS::Region'
                      - !Ref 'AWS::StackName'
                      - replicationbucket
              StorageClass: STANDARD
            Id: Backup
            Prefix: ''
            Status: Enabled
      VersioningConfiguration:
        Status: Enabled
  WorkItemBucketBackupRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action:
              - 'sts:AssumeRole'
            Effect: Allow
            Principal:
              Service:
                - s3.amazonaws.com
  BucketBackupPolicy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - 's3:GetReplicationConfiguration'
              - 's3:ListBucket'
            Effect: Allow
            Resource:
              - !Join
                - ''
                - - 'arn:aws:s3:::'
                  - !Ref RecordServiceS3Bucket
          - Action:
              - 's3:GetObjectVersion'
              - 's3:GetObjectVersionAcl'
            Effect: Allow
            Resource:
              - !Join
                - ''
                - - 'arn:aws:s3:::'
                  - !Ref RecordServiceS3Bucket
                  - /*
          - Action:
              - 's3:ReplicateObject'
              - 's3:ReplicateDelete'
            Effect: Allow
            Resource:
              - !Join
                - ''
                - - 'arn:aws:s3:::'
                  - !Join
                    - '-'
                    - - !Ref 'AWS::Region'
                      - !Ref 'AWS::StackName'
                      - replicationbucket
                  - /*
      PolicyName: BucketBackupPolicy
      Roles:
        - !Ref WorkItemBucketBackupRole
```

### Enable versioning and replicate objects
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Enable_versioning_and_replicate_objects"></a>

The following example enables versioning and two replication rules. The rules copy objects prefixed with either `MyPrefix` and `MyOtherPrefix` and stores the copied objects in a bucket named `my-replication-bucket`.

#### JSON
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Enable_versioning_and_replicate_objects--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "VersioningConfiguration": {
                    "Status": "Enabled"
                },
                "ReplicationConfiguration": {
                    "Role": "arn:aws:iam::123456789012:role/replication_role",
                    "Rules": [
                        {
                            "Id": "MyRule1",
                            "Status": "Enabled",
                            "Prefix": "MyPrefix",
                            "Destination": {
                                "Bucket": "arn:aws:s3:::my-replication-bucket",
                                "StorageClass": "STANDARD"
                            }
                        },
                        {
                            "Status": "Enabled",
                            "Prefix": "MyOtherPrefix",
                            "Destination": {
                                "Bucket": "arn:aws:s3:::my-replication-bucket"
                            }
                        }
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-bucket-replicationconfiguration--examples--Enable_versioning_and_replicate_objects--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      VersioningConfiguration:
        Status: Enabled
      ReplicationConfiguration:
        Role: 'arn:aws:iam::123456789012:role/replication_role'
        Rules:
          - Id: MyRule1
            Status: Enabled
            Prefix: MyPrefix
            Destination:
              Bucket: 'arn:aws:s3:::my-replication-bucket'
              StorageClass: STANDARD
          - Status: Enabled
            Prefix: MyOtherPrefix
            Destination:
              Bucket: 'arn:aws:s3:::my-replication-bucket'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
