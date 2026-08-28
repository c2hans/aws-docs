---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleAction
<a name="aws-properties-ses-mailmanagerruleset-ruleaction"></a>

The action for a rule to take. Only one of the contained actions can be set.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleaction-syntax.json"></a>

```
{
  "[AddHeader](#cfn-ses-mailmanagerruleset-ruleaction-addheader)" : {{AddHeaderAction}},
  "[Archive](#cfn-ses-mailmanagerruleset-ruleaction-archive)" : {{ArchiveAction}},
  "[Bounce](#cfn-ses-mailmanagerruleset-ruleaction-bounce)" : {{BounceAction}},
  "[DeliverToMailbox](#cfn-ses-mailmanagerruleset-ruleaction-delivertomailbox)" : {{DeliverToMailboxAction}},
  "[DeliverToQBusiness](#cfn-ses-mailmanagerruleset-ruleaction-delivertoqbusiness)" : {{DeliverToQBusinessAction}},
  "[Drop](#cfn-ses-mailmanagerruleset-ruleaction-drop)" : {{Json}},
  "[InvokeLambda](#cfn-ses-mailmanagerruleset-ruleaction-invokelambda)" : {{InvokeLambdaAction}},
  "[PublishToSns](#cfn-ses-mailmanagerruleset-ruleaction-publishtosns)" : {{SnsAction}},
  "[Relay](#cfn-ses-mailmanagerruleset-ruleaction-relay)" : {{RelayAction}},
  "[ReplaceRecipient](#cfn-ses-mailmanagerruleset-ruleaction-replacerecipient)" : {{ReplaceRecipientAction}},
  "[Send](#cfn-ses-mailmanagerruleset-ruleaction-send)" : {{SendAction}},
  "[WriteToS3](#cfn-ses-mailmanagerruleset-ruleaction-writetos3)" : {{S3Action}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleaction-syntax.yaml"></a>

```
  [AddHeader](#cfn-ses-mailmanagerruleset-ruleaction-addheader): {{
    AddHeaderAction}}
  [Archive](#cfn-ses-mailmanagerruleset-ruleaction-archive): {{
    ArchiveAction}}
  [Bounce](#cfn-ses-mailmanagerruleset-ruleaction-bounce): {{
    BounceAction}}
  [DeliverToMailbox](#cfn-ses-mailmanagerruleset-ruleaction-delivertomailbox): {{
    DeliverToMailboxAction}}
  [DeliverToQBusiness](#cfn-ses-mailmanagerruleset-ruleaction-delivertoqbusiness): {{
    DeliverToQBusinessAction}}
  [Drop](#cfn-ses-mailmanagerruleset-ruleaction-drop): {{Json}}
  [InvokeLambda](#cfn-ses-mailmanagerruleset-ruleaction-invokelambda): {{
    InvokeLambdaAction}}
  [PublishToSns](#cfn-ses-mailmanagerruleset-ruleaction-publishtosns): {{
    SnsAction}}
  [Relay](#cfn-ses-mailmanagerruleset-ruleaction-relay): {{
    RelayAction}}
  [ReplaceRecipient](#cfn-ses-mailmanagerruleset-ruleaction-replacerecipient): {{
    ReplaceRecipientAction}}
  [Send](#cfn-ses-mailmanagerruleset-ruleaction-send): {{
    SendAction}}
  [WriteToS3](#cfn-ses-mailmanagerruleset-ruleaction-writetos3): {{
    S3Action}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleaction-properties"></a>

`AddHeader`  <a name="cfn-ses-mailmanagerruleset-ruleaction-addheader"></a>
This action adds a header. This can be used to add arbitrary email headers.
*Required*: No
*Type*: [AddHeaderAction](aws-properties-ses-mailmanagerruleset-addheaderaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Archive`  <a name="cfn-ses-mailmanagerruleset-ruleaction-archive"></a>
This action archives the email. This can be used to deliver an email to an archive.
*Required*: No
*Type*: [ArchiveAction](aws-properties-ses-mailmanagerruleset-archiveaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bounce`  <a name="cfn-ses-mailmanagerruleset-ruleaction-bounce"></a>
This action sends a bounce response for the email.
*Required*: No
*Type*: [BounceAction](aws-properties-ses-mailmanagerruleset-bounceaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliverToMailbox`  <a name="cfn-ses-mailmanagerruleset-ruleaction-delivertomailbox"></a>
This action delivers an email to a WorkMail mailbox.
*Required*: No
*Type*: [DeliverToMailboxAction](aws-properties-ses-mailmanagerruleset-delivertomailboxaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliverToQBusiness`  <a name="cfn-ses-mailmanagerruleset-ruleaction-delivertoqbusiness"></a>
This action delivers an email to an Amazon Q Business application for ingestion into its knowledge base.
*Required*: No
*Type*: [DeliverToQBusinessAction](aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Drop`  <a name="cfn-ses-mailmanagerruleset-ruleaction-drop"></a>
This action terminates the evaluation of rules in the rule set.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokeLambda`  <a name="cfn-ses-mailmanagerruleset-ruleaction-invokelambda"></a>
This action invokes an AWS Lambda function to process the email.
*Required*: No
*Type*: [InvokeLambdaAction](aws-properties-ses-mailmanagerruleset-invokelambdaaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishToSns`  <a name="cfn-ses-mailmanagerruleset-ruleaction-publishtosns"></a>
This action publishes the email content to an Amazon SNS topic.
*Required*: No
*Type*: [SnsAction](aws-properties-ses-mailmanagerruleset-snsaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Relay`  <a name="cfn-ses-mailmanagerruleset-ruleaction-relay"></a>
This action relays the email to another SMTP server.
*Required*: No
*Type*: [RelayAction](aws-properties-ses-mailmanagerruleset-relayaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplaceRecipient`  <a name="cfn-ses-mailmanagerruleset-ruleaction-replacerecipient"></a>
The action replaces certain or all recipients with a different set of recipients.
*Required*: No
*Type*: [ReplaceRecipientAction](aws-properties-ses-mailmanagerruleset-replacerecipientaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Send`  <a name="cfn-ses-mailmanagerruleset-ruleaction-send"></a>
This action sends the email to the internet.
*Required*: No
*Type*: [SendAction](aws-properties-ses-mailmanagerruleset-sendaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteToS3`  <a name="cfn-ses-mailmanagerruleset-ruleaction-writetos3"></a>
This action writes the MIME content of the email to an S3 bucket.
*Required*: No
*Type*: [S3Action](aws-properties-ses-mailmanagerruleset-s3action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
