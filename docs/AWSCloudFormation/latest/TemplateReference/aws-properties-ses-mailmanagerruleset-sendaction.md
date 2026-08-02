---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-sendaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet SendAction
<a name="aws-properties-ses-mailmanagerruleset-sendaction"></a>

Sends the email to the internet using the ses:SendRawEmail API.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-sendaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-sendaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-sendaction-actionfailurepolicy)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-sendaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-sendaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-sendaction-actionfailurepolicy): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-sendaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-sendaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-sendaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the sendRawEmail API.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-sendaction-rolearn"></a>
The Amazon Resource Name (ARN) of the role to use for this action. This role must have access to the ses:SendRawEmail API.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
