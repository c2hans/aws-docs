---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule PathPatternConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig"></a>

Information about a path pattern condition.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig-syntax.json"></a>

```
{
  "[RegexValues](#cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-regexvalues)" : {{[ String, ... ]}},
  "[Values](#cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig-syntax.yaml"></a>

```
  [RegexValues](#cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-regexvalues): {{
    - String}}
  [Values](#cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig-properties"></a>

`RegexValues`  <a name="cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-regexvalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-values"></a>
The path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
