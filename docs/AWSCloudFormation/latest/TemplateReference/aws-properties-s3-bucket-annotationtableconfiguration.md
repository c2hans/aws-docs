---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-annotationtableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket AnnotationTableConfiguration
<a name="aws-properties-s3-bucket-annotationtableconfiguration"></a>

The annotation table configuration for an S3 Metadata configuration. The annotation table tracks all annotations on objects in your bucket so that you can query annotation data at scale.

**Note**
If you've disabled your annotation table configuration and now want to re-enable it, you must first manually delete the old annotation table from your AWS managed table bucket. Otherwise, the newly re-enabled annotation table configuration will enter a failed state because the annotation table already exists in the table bucket.

## Syntax
<a name="aws-properties-s3-bucket-annotationtableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-annotationtableconfiguration-syntax.json"></a>

```
{
  "[ConfigurationState](#cfn-s3-bucket-annotationtableconfiguration-configurationstate)" : {{String}},
  "[EncryptionConfiguration](#cfn-s3-bucket-annotationtableconfiguration-encryptionconfiguration)" : {{MetadataTableEncryptionConfiguration}},
  "[Role](#cfn-s3-bucket-annotationtableconfiguration-role)" : {{String}},
  "[TableArn](#cfn-s3-bucket-annotationtableconfiguration-tablearn)" : {{String}},
  "[TableName](#cfn-s3-bucket-annotationtableconfiguration-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-annotationtableconfiguration-syntax.yaml"></a>

```
  [ConfigurationState](#cfn-s3-bucket-annotationtableconfiguration-configurationstate): {{String}}
  [EncryptionConfiguration](#cfn-s3-bucket-annotationtableconfiguration-encryptionconfiguration): {{
    MetadataTableEncryptionConfiguration}}
  [Role](#cfn-s3-bucket-annotationtableconfiguration-role): {{String}}
  [TableArn](#cfn-s3-bucket-annotationtableconfiguration-tablearn): {{String}}
  [TableName](#cfn-s3-bucket-annotationtableconfiguration-tablename): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-annotationtableconfiguration-properties"></a>

`ConfigurationState`  <a name="cfn-s3-bucket-annotationtableconfiguration-configurationstate"></a>
Specifies whether the annotation table configuration is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-s3-bucket-annotationtableconfiguration-encryptionconfiguration"></a>
The encryption configuration for the annotation table. To encrypt your annotation table with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS), set `SseAlgorithm` to `aws:kms`. You must also set `KmsKeyArn` to the ARN of a customer managed KMS key in the same Region where your general purpose bucket is located.
*Required*: No
*Type*: [MetadataTableEncryptionConfiguration](aws-properties-s3-bucket-metadatatableencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-s3-bucket-annotationtableconfiguration-role"></a>
The ARN of the IAM role that grants Amazon S3 Metadata permission to read annotations from your bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableArn`  <a name="cfn-s3-bucket-annotationtableconfiguration-tablearn"></a>
The Amazon Resource Name (ARN) for the annotation table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-s3-bucket-annotationtableconfiguration-tablename"></a>
The name of the annotation table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples"></a>

**Topics**
+ [Enable an annotation table with SSE-KMS encryption](#aws-properties-s3-bucket-annotationtableconfiguration--examples--Enable_an_annotation_table_with_SSE-KMS_encryption)
+ [Disable an annotation table](#aws-properties-s3-bucket-annotationtableconfiguration--examples--Disable_an_annotation_table)

### Enable an annotation table with SSE-KMS encryption
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Enable_an_annotation_table_with_SSE-KMS_encryption"></a>

The following example enables an annotation table configuration with server-side encryption using AWS KMS keys (SSE-KMS) for a bucket that already has a metadata configuration.

#### JSON
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Enable_an_annotation_table_with_SSE-KMS_encryption--json"></a>

```
{
  "Resources": {
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket1",
        "MetadataConfiguration": {
          "AnnotationTableConfiguration": {
            "ConfigurationState": "ENABLED",
            "EncryptionConfiguration": {
              "SseAlgorithm": "aws:kms",
              "KmsKeyArn": "arn:aws:kms:us-east-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
            },
            "Role": "arn:aws:iam::123456789012:role/my-annotation-role"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Enable_an_annotation_table_with_SSE-KMS_encryption--yaml"></a>

```
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    Properties:
      BucketName: amzn-s3-demo-bucket1
      MetadataConfiguration:
        AnnotationTableConfiguration:
          ConfigurationState: ENABLED
          EncryptionConfiguration:
            SseAlgorithm: 'aws:kms'
            KmsKeyArn: arn:aws:kms:us-east-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab
          Role: arn:aws:iam::123456789012:role/my-annotation-role
```

### Disable an annotation table
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Disable_an_annotation_table"></a>

The following example disables an annotation table configuration. Disabling the annotation table doesn't delete it. The annotation table is retained for your records until you decide to delete it.

#### JSON
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Disable_an_annotation_table--json"></a>

```
{
  "Resources": {
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket1",
        "MetadataConfiguration": {
          "AnnotationTableConfiguration": {
            "ConfigurationState": "DISABLED"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-annotationtableconfiguration--examples--Disable_an_annotation_table--yaml"></a>

```
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    Properties:
      BucketName: amzn-s3-demo-bucket1
      MetadataConfiguration:
        AnnotationTableConfiguration:
          ConfigurationState: DISABLED
```
