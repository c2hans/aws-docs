---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket Rule
<a name="aws-properties-s3express-directorybucket-rule"></a>

Specifies lifecycle rules for an Amazon S3 bucket. For more information, see [Put Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html) in the *Amazon S3 API Reference*. For examples, see [Put Bucket Lifecycle Configuration Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html#API_PutBucketLifecycleConfiguration_Examples).

You must specify at least one of the following properties: `AbortIncompleteMultipartUpload`, or `ExpirationInDays`.

## Syntax
<a name="aws-properties-s3express-directorybucket-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-rule-syntax.json"></a>

```
{
  "[AbortIncompleteMultipartUpload](#cfn-s3express-directorybucket-rule-abortincompletemultipartupload)" : {{AbortIncompleteMultipartUpload}},
  "[ExpirationInDays](#cfn-s3express-directorybucket-rule-expirationindays)" : {{Integer}},
  "[Id](#cfn-s3express-directorybucket-rule-id)" : {{String}},
  "[ObjectSizeGreaterThan](#cfn-s3express-directorybucket-rule-objectsizegreaterthan)" : {{String}},
  "[ObjectSizeLessThan](#cfn-s3express-directorybucket-rule-objectsizelessthan)" : {{String}},
  "[Prefix](#cfn-s3express-directorybucket-rule-prefix)" : {{String}},
  "[Status](#cfn-s3express-directorybucket-rule-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-rule-syntax.yaml"></a>

```
  [AbortIncompleteMultipartUpload](#cfn-s3express-directorybucket-rule-abortincompletemultipartupload): {{
    AbortIncompleteMultipartUpload}}
  [ExpirationInDays](#cfn-s3express-directorybucket-rule-expirationindays): {{Integer}}
  [Id](#cfn-s3express-directorybucket-rule-id): {{String}}
  [ObjectSizeGreaterThan](#cfn-s3express-directorybucket-rule-objectsizegreaterthan): {{String}}
  [ObjectSizeLessThan](#cfn-s3express-directorybucket-rule-objectsizelessthan): {{String}}
  [Prefix](#cfn-s3express-directorybucket-rule-prefix): {{String}}
  [Status](#cfn-s3express-directorybucket-rule-status): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-rule-properties"></a>

`AbortIncompleteMultipartUpload`  <a name="cfn-s3express-directorybucket-rule-abortincompletemultipartupload"></a>
Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload.
*Required*: No
*Type*: [AbortIncompleteMultipartUpload](aws-properties-s3express-directorybucket-abortincompletemultipartupload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpirationInDays`  <a name="cfn-s3express-directorybucket-rule-expirationindays"></a>
Indicates the number of days after creation when objects are deleted from Amazon S3 and Amazon S3 Glacier. If you specify an expiration and transition time, you must use the same time unit for both properties (either in days or by date). The expiration time must also be later than the transition time.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-s3express-directorybucket-rule-id"></a>
Unique identifier for the rule. The value can't be longer than 255 characters.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectSizeGreaterThan`  <a name="cfn-s3express-directorybucket-rule-objectsizegreaterthan"></a>
Specifies the minimum object size in bytes for this rule to apply to. Objects must be larger than this value in bytes. For more information about size based rules, see [Lifecycle configuration using size-based rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[0-9]+`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectSizeLessThan`  <a name="cfn-s3express-directorybucket-rule-objectsizelessthan"></a>
Specifies the maximum object size in bytes for this rule to apply to. Objects must be smaller than this value in bytes. For more information about sized based rules, see [Lifecycle configuration using size-based rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[0-9]+`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-s3express-directorybucket-rule-prefix"></a>
Object key prefix that identifies one or more objects to which this rule applies.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-s3express-directorybucket-rule-status"></a>
If `Enabled`, the rule is currently being applied. If `Disabled`, the rule is not currently being applied.
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3express-directorybucket-rule--examples"></a>

### Manage the lifecycle for S3 objects
<a name="aws-properties-s3express-directorybucket-rule--examples--Manage_the_lifecycle_for_S3_objects"></a>

The following example template shows an S3 directory bucket with a lifecycle configuration rule. The rule applies to all objects with the `foo/` key prefix. The objects are expired after seven days, and incomplete multipart uploads are deleted 3 days after initiation.

#### JSON
<a name="aws-properties-s3express-directorybucket-rule--examples--Manage_the_lifecycle_for_S3_objects--json"></a>

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
<a name="aws-properties-s3express-directorybucket-rule--examples--Manage_the_lifecycle_for_S3_objects--yaml"></a>

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
