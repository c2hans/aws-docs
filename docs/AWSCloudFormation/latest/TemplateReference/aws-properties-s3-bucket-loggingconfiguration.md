---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket LoggingConfiguration
<a name="aws-properties-s3-bucket-loggingconfiguration"></a>

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket. For examples and more information, see [PUT Bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html) in the *Amazon S3 API Reference*.

**Note**
To successfully complete the `AWS::S3::Bucket LoggingConfiguration` request, you must have `s3:PutObject` and `s3:PutObjectAcl` in your IAM permissions.

## Syntax
<a name="aws-properties-s3-bucket-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-loggingconfiguration-syntax.json"></a>

```
{
  "[DestinationBucketName](#cfn-s3-bucket-loggingconfiguration-destinationbucketname)" : {{String}},
  "[LogFilePrefix](#cfn-s3-bucket-loggingconfiguration-logfileprefix)" : {{String}},
  "[TargetObjectKeyFormat](#cfn-s3-bucket-loggingconfiguration-targetobjectkeyformat)" : {{TargetObjectKeyFormat}}
}
```

### YAML
<a name="aws-properties-s3-bucket-loggingconfiguration-syntax.yaml"></a>

```
  [DestinationBucketName](#cfn-s3-bucket-loggingconfiguration-destinationbucketname): {{String}}
  [LogFilePrefix](#cfn-s3-bucket-loggingconfiguration-logfileprefix): {{String}}
  [TargetObjectKeyFormat](#cfn-s3-bucket-loggingconfiguration-targetobjectkeyformat): {{
    TargetObjectKeyFormat}}
```

## Properties
<a name="aws-properties-s3-bucket-loggingconfiguration-properties"></a>

