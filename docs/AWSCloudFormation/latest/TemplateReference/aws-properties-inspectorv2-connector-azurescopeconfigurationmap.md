---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-azurescopeconfigurationmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector AzureScopeConfigurationMap
<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap"></a>

<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap-description"></a>The `AzureScopeConfigurationMap` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap-syntax.json"></a>

```
{
  "[ContainerImageScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-containerimagescanning)" : {{ScopeConfiguration}},
  "[ServerlessScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-serverlessscanning)" : {{ScopeConfiguration}},
  "[VmScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-vmscanning)" : {{ScopeConfiguration}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap-syntax.yaml"></a>

```
  [ContainerImageScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-containerimagescanning): {{
    ScopeConfiguration}}
  [ServerlessScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-serverlessscanning): {{
    ScopeConfiguration}}
  [VmScanning](#cfn-inspectorv2-connector-azurescopeconfigurationmap-vmscanning): {{
    ScopeConfiguration}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-azurescopeconfigurationmap-properties"></a>

`ContainerImageScanning`  <a name="cfn-inspectorv2-connector-azurescopeconfigurationmap-containerimagescanning"></a>
Property description not available.
*Required*: No
*Type*: [ScopeConfiguration](aws-properties-inspectorv2-connector-scopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerlessScanning`  <a name="cfn-inspectorv2-connector-azurescopeconfigurationmap-serverlessscanning"></a>
Property description not available.
*Required*: No
*Type*: [ScopeConfiguration](aws-properties-inspectorv2-connector-scopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VmScanning`  <a name="cfn-inspectorv2-connector-azurescopeconfigurationmap-vmscanning"></a>
Property description not available.
*Required*: No
*Type*: [ScopeConfiguration](aws-properties-inspectorv2-connector-scopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
