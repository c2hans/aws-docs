---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-deviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool DeviceConfiguration
<a name="aws-properties-cognito-userpool-deviceconfiguration"></a>

The device-remembering configuration for a user pool.

## Syntax
<a name="aws-properties-cognito-userpool-deviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-deviceconfiguration-syntax.json"></a>

```
{
  "[ChallengeRequiredOnNewDevice](#cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice)" : {{Boolean}},
  "[DeviceOnlyRememberedOnUserPrompt](#cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-deviceconfiguration-syntax.yaml"></a>

```
  [ChallengeRequiredOnNewDevice](#cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice): {{Boolean}}
  [DeviceOnlyRememberedOnUserPrompt](#cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt): {{Boolean}}
```

## Properties
<a name="aws-properties-cognito-userpool-deviceconfiguration-properties"></a>

`ChallengeRequiredOnNewDevice`  <a name="cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice"></a>
When true, a remembered device can sign in with device authentication instead of SMS and time-based one-time password (TOTP) factors for multi-factor authentication (MFA).
Whether or not `ChallengeRequiredOnNewDevice` is true, users who sign in with devices that have not been confirmed or remembered must still provide a second factor in a user pool that requires MFA.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceOnlyRememberedOnUserPrompt`  <a name="cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt"></a>
When true, Amazon Cognito doesn't automatically remember a user's device when your app sends a `ConfirmDevice` API request. In your app, create a prompt for your user to choose whether they want to remember their device. Return the user's choice in an `UpdateDeviceStatus` API request.
When `DeviceOnlyRememberedOnUserPrompt` is `false`, Amazon Cognito immediately remembers devices that you register in a `ConfirmDevice` API request.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
