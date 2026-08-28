---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy SecurityControlCustomParameter
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter"></a>

 A list of security controls and control parameter values that are included in a configuration policy.

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter-syntax.json"></a>

```
{
  "[Parameters](#cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SecurityControlId](#cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-securitycontrolid)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter-syntax.yaml"></a>

```
  [Parameters](#cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-parameters): {{
    {{Key}}: {{Value}}}}
  [SecurityControlId](#cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-securitycontrolid): {{String}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter-properties"></a>

`Parameters`  <a name="cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-parameters"></a>
 An object that specifies parameter values for a control in a configuration policy.
*Required*: No
*Type*: Object of [ParameterConfiguration](aws-properties-securityhub-configurationpolicy-parameterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityControlId`  <a name="cfn-securityhub-configurationpolicy-securitycontrolcustomparameter-securitycontrolid"></a>
 The ID of the security control.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
