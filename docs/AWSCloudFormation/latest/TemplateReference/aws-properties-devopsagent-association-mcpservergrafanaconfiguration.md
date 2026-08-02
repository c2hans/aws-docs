---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-mcpservergrafanaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association MCPServerGrafanaConfiguration
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration"></a>

<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-description"></a>The `MCPServerGrafanaConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[Endpoint](#cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint)" : {{String}},
  "[Tools](#cfn-devopsagent-association-mcpservergrafanaconfiguration-tools)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates): {{Boolean}}
  [Endpoint](#cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint): {{String}}
  [Tools](#cfn-devopsagent-association-mcpservergrafanaconfiguration-tools): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tools`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-tools"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `alerting | annotations | asserts | cloudwatch | dashboard | datasource | elasticsearch | examples | incident | loki | navigation | oncall | prometheus | pyroscope | rendering | runpanelquery | search | searchlogs | sift`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
