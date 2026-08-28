---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-delivertomailboxaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet DeliverToMailboxAction
<a name="aws-properties-ses-mailmanagerruleset-delivertomailboxaction"></a>

This action to delivers an email to a mailbox.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-delivertomailboxaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-delivertomailboxaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-delivertomailboxaction-actionfailurepolicy)" : {{String}},
  "[MailboxArn](#cfn-ses-mailmanagerruleset-delivertomailboxaction-mailboxarn)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-delivertomailboxaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-delivertomailboxaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-delivertomailboxaction-actionfailurepolicy): {{String}}
  [MailboxArn](#cfn-ses-mailmanagerruleset-delivertomailboxaction-mailboxarn): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-delivertomailboxaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-delivertomailboxaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-delivertomailboxaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the mailbox ARN is no longer valid.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailboxArn`  <a name="cfn-ses-mailmanagerruleset-delivertomailboxaction-mailboxarn"></a>
The Amazon Resource Name (ARN) of a WorkMail organization to deliver the email to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-delivertomailboxaction-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role to use to execute this action. The role must have access to the workmail:DeliverToMailbox API.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
