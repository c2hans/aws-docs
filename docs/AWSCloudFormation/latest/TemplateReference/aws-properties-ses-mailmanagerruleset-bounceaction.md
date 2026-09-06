---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-bounceaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet BounceAction
<a name="aws-properties-ses-mailmanagerruleset-bounceaction"></a>

The action to send a bounce response for the email. When executed, this action generates a non-delivery report (bounce) back to the sender.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-bounceaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-bounceaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-bounceaction-actionfailurepolicy)" : {{String}},
  "[DiagnosticMessage](#cfn-ses-mailmanagerruleset-bounceaction-diagnosticmessage)" : {{String}},
  "[Message](#cfn-ses-mailmanagerruleset-bounceaction-message)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-bounceaction-rolearn)" : {{String}},
  "[Sender](#cfn-ses-mailmanagerruleset-bounceaction-sender)" : {{String}},
  "[SmtpReplyCode](#cfn-ses-mailmanagerruleset-bounceaction-smtpreplycode)" : {{String}},
  "[StatusCode](#cfn-ses-mailmanagerruleset-bounceaction-statuscode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-bounceaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-bounceaction-actionfailurepolicy): {{String}}
  [DiagnosticMessage](#cfn-ses-mailmanagerruleset-bounceaction-diagnosticmessage): {{String}}
  [Message](#cfn-ses-mailmanagerruleset-bounceaction-message): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-bounceaction-rolearn): {{String}}
  [Sender](#cfn-ses-mailmanagerruleset-bounceaction-sender): {{String}}
  [SmtpReplyCode](#cfn-ses-mailmanagerruleset-bounceaction-smtpreplycode): {{String}}
  [StatusCode](#cfn-ses-mailmanagerruleset-bounceaction-statuscode): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-bounceaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-bounceaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the SendBounce API.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiagnosticMessage`  <a name="cfn-ses-mailmanagerruleset-bounceaction-diagnosticmessage"></a>
The diagnostic message included in the Diagnostic-Code header of the bounce.
*Required*: Yes
*Type*: String
*Pattern*: `^[\x20-\x7e]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-ses-mailmanagerruleset-bounceaction-message"></a>
The human-readable text to include in the bounce message.
*Required*: No
*Type*: String
*Pattern*: `^[\r\n\x20-\x7e]+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-bounceaction-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to use to send the bounce message.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sender`  <a name="cfn-ses-mailmanagerruleset-bounceaction-sender"></a>
The sender email address of the bounce message.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z@+.-]+$`
*Minimum*: `0`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmtpReplyCode`  <a name="cfn-ses-mailmanagerruleset-bounceaction-smtpreplycode"></a>
The SMTP reply code for the bounce, as defined by RFC 5321.
*Required*: Yes
*Type*: String
*Pattern*: `^[45][0-9][0-9]$`
*Minimum*: `3`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCode`  <a name="cfn-ses-mailmanagerruleset-bounceaction-statuscode"></a>
The enhanced status code for the bounce, in the format of x.y.z (e.g. 5.1.1).
*Required*: Yes
*Type*: String
*Pattern*: `^[45]\.[0-9]{1,3}\.[0-9]{1,3}$`
*Minimum*: `5`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
