---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbinstance-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBInstance S3Configuration
<a name="aws-properties-timestream-influxdbinstance-s3configuration"></a>

Configuration for S3 bucket log delivery.

## Syntax
<a name="aws-properties-timestream-influxdbinstance-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbinstance-s3configuration-syntax.json"></a>

```
{
  "[BucketName](#cfn-timestream-influxdbinstance-s3configuration-bucketname)" : {{String}},
  "[Enabled](#cfn-timestream-influxdbinstance-s3configuration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbinstance-s3configuration-syntax.yaml"></a>

```
  [BucketName](#cfn-timestream-influxdbinstance-s3configuration-bucketname): {{String}}
  [Enabled](#cfn-timestream-influxdbinstance-s3configuration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-timestream-influxdbinstance-s3configuration-properties"></a>

`BucketName`  <a name="cfn-timestream-influxdbinstance-s3configuration-bucketname"></a>
The bucket name of the customer S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-timestream-influxdbinstance-s3configuration-enabled"></a>
Indicates whether log delivery to the S3 bucket is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
