---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy SecurityControlsConfiguration
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration"></a>

 An object that defines which security controls are enabled in an AWS Security Hub CSPM configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account.

This property is required only if `ServiceEnabled` is set to `true` in your configuration policy.

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration-syntax.json"></a>

```
{
  "[DisabledSecurityControlIdentifiers](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-disabledsecuritycontrolidentifiers)" : {{[ String, ... ]}},
  "[EnabledSecurityControlIdentifiers](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-enabledsecuritycontrolidentifiers)" : {{[ String, ... ]}},
  "[SecurityControlCustomParameters](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-securitycontrolcustomparameters)" : {{[ SecurityControlCustomParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration-syntax.yaml"></a>

```
  [DisabledSecurityControlIdentifiers](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-disabledsecuritycontrolidentifiers): {{
    - String}}
  [EnabledSecurityControlIdentifiers](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-enabledsecuritycontrolidentifiers): {{
    - String}}
  [SecurityControlCustomParameters](#cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-securitycontrolcustomparameters): {{
    - SecurityControlCustomParameter}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration-properties"></a>

`DisabledSecurityControlIdentifiers`  <a name="cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-disabledsecuritycontrolidentifiers"></a>
 A list of security controls that are disabled in the configuration policy.
Provide only one of `EnabledSecurityControlIdentifiers` or `DisabledSecurityControlIdentifiers`.
If you provide `DisabledSecurityControlIdentifiers`, Security Hub CSPM enables all other controls not in the list, and enables [AutoEnableControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html#securityhub-UpdateSecurityHubConfiguration-request-AutoEnableControls).
*Required*: No
*Type*: Array of String
*Maximum*: `2048 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnabledSecurityControlIdentifiers`  <a name="cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-enabledsecuritycontrolidentifiers"></a>
 A list of security controls that are enabled in the configuration policy.
Provide only one of `EnabledSecurityControlIdentifiers` or `DisabledSecurityControlIdentifiers`.
If you provide `EnabledSecurityControlIdentifiers`, Security Hub CSPM disables all other controls not in the list, and disables [AutoEnableControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html#securityhub-UpdateSecurityHubConfiguration-request-AutoEnableControls).
*Required*: No
*Type*: Array of String
*Maximum*: `2048 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityControlCustomParameters`  <a name="cfn-securityhub-configurationpolicy-securitycontrolsconfiguration-securitycontrolcustomparameters"></a>
 A list of security controls and control parameter values that are included in a configuration policy.
*Required*: No
*Type*: Array of [SecurityControlCustomParameter](aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter.md)
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
