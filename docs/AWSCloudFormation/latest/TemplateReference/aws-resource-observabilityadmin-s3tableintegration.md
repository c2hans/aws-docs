---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-s3tableintegration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::S3TableIntegration
<a name="aws-resource-observabilityadmin-s3tableintegration"></a>

Creates an integration between CloudWatch and S3 Tables for analytics. This integration enables querying CloudWatch telemetry data using analytics engines like Amazon Athena, Amazon Redshift, and Apache Spark.

## Syntax
<a name="aws-resource-observabilityadmin-s3tableintegration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-s3tableintegration-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::S3TableIntegration",
  "Properties" : {
      "[Encryption](#cfn-observabilityadmin-s3tableintegration-encryption)" : {{EncryptionConfig}},
      "[LogSources](#cfn-observabilityadmin-s3tableintegration-logsources)" : {{[ LogSource, ... ]}},
      "[RoleArn](#cfn-observabilityadmin-s3tableintegration-rolearn)" : {{String}},
      "[Tags](#cfn-observabilityadmin-s3tableintegration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-s3tableintegration-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::S3TableIntegration
Properties:
  [Encryption](#cfn-observabilityadmin-s3tableintegration-encryption): {{
    EncryptionConfig}}
  [LogSources](#cfn-observabilityadmin-s3tableintegration-logsources): {{
    - LogSource}}
  [RoleArn](#cfn-observabilityadmin-s3tableintegration-rolearn): {{String}}
  [Tags](#cfn-observabilityadmin-s3tableintegration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-s3tableintegration-properties"></a>

`Encryption`  <a name="cfn-observabilityadmin-s3tableintegration-encryption"></a>
Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.
*Required*: Yes
*Type*: [EncryptionConfig](aws-properties-observabilityadmin-s3tableintegration-encryptionconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogSources`  <a name="cfn-observabilityadmin-s3tableintegration-logsources"></a>
A data source with an S3 Table integration for query access in the `logs` namespace.
*Required*: No
*Type*: Array of [LogSource](aws-properties-observabilityadmin-s3tableintegration-logsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-observabilityadmin-s3tableintegration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-observabilityadmin-s3tableintegration-tags"></a>
The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-s3tableintegration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-s3tableintegration-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-s3tableintegration-return-values-ref"></a>

The Amazon Resource Name (ARN) of the created S3 Table integration.

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-s3tableintegration-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-s3tableintegration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the S3 Table integration.
