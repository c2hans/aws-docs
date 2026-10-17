---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-devopsagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service DevOpsAgentConfiguration
<a name="aws-properties-resiliencehubv2-service-devopsagentconfiguration"></a>

The AWS DevOps Agent (DevOps Agent) integration configuration that you supply when creating or updating a service. Connecting a service to an Agent Space lets DevOps Agent investigate the service's resilience test runs and attach its analysis to the results. Include this block with an Agent Space Amazon Resource Name (ARN) to connect or reconnect the service to an Agent Space. Include it without an Agent Space ARN to disconnect the service. Omit it to leave the existing linkage unchanged.

## Syntax
<a name="aws-properties-resiliencehubv2-service-devopsagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-devopsagentconfiguration-syntax.json"></a>

```
{
  "[AgentSpaceArn](#cfn-resiliencehubv2-service-devopsagentconfiguration-agentspacearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-devopsagentconfiguration-syntax.yaml"></a>

```
  [AgentSpaceArn](#cfn-resiliencehubv2-service-devopsagentconfiguration-agentspacearn): {{String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-devopsagentconfiguration-properties"></a>

`AgentSpaceArn`  <a name="cfn-resiliencehubv2-service-devopsagentconfiguration-agentspacearn"></a>
The ARN of the DevOps Agent Agent Space to link to this service.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
