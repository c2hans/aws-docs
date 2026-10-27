---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-signingprofileparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate SigningProfileParameter
<a name="aws-properties-iot-otaupdate-signingprofileparameter"></a>

Describes the code-signing profile.

## Syntax
<a name="aws-properties-iot-otaupdate-signingprofileparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-signingprofileparameter-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-iot-otaupdate-signingprofileparameter-certificatearn)" : {{String}},
  "[CertificatePathOnDevice](#cfn-iot-otaupdate-signingprofileparameter-certificatepathondevice)" : {{String}},
  "[Platform](#cfn-iot-otaupdate-signingprofileparameter-platform)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-signingprofileparameter-syntax.yaml"></a>

```
  [CertificateArn](#cfn-iot-otaupdate-signingprofileparameter-certificatearn): {{String}}
  [CertificatePathOnDevice](#cfn-iot-otaupdate-signingprofileparameter-certificatepathondevice): {{String}}
  [Platform](#cfn-iot-otaupdate-signingprofileparameter-platform): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-signingprofileparameter-properties"></a>

`CertificateArn`  <a name="cfn-iot-otaupdate-signingprofileparameter-certificatearn"></a>
Certificate ARN.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificatePathOnDevice`  <a name="cfn-iot-otaupdate-signingprofileparameter-certificatepathondevice"></a>
The location of the code-signing certificate on your device.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Platform`  <a name="cfn-iot-otaupdate-signingprofileparameter-platform"></a>
The hardware platform of your device.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
