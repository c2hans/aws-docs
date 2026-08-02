---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-mitigationaction-updatecacertificateparams.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction UpdateCACertificateParams
<a name="aws-properties-iot-mitigationaction-updatecacertificateparams"></a>

Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

## Syntax
<a name="aws-properties-iot-mitigationaction-updatecacertificateparams-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-mitigationaction-updatecacertificateparams-syntax.json"></a>

```
{
  "[Action](#cfn-iot-mitigationaction-updatecacertificateparams-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-mitigationaction-updatecacertificateparams-syntax.yaml"></a>

```
  [Action](#cfn-iot-mitigationaction-updatecacertificateparams-action): {{String}}
```

## Properties
<a name="aws-properties-iot-mitigationaction-updatecacertificateparams-properties"></a>

`Action`  <a name="cfn-iot-mitigationaction-updatecacertificateparams-action"></a>
The action that you want to apply to the CA certificate. The only supported value is `DEACTIVATE`.
*Required*: Yes
*Type*: String
*Allowed values*: `DEACTIVATE | UNSET_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
