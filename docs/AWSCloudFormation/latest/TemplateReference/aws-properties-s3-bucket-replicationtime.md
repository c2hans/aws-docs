---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationtime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ReplicationTime
<a name="aws-properties-s3-bucket-replicationtime"></a>

 A container specifying S3 Replication Time Control (S3 RTC) related information, including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a `Metrics` block.

## Syntax
<a name="aws-properties-s3-bucket-replicationtime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-replicationtime-syntax.json"></a>

```
{
  "[Status](#cfn-s3-bucket-replicationtime-status)" : {{String}},
  "[Time](#cfn-s3-bucket-replicationtime-time)" : {{ReplicationTimeValue}}
}
```

### YAML
<a name="aws-properties-s3-bucket-replicationtime-syntax.yaml"></a>

```
  [Status](#cfn-s3-bucket-replicationtime-status): {{String}}
  [Time](#cfn-s3-bucket-replicationtime-time): {{
    ReplicationTimeValue}}
```

## Properties
<a name="aws-properties-s3-bucket-replicationtime-properties"></a>

`Status`  <a name="cfn-s3-bucket-replicationtime-status"></a>
 Specifies whether the replication time is enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-s3-bucket-replicationtime-time"></a>
 A container specifying the time by which replication should be complete for all objects and operations on objects.
*Required*: Yes
*Type*: [ReplicationTimeValue](aws-properties-s3-bucket-replicationtimevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-replicationtime--examples"></a>

### Enable S3 Replication Time Control
<a name="aws-properties-s3-bucket-replicationtime--examples--Enable_S3_Replication_Time_Control"></a>

The following example creates a replication configuration with S3 Replication Time Control (S3 RTC) enabled. To use this example, replace {{amzn-s3-demo-source-bucket}} with the name of your source bucket and replace {{amzn-s3-demo-destination-bucket}} with the name of your destination bucket. Make sure to update the AWS Identity and Access Management (IAM) role and the replication rule as needed.

#### JSON
<a name="aws-properties-s3-bucket-replicationtime--examples--Enable_S3_Replication_Time_Control--json"></a>

```
      {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Template for S3 Bucket Replication",
    "Resources": {
      "MyS3Bucket": {
        "Type": "AWS::S3::Bucket",
        "Properties": {
          "BucketName": "{{amzn-s3-demo-source-bucket}}",
          "VersioningConfiguration": {
            "Status": "Enabled"
          },
          "ReplicationConfiguration": {
            "Role": "arn:aws:iam::account:role/s3-replication-role",
            "Rules": [
              {
                "Id": "ReplicationRule1",
                "Status": "Enabled",
                "Filter": {
                  "Prefix": ""
                },
                "Destination": {
                  "Bucket": "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}",
                  "ReplicationTime": {
                    "Status": "Enabled",
                    "Time": {
                      "Minutes": 15
                    }
                  },
                  "Metrics": {
                    "Status": "Enabled",
                    "EventThreshold": {
                      "Minutes": 15
                    }
                  }
                },
                "Priority": 1,
                "DeleteMarkerReplication": {
                  "Status": "Enabled"
                },
                "SourceSelectionCriteria": {
                  "ReplicaModifications": {
                    "Status": "Disabled"
                  }
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
<a name="aws-properties-s3-bucket-replicationtime--examples--Enable_S3_Replication_Time_Control--yaml"></a>

```
        AWSTemplateFormatVersion: '2010-09-09'
Description: 'AWS CloudFormation Template for S3 Bucket Replication'

Resources:
  MyS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: '{{amzn-s3-demo-source-bucket}}'
      VersioningConfiguration:
        Status: 'Enabled'
      ReplicationConfiguration:
        Role: 'arn:aws:iam::account:role/s3-replication-role'
        Rules:
          - Id: 'ReplicationRule1'
            Status: 'Enabled'
            Filter:
              Prefix: ""
            Destination:
              Bucket: 'arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}'
              ReplicationTime:
                  Status: Enabled
                  Time:
                    Minutes: 15
              Metrics:
                Status: Enabled
                EventThreshold:
                  Minutes: 15
            Priority: 1
            DeleteMarkerReplication:
              Status: Enabled
            SourceSelectionCriteria:
              ReplicaModifications:
                Status: Disabled
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
