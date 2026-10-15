---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbbackup-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBBackup S3Configuration
<a name="aws-properties-timestream-influxdbbackup-s3configuration"></a>

The configuration that specifies an S3 location.

## Syntax
<a name="aws-properties-timestream-influxdbbackup-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbbackup-s3configuration-syntax.json"></a>

```
{
  "[BucketName](#cfn-timestream-influxdbbackup-s3configuration-bucketname)" : {{String}},
  "[Enabled](#cfn-timestream-influxdbbackup-s3configuration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbbackup-s3configuration-syntax.yaml"></a>

```
  [BucketName](#cfn-timestream-influxdbbackup-s3configuration-bucketname): {{String}}
  [Enabled](#cfn-timestream-influxdbbackup-s3configuration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-timestream-influxdbbackup-s3configuration-properties"></a>

`BucketName`  <a name="cfn-timestream-influxdbbackup-s3configuration-bucketname"></a>
The bucket name of the customer S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-timestream-influxdbbackup-s3configuration-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