`DestinationBucketName`  <a name="cfn-s3-bucket-loggingconfiguration-destinationbucketname"></a>
The name of the bucket where Amazon S3 should store server access log files. You can store log files in any bucket that you own. By default, logs are stored in the bucket where the `LoggingConfiguration` property is defined.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogFilePrefix`  <a name="cfn-s3-bucket-loggingconfiguration-logfileprefix"></a>
A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetObjectKeyFormat`  <a name="cfn-s3-bucket-loggingconfiguration-targetobjectkeyformat"></a>
Amazon S3 key format for log objects. Only one format, either PartitionedPrefix or SimplePrefix, is allowed.
*Required*: No
*Type*: [TargetObjectKeyFormat](aws-properties-s3-bucket-targetobjectkeyformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-loggingconfiguration--examples"></a>

**Topics**
+ [Log access requests for a specific S3 bucket](#aws-properties-s3-bucket-loggingconfiguration--examples--Log_access_requests_for_a_specific_S3_bucket)
+ [Setting up logging configurations with log prefixes based on event time](#aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_event_time)
+ [Setting up logging configurations with log prefixes based on delivery time](#aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_delivery_time)
+ [Setting up logging configurations with a simple prefix](#aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_a_simple_prefix)

### Log access requests for a specific S3 bucket
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Log_access_requests_for_a_specific_S3_bucket"></a>

The following example template creates two S3 buckets. The `LoggingBucket` bucket store the logs from the `S3Bucket` bucket. To receive logs from the `S3Bucket` bucket, the logging bucket requires log delivery write permissions.

#### JSON
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Log_access_requests_for_a_specific_S3_bucket--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "LoggingConfiguration": {
                    "DestinationBucketName": {
                        "Ref": "LoggingBucket"
                    },
                    "LogFilePrefix": "testing-logs"
                }
            }
        },
        "LoggingBucket": {
            "Type": "AWS::S3::Bucket"
        },
        "S3BucketPolicy": {
            "Type": "AWS::S3::BucketPolicy",
            "Properties": {
                "Bucket": {
                    "Ref": "LoggingBucket"
                },
                "PolicyDocument": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Action": [
                                "s3:PutObject"
                            ],
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "logging.s3.amazonaws.com"
                            },
                            "Resource": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "arn:aws:s3:::",
                                        {
                                            "Ref": "LoggingBucket"
                                        },
                                        "/*"
                                    ]
                                ]
                            },
                            "Condition": {
                                "ArnLike": {
                                    "aws:SourceArn": {
                                        "Fn::GetAtt": [
                                            "S3Bucket",
                                            "Arn"
                                        ]
                                    }
                                },
                                "StringEquals": {
                                    "aws:SourceAccount": {
                                        "Fn::Sub": "${AWS::AccountId}"
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        }
    },
    "Outputs": {
        "BucketName": {
            "Value": {
                "Ref": "S3Bucket"
            },
            "Description": "Name of the sample Amazon S3 bucket with a logging configuration."
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Log_access_requests_for_a_specific_S3_bucket--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      LoggingConfiguration:
        DestinationBucketName: !Ref LoggingBucket
        LogFilePrefix: testing-logs
  LoggingBucket:
    Type: 'AWS::S3::Bucket'
  S3BucketPolicy:
    Type: 'AWS::S3::BucketPolicy'
    Properties:
      Bucket: !Ref LoggingBucket
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Action:
              - 's3:PutObject'
            Effect: Allow
            Principal:
              Service: logging.s3.amazonaws.com
            Resource: !Join
              - ''
              - - 'arn:aws:s3:::'
                - !Ref LoggingBucket
                - /*
            Condition:
              ArnLike:
                'aws:SourceArn': !GetAtt
                  - S3Bucket
                  - Arn
              StringEquals:
                'aws:SourceAccount': !Sub '${AWS::AccountId}'
Outputs:
  BucketName:
    Value: !Ref S3Bucket
    Description: Name of the sample Amazon S3 bucket with a logging configuration.
```

### Setting up logging configurations with log prefixes based on event time
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_event_time"></a>

The following example template configures the `DOC-EXAMPLE-BUCKET` destination bucket with a `logs/` prefix and event time log delivery.

#### JSON
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_event_time--json"></a>

```
        "LoggingConfiguration": {
            "DestinationBucketName": "DOC-EXAMPLE-BUCKET",
            "LogFilePrefix": "logs/",
            "TargetObjectKeyFormat": {
                "PartitionedPrefix": {
                    "PartitionDateSource": "EventTime"
                }
            }
        }
```

#### YAML
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_event_time--yaml"></a>

```
        LoggingConfiguration:
          DestinationBucketName: "DOC-EXAMPLE-BUCKET"
          LogFilePrefix: logs/
          TargetObjectKeyFormat:
            PartitionedPrefix:
              PartitionDateSource: EventTime
```

### Setting up logging configurations with log prefixes based on delivery time
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_delivery_time"></a>

The following example template configures the `DOC-EXAMPLE-BUCKET` destination bucket with a `logs/` prefix and delivery time log delivery.

#### JSON
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_delivery_time--json"></a>

```
        "LoggingConfiguration": {
            "DestinationBucketName": "DOC-EXAMPLE-BUCKET",
            "LogFilePrefix": "logs/",
            "TargetObjectKeyFormat": {
                "PartitionedPrefix": {
                    "PartitionDateSource": "DeliveryTime"
                }
            }
        }
```

#### YAML
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_log_prefixes_based_on_delivery_time--yaml"></a>

```
        LoggingConfiguration:
          DestinationBucketName: "DOC-EXAMPLE-BUCKET"
          LogFilePrefix: logs/
          TargetObjectKeyFormat:
            PartitionedPrefix:
              PartitionDateSource: DeliveryTime
```

### Setting up logging configurations with a simple prefix
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_a_simple_prefix"></a>

The following example template configures the `DOC-EXAMPLE-BUCKET` destination bucket with a `logs/` prefix and simple prefix delivery.

#### JSON
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_a_simple_prefix--json"></a>

```
        "LoggingConfiguration": {
            "DestinationBucketName": "DOC-EXAMPLE-BUCKET",
            "LogFilePrefix": "logs/",
            "TargetObjectKeyFormat": {
                "SimplePrefix": {}
            }
        }
```

#### YAML
<a name="aws-properties-s3-bucket-loggingconfiguration--examples--Setting_up_logging_configurations_with_a_simple_prefix--yaml"></a>

```
        LoggingConfiguration:
          DestinationBucketName: "DOC-EXAMPLE-BUCKET"
          LogFilePrefix: logs/
          TargetObjectKeyFormat:
            SimplePrefix: {}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
