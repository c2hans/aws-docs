---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-windowsuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue WindowsUser
<a name="aws-properties-deadline-queue-windowsuser"></a>

The Windows user details.

## Syntax
<a name="aws-properties-deadline-queue-windowsuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-windowsuser-syntax.json"></a>

```
{
  "[PasswordArn](#cfn-deadline-queue-windowsuser-passwordarn)" : {{String}},
  "[User](#cfn-deadline-queue-windowsuser-user)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-queue-windowsuser-syntax.yaml"></a>

```
  [PasswordArn](#cfn-deadline-queue-windowsuser-passwordarn): {{String}}
  [User](#cfn-deadline-queue-windowsuser-user): {{String}}
```

## Properties
<a name="aws-properties-deadline-queue-windowsuser-properties"></a>

`PasswordArn`  <a name="cfn-deadline-queue-windowsuser-passwordarn"></a>
The password ARN for the Windows user.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:secret:[a-zA-Z0-9-/_+=.@]{1,2028}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-deadline-queue-windowsuser-user"></a>
The user.
*Required*: Yes
*Type*: String
*Pattern*: `^[^"'/\[\]:;|=,+*?<>\s]*$`
*Minimum*: `0`
*Maximum*: `111`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
