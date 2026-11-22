---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-azureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector AzureConfiguration

The configuration for connecting to Microsoft Azure, including the tenant and application details.

## Syntax
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-syntax.json"></a>

```json
{
  "[ApplicationDisplayName](#cfn-ssm-cloudconnector-azureconfiguration-applicationdisplayname)" : {{String}},
  "[ApplicationId](#cfn-ssm-cloudconnector-azureconfiguration-applicationid)" : {{String}},
  "[Targets](#cfn-ssm-cloudconnector-azureconfiguration-targets)" : {{ConfigurationTargets}},
  "[TenantDisplayName](#cfn-ssm-cloudconnector-azureconfiguration-tenantdisplayname)" : {{String}},
  "[TenantId](#cfn-ssm-cloudconnector-azureconfiguration-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-syntax.yaml"></a>

```yaml
  [ApplicationDisplayName](#cfn-ssm-cloudconnector-azureconfiguration-applicationdisplayname): {{String}}
  [ApplicationId](#cfn-ssm-cloudconnector-azureconfiguration-applicationid): {{String}}
  [Targets](#cfn-ssm-cloudconnector-azureconfiguration-targets): {{
    ConfigurationTargets}}
  [TenantDisplayName](#cfn-ssm-cloudconnector-azureconfiguration-tenantdisplayname): {{String}}
  [TenantId](#cfn-ssm-cloudconnector-azureconfiguration-tenantid): {{String}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-properties"></a>

`ApplicationDisplayName`  <a name="cfn-ssm-cloudconnector-azureconfiguration-applicationdisplayname"></a>
The display name of the Azure AD application.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-ssm-cloudconnector-azureconfiguration-applicationid"></a>
The Azure AD application (client) ID used for authentication.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-ssm-cloudconnector-azureconfiguration-targets"></a>
The targets for the cloud connector. If you omit this property, the connector targets the entire Azure tenant.
*Required*: No
*Type*: [ConfigurationTargets](aws-properties-ssm-cloudconnector-configurationtargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantDisplayName`  <a name="cfn-ssm-cloudconnector-azureconfiguration-tenantdisplayname"></a>
The display name of the Azure AD tenant.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-ssm-cloudconnector-azureconfiguration-tenantid"></a>
The Azure Active Directory (Azure AD) tenant ID. You cannot change this value after you create the connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
