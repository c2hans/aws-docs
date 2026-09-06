---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-connectivityparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection ConnectivityParameters
<a name="aws-properties-events-connection-connectivityparameters"></a>

If you specify a private OAuth endpoint, the parameters for EventBridge to use when authenticating against the endpoint.

For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* *.

## Syntax
<a name="aws-properties-events-connection-connectivityparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-connectivityparameters-syntax.json"></a>

```
{
  "[ResourceParameters](#cfn-events-connection-connectivityparameters-resourceparameters)" : {{ResourceParameters}}
}
```

### YAML
<a name="aws-properties-events-connection-connectivityparameters-syntax.yaml"></a>

```
  [ResourceParameters](#cfn-events-connection-connectivityparameters-resourceparameters): {{
    ResourceParameters}}
```

## Properties
<a name="aws-properties-events-connection-connectivityparameters-properties"></a>

`ResourceParameters`  <a name="cfn-events-connection-connectivityparameters-resourceparameters"></a>
The parameters for EventBridge to use when invoking the resource endpoint.
*Required*: Yes
*Type*: [ResourceParameters](aws-properties-events-connection-resourceparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
