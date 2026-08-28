---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-visibilityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup VisibilityConfig
<a name="aws-properties-wafv2-rulegroup-visibilityconfig"></a>

Defines and enables Amazon CloudWatch metrics and web request sample collection.

## Syntax
<a name="aws-properties-wafv2-rulegroup-visibilityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-visibilityconfig-syntax.json"></a>

```
{
  "[CloudWatchMetricsEnabled](#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled)" : {{Boolean}},
  "[MetricName](#cfn-wafv2-rulegroup-visibilityconfig-metricname)" : {{String}},
  "[SampledRequestsEnabled](#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-visibilityconfig-syntax.yaml"></a>

```
  [CloudWatchMetricsEnabled](#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled): {{Boolean}}
  [MetricName](#cfn-wafv2-rulegroup-visibilityconfig-metricname): {{String}}
  [SampledRequestsEnabled](#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-visibilityconfig-properties"></a>

`CloudWatchMetricsEnabled`  <a name="cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled"></a>
Indicates whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see [AWS WAF Metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics) in the *AWS WAF Developer Guide*.
For web ACLs, the metrics are for web requests that have the web ACL default action applied. AWS WAF applies the default action to web requests that pass the inspection of all rules in the web ACL without being either allowed or blocked. For more information, see [The web ACL default action](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-default-action.html) in the *AWS WAF Developer Guide*.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-wafv2-rulegroup-visibilityconfig-metricname"></a>
A name of the Amazon CloudWatch metric dimension. The name can contain only the characters: A-Z, a-z, 0-9, - (hyphen), and \_ (underscore). The name can be from one to 128 characters long. It can't contain whitespace or metric names that are reserved for AWS WAF, for example `All` and `Default_Action`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampledRequestsEnabled`  <a name="cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled"></a>
Indicates whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.
If you configure data protection for the web ACL, the protection applies to the web ACL's sampled web request data.
Request sampling doesn't provide a field redaction option, and any field redaction that you specify in your logging configuration doesn't affect sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
