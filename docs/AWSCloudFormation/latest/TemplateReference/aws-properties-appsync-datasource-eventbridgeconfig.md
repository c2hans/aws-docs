---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-eventbridgeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource EventBridgeConfig
<a name="aws-properties-appsync-datasource-eventbridgeconfig"></a>

The data source. This can be an API destination, resource, or AWS service.

## Syntax
<a name="aws-properties-appsync-datasource-eventbridgeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-eventbridgeconfig-syntax.json"></a>

```
{
  "[EventBusArn](#cfn-appsync-datasource-eventbridgeconfig-eventbusarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-eventbridgeconfig-syntax.yaml"></a>

```
  [EventBusArn](#cfn-appsync-datasource-eventbridgeconfig-eventbusarn): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-eventbridgeconfig-properties"></a>

`EventBusArn`  <a name="cfn-appsync-datasource-eventbridgeconfig-eventbusarn"></a>
The event bus pipeline's ARN. For more information about event buses, see [EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
