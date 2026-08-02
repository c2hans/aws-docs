---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-ingresspathsummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService IngressPathSummary
<a name="aws-properties-ecs-expressgatewayservice-ingresspathsummary"></a>

The entry point into an Express service.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-ingresspathsummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-ingresspathsummary-syntax.json"></a>

```
{
  "[AccessType](#cfn-ecs-expressgatewayservice-ingresspathsummary-accesstype)" : {{String}},
  "[Endpoint](#cfn-ecs-expressgatewayservice-ingresspathsummary-endpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-ingresspathsummary-syntax.yaml"></a>

```
  [AccessType](#cfn-ecs-expressgatewayservice-ingresspathsummary-accesstype): {{String}}
  [Endpoint](#cfn-ecs-expressgatewayservice-ingresspathsummary-endpoint): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-ingresspathsummary-properties"></a>

`AccessType`  <a name="cfn-ecs-expressgatewayservice-ingresspathsummary-accesstype"></a>
The type of access to the endpoint for the Express service.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | PRIVATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-ecs-expressgatewayservice-ingresspathsummary-endpoint"></a>
The endpoint for access to the service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
