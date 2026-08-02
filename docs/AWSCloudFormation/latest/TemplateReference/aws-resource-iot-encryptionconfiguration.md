---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::EncryptionConfiguration
<a name="aws-resource-iot-encryptionconfiguration"></a>

Retrieves the encryption configuration for resources and data of your AWS account in AWS IoT Core. For more information, see [Data encryption at rest](https://docs.aws.amazon.com/iot/latest/developerguide/encryption-at-rest.html) in the *AWS IoT Core Developer Guide*.

## Syntax
<a name="aws-resource-iot-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-encryptionconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::EncryptionConfiguration",
  "Properties" : {
      "[EncryptionType](#cfn-iot-encryptionconfiguration-encryptiontype)" : {{String}},
      "[KmsAccessRoleArn](#cfn-iot-encryptionconfiguration-kmsaccessrolearn)" : {{String}},
      "[KmsKeyArn](#cfn-iot-encryptionconfiguration-kmskeyarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-encryptionconfiguration-syntax.yaml"></a>

```
Type: AWS::IoT::EncryptionConfiguration
Properties:
  [EncryptionType](#cfn-iot-encryptionconfiguration-encryptiontype): {{String}}
  [KmsAccessRoleArn](#cfn-iot-encryptionconfiguration-kmsaccessrolearn): {{String}}
  [KmsKeyArn](#cfn-iot-encryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-resource-iot-encryptionconfiguration-properties"></a>

`EncryptionType`  <a name="cfn-iot-encryptionconfiguration-encryptiontype"></a>
The type of the KMS key.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsAccessRoleArn`  <a name="cfn-iot-encryptionconfiguration-kmsaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role assumed by AWS IoT Core to call AWS KMS on behalf of the customer.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-iot-encryptionconfiguration-kmskeyarn"></a>
The ARN of the customer managed KMS key.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-encryptionconfiguration-return-values"></a>

### Ref
<a name="aws-resource-iot-encryptionconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the AWS account ID. For example:

 `{ "Ref": "MyEncryptionConfiguration" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-encryptionconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-encryptionconfiguration-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The unique identifier (ID) of an AWS account.

`LastModifiedDate`  <a name="LastModifiedDate-fn::getatt"></a>
The date when encryption configuration is last updated.

## Examples
<a name="aws-resource-iot-encryptionconfiguration--examples"></a>

The following example creates an encryption configuration using a customer managed AWS KMS key.

###
<a name="aws-resource-iot-encryptionconfiguration--examples--"></a>

#### JSON
<a name="aws-resource-iot-encryptionconfiguration--examples----json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyEncryptionConfiguration": {
      "Type": "AWS::IoT::EncryptionConfiguration",
      "Properties": {
        "EncryptionType": "CUSTOMER_MANAGED_KMS_KEY",
        "KmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/abcd1234-ab12-cd34-ef56-abcdef123456",
        "KmsAccessRoleArn": "arn:aws:iam::123456789012:role/IoTKmsAccessRole"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-iot-encryptionconfiguration--examples----yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyEncryptionConfiguration:
    Type: AWS::IoT::EncryptionConfiguration
    Properties:
      EncryptionType: CUSTOMER_MANAGED_KMS_KEY
      KmsKeyArn: arn:aws:kms:us-east-1:123456789012:key/abcd1234-ab12-cd34-ef56-abcdef123456
      KmsAccessRoleArn: arn:aws:iam::123456789012:role/IoTKmsAccessRole
```
