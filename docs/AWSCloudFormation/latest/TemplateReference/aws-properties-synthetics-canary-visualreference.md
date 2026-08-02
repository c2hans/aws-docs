---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-visualreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary VisualReference
<a name="aws-properties-synthetics-canary-visualreference"></a>

Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary. If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.

Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later. For more information, see [ Visual monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html) and [ Visual monitoring blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html)

## Syntax
<a name="aws-properties-synthetics-canary-visualreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-visualreference-syntax.json"></a>

```
{
  "[BaseCanaryRunId](#cfn-synthetics-canary-visualreference-basecanaryrunid)" : {{String}},
  "[BaseScreenshots](#cfn-synthetics-canary-visualreference-basescreenshots)" : {{[ BaseScreenshot, ... ]}},
  "[BrowserType](#cfn-synthetics-canary-visualreference-browsertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-visualreference-syntax.yaml"></a>

```
  [BaseCanaryRunId](#cfn-synthetics-canary-visualreference-basecanaryrunid): {{String}}
  [BaseScreenshots](#cfn-synthetics-canary-visualreference-basescreenshots): {{
    - BaseScreenshot}}
  [BrowserType](#cfn-synthetics-canary-visualreference-browsertype): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-visualreference-properties"></a>

`BaseCanaryRunId`  <a name="cfn-synthetics-canary-visualreference-basecanaryrunid"></a>
Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are `nextrun` to use the screenshots from the next run after this update is made, `lastrun` to use the screenshots from the most recent run before this update was made, or the value of `Id` in the [ CanaryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html) from any past run of this canary.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseScreenshots`  <a name="cfn-synthetics-canary-visualreference-basescreenshots"></a>
An array of screenshots that are used as the baseline for comparisons during visual monitoring.
*Required*: No
*Type*: Array of [BaseScreenshot](aws-properties-synthetics-canary-basescreenshot.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrowserType`  <a name="cfn-synthetics-canary-visualreference-browsertype"></a>
The browser type associated with this visual reference configuration. Valid values are `CHROME` and `FIREFOX`.
*Required*: No
*Type*: String
*Allowed values*: `CHROME | FIREFOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
