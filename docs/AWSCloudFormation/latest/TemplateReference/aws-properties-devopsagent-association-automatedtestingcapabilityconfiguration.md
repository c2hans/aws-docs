---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association AutomatedTestingCapabilityConfiguration
<a name="aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration"></a>

The configuration for automated testing during code change risk analysis. This capability doesn't support trigger filter groups.

## Syntax
<a name="aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-devopsagent-association-automatedtestingcapabilityconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-devopsagent-association-automatedtestingcapabilityconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-devopsagent-association-automatedtestingcapabilityconfiguration-properties"></a>

`Enabled`  <a name="cfn-devopsagent-association-automatedtestingcapabilityconfiguration-enabled"></a>
Specifies whether automated testing is enabled for this association.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
