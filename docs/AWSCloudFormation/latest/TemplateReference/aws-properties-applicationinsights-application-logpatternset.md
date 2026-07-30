---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-logpatternset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application LogPatternSet
<a name="aws-properties-applicationinsights-application-logpatternset"></a>

The `AWS::ApplicationInsights::Application LogPatternSet` property type specifies the log pattern set.

## Syntax
<a name="aws-properties-applicationinsights-application-logpatternset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-logpatternset-syntax.json"></a>

```
{
  "[LogPatterns](#cfn-applicationinsights-application-logpatternset-logpatterns)" : {{[ LogPattern, ... ]}},
  "[PatternSetName](#cfn-applicationinsights-application-logpatternset-patternsetname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-logpatternset-syntax.yaml"></a>

```
  [LogPatterns](#cfn-applicationinsights-application-logpatternset-logpatterns): {{
    - LogPattern}}
  [PatternSetName](#cfn-applicationinsights-application-logpatternset-patternsetname): {{String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-logpatternset-properties"></a>

`LogPatterns`  <a name="cfn-applicationinsights-application-logpatternset-logpatterns"></a>
A list of objects that define the log patterns that belong to `LogPatternSet`.
*Required*: Yes
*Type*: Array of [LogPattern](aws-properties-applicationinsights-application-logpattern.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatternSetName`  <a name="cfn-applicationinsights-application-logpatternset-patternsetname"></a>
The name of the log pattern. A log pattern name can contain up to 30 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9.-_]*`
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
