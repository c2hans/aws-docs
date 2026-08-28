---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::QuickConnect PhoneNumberQuickConnectConfig
<a name="aws-properties-connect-quickconnect-phonenumberquickconnectconfig"></a>

Contains information about a phone number for a quick connect.

## Syntax
<a name="aws-properties-connect-quickconnect-phonenumberquickconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-quickconnect-phonenumberquickconnectconfig-syntax.json"></a>

```
{
  "[PhoneNumber](#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-quickconnect-phonenumberquickconnectconfig-syntax.yaml"></a>

```
  [PhoneNumber](#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber): {{String}}
```

## Properties
<a name="aws-properties-connect-quickconnect-phonenumberquickconnectconfig-properties"></a>

`PhoneNumber`  <a name="cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber"></a>
The phone number in E.164 format.
*Required*: Yes
*Type*: String
*Pattern*: `^\+[1-9]\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
