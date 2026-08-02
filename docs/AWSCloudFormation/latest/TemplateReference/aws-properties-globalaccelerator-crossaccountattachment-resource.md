---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-globalaccelerator-crossaccountattachment-resource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::CrossAccountAttachment Resource
<a name="aws-properties-globalaccelerator-crossaccountattachment-resource"></a>

A resource is one of the following: the ARN for an AWS resource that is supported by AWS Global Accelerator to be added as an endpoint, or a CIDR range that specifies a bring your own IP (BYOIP) address pool.

## Syntax
<a name="aws-properties-globalaccelerator-crossaccountattachment-resource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-globalaccelerator-crossaccountattachment-resource-syntax.json"></a>

```
{
  "[Cidr](#cfn-globalaccelerator-crossaccountattachment-resource-cidr)" : {{String}},
  "[EndpointId](#cfn-globalaccelerator-crossaccountattachment-resource-endpointid)" : {{String}},
  "[Region](#cfn-globalaccelerator-crossaccountattachment-resource-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-globalaccelerator-crossaccountattachment-resource-syntax.yaml"></a>

```
  [Cidr](#cfn-globalaccelerator-crossaccountattachment-resource-cidr): {{String}}
  [EndpointId](#cfn-globalaccelerator-crossaccountattachment-resource-endpointid): {{String}}
  [Region](#cfn-globalaccelerator-crossaccountattachment-resource-region): {{String}}
```

## Properties
<a name="aws-properties-globalaccelerator-crossaccountattachment-resource-properties"></a>

`Cidr`  <a name="cfn-globalaccelerator-crossaccountattachment-resource-cidr"></a>
An IP address range, in CIDR format, that is specified as resource. The address must be provisioned and advertised in AWS Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointId`  <a name="cfn-globalaccelerator-crossaccountattachment-resource-endpointid"></a>
The endpoint ID for the endpoint that is specified as a AWS resource.
An endpoint ID for the cross-account feature is the ARN of an AWS resource, such as a Network Load Balancer, that Global Accelerator supports as an endpoint for an accelerator.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-globalaccelerator-crossaccountattachment-resource-region"></a>
The AWS Region where a shared endpoint resource is located.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
