---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-invocationconnectivityparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection InvocationConnectivityParameters
<a name="aws-properties-events-connection-invocationconnectivityparameters"></a>

For connections to private APIs, the parameters to use for invoking the API.

For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* *.

## Syntax
<a name="aws-properties-events-connection-invocationconnectivityparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-invocationconnectivityparameters-syntax.json"></a>

```
{
  "[ResourceParameters](#cfn-events-connection-invocationconnectivityparameters-resourceparameters)" : {{ResourceParameters}}
}
```

### YAML
<a name="aws-properties-events-connection-invocationconnectivityparameters-syntax.yaml"></a>

```
  [ResourceParameters](#cfn-events-connection-invocationconnectivityparameters-resourceparameters): {{
    ResourceParameters}}
```

## Properties
<a name="aws-properties-events-connection-invocationconnectivityparameters-properties"></a>

`ResourceParameters`  <a name="cfn-events-connection-invocationconnectivityparameters-resourceparameters"></a>
The parameters for EventBridge to use when invoking the resource endpoint.
*Required*: Yes
*Type*: [ResourceParameters](aws-properties-events-connection-resourceparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
