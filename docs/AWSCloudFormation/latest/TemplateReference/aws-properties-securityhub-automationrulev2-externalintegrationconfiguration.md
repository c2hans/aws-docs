---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-externalintegrationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 ExternalIntegrationConfiguration
<a name="aws-properties-securityhub-automationrulev2-externalintegrationconfiguration"></a>

The settings for integrating automation rule actions with external systems or service.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-externalintegrationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-externalintegrationconfiguration-syntax.json"></a>

```
{
  "[ConnectorArn](#cfn-securityhub-automationrulev2-externalintegrationconfiguration-connectorarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-externalintegrationconfiguration-syntax.yaml"></a>

```
  [ConnectorArn](#cfn-securityhub-automationrulev2-externalintegrationconfiguration-connectorarn): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-externalintegrationconfiguration-properties"></a>

`ConnectorArn`  <a name="cfn-securityhub-automationrulev2-externalintegrationconfiguration-connectorarn"></a>
The ARN of the connector that establishes the integration.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
