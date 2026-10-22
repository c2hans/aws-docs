---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayElbAccessLogDestination
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogdestination"></a>

The destination where the access logs for a gateway's load balancers are delivered.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogdestination-syntax.json"></a>

```
{
  "[S3](#cfn-ecs-gateway-gatewayelbaccesslogdestination-s3)" : {{GatewayElbAccessLogS3Destination}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogdestination-syntax.yaml"></a>

```
  [S3](#cfn-ecs-gateway-gatewayelbaccesslogdestination-s3): {{
    GatewayElbAccessLogS3Destination}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogdestination-properties"></a>

`S3`  <a name="cfn-ecs-gateway-gatewayelbaccesslogdestination-s3"></a>
The Amazon S3 destination for access logs.
*Required*: No
*Type*: [GatewayElbAccessLogS3Destination](aws-properties-ecs-gateway-gatewayelbaccesslogs3destination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
