---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::RoutingProfile RoutingProfileManualAssignmentQueueConfig
<a name="aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig"></a>

Contains information about the queue and channel for manual assignment behaviour can be enabled.

## Syntax
<a name="aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig-syntax.json"></a>

```
{
  "[QueueReference](#cfn-connect-routingprofile-routingprofilemanualassignmentqueueconfig-queuereference)" : {{RoutingProfileQueueReference}}
}
```

### YAML
<a name="aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig-syntax.yaml"></a>

```
  [QueueReference](#cfn-connect-routingprofile-routingprofilemanualassignmentqueueconfig-queuereference): {{
    RoutingProfileQueueReference}}
```

## Properties
<a name="aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig-properties"></a>

`QueueReference`  <a name="cfn-connect-routingprofile-routingprofilemanualassignmentqueueconfig-queuereference"></a>
Contains information about a queue resource.
*Required*: Yes
*Type*: [RoutingProfileQueueReference](aws-properties-connect-routingprofile-routingprofilequeuereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
