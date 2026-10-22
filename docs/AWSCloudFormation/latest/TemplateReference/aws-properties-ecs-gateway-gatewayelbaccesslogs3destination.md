---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogs3destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayElbAccessLogS3Destination
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogs3destination"></a>

The Amazon S3 destination for the access logs of a gateway's load balancers.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogs3destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogs3destination-syntax.json"></a>

```
{
  "[Bucket](#cfn-ecs-gateway-gatewayelbaccesslogs3destination-bucket)" : {{String}},
  "[Prefix](#cfn-ecs-gateway-gatewayelbaccesslogs3destination-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogs3destination-syntax.yaml"></a>

```
  [Bucket](#cfn-ecs-gateway-gatewayelbaccesslogs3destination-bucket): {{String}}
  [Prefix](#cfn-ecs-gateway-gatewayelbaccesslogs3destination-prefix): {{String}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogs3destination-properties"></a>

`Bucket`  <a name="cfn-ecs-gateway-gatewayelbaccesslogs3destination-bucket"></a>
The name of the Amazon S3 bucket where access logs are delivered.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-ecs-gateway-gatewayelbaccesslogs3destination-prefix"></a>
The object key prefix for the access logs in the Amazon S3 bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
