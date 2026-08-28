---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-securityhubpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy SecurityHubPolicy
<a name="aws-properties-securityhub-configurationpolicy-securityhubpolicy"></a>

 An object that defines how AWS Security Hub CSPM is configured. The configuration policy includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-securityhubpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-securityhubpolicy-syntax.json"></a>

```
{
  "[EnabledStandardIdentifiers](#cfn-securityhub-configurationpolicy-securityhubpolicy-enabledstandardidentifiers)" : {{[ String, ... ]}},
  "[SecurityControlsConfiguration](#cfn-securityhub-configurationpolicy-securityhubpolicy-securitycontrolsconfiguration)" : {{SecurityControlsConfiguration}},
  "[ServiceEnabled](#cfn-securityhub-configurationpolicy-securityhubpolicy-serviceenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-securityhubpolicy-syntax.yaml"></a>

```
  [EnabledStandardIdentifiers](#cfn-securityhub-configurationpolicy-securityhubpolicy-enabledstandardidentifiers): {{
    - String}}
  [SecurityControlsConfiguration](#cfn-securityhub-configurationpolicy-securityhubpolicy-securitycontrolsconfiguration): {{
    SecurityControlsConfiguration}}
  [ServiceEnabled](#cfn-securityhub-configurationpolicy-securityhubpolicy-serviceenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-securityhubpolicy-properties"></a>

`EnabledStandardIdentifiers`  <a name="cfn-securityhub-configurationpolicy-securityhubpolicy-enabledstandardidentifiers"></a>
A list that defines which security standards are enabled in the configuration policy.
This property is required only if `ServiceEnabled` is set to `true` in your configuration policy.
*Required*: Conditional
*Type*: Array of String
*Maximum*: `2048 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityControlsConfiguration`  <a name="cfn-securityhub-configurationpolicy-securityhubpolicy-securitycontrolsconfiguration"></a>
 An object that defines which security controls are enabled in the configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account.
This property is required only if `ServiceEnabled` is set to true in your configuration policy.
*Required*: Conditional
*Type*: [SecurityControlsConfiguration](aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceEnabled`  <a name="cfn-securityhub-configurationpolicy-securityhubpolicy-serviceenabled"></a>
 Indicates whether Security Hub CSPM is enabled in the policy.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
