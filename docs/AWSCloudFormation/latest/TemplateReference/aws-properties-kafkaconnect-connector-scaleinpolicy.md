---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-scaleinpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector ScaleInPolicy
<a name="aws-properties-kafkaconnect-connector-scaleinpolicy"></a>

The scale-in policy for the connector.

## Syntax
<a name="aws-properties-kafkaconnect-connector-scaleinpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-scaleinpolicy-syntax.json"></a>

```
{
  "[CpuUtilizationPercentage](#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-scaleinpolicy-syntax.yaml"></a>

```
  [CpuUtilizationPercentage](#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage): {{Integer}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-scaleinpolicy-properties"></a>

`CpuUtilizationPercentage`  <a name="cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage"></a>
Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
