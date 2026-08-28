---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment RiskExceptionConfigurationType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype"></a>

Exceptions to the risk evaluation configuration, including always-allow and always-block IP address ranges.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-syntax.json"></a>

```
{
  "[BlockedIPRangeList](#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-blockediprangelist)" : {{[ String, ... ]}},
  "[SkippedIPRangeList](#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-skippediprangelist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-syntax.yaml"></a>

```
  [BlockedIPRangeList](#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-blockediprangelist): {{
    - String}}
  [SkippedIPRangeList](#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-skippediprangelist): {{
    - String}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-properties"></a>

`BlockedIPRangeList`  <a name="cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-blockediprangelist"></a>
An always-block IP address list. Overrides the risk decision and always blocks authentication requests. This parameter is displayed and set in CIDR notation.
*Required*: No
*Type*: Array of String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkippedIPRangeList`  <a name="cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-skippediprangelist"></a>
An always-allow IP address list. Risk detection isn't performed on the IP addresses in this range list. This parameter is displayed and set in CIDR notation.
*Required*: No
*Type*: Array of String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
