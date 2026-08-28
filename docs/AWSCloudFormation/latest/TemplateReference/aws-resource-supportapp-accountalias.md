---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-supportapp-accountalias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportApp::AccountAlias
<a name="aws-resource-supportapp-accountalias"></a>

You can use the `AWS::SupportApp::AccountAlias` resource to specify your AWS account when you configure the AWS Support App in Slack. Your alias name appears on the AWS Support App page in the Support Center Console and in messages from the AWS Support App. You can use this alias to identify the account you've configured with the AWS Support App.

For more information, see [AWS Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html) in the *AWS Support User Guide*.

## Syntax
<a name="aws-resource-supportapp-accountalias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-supportapp-accountalias-syntax.json"></a>

```
{
  "Type" : "AWS::SupportApp::AccountAlias",
  "Properties" : {
      "[AccountAlias](#cfn-supportapp-accountalias-accountalias)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-supportapp-accountalias-syntax.yaml"></a>

```
Type: AWS::SupportApp::AccountAlias
Properties:
  [AccountAlias](#cfn-supportapp-accountalias-accountalias): {{String}}
```

## Properties
<a name="aws-resource-supportapp-accountalias-properties"></a>

`AccountAlias`  <a name="cfn-supportapp-accountalias-accountalias"></a>
An alias or short name for an AWS account.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\- ]+$`
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-supportapp-accountalias-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-supportapp-accountalias-return-values-fn--getatt"></a>

####
<a name="aws-resource-supportapp-accountalias-return-values-fn--getatt-fn--getatt"></a>

`AccountAliasResourceId`  <a name="AccountAliasResourceId-fn::getatt"></a>
The `AccountAlias` resource type has an attribute `AccountAliasResourceId`. You can use this attribute to identify the resource.
The `AccountAliasResourceId` will be `AccountAlias_for_accountId`. In this example, `AccountAlias_for_` is the prefix and `accountId` is your AWS account number, such as `AccountAlias_for_123456789012`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
