---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-codesigning.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate CodeSigning
<a name="aws-properties-iot-otaupdate-codesigning"></a>

Describes the method to use when code signing a file.

## Syntax
<a name="aws-properties-iot-otaupdate-codesigning-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-codesigning-syntax.json"></a>

```
{
  "[AwsSignerJobId](#cfn-iot-otaupdate-codesigning-awssignerjobid)" : {{String}},
  "[CustomCodeSigning](#cfn-iot-otaupdate-codesigning-customcodesigning)" : {{CustomCodeSigning}},
  "[StartSigningJobParameter](#cfn-iot-otaupdate-codesigning-startsigningjobparameter)" : {{StartSigningJobParameter}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-codesigning-syntax.yaml"></a>

```
  [AwsSignerJobId](#cfn-iot-otaupdate-codesigning-awssignerjobid): {{String}}
  [CustomCodeSigning](#cfn-iot-otaupdate-codesigning-customcodesigning): {{
    CustomCodeSigning}}
  [StartSigningJobParameter](#cfn-iot-otaupdate-codesigning-startsigningjobparameter): {{
    StartSigningJobParameter}}
```

## Properties
<a name="aws-properties-iot-otaupdate-codesigning-properties"></a>

`AwsSignerJobId`  <a name="cfn-iot-otaupdate-codesigning-awssignerjobid"></a>
The ID of the `AWSSignerJob` which was created to sign the file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomCodeSigning`  <a name="cfn-iot-otaupdate-codesigning-customcodesigning"></a>
A custom method for code signing a file.
*Required*: No
*Type*: [CustomCodeSigning](aws-properties-iot-otaupdate-customcodesigning.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartSigningJobParameter`  <a name="cfn-iot-otaupdate-codesigning-startsigningjobparameter"></a>
Describes the code-signing job.
*Required*: No
*Type*: [StartSigningJobParameter](aws-properties-iot-otaupdate-startsigningjobparameter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
