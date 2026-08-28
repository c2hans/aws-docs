---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-emailaddress-aliasconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EmailAddress AliasConfiguration
<a name="aws-properties-connect-emailaddress-aliasconfiguration"></a>

Configuration information of an email alias.

## Syntax
<a name="aws-properties-connect-emailaddress-aliasconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-emailaddress-aliasconfiguration-syntax.json"></a>

```
{
  "[EmailAddressArn](#cfn-connect-emailaddress-aliasconfiguration-emailaddressarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-emailaddress-aliasconfiguration-syntax.yaml"></a>

```
  [EmailAddressArn](#cfn-connect-emailaddress-aliasconfiguration-emailaddressarn): {{String}}
```

## Properties
<a name="aws-properties-connect-emailaddress-aliasconfiguration-properties"></a>

`EmailAddressArn`  <a name="cfn-connect-emailaddress-aliasconfiguration-emailaddressarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/email-address/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
