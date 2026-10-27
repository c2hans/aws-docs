---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-startsigningjobparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate StartSigningJobParameter
<a name="aws-properties-iot-otaupdate-startsigningjobparameter"></a>

Information required to start a signing job.

## Syntax
<a name="aws-properties-iot-otaupdate-startsigningjobparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-startsigningjobparameter-syntax.json"></a>

```
{
  "[Destination](#cfn-iot-otaupdate-startsigningjobparameter-destination)" : {{Destination}},
  "[SigningProfileName](#cfn-iot-otaupdate-startsigningjobparameter-signingprofilename)" : {{String}},
  "[SigningProfileParameter](#cfn-iot-otaupdate-startsigningjobparameter-signingprofileparameter)" : {{SigningProfileParameter}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-startsigningjobparameter-syntax.yaml"></a>

```
  [Destination](#cfn-iot-otaupdate-startsigningjobparameter-destination): {{
    Destination}}
  [SigningProfileName](#cfn-iot-otaupdate-startsigningjobparameter-signingprofilename): {{String}}
  [SigningProfileParameter](#cfn-iot-otaupdate-startsigningjobparameter-signingprofileparameter): {{
    SigningProfileParameter}}
```

## Properties
<a name="aws-properties-iot-otaupdate-startsigningjobparameter-properties"></a>

`Destination`  <a name="cfn-iot-otaupdate-startsigningjobparameter-destination"></a>
The location to write the code-signed file.
*Required*: No
*Type*: [Destination](aws-properties-iot-otaupdate-destination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SigningProfileName`  <a name="cfn-iot-otaupdate-startsigningjobparameter-signingprofilename"></a>
The code-signing profile name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SigningProfileParameter`  <a name="cfn-iot-otaupdate-startsigningjobparameter-signingprofileparameter"></a>
Describes the code-signing profile.
*Required*: No
*Type*: [SigningProfileParameter](aws-properties-iot-otaupdate-signingprofileparameter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
