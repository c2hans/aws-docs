---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-rollinginterval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective RollingInterval
<a name="aws-properties-applicationsignals-servicelevelobjective-rollinginterval"></a>

If the interval for this SLO is a rolling interval, this structure contains the interval specifications.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-rollinginterval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-rollinginterval-syntax.json"></a>

```
{
  "[Duration](#cfn-applicationsignals-servicelevelobjective-rollinginterval-duration)" : {{Integer}},
  "[DurationUnit](#cfn-applicationsignals-servicelevelobjective-rollinginterval-durationunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-rollinginterval-syntax.yaml"></a>

```
  [Duration](#cfn-applicationsignals-servicelevelobjective-rollinginterval-duration): {{Integer}}
  [DurationUnit](#cfn-applicationsignals-servicelevelobjective-rollinginterval-durationunit): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-rollinginterval-properties"></a>

`Duration`  <a name="cfn-applicationsignals-servicelevelobjective-rollinginterval-duration"></a>
Specifies the duration of each rolling interval. For example, if `Duration` is `7` and `DurationUnit` is `DAY`, each rolling interval is seven days.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DurationUnit`  <a name="cfn-applicationsignals-servicelevelobjective-rollinginterval-durationunit"></a>
Specifies the rolling interval unit.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTE | HOUR | DAY | MONTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
