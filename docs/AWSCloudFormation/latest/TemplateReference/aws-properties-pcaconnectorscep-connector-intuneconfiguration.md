---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorscep-connector-intuneconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorSCEP::Connector IntuneConfiguration
<a name="aws-properties-pcaconnectorscep-connector-intuneconfiguration"></a>

Contains configuration details for use with Microsoft Intune. For information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).

When you use Connector for SCEP for Microsoft Intune, certain functionalities are enabled by accessing Microsoft Intune through the Microsoft API. Your use of the Connector for SCEP and accompanying AWS services doesn't remove your need to have a valid license for your use of the Microsoft Intune service. You should also review the [Microsoft Intune® App Protection Policies](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy).

## Syntax
<a name="aws-properties-pcaconnectorscep-connector-intuneconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorscep-connector-intuneconfiguration-syntax.json"></a>

```
{
  "[AzureApplicationId](#cfn-pcaconnectorscep-connector-intuneconfiguration-azureapplicationid)" : {{String}},
  "[Domain](#cfn-pcaconnectorscep-connector-intuneconfiguration-domain)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcaconnectorscep-connector-intuneconfiguration-syntax.yaml"></a>

```
  [AzureApplicationId](#cfn-pcaconnectorscep-connector-intuneconfiguration-azureapplicationid): {{String}}
  [Domain](#cfn-pcaconnectorscep-connector-intuneconfiguration-domain): {{String}}
```

## Properties
<a name="aws-properties-pcaconnectorscep-connector-intuneconfiguration-properties"></a>

`AzureApplicationId`  <a name="cfn-pcaconnectorscep-connector-intuneconfiguration-azureapplicationid"></a>
The directory (tenant) ID from your Microsoft Entra ID app registration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}$`
*Minimum*: `15`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Domain`  <a name="cfn-pcaconnectorscep-connector-intuneconfiguration-domain"></a>
The primary domain from your Microsoft Entra ID app registration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
