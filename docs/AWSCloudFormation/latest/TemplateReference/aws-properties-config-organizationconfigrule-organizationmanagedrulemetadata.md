---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::OrganizationConfigRule OrganizationManagedRuleMetadata
<a name="aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata"></a>

An object that specifies organization managed rule metadata such as resource type and ID of AWS resource along with the rule identifier. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

## Syntax
<a name="aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata-syntax.json"></a>

```
{
  "[Description](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description)" : {{String}},
  "[InputParameters](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters)" : {{String}},
  "[MaximumExecutionFrequency](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency)" : {{String}},
  "[ResourceIdScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope)" : {{String}},
  "[ResourceTypesScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope)" : {{[ String, ... ]}},
  "[RuleIdentifier](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier)" : {{String}},
  "[TagKeyScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope)" : {{String}},
  "[TagValueScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata-syntax.yaml"></a>

```
  [Description](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description): {{String}}
  [InputParameters](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters): {{String}}
  [MaximumExecutionFrequency](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency): {{String}}
  [ResourceIdScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope): {{String}}
  [ResourceTypesScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope): {{
    - String}}
  [RuleIdentifier](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier): {{String}}
  [TagKeyScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope): {{String}}
  [TagValueScope](#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope): {{String}}
```

## Properties
<a name="aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata-properties"></a>

`Description`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description"></a>
The description that you provide for your organization AWS Config rule.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputParameters`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters"></a>
A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumExecutionFrequency`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. This is for an AWS Config managed rule that is triggered at a periodic frequency.
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.
*Required*: No
*Type*: String
*Allowed values*: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdScope`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope"></a>
The ID of the AWS resource that was evaluated.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypesScope`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope"></a>
The type of the AWS resource that was evaluated.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleIdentifier`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier"></a>
For organization config managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [Using AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagKeyScope`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagValueScope`  <a name="cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope"></a>
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
