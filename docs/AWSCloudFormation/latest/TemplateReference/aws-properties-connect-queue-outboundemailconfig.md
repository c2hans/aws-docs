---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-queue-outboundemailconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Queue OutboundEmailConfig
<a name="aws-properties-connect-queue-outboundemailconfig"></a>

The outbound email address ID.

## Syntax
<a name="aws-properties-connect-queue-outboundemailconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-queue-outboundemailconfig-syntax.json"></a>

```
{
  "[OutboundEmailAddressId](#cfn-connect-queue-outboundemailconfig-outboundemailaddressid)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-queue-outboundemailconfig-syntax.yaml"></a>

```
  [OutboundEmailAddressId](#cfn-connect-queue-outboundemailconfig-outboundemailaddressid): {{String}}
```

## Properties
<a name="aws-properties-connect-queue-outboundemailconfig-properties"></a>

`OutboundEmailAddressId`  <a name="cfn-connect-queue-outboundemailconfig-outboundemailaddressid"></a>
The identifier of the email address.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/email-address/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
