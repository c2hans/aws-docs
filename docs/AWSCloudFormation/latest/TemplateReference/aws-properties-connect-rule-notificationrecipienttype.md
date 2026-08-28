---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-notificationrecipienttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule NotificationRecipientType
<a name="aws-properties-connect-rule-notificationrecipienttype"></a>

The type of notification recipient.

## Syntax
<a name="aws-properties-connect-rule-notificationrecipienttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-notificationrecipienttype-syntax.json"></a>

```
{
  "[UserArns](#cfn-connect-rule-notificationrecipienttype-userarns)" : {{[ String, ... ]}},
  "[UserTags](#cfn-connect-rule-notificationrecipienttype-usertags)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-notificationrecipienttype-syntax.yaml"></a>

```
  [UserArns](#cfn-connect-rule-notificationrecipienttype-userarns): {{
    - String}}
  [UserTags](#cfn-connect-rule-notificationrecipienttype-usertags): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-notificationrecipienttype-properties"></a>

`UserArns`  <a name="cfn-connect-rule-notificationrecipienttype-userarns"></a>
The Amazon Resource Name (ARN) of the user account.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserTags`  <a name="cfn-connect-rule-notificationrecipienttype-usertags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }. Connect Customer users with the specified tags will be notified.
*Required*: No
*Type*: String
*Pattern*: `^.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
