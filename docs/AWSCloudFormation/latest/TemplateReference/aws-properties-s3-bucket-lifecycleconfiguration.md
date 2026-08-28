---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket LifecycleConfiguration
<a name="aws-properties-s3-bucket-lifecycleconfiguration"></a>

Specifies the lifecycle configuration for objects in an Amazon S3 bucket. For more information, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-lifecycleconfiguration-syntax.json"></a>

```
{
  "[Rules](#cfn-s3-bucket-lifecycleconfiguration-rules)" : {{[ Rule, ... ]}},
  "[TransitionDefaultMinimumObjectSize](#cfn-s3-bucket-lifecycleconfiguration-transitiondefaultminimumobjectsize)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-lifecycleconfiguration-syntax.yaml"></a>

```
  [Rules](#cfn-s3-bucket-lifecycleconfiguration-rules): {{
    - Rule}}
  [TransitionDefaultMinimumObjectSize](#cfn-s3-bucket-lifecycleconfiguration-transitiondefaultminimumobjectsize): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-lifecycleconfiguration-properties"></a>

`Rules`  <a name="cfn-s3-bucket-lifecycleconfiguration-rules"></a>
A lifecycle rule for individual objects in an Amazon S3 bucket.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-s3-bucket-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitionDefaultMinimumObjectSize`  <a name="cfn-s3-bucket-lifecycleconfiguration-transitiondefaultminimumobjectsize"></a>
Indicates which default minimum object size behavior is applied to the lifecycle configuration.
This parameter applies to general purpose buckets only. It isn't supported for directory bucket lifecycle configurations.
+ `all_storage_classes_128K` - Objects smaller than 128 KB will not transition to any storage class by default.
+ `varies_by_storage_class` - Objects smaller than 128 KB will transition to Glacier Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes will prevent transitions smaller than 128 KB.
To customize the minimum object size for any transition you can add a filter that specifies a custom `ObjectSizeGreaterThan` or `ObjectSizeLessThan` in the body of your transition rule. Custom filters always take precedence over the default transition behavior.
*Required*: No
*Type*: String
*Allowed values*: `varies_by_storage_class | all_storage_classes_128K`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-lifecycleconfiguration--examples"></a>

### Manage the lifecycle for S3 objects
<a name="aws-properties-s3-bucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects"></a>

The following example template shows an S3 bucket with a lifecycle configuration rule. The rule applies to all objects with the `glacier` key prefix. The objects are transitioned to Glacier after one day, and deleted after one year.

#### JSON
<a name="aws-properties-s3-bucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "AccessControl": "Private",
                "LifecycleConfiguration": {
                    "Rules": [
                        {
                            "Id": "GlacierRule",
                            "Prefix": "glacier",
                            "Status": "Enabled",
                            "ExpirationInDays": 365,
                            "Transitions": [
                                {
                                    "TransitionInDays": 1,
                                    "StorageClass": "GLACIER"
                                }
                            ]
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
            "Description": "Name of the sample Amazon S3 bucket with a lifecycle configuration."
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-bucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      AccessControl: Private
      LifecycleConfiguration:
        Rules:
          - Id: GlacierRule
            Prefix: glacier
            Status: Enabled
            ExpirationInDays: 365
            Transitions:
              - TransitionInDays: 1
                StorageClass: GLACIER
Outputs:
  BucketName:
    Value: !Ref S3Bucket
    Description: Name of the sample Amazon S3 bucket with a lifecycle configuration.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
