---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan PagerDutyIncidentConfiguration
<a name="aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration"></a>

Details about the PagerDuty service where the response plan creates an incident.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration-syntax.json"></a>

```
{
  "[ServiceId](#cfn-ssmincidents-responseplan-pagerdutyincidentconfiguration-serviceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration-syntax.yaml"></a>

```
  [ServiceId](#cfn-ssmincidents-responseplan-pagerdutyincidentconfiguration-serviceid): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration-properties"></a>

`ServiceId`  <a name="cfn-ssmincidents-responseplan-pagerdutyincidentconfiguration-serviceid"></a>
The ID of the PagerDuty service that the response plan associates with an incident when it launches.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
