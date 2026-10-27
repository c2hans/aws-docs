---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-codesigningsignature.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate CodeSigningSignature
<a name="aws-properties-iot-otaupdate-codesigningsignature"></a>

Describes the signature for a file.

## Syntax
<a name="aws-properties-iot-otaupdate-codesigningsignature-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-codesigningsignature-syntax.json"></a>

```
{
  "[InlineDocument](#cfn-iot-otaupdate-codesigningsignature-inlinedocument)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-codesigningsignature-syntax.yaml"></a>

```
  [InlineDocument](#cfn-iot-otaupdate-codesigningsignature-inlinedocument): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-codesigningsignature-properties"></a>

`InlineDocument`  <a name="cfn-iot-otaupdate-codesigningsignature-inlinedocument"></a>
A base64 encoded binary representation of the code signing signature.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
