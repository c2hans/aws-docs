---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-defaulteventhold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket DefaultEventHold
<a name="aws-properties-s3-bucket-defaulteventhold"></a>

The default Object Lock event hold duration that you want to apply to new objects placed in the specified bucket, unless an object's upload request specifies its own Object Lock settings. New object versions are placed under an event hold and remain protected while the hold is active. When the event hold is released, Amazon S3 retains the object version for this duration, measured from the time the hold is released.

**Note**
The `DefaultEventHold` duration can be specified in either `Days` or `Years`, but you must select one. You can't specify `Days` and `Years` at the same time.

## Syntax
<a name="aws-properties-s3-bucket-defaulteventhold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-defaulteventhold-syntax.json"></a>

```
{
  "[Days](#cfn-s3-bucket-defaulteventhold-days)" : {{Integer}},
  "[Years](#cfn-s3-bucket-defaulteventhold-years)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3-bucket-defaulteventhold-syntax.yaml"></a>

```
  [Days](#cfn-s3-bucket-defaulteventhold-days): {{Integer}}
  [Years](#cfn-s3-bucket-defaulteventhold-years): {{Integer}}
```

## Properties
<a name="aws-properties-s3-bucket-defaulteventhold-properties"></a>

`Days`  <a name="cfn-s3-bucket-defaulteventhold-days"></a>
The number of days that you want to specify for the default event hold duration. Valid values are `1` to `36500` days. You must specify either `Days` or `Years`, but not both.
*Required*: Conditional
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Years`  <a name="cfn-s3-bucket-defaulteventhold-years"></a>
The number of years that you want to specify for the default event hold duration. Valid values are `1` to `100` years. You must specify either `Days` or `Years`, but not both.
*Required*: Conditional
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-defaulteventhold--examples"></a>

**Topics**
+ [Set a bucket default event hold](#aws-properties-s3-bucket-defaulteventhold--examples--Set_a_bucket_default_event_hold)
+ [Combine a default retention period with an event hold](#aws-properties-s3-bucket-defaulteventhold--examples--Combine_a_default_retention_period_with_an_event_hold)

### Set a bucket default event hold
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Set_a_bucket_default_event_hold"></a>

The following example enables Object Lock on a bucket and configures a default retention that places an event hold with a 365-day duration on every new object. While the event hold is active, the object version is protected; when the hold is released, AWS retains the object version for 365 days from the release time. A default event hold is useful as a ransomware recovery window or to start the retention countdown from a business event.

#### JSON
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Set_a_bucket_default_event_hold--json"></a>

```
{
  "Resources": {
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket1",
        "ObjectLockEnabled": true,
        "ObjectLockConfiguration": {
          "ObjectLockEnabled": "Enabled",
          "Rule": {
            "DefaultRetention": {
              "Mode": "COMPLIANCE",
              "DefaultEventHold": {
                "Days": 365
              }
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Set_a_bucket_default_event_hold--yaml"></a>

```
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    Properties:
      BucketName: amzn-s3-demo-bucket1
      ObjectLockEnabled: true
      ObjectLockConfiguration:
        ObjectLockEnabled: Enabled
        Rule:
          DefaultRetention:
            Mode: COMPLIANCE
            DefaultEventHold:
              Days: 365
```

### Combine a default retention period with an event hold
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Combine_a_default_retention_period_with_an_event_hold"></a>

The following example configures a bucket default that combines a fixed retention period with an event hold. The event hold duration can't exceed the default retention period, so a 1-year event hold is valid alongside a 2-year retention period.

#### JSON
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Combine_a_default_retention_period_with_an_event_hold--json"></a>

```
{
  "Resources": {
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket1",
        "ObjectLockEnabled": true,
        "ObjectLockConfiguration": {
          "ObjectLockEnabled": "Enabled",
          "Rule": {
            "DefaultRetention": {
              "Mode": "GOVERNANCE",
              "Years": 2,
              "DefaultEventHold": {
                "Years": 1
              }
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-defaulteventhold--examples--Combine_a_default_retention_period_with_an_event_hold--yaml"></a>

```
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    Properties:
      BucketName: amzn-s3-demo-bucket1
      ObjectLockEnabled: true
      ObjectLockConfiguration:
        ObjectLockEnabled: Enabled
        Rule:
          DefaultRetention:
            Mode: GOVERNANCE
            Years: 2
            DefaultEventHold:
              Years: 1
```
