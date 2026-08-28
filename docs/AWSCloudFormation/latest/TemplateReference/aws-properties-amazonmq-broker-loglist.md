---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amazonmq-broker-loglist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::Broker LogList
<a name="aws-properties-amazonmq-broker-loglist"></a>

The list of information about logs to be enabled for the specified broker.

## Syntax
<a name="aws-properties-amazonmq-broker-loglist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amazonmq-broker-loglist-syntax.json"></a>

```
{
  "[Audit](#cfn-amazonmq-broker-loglist-audit)" : {{Boolean}},
  "[General](#cfn-amazonmq-broker-loglist-general)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-amazonmq-broker-loglist-syntax.yaml"></a>

```
  [Audit](#cfn-amazonmq-broker-loglist-audit): {{Boolean}}
  [General](#cfn-amazonmq-broker-loglist-general): {{Boolean}}
```

## Properties
<a name="aws-properties-amazonmq-broker-loglist-properties"></a>

`Audit`  <a name="cfn-amazonmq-broker-loglist-audit"></a>
Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`General`  <a name="cfn-amazonmq-broker-loglist-general"></a>
Enables general logging.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
