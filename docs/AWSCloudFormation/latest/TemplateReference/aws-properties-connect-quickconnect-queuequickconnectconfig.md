---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-quickconnect-queuequickconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::QuickConnect QueueQuickConnectConfig
<a name="aws-properties-connect-quickconnect-queuequickconnectconfig"></a>

Contains information about a queue for a quick connect. The flow must be of type Transfer to Queue.

## Syntax
<a name="aws-properties-connect-quickconnect-queuequickconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-quickconnect-queuequickconnectconfig-syntax.json"></a>

```
{
  "[ContactFlowArn](#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn)" : {{String}},
  "[QueueArn](#cfn-connect-quickconnect-queuequickconnectconfig-queuearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-quickconnect-queuequickconnectconfig-syntax.yaml"></a>

```
  [ContactFlowArn](#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn): {{String}}
  [QueueArn](#cfn-connect-quickconnect-queuequickconnectconfig-queuearn): {{String}}
```

## Properties
<a name="aws-properties-connect-quickconnect-queuequickconnectconfig-properties"></a>

`ContactFlowArn`  <a name="cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn"></a>
The Amazon Resource Name (ARN) of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*(:[a-zA-Z0-9-]+)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueArn`  <a name="cfn-connect-quickconnect-queuequickconnectconfig-queuearn"></a>
The Amazon Resource Name (ARN) of the queue.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/queue/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
