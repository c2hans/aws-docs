---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-emailidentity-feedbackattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::EmailIdentity FeedbackAttributes
<a name="aws-properties-ses-emailidentity-feedbackattributes"></a>

Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

## Syntax
<a name="aws-properties-ses-emailidentity-feedbackattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-emailidentity-feedbackattributes-syntax.json"></a>

```
{
  "[EmailForwardingEnabled](#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ses-emailidentity-feedbackattributes-syntax.yaml"></a>

```
  [EmailForwardingEnabled](#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ses-emailidentity-feedbackattributes-properties"></a>

`EmailForwardingEnabled`  <a name="cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled"></a>
Sets the feedback forwarding configuration for the identity.
 If the value is `true`, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the `Return-Path` header of the original email.
 You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
