---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-azureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector AzureConfiguration
<a name="aws-properties-ssm-cloudconnector-azureconfiguration"></a>

The access details and targets for connecting to a Microsoft Azure tenant, including the application registration used for authentication and the subscriptions to target.

## Syntax
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-azureconfiguration-syntax.json"></a>

```
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

```
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
The display name of the Azure application registration.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-ssm-cloudconnector-azureconfiguration-applicationid"></a>
The ID of the Azure application registration used for authentication.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-ssm-cloudconnector-azureconfiguration-targets"></a>
The target Azure subscriptions for the cloud connector.
*Required*: No
*Type*: [ConfigurationTargets](aws-properties-ssm-cloudconnector-configurationtargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantDisplayName`  <a name="cfn-ssm-cloudconnector-azureconfiguration-tenantdisplayname"></a>
The display name of the Azure tenant.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-ssm-cloudconnector-azureconfiguration-tenantid"></a>
The ID of the Azure tenant.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
