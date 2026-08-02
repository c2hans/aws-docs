---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceStatus
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus"></a>

An object that defines the status of Express service creation and information about the status of the service.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus-syntax.json"></a>

```
{
  "[StatusCode](#cfn-ecs-expressgatewayservice-expressgatewayservicestatus-statuscode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus-syntax.yaml"></a>

```
  [StatusCode](#cfn-ecs-expressgatewayservice-expressgatewayservicestatus-statuscode): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus-properties"></a>

`StatusCode`  <a name="cfn-ecs-expressgatewayservice-expressgatewayservicestatus-statuscode"></a>
The status of the Express service.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | DRAINING | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
