---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-reportgenerator-reportfrequency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::ReportGenerator ReportFrequency
<a name="aws-properties-licensemanager-reportgenerator-reportfrequency"></a>

Details about how frequently reports are generated.

## Syntax
<a name="aws-properties-licensemanager-reportgenerator-reportfrequency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-reportgenerator-reportfrequency-syntax.json"></a>

```
{
  "[Period](#cfn-licensemanager-reportgenerator-reportfrequency-period)" : {{String}},
  "[Value](#cfn-licensemanager-reportgenerator-reportfrequency-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-licensemanager-reportgenerator-reportfrequency-syntax.yaml"></a>

```
  [Period](#cfn-licensemanager-reportgenerator-reportfrequency-period): {{String}}
  [Value](#cfn-licensemanager-reportgenerator-reportfrequency-value): {{Integer}}
```

## Properties
<a name="aws-properties-licensemanager-reportgenerator-reportfrequency-properties"></a>

`Period`  <a name="cfn-licensemanager-reportgenerator-reportfrequency-period"></a>
Time period between each report. The period can be daily, weekly, or monthly.
*Required*: No
*Type*: String
*Allowed values*: `DAY | WEEK | MONTH | ONE_TIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-licensemanager-reportgenerator-reportfrequency-value"></a>
Number of times within the frequency period that a report is generated. The only supported value is `1`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
