---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-recurrencerule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective RecurrenceRule
<a name="aws-properties-applicationsignals-servicelevelobjective-recurrencerule"></a>

The recurrence rule for the time exclusion window.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-recurrencerule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-recurrencerule-syntax.json"></a>

```
{
  "[Expression](#cfn-applicationsignals-servicelevelobjective-recurrencerule-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-recurrencerule-syntax.yaml"></a>

```
  [Expression](#cfn-applicationsignals-servicelevelobjective-recurrencerule-expression): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-recurrencerule-properties"></a>

`Expression`  <a name="cfn-applicationsignals-servicelevelobjective-recurrencerule-expression"></a>
The following two rules are supported:
+ rate(value unit) - The value must be a positive integer and the unit can be hour\|day\|month.
+ cron - An expression which consists of six fields separated by white spaces: (minutes hours day\_of\_month month day\_of\_week year).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
