---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DeviceFleet EdgeOutputConfig
<a name="aws-properties-sagemaker-devicefleet-edgeoutputconfig"></a>

The output configuration for storing sample data collected by the fleet.

## Syntax
<a name="aws-properties-sagemaker-devicefleet-edgeoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-devicefleet-edgeoutputconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid)" : {{String}},
  "[S3OutputLocation](#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-devicefleet-edgeoutputconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid): {{String}}
  [S3OutputLocation](#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-devicefleet-edgeoutputconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume after compilation job. If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3OutputLocation`  <a name="cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation"></a>
The Amazon Simple Storage (S3) bucket URI.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
