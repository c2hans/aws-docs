---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-scopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector ScopeConfiguration
<a name="aws-properties-inspectorv2-connector-scopeconfiguration"></a>

<a name="aws-properties-inspectorv2-connector-scopeconfiguration-description"></a>The `ScopeConfiguration` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-scopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-scopeconfiguration-syntax.json"></a>

```
{
  "[ScopeType](#cfn-inspectorv2-connector-scopeconfiguration-scopetype)" : {{String}},
  "[ScopeValues](#cfn-inspectorv2-connector-scopeconfiguration-scopevalues)" : {{[ String, ... ]}},
  "[State](#cfn-inspectorv2-connector-scopeconfiguration-state)" : {{String}},
  "[StateReason](#cfn-inspectorv2-connector-scopeconfiguration-statereason)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-scopeconfiguration-syntax.yaml"></a>

```
  [ScopeType](#cfn-inspectorv2-connector-scopeconfiguration-scopetype): {{String}}
  [ScopeValues](#cfn-inspectorv2-connector-scopeconfiguration-scopevalues): {{
    - String}}
  [State](#cfn-inspectorv2-connector-scopeconfiguration-state): {{String}}
  [StateReason](#cfn-inspectorv2-connector-scopeconfiguration-statereason): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-scopeconfiguration-properties"></a>

`ScopeType`  <a name="cfn-inspectorv2-connector-scopeconfiguration-scopetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `TENANT | SUBSCRIPTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeValues`  <a name="cfn-inspectorv2-connector-scopeconfiguration-scopevalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-inspectorv2-connector-scopeconfiguration-state"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | PENDING | ERROR | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StateReason`  <a name="cfn-inspectorv2-connector-scopeconfiguration-statereason"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
