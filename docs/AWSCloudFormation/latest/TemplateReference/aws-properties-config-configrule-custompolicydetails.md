---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-custompolicydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigRule CustomPolicyDetails
<a name="aws-properties-config-configrule-custompolicydetails"></a>

Provides the CustomPolicyDetails, the rule owner (` AWS ` for managed rules, `CUSTOM_POLICY` for Custom Policy rules, and `CUSTOM_LAMBDA` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

## Syntax
<a name="aws-properties-config-configrule-custompolicydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configrule-custompolicydetails-syntax.json"></a>

```
{
  "[EnableDebugLogDelivery](#cfn-config-configrule-custompolicydetails-enabledebuglogdelivery)" : {{Boolean}},
  "[PolicyRuntime](#cfn-config-configrule-custompolicydetails-policyruntime)" : {{String}},
  "[PolicyText](#cfn-config-configrule-custompolicydetails-policytext)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-configrule-custompolicydetails-syntax.yaml"></a>

```
  [EnableDebugLogDelivery](#cfn-config-configrule-custompolicydetails-enabledebuglogdelivery): {{Boolean}}
  [PolicyRuntime](#cfn-config-configrule-custompolicydetails-policyruntime): {{String}}
  [PolicyText](#cfn-config-configrule-custompolicydetails-policytext): {{String}}
```

## Properties
<a name="aws-properties-config-configrule-custompolicydetails-properties"></a>

`EnableDebugLogDelivery`  <a name="cfn-config-configrule-custompolicydetails-enabledebuglogdelivery"></a>
The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyRuntime`  <a name="cfn-config-configrule-custompolicydetails-policyruntime"></a>
The runtime system for your AWS Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard).
*Required*: No
*Type*: String
*Pattern*: `guard\-2\.x\.x`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyText`  <a name="cfn-config-configrule-custompolicydetails-policytext"></a>
The policy definition containing the logic for your AWS Config Custom Policy rule.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
