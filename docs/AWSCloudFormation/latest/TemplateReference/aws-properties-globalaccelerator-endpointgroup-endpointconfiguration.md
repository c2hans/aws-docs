---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::EndpointGroup EndpointConfiguration
<a name="aws-properties-globalaccelerator-endpointgroup-endpointconfiguration"></a>

A complex type for endpoints. A resource must be valid and active when you add it as an endpoint.

## Syntax
<a name="aws-properties-globalaccelerator-endpointgroup-endpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-globalaccelerator-endpointgroup-endpointconfiguration-syntax.json"></a>

```
{
  "[AttachmentArn](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-attachmentarn)" : {{String}},
  "[ClientIPPreservationEnabled](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled)" : {{Boolean}},
  "[EndpointId](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid)" : {{String}},
  "[Weight](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-globalaccelerator-endpointgroup-endpointconfiguration-syntax.yaml"></a>

```
  [AttachmentArn](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-attachmentarn): {{String}}
  [ClientIPPreservationEnabled](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled): {{Boolean}}
  [EndpointId](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid): {{String}}
  [Weight](#cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight): {{Integer}}
```

## Properties
<a name="aws-properties-globalaccelerator-endpointgroup-endpointconfiguration-properties"></a>

`AttachmentArn`  <a name="cfn-globalaccelerator-endpointgroup-endpointconfiguration-attachmentarn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment that specifies the endpoints (resources) that can be added to accelerators and principals that have permission to add the endpoints.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientIPPreservationEnabled`  <a name="cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled"></a>
Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.
If the value is set to true, the client's IP address is preserved in the `X-Forwarded-For` request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.
For more information, see [ Preserve Client IP Addresses](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html) in the *AWS Global Accelerator Developer Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointId`  <a name="cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid"></a>
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. A resource must be valid and active when you add it as an endpoint.
For cross-account endpoints, this must be the ARN of the resource.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight"></a>
The weight associated with the endpoint. When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see [Endpoint Weights](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html) in the *AWS Global Accelerator Developer Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
