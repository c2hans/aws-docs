---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-logpattern.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application LogPattern
<a name="aws-properties-applicationinsights-application-logpattern"></a>

The `AWS::ApplicationInsights::Application LogPattern` property type specifies an object that defines the log patterns that belong to a `LogPatternSet`.

## Syntax
<a name="aws-properties-applicationinsights-application-logpattern-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-logpattern-syntax.json"></a>

```
{
  "[Pattern](#cfn-applicationinsights-application-logpattern-pattern)" : {{String}},
  "[PatternName](#cfn-applicationinsights-application-logpattern-patternname)" : {{String}},
  "[Rank](#cfn-applicationinsights-application-logpattern-rank)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-logpattern-syntax.yaml"></a>

```
  [Pattern](#cfn-applicationinsights-application-logpattern-pattern): {{String}}
  [PatternName](#cfn-applicationinsights-application-logpattern-patternname): {{String}}
  [Rank](#cfn-applicationinsights-application-logpattern-rank): {{Integer}}
```

## Properties
<a name="aws-properties-applicationinsights-application-logpattern-properties"></a>

`Pattern`  <a name="cfn-applicationinsights-application-logpattern-pattern"></a>
A regular expression that defines the log pattern. A log pattern can contain up to 50 characters, and it cannot be empty.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatternName`  <a name="cfn-applicationinsights-application-logpattern-patternname"></a>
The name of the log pattern. A log pattern name can contain up to 50 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9.-_]*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rank`  <a name="cfn-applicationinsights-application-logpattern-rank"></a>
The rank of the log pattern.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
