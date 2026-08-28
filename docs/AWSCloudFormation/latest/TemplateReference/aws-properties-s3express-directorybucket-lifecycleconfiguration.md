---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket LifecycleConfiguration
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration"></a>

Container for lifecycle rules. You can add as many as 1000 rules.

For more information see, [Creating and managing a lifecycle configuration for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html          ) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration-syntax.json"></a>

```
{
  "[Rules](#cfn-s3express-directorybucket-lifecycleconfiguration-rules)" : {{[ Rule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration-syntax.yaml"></a>

```
  [Rules](#cfn-s3express-directorybucket-lifecycleconfiguration-rules): {{
    - Rule}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration-properties"></a>

`Rules`  <a name="cfn-s3express-directorybucket-lifecycleconfiguration-rules"></a>
A lifecycle rule for individual objects in an Amazon S3 Express bucket.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-s3express-directorybucket-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration--examples"></a>

### Manage the lifecycle for S3 objects
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects"></a>

The following example template shows an S3 directory bucket with a lifecycle configuration rule. The rule applies to all objects with the `foo/` key prefix. The objects are expired after seven days, and incomplete multipart uploads are deleted 3 days after initiation.

#### JSON
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3ExpressBucket": {
            "Type": "AWS::S3Express::DirectoryBucket",
            "Properties": {
                "LocationName": "usw2-az1",
                "DataRedundancy": "SingleAvailabilityZone",
                "LifecycleConfiguration": {
                    "Rules": [
                        {
                            "Id": "ExipiryRule",
                            "Prefix": "foo/",
                            "Status": "Enabled",
                            "ExpirationInDays": 7,
                            "AbortIncompleteMultipartUpload": {
                                "DaysAfterInitiation": 3
                            },
                        }
                    ]
                }
            }
        }
    },
    "Outputs": {
        "BucketName": {
            "Value": {
                "Ref": "S3ExpressBucket"
            },
            "Description": "Name of the sample Amazon S3 Directory Bucket with a lifecycle configuration."
        }
    }
}
```

#### YAML
<a name="aws-properties-s3express-directorybucket-lifecycleconfiguration--examples--Manage_the_lifecycle_for_S3_objects--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3ExpressBucket:
    Type: 'AWS::S3Express::DirectoryBucket'
    Properties:
      LocationName: usw2-az1
      DataRedundancy: SingleAvailabilityZone
      LifecycleConfiguration:
        Rules:
          - Id: ExipiryRule
            Prefix: foo/
            Status: Enabled
            ExpirationInDays:7
            AbortIncompleteMultipartUpload:
            DaysAfterInitiation:3
Outputs:
  BucketName:
    Value: !Ref S3ExpressBucket
    Description: Name of the sample Amazon S3 Directory Bucket with a lifecycle configuration.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
