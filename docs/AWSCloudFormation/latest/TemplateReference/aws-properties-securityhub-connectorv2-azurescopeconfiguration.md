---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-azurescopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 AzureScopeConfiguration
<a name="aws-properties-securityhub-connectorv2-azurescopeconfiguration"></a>

The scope configuration for an Azure connector, defining the tenant or subscription scope.

## Syntax
<a name="aws-properties-securityhub-connectorv2-azurescopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-azurescopeconfiguration-syntax.json"></a>

```
{
  "[ScopeType](#cfn-securityhub-connectorv2-azurescopeconfiguration-scopetype)" : {{String}},
  "[ScopeValues](#cfn-securityhub-connectorv2-azurescopeconfiguration-scopevalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-azurescopeconfiguration-syntax.yaml"></a>

```
  [ScopeType](#cfn-securityhub-connectorv2-azurescopeconfiguration-scopetype): {{String}}
  [ScopeValues](#cfn-securityhub-connectorv2-azurescopeconfiguration-scopevalues): {{
    - String}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-azurescopeconfiguration-properties"></a>

`ScopeType`  <a name="cfn-securityhub-connectorv2-azurescopeconfiguration-scopetype"></a>
The type of scope. Valid values are `tenant` and `subscription`.
*Required*: Yes
*Type*: String
*Allowed values*: `TENANT | SUBSCRIPTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeValues`  <a name="cfn-securityhub-connectorv2-azurescopeconfiguration-scopevalues"></a>
The list of scope values, such as subscription IDs, when the scope type is `subscription`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
