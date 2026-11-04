---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-osis-pipelineendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::PipelineEndpoint
<a name="aws-resource-osis-pipelineendpoint"></a>

Represents a VPC endpoint for an OpenSearch Ingestion pipeline, enabling private connectivity between your VPC and the pipeline.

## Syntax
<a name="aws-resource-osis-pipelineendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-osis-pipelineendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::OSIS::PipelineEndpoint",
  "Properties" : {
      "[PipelineArn](#cfn-osis-pipelineendpoint-pipelinearn)" : {{String}},
      "[VpcOptions](#cfn-osis-pipelineendpoint-vpcoptions)" : {{VpcOptions}}
    }
}
```

### YAML
<a name="aws-resource-osis-pipelineendpoint-syntax.yaml"></a>

```
Type: AWS::OSIS::PipelineEndpoint
Properties:
  [PipelineArn](#cfn-osis-pipelineendpoint-pipelinearn): {{String}}
  [VpcOptions](#cfn-osis-pipelineendpoint-vpcoptions): {{
    VpcOptions}}
```

## Properties
<a name="aws-resource-osis-pipelineendpoint-properties"></a>

`PipelineArn`  <a name="cfn-osis-pipelineendpoint-pipelinearn"></a>
The Amazon Resource Name (ARN) of the pipeline associated with this endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):osis:.+:pipeline/.+$`
*Minimum*: `46`
*Maximum*: `76`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcOptions`  <a name="cfn-osis-pipelineendpoint-vpcoptions"></a>
Configuration options for the VPC endpoint, including subnet and security group settings.
*Required*: Yes
*Type*: [VpcOptions](aws-properties-osis-pipelineendpoint-vpcoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-osis-pipelineendpoint-return-values"></a>

### Ref
<a name="aws-resource-osis-pipelineendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-osis-pipelineendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-osis-pipelineendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`EndpointId`  <a name="EndpointId-fn::getatt"></a>
The unique identifier for the pipeline endpoint.

`IngestEndpointUrl`  <a name="IngestEndpointUrl-fn::getatt"></a>
The URL used to ingest data to the pipeline through the VPC endpoint.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the pipeline endpoint.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC where the pipeline endpoint is created.
