---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-sourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase SourceConfiguration
<a name="aws-properties-wisdom-knowledgebase-sourceconfiguration"></a>

Configuration information about the external data source.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-sourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-sourceconfiguration-syntax.json"></a>

```
{
  "[AppIntegrations](#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations)" : {{AppIntegrationsConfiguration}},
  "[ManagedSourceConfiguration](#cfn-wisdom-knowledgebase-sourceconfiguration-managedsourceconfiguration)" : {{ManagedSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-sourceconfiguration-syntax.yaml"></a>

```
  [AppIntegrations](#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations): {{
    AppIntegrationsConfiguration}}
  [ManagedSourceConfiguration](#cfn-wisdom-knowledgebase-sourceconfiguration-managedsourceconfiguration): {{
    ManagedSourceConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-sourceconfiguration-properties"></a>

`AppIntegrations`  <a name="cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations"></a>
Configuration information for Amazon AppIntegrations to automatically ingest content.
*Required*: No
*Type*: [AppIntegrationsConfiguration](aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedSourceConfiguration`  <a name="cfn-wisdom-knowledgebase-sourceconfiguration-managedsourceconfiguration"></a>
Source configuration for managed resources.
*Required*: No
*Type*: [ManagedSourceConfiguration](aws-properties-wisdom-knowledgebase-managedsourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
