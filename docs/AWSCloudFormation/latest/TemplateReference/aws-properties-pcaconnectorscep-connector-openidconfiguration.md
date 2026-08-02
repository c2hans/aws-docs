---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorscep-connector-openidconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorSCEP::Connector OpenIdConfiguration
<a name="aws-properties-pcaconnectorscep-connector-openidconfiguration"></a>

Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune. For more information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).

## Syntax
<a name="aws-properties-pcaconnectorscep-connector-openidconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorscep-connector-openidconfiguration-syntax.json"></a>

```
{
  "[Audience](#cfn-pcaconnectorscep-connector-openidconfiguration-audience)" : {{String}},
  "[Issuer](#cfn-pcaconnectorscep-connector-openidconfiguration-issuer)" : {{String}},
  "[Subject](#cfn-pcaconnectorscep-connector-openidconfiguration-subject)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcaconnectorscep-connector-openidconfiguration-syntax.yaml"></a>

```
  [Audience](#cfn-pcaconnectorscep-connector-openidconfiguration-audience): {{String}}
  [Issuer](#cfn-pcaconnectorscep-connector-openidconfiguration-issuer): {{String}}
  [Subject](#cfn-pcaconnectorscep-connector-openidconfiguration-subject): {{String}}
```

## Properties
<a name="aws-properties-pcaconnectorscep-connector-openidconfiguration-properties"></a>

`Audience`  <a name="cfn-pcaconnectorscep-connector-openidconfiguration-audience"></a>
The audience value to copy into your Microsoft Entra app registration's OIDC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-pcaconnectorscep-connector-openidconfiguration-issuer"></a>
The issuer value to copy into your Microsoft Entra app registration's OIDC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subject`  <a name="cfn-pcaconnectorscep-connector-openidconfiguration-subject"></a>
The subject value to copy into your Microsoft Entra app registration's OIDC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
