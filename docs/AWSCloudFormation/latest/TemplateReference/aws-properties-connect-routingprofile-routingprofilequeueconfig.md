---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-routingprofile-routingprofilequeueconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::RoutingProfile RoutingProfileQueueConfig
<a name="aws-properties-connect-routingprofile-routingprofilequeueconfig"></a>

Contains information about the queue and channel for which priority and delay can be set.

## Syntax
<a name="aws-properties-connect-routingprofile-routingprofilequeueconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-routingprofile-routingprofilequeueconfig-syntax.json"></a>

```
{
  "[Delay](#cfn-connect-routingprofile-routingprofilequeueconfig-delay)" : {{Integer}},
  "[Priority](#cfn-connect-routingprofile-routingprofilequeueconfig-priority)" : {{Integer}},
  "[QueueReference](#cfn-connect-routingprofile-routingprofilequeueconfig-queuereference)" : {{RoutingProfileQueueReference}}
}
```

### YAML
<a name="aws-properties-connect-routingprofile-routingprofilequeueconfig-syntax.yaml"></a>

```
  [Delay](#cfn-connect-routingprofile-routingprofilequeueconfig-delay): {{Integer}}
  [Priority](#cfn-connect-routingprofile-routingprofilequeueconfig-priority): {{Integer}}
  [QueueReference](#cfn-connect-routingprofile-routingprofilequeueconfig-queuereference): {{
    RoutingProfileQueueReference}}
```

## Properties
<a name="aws-properties-connect-routingprofile-routingprofilequeueconfig-properties"></a>

`Delay`  <a name="cfn-connect-routingprofile-routingprofilequeueconfig-delay"></a>
The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html) in the *Connect Customer Administrator Guide*.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `9999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-connect-routingprofile-routingprofilequeueconfig-priority"></a>
The order in which contacts are to be handled for the queue. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html).
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueReference`  <a name="cfn-connect-routingprofile-routingprofilequeueconfig-queuereference"></a>
Contains information about a queue resource.
*Required*: Yes
*Type*: [RoutingProfileQueueReference](aws-properties-connect-routingprofile-routingprofilequeuereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
