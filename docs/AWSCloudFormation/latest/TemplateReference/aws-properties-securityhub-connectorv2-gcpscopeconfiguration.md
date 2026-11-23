---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-gcpscopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 GcpScopeConfiguration

<a name="aws-properties-securityhub-connectorv2-gcpscopeconfiguration-description"></a>The `GcpScopeConfiguration` property type specifies Property description not available. for an [AWS::SecurityHub::ConnectorV2](aws-resource-securityhub-connectorv2.md).

## Syntax
<a name="aws-properties-securityhub-connectorv2-gcpscopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-gcpscopeconfiguration-syntax.json"></a>

```json
{
  "[ScopeType](#cfn-securityhub-connectorv2-gcpscopeconfiguration-scopetype)" : {{String}},
  "[ScopeValues](#cfn-securityhub-connectorv2-gcpscopeconfiguration-scopevalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-gcpscopeconfiguration-syntax.yaml"></a>

```yaml
  [ScopeType](#cfn-securityhub-connectorv2-gcpscopeconfiguration-scopetype): {{String}}
  [ScopeValues](#cfn-securityhub-connectorv2-gcpscopeconfiguration-scopevalues): {{
    - String}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-gcpscopeconfiguration-properties"></a>

`ScopeType`  <a name="cfn-securityhub-connectorv2-gcpscopeconfiguration-scopetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PROJECT | ORGANIZATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeValues`  <a name="cfn-securityhub-connectorv2-gcpscopeconfiguration-scopevalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
