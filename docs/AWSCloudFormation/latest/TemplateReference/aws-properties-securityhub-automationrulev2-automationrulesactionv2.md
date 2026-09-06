---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-automationrulesactionv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 AutomationRulesActionV2
<a name="aws-properties-securityhub-automationrulev2-automationrulesactionv2"></a>

Allows you to configure automated responses.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-automationrulesactionv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-automationrulesactionv2-syntax.json"></a>

```
{
  "[ExternalIntegrationConfiguration](#cfn-securityhub-automationrulev2-automationrulesactionv2-externalintegrationconfiguration)" : {{ExternalIntegrationConfiguration}},
  "[FindingFieldsUpdate](#cfn-securityhub-automationrulev2-automationrulesactionv2-findingfieldsupdate)" : {{AutomationRulesFindingFieldsUpdateV2}},
  "[Type](#cfn-securityhub-automationrulev2-automationrulesactionv2-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-automationrulesactionv2-syntax.yaml"></a>

```
  [ExternalIntegrationConfiguration](#cfn-securityhub-automationrulev2-automationrulesactionv2-externalintegrationconfiguration): {{
    ExternalIntegrationConfiguration}}
  [FindingFieldsUpdate](#cfn-securityhub-automationrulev2-automationrulesactionv2-findingfieldsupdate): {{
    AutomationRulesFindingFieldsUpdateV2}}
  [Type](#cfn-securityhub-automationrulev2-automationrulesactionv2-type): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-automationrulesactionv2-properties"></a>

`ExternalIntegrationConfiguration`  <a name="cfn-securityhub-automationrulev2-automationrulesactionv2-externalintegrationconfiguration"></a>
The settings for integrating automation rule actions with external systems or service.
*Required*: No
*Type*: [ExternalIntegrationConfiguration](aws-properties-securityhub-automationrulev2-externalintegrationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingFieldsUpdate`  <a name="cfn-securityhub-automationrulev2-automationrulesactionv2-findingfieldsupdate"></a>
 Specifies that the automation rule action is an update to a finding field.
*Required*: No
*Type*: [AutomationRulesFindingFieldsUpdateV2](aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-securityhub-automationrulev2-automationrulesactionv2-type"></a>
 Specifies the type of action that Security Hub CSPM takes when a finding matches the defined criteria of a rule.
*Required*: Yes
*Type*: String
*Allowed values*: `FINDING_FIELDS_UPDATE | EXTERNAL_INTEGRATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
