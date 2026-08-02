---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttesttrafficrules.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectTestTrafficRules
<a name="aws-properties-ecs-service-serviceconnecttesttrafficrules"></a>

The test traffic routing configuration for Amazon ECS blue/green deployments. This configuration allows you to define rules for routing specific traffic to the new service revision during the deployment process, allowing for safe testing before full production traffic shift.

For more information, see [Service Connect for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-blue-green.html) in the * Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-serviceconnecttesttrafficrules-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnecttesttrafficrules-syntax.json"></a>

```
{
  "[Header](#cfn-ecs-service-serviceconnecttesttrafficrules-header)" : {{ServiceConnectTestTrafficRulesHeader}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnecttesttrafficrules-syntax.yaml"></a>

```
  [Header](#cfn-ecs-service-serviceconnecttesttrafficrules-header): {{
    ServiceConnectTestTrafficRulesHeader}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnecttesttrafficrules-properties"></a>

`Header`  <a name="cfn-ecs-service-serviceconnecttesttrafficrules-header"></a>
The HTTP header-based routing rules that determine which requests should be routed to the new service version during blue/green deployment testing. These rules provide fine-grained control over test traffic routing based on request headers.
*Required*: Yes
*Type*: [ServiceConnectTestTrafficRulesHeader](aws-properties-ecs-service-serviceconnecttesttrafficrulesheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
