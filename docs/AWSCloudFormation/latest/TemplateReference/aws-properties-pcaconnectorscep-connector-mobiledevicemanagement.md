---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorscep-connector-mobiledevicemanagement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorSCEP::Connector MobileDeviceManagement
<a name="aws-properties-pcaconnectorscep-connector-mobiledevicemanagement"></a>

If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. For information about considerations and limitations with using Connector for SCEP, see [Considerations and Limitations](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html).

If you provide an `IntuneConfiguration`, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).

## Syntax
<a name="aws-properties-pcaconnectorscep-connector-mobiledevicemanagement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorscep-connector-mobiledevicemanagement-syntax.json"></a>

```
{
  "[Intune](#cfn-pcaconnectorscep-connector-mobiledevicemanagement-intune)" : {{IntuneConfiguration}}
}
```

### YAML
<a name="aws-properties-pcaconnectorscep-connector-mobiledevicemanagement-syntax.yaml"></a>

```
  [Intune](#cfn-pcaconnectorscep-connector-mobiledevicemanagement-intune): {{
    IntuneConfiguration}}
```

## Properties
<a name="aws-properties-pcaconnectorscep-connector-mobiledevicemanagement-properties"></a>

`Intune`  <a name="cfn-pcaconnectorscep-connector-mobiledevicemanagement-intune"></a>
Configuration settings for use with Microsoft Intune. For information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).
*Required*: Yes
*Type*: [IntuneConfiguration](aws-properties-pcaconnectorscep-connector-intuneconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
