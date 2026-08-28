---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource S3ReferenceDataSource
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource"></a>

For an SQL-based Amazon Kinesis Data Analytics application, identifies the Amazon S3 bucket and object that contains the reference data.

A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) operation to trigger reloading of data into your application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-syntax.json"></a>

```
{
  "[BucketARN](#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn)" : {{String}},
  "[FileKey](#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-syntax.yaml"></a>

```
  [BucketARN](#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn): {{String}}
  [FileKey](#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-properties"></a>

`BucketARN`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileKey`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey"></a>
The object key name containing the reference data.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource--seealso"></a>
+ [S3ReferenceDataSource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ReferenceDataSource.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
