---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket MetadataConfiguration
<a name="aws-properties-s3-bucket-metadataconfiguration"></a>

 Creates a V2 Amazon S3 Metadata configuration of a general purpose bucket. For more information, see [ Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-metadataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-metadataconfiguration-syntax.json"></a>

```
{
  "[AnnotationTableConfiguration](#cfn-s3-bucket-metadataconfiguration-annotationtableconfiguration)" : {{AnnotationTableConfiguration}},
  "[Destination](#cfn-s3-bucket-metadataconfiguration-destination)" : {{MetadataDestination}},
  "[InventoryTableConfiguration](#cfn-s3-bucket-metadataconfiguration-inventorytableconfiguration)" : {{InventoryTableConfiguration}},
  "[JournalTableConfiguration](#cfn-s3-bucket-metadataconfiguration-journaltableconfiguration)" : {{JournalTableConfiguration}}
}
```

### YAML
<a name="aws-properties-s3-bucket-metadataconfiguration-syntax.yaml"></a>

```
  [AnnotationTableConfiguration](#cfn-s3-bucket-metadataconfiguration-annotationtableconfiguration): {{
    AnnotationTableConfiguration}}
  [Destination](#cfn-s3-bucket-metadataconfiguration-destination): {{
    MetadataDestination}}
  [InventoryTableConfiguration](#cfn-s3-bucket-metadataconfiguration-inventorytableconfiguration): {{
    InventoryTableConfiguration}}
  [JournalTableConfiguration](#cfn-s3-bucket-metadataconfiguration-journaltableconfiguration): {{
    JournalTableConfiguration}}
```

## Properties
<a name="aws-properties-s3-bucket-metadataconfiguration-properties"></a>

`AnnotationTableConfiguration`  <a name="cfn-s3-bucket-metadataconfiguration-annotationtableconfiguration"></a>
The annotation table configuration for a metadata configuration.
*Required*: No
*Type*: [AnnotationTableConfiguration](aws-properties-s3-bucket-annotationtableconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-s3-bucket-metadataconfiguration-destination"></a>
 The destination information for the S3 Metadata configuration.
*Required*: No
*Type*: [MetadataDestination](aws-properties-s3-bucket-metadatadestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InventoryTableConfiguration`  <a name="cfn-s3-bucket-metadataconfiguration-inventorytableconfiguration"></a>
 The inventory table configuration for a metadata configuration.
*Required*: No
*Type*: [InventoryTableConfiguration](aws-properties-s3-bucket-inventorytableconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JournalTableConfiguration`  <a name="cfn-s3-bucket-metadataconfiguration-journaltableconfiguration"></a>
 The journal table configuration for a metadata configuration.
*Required*: Yes
*Type*: [JournalTableConfiguration](aws-properties-s3-bucket-journaltableconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-metadataconfiguration--examples"></a>

### Create a metadata configuration
<a name="aws-properties-s3-bucket-metadataconfiguration--examples--Create_a_metadata_configuration"></a>

The following example creates an S3 Metadata configuration for the specified general purpose bucket. To use this example, replace ` {{amzn-s3-demo-bucket}} ` with the name of your general purpose bucket. Also make sure to update the AWS Identity and Access Management (IAM) Amazon Resource Name (ARN) with the name of the IAM role that you want to use.

#### JSON
<a name="aws-properties-s3-bucket-metadataconfiguration--examples--Create_a_metadata_configuration--json"></a>

```
{
  "Resources": {
    "S3MetadataKMSKey": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "Description": "KMS key for S3 metadata encryption",
        "EnableKeyRotation": true,
        "KeyPolicy": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": {
                  "Fn::Sub": "arn:aws:iam::${AWS::AccountId}:role/SpecificRoleName"
                }
              },
              "Action": "kms:*",
              "Resource": "*"
            },
            {
              "Sid": "Allow S3 Metadata Service",
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "maintenance.s3tables.amazonaws.com",
                  "metadata.s3.amazonaws.com"
                ]
              },
              "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
              ],
              "Resource": "*"
            }
          ]
        }
      }
    },
    "S3MetadataKMSKeyAlias": {
      "Type": "AWS::KMS::Alias",
      "Properties": {
        "AliasName": "alias/s3-metadata-key",
        "TargetKeyId": {
          "Ref": "S3MetadataKMSKey"
        }
      }
    },
    "TestMetadataBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "{{amzn-s3-demo-bucket}}",
        "MetadataConfiguration": {
          "JournalTableConfiguration": {
            "RecordExpiration": {
              "Expiration": "ENABLED",
              "Days": 10
            },
            "EncryptionConfiguration": {
              "SseAlgorithm": "aws:kms",
              "KmsKeyArn": {
                "Fn::GetAtt": [
                  "S3MetadataKMSKey",
                  "Arn"
                ]
              }
            }
          },
          "InventoryTableConfiguration": {
            "ConfigurationState": "ENABLED",
            "EncryptionConfiguration": {
              "SseAlgorithm": "aws:kms",
              "KmsKeyArn": {
                "Fn::GetAtt": [
                  "S3MetadataKMSKey",
                  "Arn"
                ]
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
<a name="aws-properties-s3-bucket-metadataconfiguration--examples--Create_a_metadata_configuration--yaml"></a>

```
Resources:
  S3MetadataKMSKey:
    Type: 'AWS::KMS::Key'
    Properties:
      Description: 'KMS key for S3 metadata encryption'
      EnableKeyRotation: true
      KeyPolicy:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Sid: 'Enable IAM User Permissions'
            Effect: Allow
            Principal:
              AWS: !Sub 'arn:aws:iam::${AWS::AccountId}:role/SpecificRoleName'
            Action: 'kms:*'
            Resource: '*'
          - Sid: 'Allow S3 Metadata Service'
            Effect: Allow
            Principal:
              Service:
                - 'maintenance.s3tables.amazonaws.com'
                - 'metadata.s3.amazonaws.com'
            Action:
              - 'kms:Decrypt'
              - 'kms:GenerateDataKey'
            Resource: '*'

  S3MetadataKMSKeyAlias:
    Type: 'AWS::KMS::Alias'
    Properties:
      AliasName: 'alias/s3-metadata-key'
      TargetKeyId: !Ref S3MetadataKMSKey

  TestMetadataBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: {{amzn-s3-demo-bucket}}
      MetadataConfiguration:
        JournalTableConfiguration:
          RecordExpiration:
            Expiration: ENABLED
            Days: 10
          EncryptionConfiguration:
            SseAlgorithm: aws:kms
            KmsKeyArn: !GetAtt S3MetadataKMSKey.Arn
        InventoryTableConfiguration:
          ConfigurationState: ENABLED
          EncryptionConfiguration:
            SseAlgorithm: aws:kms
            KmsKeyArn: !GetAtt S3MetadataKMSKey.Arn
```
