---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-queue-emailaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Queue EmailAddress
<a name="aws-properties-connect-queue-emailaddress"></a>

<a name="aws-properties-connect-queue-emailaddress-description"></a>The `EmailAddress` property type specifies Property description not available. for an [AWS::Connect::Queue](aws-resource-connect-queue.md).

## Syntax
<a name="aws-properties-connect-queue-emailaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-queue-emailaddress-syntax.json"></a>

```
{
  "[EmailAddressArn](#cfn-connect-queue-emailaddress-emailaddressarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-queue-emailaddress-syntax.yaml"></a>

```
  [EmailAddressArn](#cfn-connect-queue-emailaddress-emailaddressarn): {{String}}
```

## Properties
<a name="aws-properties-connect-queue-emailaddress-properties"></a>

`EmailAddressArn`  <a name="cfn-connect-queue-emailaddress-emailaddressarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-f0-9]{8}-[-a-f0-9]{4}-[-a-f0-9]{4}-[-a-f0-9]{4}-[-a-f0-9]{12}/email-address/[-a-f0-9]{8}-[-a-f0-9]{4}-[-a-f0-9]{4}-[-a-f0-9]{4}-[-a-f0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
