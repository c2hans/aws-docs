---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan PagerDutyConfiguration
<a name="aws-properties-ssmincidents-responseplan-pagerdutyconfiguration"></a>

Details about the PagerDuty configuration for a response plan.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-pagerdutyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-pagerdutyconfiguration-syntax.json"></a>

```
{
  "[Name](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-name)" : {{String}},
  "[PagerDutyIncidentConfiguration](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-pagerdutyincidentconfiguration)" : {{PagerDutyIncidentConfiguration}},
  "[SecretId](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-secretid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-pagerdutyconfiguration-syntax.yaml"></a>

```
  [Name](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-name): {{String}}
  [PagerDutyIncidentConfiguration](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-pagerdutyincidentconfiguration): {{
    PagerDutyIncidentConfiguration}}
  [SecretId](#cfn-ssmincidents-responseplan-pagerdutyconfiguration-secretid): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-pagerdutyconfiguration-properties"></a>

`Name`  <a name="cfn-ssmincidents-responseplan-pagerdutyconfiguration-name"></a>
The name of the PagerDuty configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDutyIncidentConfiguration`  <a name="cfn-ssmincidents-responseplan-pagerdutyconfiguration-pagerdutyincidentconfiguration"></a>
Details about the PagerDuty service associated with the configuration.
*Required*: Yes
*Type*: [PagerDutyIncidentConfiguration](aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretId`  <a name="cfn-ssmincidents-responseplan-pagerdutyconfiguration-secretid"></a>
The ID of the AWS Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
