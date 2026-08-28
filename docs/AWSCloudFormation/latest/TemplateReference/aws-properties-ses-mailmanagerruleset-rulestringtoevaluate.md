---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulestringtoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleStringToEvaluate
<a name="aws-properties-ses-mailmanagerruleset-rulestringtoevaluate"></a>

The string to evaluate in a string condition expression.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulestringtoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulestringtoevaluate-syntax.json"></a>

```
{
  "[Analysis](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-analysis)" : {{Analysis}},
  "[Attribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-attribute)" : {{String}},
  "[ClientCertificateAttribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-clientcertificateattribute)" : {{String}},
  "[MimeHeaderAttribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-mimeheaderattribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulestringtoevaluate-syntax.yaml"></a>

```
  [Analysis](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-analysis): {{
    Analysis}}
  [Attribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-attribute): {{String}}
  [ClientCertificateAttribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-clientcertificateattribute): {{String}}
  [MimeHeaderAttribute](#cfn-ses-mailmanagerruleset-rulestringtoevaluate-mimeheaderattribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulestringtoevaluate-properties"></a>

`Analysis`  <a name="cfn-ses-mailmanagerruleset-rulestringtoevaluate-analysis"></a>
The Add On ARN and its returned value to evaluate in a string condition expression.
*Required*: No
*Type*: [Analysis](aws-properties-ses-mailmanagerruleset-analysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagerruleset-rulestringtoevaluate-attribute"></a>
The email attribute to evaluate in a string condition expression.
*Required*: No
*Type*: String
*Allowed values*: `MAIL_FROM | HELO | RECIPIENT | SENDER | FROM | SUBJECT | TO | CC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCertificateAttribute`  <a name="cfn-ses-mailmanagerruleset-rulestringtoevaluate-clientcertificateattribute"></a>
The client certificate attribute to evaluate in a string condition expression.
*Required*: No
*Type*: String
*Allowed values*: `CN | SAN_RFC822_NAME | SAN_DNS_NAME | SAN_DIRECTORY_NAME | SAN_UNIFORM_RESOURCE_IDENTIFIER | SAN_IP_ADDRESS | SAN_REGISTERED_ID | SERIAL_NUMBER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MimeHeaderAttribute`  <a name="cfn-ses-mailmanagerruleset-rulestringtoevaluate-mimeheaderattribute"></a>
The email MIME X-Header attribute to evaluate in a string condition expression.
*Required*: No
*Type*: String
*Pattern*: `^X-[a-zA-Z0-9-]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
