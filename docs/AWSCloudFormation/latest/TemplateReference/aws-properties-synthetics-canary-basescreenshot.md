---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-basescreenshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary BaseScreenshot
<a name="aws-properties-synthetics-canary-basescreenshot"></a>

A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

## Syntax
<a name="aws-properties-synthetics-canary-basescreenshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-basescreenshot-syntax.json"></a>

```
{
  "[IgnoreCoordinates](#cfn-synthetics-canary-basescreenshot-ignorecoordinates)" : {{[ String, ... ]}},
  "[ScreenshotName](#cfn-synthetics-canary-basescreenshot-screenshotname)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-basescreenshot-syntax.yaml"></a>

```
  [IgnoreCoordinates](#cfn-synthetics-canary-basescreenshot-ignorecoordinates): {{
    - String}}
  [ScreenshotName](#cfn-synthetics-canary-basescreenshot-screenshotname): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-basescreenshot-properties"></a>

`IgnoreCoordinates`  <a name="cfn-synthetics-canary-basescreenshot-ignorecoordinates"></a>
Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see [ Edit or delete a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScreenshotName`  <a name="cfn-synthetics-canary-basescreenshot-screenshotname"></a>
The name of the screenshot. This is generated the first time the canary is run after the `UpdateCanary` operation that specified for this canary to perform visual monitoring.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
