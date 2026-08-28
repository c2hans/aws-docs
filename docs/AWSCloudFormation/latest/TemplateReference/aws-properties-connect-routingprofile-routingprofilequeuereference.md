---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-routingprofile-routingprofilequeuereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::RoutingProfile RoutingProfileQueueReference
<a name="aws-properties-connect-routingprofile-routingprofilequeuereference"></a>

Contains the channel and queue identifier for a routing profile.

## Syntax
<a name="aws-properties-connect-routingprofile-routingprofilequeuereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-routingprofile-routingprofilequeuereference-syntax.json"></a>

```
{
  "[Channel](#cfn-connect-routingprofile-routingprofilequeuereference-channel)" : {{String}},
  "[QueueArn](#cfn-connect-routingprofile-routingprofilequeuereference-queuearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-routingprofile-routingprofilequeuereference-syntax.yaml"></a>

```
  [Channel](#cfn-connect-routingprofile-routingprofilequeuereference-channel): {{String}}
  [QueueArn](#cfn-connect-routingprofile-routingprofilequeuereference-queuearn): {{String}}
```

## Properties
<a name="aws-properties-connect-routingprofile-routingprofilequeuereference-properties"></a>

`Channel`  <a name="cfn-connect-routingprofile-routingprofilequeuereference-channel"></a>
The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueArn`  <a name="cfn-connect-routingprofile-routingprofilequeuereference-queuearn"></a>
The Amazon Resource Name (ARN) of the queue.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/queue/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
