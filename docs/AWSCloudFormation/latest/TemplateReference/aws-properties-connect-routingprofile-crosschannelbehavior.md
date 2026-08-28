---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-routingprofile-crosschannelbehavior.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::RoutingProfile CrossChannelBehavior
<a name="aws-properties-connect-routingprofile-crosschannelbehavior"></a>

Defines the cross-channel routing behavior that allows an agent working on a contact in one channel to be offered a contact from a different channel.

## Syntax
<a name="aws-properties-connect-routingprofile-crosschannelbehavior-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-routingprofile-crosschannelbehavior-syntax.json"></a>

```
{
  "[BehaviorType](#cfn-connect-routingprofile-crosschannelbehavior-behaviortype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-routingprofile-crosschannelbehavior-syntax.yaml"></a>

```
  [BehaviorType](#cfn-connect-routingprofile-crosschannelbehavior-behaviortype): {{String}}
```

## Properties
<a name="aws-properties-connect-routingprofile-crosschannelbehavior-properties"></a>

`BehaviorType`  <a name="cfn-connect-routingprofile-crosschannelbehavior-behaviortype"></a>
Specifies the other channels that can be routed to an agent handling their current channel.
*Required*: Yes
*Type*: String
*Allowed values*: `ROUTE_CURRENT_CHANNEL_ONLY | ROUTE_ANY_CHANNEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
