---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-insightrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::InsightRule
<a name="aws-resource-cloudwatch-insightrule"></a>

Creates or updates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see [ Using Contributor Insights to Analyze High-Cardinality Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-cloudwatch-insightrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-insightrule-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::InsightRule",
  "Properties" : {
      "[ApplyOnTransformedLogs](#cfn-cloudwatch-insightrule-applyontransformedlogs)" : {{Boolean}},
      "[RuleBody](#cfn-cloudwatch-insightrule-rulebody)" : {{String}},
      "[RuleName](#cfn-cloudwatch-insightrule-rulename)" : {{String}},
      "[RuleState](#cfn-cloudwatch-insightrule-rulestate)" : {{String}},
      "[Tags](#cfn-cloudwatch-insightrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-insightrule-syntax.yaml"></a>

```
Type: AWS::CloudWatch::InsightRule
Properties:
  [ApplyOnTransformedLogs](#cfn-cloudwatch-insightrule-applyontransformedlogs): {{Boolean}}
  [RuleBody](#cfn-cloudwatch-insightrule-rulebody): {{String}}
  [RuleName](#cfn-cloudwatch-insightrule-rulename): {{String}}
  [RuleState](#cfn-cloudwatch-insightrule-rulestate): {{String}}
  [Tags](#cfn-cloudwatch-insightrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-insightrule-properties"></a>

`ApplyOnTransformedLogs`  <a name="cfn-cloudwatch-insightrule-applyontransformedlogs"></a>
Determines whether the rules is evaluated on transformed versions of logs. Valid values are `TRUE` and `FALSE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleBody`  <a name="cfn-cloudwatch-insightrule-rulebody"></a>
The definition of the rule, as a JSON object. For details about the syntax, see [ Contributor Insights Rule Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html) in the *Amazon CloudWatch User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-cloudwatch-insightrule-rulename"></a>
The name of the rule.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuleState`  <a name="cfn-cloudwatch-insightrule-rulestate"></a>
The current state of the rule. Valid values are `ENABLED` and `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-insightrule-tags"></a>
A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule.
Tags can help you organize and categorize your resources. For more information, see [ Tagging Your Amazon CloudWatch Resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html).
To be able to associate tags with a rule, you must have the `cloudwatch:TagResource` permission in addition to the `cloudwatch:PutInsightRule` permission.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-insightrule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-insightrule-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-insightrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the rule.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-insightrule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-insightrule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the Contributor Insights rule, such as `arn:aws:cloudwatch:us-west-2:123456789012:insight-rule/MyInsightRuleName`.

`RuleName`  <a name="RuleName-fn::getatt"></a>
The name of the Contributor Insights rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
