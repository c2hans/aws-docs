---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanagerruleset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet
<a name="aws-resource-ses-mailmanagerruleset"></a>

Resource to create a rule set for a Mail Manager ingress endpoint which contains a list of rules that are evaluated sequentially for each email.

## Syntax
<a name="aws-resource-ses-mailmanagerruleset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanagerruleset-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerRuleSet",
  "Properties" : {
      "[Rules](#cfn-ses-mailmanagerruleset-rules)" : {{[ Rule, ... ]}},
      "[RuleSetName](#cfn-ses-mailmanagerruleset-rulesetname)" : {{String}},
      "[Tags](#cfn-ses-mailmanagerruleset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanagerruleset-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerRuleSet
Properties:
  [Rules](#cfn-ses-mailmanagerruleset-rules): {{
    - Rule}}
  [RuleSetName](#cfn-ses-mailmanagerruleset-rulesetname): {{String}}
  [Tags](#cfn-ses-mailmanagerruleset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanagerruleset-properties"></a>

`Rules`  <a name="cfn-ses-mailmanagerruleset-rules"></a>
Conditional rules that are evaluated for determining actions on email.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-ses-mailmanagerruleset-rule.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleSetName`  <a name="cfn-ses-mailmanagerruleset-rulesetname"></a>
A user-friendly name for the rule set.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-mailmanagerruleset-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanagerruleset-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanagerruleset-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanagerruleset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanagerruleset-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanagerruleset-return-values-fn--getatt-fn--getatt"></a>

`RuleSetArn`  <a name="RuleSetArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the rule set resource.

`RuleSetId`  <a name="RuleSetId-fn::getatt"></a>
The identifier of the rule set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
