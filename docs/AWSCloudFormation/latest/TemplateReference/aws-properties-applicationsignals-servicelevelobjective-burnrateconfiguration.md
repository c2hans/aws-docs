---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective BurnRateConfiguration
<a name="aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration"></a>

This object defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO. A burn rate of exactly 1 indicates that the SLO goal will be met exactly.

For example, if you specify 60 as the number of minutes in the look-back window, the burn rate is calculated as the following:

 *burn rate = error rate over the look-back window / (100% - attainment goal percentage)*

For more information about burn rates, see [Calculate burn rates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-burn).

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration-syntax.json"></a>

```
{
  "[LookBackWindowMinutes](#cfn-applicationsignals-servicelevelobjective-burnrateconfiguration-lookbackwindowminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration-syntax.yaml"></a>

```
  [LookBackWindowMinutes](#cfn-applicationsignals-servicelevelobjective-burnrateconfiguration-lookbackwindowminutes): {{Integer}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-burnrateconfiguration-properties"></a>

`LookBackWindowMinutes`  <a name="cfn-applicationsignals-servicelevelobjective-burnrateconfiguration-lookbackwindowminutes"></a>
The number of minutes to use as the look-back window.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10080`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
