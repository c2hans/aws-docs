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
  "[BrokerLogs](#cfn-msk-cluster-logginginfo-brokerlogs)" : {{BrokerLogs}}
}
```

### YAML
<a name="aws-properties-msk-cluster-logginginfo-syntax.yaml"></a>

```
  [BrokerLogs](#cfn-msk-cluster-logginginfo-brokerlogs): {{
    BrokerLogs}}
```

## Properties
<a name="aws-properties-msk-cluster-logginginfo-properties"></a>

`BrokerLogs`  <a name="cfn-msk-cluster-logginginfo-brokerlogs"></a>
You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations.
*Required*: Yes
*Type*: [BrokerLogs](aws-properties-msk-cluster-brokerlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
