---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-capabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association Capabilities

The automated AWS DevOps Agent capabilities for the repository in this association.

## Syntax
<a name="aws-properties-devopsagent-association-capabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-capabilities-syntax.json"></a>

```json
{
  "[CodeChangeRiskAnalysis](#cfn-devopsagent-association-capabilities-codechangeriskanalysis)" : {{CapabilityConfiguration}},
  "[CodeChangeRiskAnalysisAutomatedTesting](#cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting)" : {{AutomatedTestingCapabilityConfiguration}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-capabilities-syntax.yaml"></a>

```yaml
  [CodeChangeRiskAnalysis](#cfn-devopsagent-association-capabilities-codechangeriskanalysis): {{
    CapabilityConfiguration}}
  [CodeChangeRiskAnalysisAutomatedTesting](#cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting): {{
    AutomatedTestingCapabilityConfiguration}}
```

## Properties
<a name="aws-properties-devopsagent-association-capabilities-properties"></a>

`CodeChangeRiskAnalysis`  <a name="cfn-devopsagent-association-capabilities-codechangeriskanalysis"></a>
The configuration for code change risk analysis. With this capability, AWS DevOps Agent analyzes pull requests and merge requests for deployment risk.
*Required*: No
*Type*: [CapabilityConfiguration](aws-properties-devopsagent-association-capabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeChangeRiskAnalysisAutomatedTesting`  <a name="cfn-devopsagent-association-capabilities-codechangeriskanalysisautomatedtesting"></a>
The configuration for automated testing during code change risk analysis. With this capability, AWS DevOps Agent also runs tests against the change as part of the analysis.
*Required*: No
*Type*: [AutomatedTestingCapabilityConfiguration](aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
