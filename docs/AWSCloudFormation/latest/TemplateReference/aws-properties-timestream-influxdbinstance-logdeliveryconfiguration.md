---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbinstance-logdeliveryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBInstance LogDeliveryConfiguration
<a name="aws-properties-timestream-influxdbinstance-logdeliveryconfiguration"></a>

Configuration for sending InfluxDB engine logs to a specified S3 bucket.

## Syntax
<a name="aws-properties-timestream-influxdbinstance-logdeliveryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbinstance-logdeliveryconfiguration-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-timestream-influxdbinstance-logdeliveryconfiguration-s3configuration)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbinstance-logdeliveryconfiguration-syntax.yaml"></a>

```
  [S3Configuration](#cfn-timestream-influxdbinstance-logdeliveryconfiguration-s3configuration): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-timestream-influxdbinstance-logdeliveryconfiguration-properties"></a>

`S3Configuration`  <a name="cfn-timestream-influxdbinstance-logdeliveryconfiguration-s3configuration"></a>
Configuration for S3 bucket log delivery
*Required*: Yes
*Type*: [S3Configuration](aws-properties-timestream-influxdbinstance-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
