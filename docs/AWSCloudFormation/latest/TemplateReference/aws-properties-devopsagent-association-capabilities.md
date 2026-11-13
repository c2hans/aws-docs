---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-capabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association Capabilities
<a name="aws-properties-devopsagent-association-capabilities"></a>

<a name="aws-properties-devopsagent-association-capabilities-description"></a>The `Capabilities` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-capabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-capabilities-syntax.json"></a>

```
{
  "[CodeChangeRiskAnalysis](#cfn-devopsagent-association-capabilities-codechangeriskanalysis)" : {{CapabilityConfiguration}},
  "[CodeChangeRiskAnalysisAutomatedTesting](#cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting)" : {{AutomatedTestingCapabilityConfiguration}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-capabilities-syntax.yaml"></a>

```
  [CodeChangeRiskAnalysis](#cfn-devopsagent-association-capabilities-codechangeriskanalysis): {{
    CapabilityConfiguration}}
  [CodeChangeRiskAnalysisAutomatedTesting](#cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting): {{
    AutomatedTestingCapabilityConfiguration}}
```

## Properties
<a name="aws-properties-devopsagent-association-capabilities-properties"></a>

`CodeChangeRiskAnalysis`  <a name="cfn-devopsagent-association-capabilities-codechangeriskanalysis"></a>
Property description not available.
*Required*: No
*Type*: [CapabilityConfiguration](aws-properties-devopsagent-association-capabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeChangeRiskAnalysisAutomatedTesting`  <a name="cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting"></a>
Property description not available.
*Required*: No
*Type*: [AutomatedTestingCapabilityConfiguration](aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
