---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-window.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Window
<a name="aws-properties-applicationsignals-servicelevelobjective-window"></a>

The start and end time of the time exclusion window.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-window-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-window-syntax.json"></a>

```
{
  "[Duration](#cfn-applicationsignals-servicelevelobjective-window-duration)" : {{Integer}},
  "[DurationUnit](#cfn-applicationsignals-servicelevelobjective-window-durationunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-window-syntax.yaml"></a>

```
  [Duration](#cfn-applicationsignals-servicelevelobjective-window-duration): {{Integer}}
  [DurationUnit](#cfn-applicationsignals-servicelevelobjective-window-durationunit): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-window-properties"></a>

`Duration`  <a name="cfn-applicationsignals-servicelevelobjective-window-duration"></a>
The start and end time of the time exclusion window.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DurationUnit`  <a name="cfn-applicationsignals-servicelevelobjective-window-durationunit"></a>
The unit of measurement to use during the time window exclusion.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTE | HOUR | DAY | MONTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
