---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-loggingconfiguration-loggingfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::LoggingConfiguration LoggingFilter
<a name="aws-properties-wafv2-loggingconfiguration-loggingfilter"></a>

Filtering that specifies which web requests are kept in the logs and which are dropped, defined for a web ACL's `LoggingConfiguration`.

You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.

## Syntax
<a name="aws-properties-wafv2-loggingconfiguration-loggingfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-loggingconfiguration-loggingfilter-syntax.json"></a>

```
{
  "[DefaultBehavior](#cfn-wafv2-loggingconfiguration-loggingfilter-defaultbehavior)" : {{String}},
  "[Filters](#cfn-wafv2-loggingconfiguration-loggingfilter-filters)" : {{[ Filter, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-loggingconfiguration-loggingfilter-syntax.yaml"></a>

```
  [DefaultBehavior](#cfn-wafv2-loggingconfiguration-loggingfilter-defaultbehavior): {{String}}
  [Filters](#cfn-wafv2-loggingconfiguration-loggingfilter-filters): {{
    - Filter}}
```

## Properties
<a name="aws-properties-wafv2-loggingconfiguration-loggingfilter-properties"></a>

`DefaultBehavior`  <a name="cfn-wafv2-loggingconfiguration-loggingfilter-defaultbehavior"></a>
Default handling for logs that don't match any of the specified filtering conditions.
*Required*: Yes
*Type*: String
*Allowed values*: `KEEP | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filters`  <a name="cfn-wafv2-loggingconfiguration-loggingfilter-filters"></a>
The filters that you want to apply to the logs.
*Required*: Yes
*Type*: Array of [Filter](aws-properties-wafv2-loggingconfiguration-filter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
