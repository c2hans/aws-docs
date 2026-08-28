---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-versioningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket VersioningConfiguration
<a name="aws-properties-s3-bucket-versioningconfiguration"></a>

Describes the versioning state of an Amazon S3 bucket. For more information, see [PUT Bucket versioning](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTVersioningStatus.html) in the *Amazon S3 API Reference*.

Keep the following timing in mind when enabling, suspending, or transitioning between versioning states:
+ **Enabling versioning** - Changes may take up to 15 minutes to propagate across all AWS regions for full consistency.
+ **Suspending versioning** - Takes effect immediately with no propagation delay.
+ **Transitioning between states** - Any change from Suspended to Enabled has a 15-minute delay.

## Syntax
<a name="aws-properties-s3-bucket-versioningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-versioningconfiguration-syntax.json"></a>

```
{
  "[Status](#cfn-s3-bucket-versioningconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-versioningconfiguration-syntax.yaml"></a>

```
  [Status](#cfn-s3-bucket-versioningconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-versioningconfiguration-properties"></a>

`Status`  <a name="cfn-s3-bucket-versioningconfiguration-status"></a>
The versioning state of the bucket.
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Suspended`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Examples
<a name="aws-properties-s3-bucket-versioningconfiguration--examples"></a>

### Enable versioning and replicate objects
<a name="aws-properties-s3-bucket-versioningconfiguration--examples--Enable_versioning_and_replicate_objects"></a>

The following example enables versioning and two replication rules. The rules copy objects prefixed with either `MyPrefix` and `MyOtherPrefix` and stores the copied objects in a bucket named `my-replication-bucket`.

#### JSON
<a name="aws-properties-s3-bucket-versioningconfiguration--examples--Enable_versioning_and_replicate_objects--json"></a>

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
<a name="aws-properties-s3-bucket-versioningconfiguration--examples--Enable_versioning_and_replicate_objects--yaml"></a>

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
