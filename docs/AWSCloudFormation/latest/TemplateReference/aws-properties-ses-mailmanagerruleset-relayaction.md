---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-relayaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RelayAction
<a name="aws-properties-ses-mailmanagerruleset-relayaction"></a>

The action relays the email via SMTP to another specific SMTP server.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-relayaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-relayaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-relayaction-actionfailurepolicy)" : {{String}},
  "[MailFrom](#cfn-ses-mailmanagerruleset-relayaction-mailfrom)" : {{String}},
  "[Relay](#cfn-ses-mailmanagerruleset-relayaction-relay)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-relayaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-relayaction-actionfailurepolicy): {{String}}
  [MailFrom](#cfn-ses-mailmanagerruleset-relayaction-mailfrom): {{String}}
  [Relay](#cfn-ses-mailmanagerruleset-relayaction-relay): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-relayaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-relayaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified relay has been deleted.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailFrom`  <a name="cfn-ses-mailmanagerruleset-relayaction-mailfrom"></a>
This action specifies whether to preserve or replace original mail from address while relaying received emails to a destination server.
*Required*: No
*Type*: String
*Allowed values*: `REPLACE | PRESERVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Relay`  <a name="cfn-ses-mailmanagerruleset-relayaction-relay"></a>
The identifier of the relay resource to be used when relaying an email.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
