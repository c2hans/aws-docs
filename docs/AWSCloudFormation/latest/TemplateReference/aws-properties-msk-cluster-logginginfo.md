---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-logginginfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster LoggingInfo
<a name="aws-properties-msk-cluster-logginginfo"></a>

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

## Syntax
<a name="aws-properties-msk-cluster-logginginfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-logginginfo-syntax.json"></a>

```
{
  "[AuthorizerLogs](#cfn-msk-cluster-logginginfo-authorizerlogs)" : {{AuthorizerLogs}},
  "[BrokerLogs](#cfn-msk-cluster-logginginfo-brokerlogs)" : {{BrokerLogs}}
}
```

### YAML
<a name="aws-properties-msk-cluster-logginginfo-syntax.yaml"></a>

```
  [AuthorizerLogs](#cfn-msk-cluster-logginginfo-authorizerlogs): {{
    AuthorizerLogs}}
  [BrokerLogs](#cfn-msk-cluster-logginginfo-brokerlogs): {{
    BrokerLogs}}
```

## Properties
<a name="aws-properties-msk-cluster-logginginfo-properties"></a>

`AuthorizerLogs`  <a name="cfn-msk-cluster-logginginfo-authorizerlogs"></a>
Property description not available.
*Required*: No
*Type*: [AuthorizerLogs](aws-properties-msk-cluster-authorizerlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrokerLogs`  <a name="cfn-msk-cluster-logginginfo-brokerlogs"></a>
You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations.
*Required*: No
*Type*: [BrokerLogs](aws-properties-msk-cluster-brokerlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
