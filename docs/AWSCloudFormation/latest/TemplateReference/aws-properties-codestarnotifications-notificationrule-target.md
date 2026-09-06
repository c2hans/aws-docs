---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codestarnotifications-notificationrule-target.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStarNotifications::NotificationRule Target
<a name="aws-properties-codestarnotifications-notificationrule-target"></a>

Information about the Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients associated with a notification rule.

## Syntax
<a name="aws-properties-codestarnotifications-notificationrule-target-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codestarnotifications-notificationrule-target-syntax.json"></a>

```
{
  "[TargetAddress](#cfn-codestarnotifications-notificationrule-target-targetaddress)" : {{String}},
  "[TargetType](#cfn-codestarnotifications-notificationrule-target-targettype)" : {{String}}
}
```

### YAML
<a name="aws-properties-codestarnotifications-notificationrule-target-syntax.yaml"></a>

```
  [TargetAddress](#cfn-codestarnotifications-notificationrule-target-targetaddress): {{String}}
  [TargetType](#cfn-codestarnotifications-notificationrule-target-targettype): {{String}}
```

## Properties
<a name="aws-properties-codestarnotifications-notificationrule-target-properties"></a>

`TargetAddress`  <a name="cfn-codestarnotifications-notificationrule-target-targetaddress"></a>
The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `320`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetType`  <a name="cfn-codestarnotifications-notificationrule-target-targettype"></a>
The target type. Can be an Amazon Simple Notification Service topic or Amazon Q Developer in chat applications client.
+ Amazon Simple Notification Service topics are specified as `SNS`.
+ Amazon Q Developer in chat applications clients are specified as `AWSChatbotSlack`.
+ Amazon Q Developer in chat applications clients for Microsoft Teams are specified as `AWSChatbotMicrosoftTeams`.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
