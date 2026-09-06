---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction UpdateDeviceCertificateParams
<a name="aws-properties-iot-mitigationaction-updatedevicecertificateparams"></a>

Parameters to define a mitigation action that changes the state of the device certificate to inactive.

## Syntax
<a name="aws-properties-iot-mitigationaction-updatedevicecertificateparams-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-mitigationaction-updatedevicecertificateparams-syntax.json"></a>

```
{
  "[Action](#cfn-iot-mitigationaction-updatedevicecertificateparams-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-mitigationaction-updatedevicecertificateparams-syntax.yaml"></a>

```
  [Action](#cfn-iot-mitigationaction-updatedevicecertificateparams-action): {{String}}
```

## Properties
<a name="aws-properties-iot-mitigationaction-updatedevicecertificateparams-properties"></a>

`Action`  <a name="cfn-iot-mitigationaction-updatedevicecertificateparams-action"></a>
The action that you want to apply to the device certificate. The only supported value is `DEACTIVATE`.
*Required*: Yes
*Type*: String
*Allowed values*: `DEACTIVATE | UNSET_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
