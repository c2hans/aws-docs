---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instanceconnectendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::InstanceConnectEndpoint
<a name="aws-resource-ec2-instanceconnectendpoint"></a>

Creates an EC2 Instance Connect Endpoint.

An EC2 Instance Connect Endpoint allows you to connect to an instance, without requiring the instance to have a public IPv4 address. For more information, see [Connect to your instances using EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect-Endpoint.html) in the *Amazon EC2 User Guide*.

With the replacement update behavior, CloudFormation usually creates the new resource first, changes references to point to the new resource, and then deletes the old resource. However, you can create only one EC2 Instance Connect Endpoint per VPC, so the replacement process fails. If you need to modify an EC2 Instance Connect Endpoint, you must replace the resource manually.

## Syntax
<a name="aws-resource-ec2-instanceconnectendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-instanceconnectendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::InstanceConnectEndpoint",
  "Properties" : {
      "[ClientToken](#cfn-ec2-instanceconnectendpoint-clienttoken)" : {{String}},
      "[PreserveClientIp](#cfn-ec2-instanceconnectendpoint-preserveclientip)" : {{Boolean}},
      "[SecurityGroupIds](#cfn-ec2-instanceconnectendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetId](#cfn-ec2-instanceconnectendpoint-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-instanceconnectendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-instanceconnectendpoint-syntax.yaml"></a>

```
Type: AWS::EC2::InstanceConnectEndpoint
Properties:
  [ClientToken](#cfn-ec2-instanceconnectendpoint-clienttoken): {{String}}
  [PreserveClientIp](#cfn-ec2-instanceconnectendpoint-preserveclientip): {{Boolean}}
  [SecurityGroupIds](#cfn-ec2-instanceconnectendpoint-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-ec2-instanceconnectendpoint-subnetid): {{String}}
  [Tags](#cfn-ec2-instanceconnectendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-instanceconnectendpoint-properties"></a>

`ClientToken`  <a name="cfn-ec2-instanceconnectendpoint-clienttoken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreserveClientIp`  <a name="cfn-ec2-instanceconnectendpoint-preserveclientip"></a>
Indicates whether the client IP address is preserved as the source. The following are the possible values.
+ `true` - Use the client IP address as the source.
+ `false` - Use the network interface IP address as the source.
`PreserveClientIp` is only supported on IPv4 EC2 Instance Connect Endpoints. To use `PreserveClientIp`, the value for `IpAddressType` must be `ipv4`.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-ec2-instanceconnectendpoint-securitygroupids"></a>
One or more security groups to associate with the endpoint. If you don't specify a security group, the default security group for your VPC will be associated with the endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-instanceconnectendpoint-subnetid"></a>
The ID of the subnet in which to create the EC2 Instance Connect Endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-instanceconnectendpoint-tags"></a>
The tags to apply to the EC2 Instance Connect Endpoint during creation.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-instanceconnectendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-instanceconnectendpoint-return-values"></a>

### Ref
<a name="aws-resource-ec2-instanceconnectendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the EC2 Instance Connect Endpoint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-instanceconnectendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-instanceconnectendpoint-return-values-fn--getatt-fn--getatt"></a>

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone of the EC2 Instance Connect Endpoint.

`AvailabilityZoneId`  <a name="AvailabilityZoneId-fn::getatt"></a>
The ID of the Availability Zone of the EC2 Instance Connect Endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the EC2 Instance Connect Endpoint was created.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the EC2 Instance Connect Endpoint.

`InstanceConnectEndpointArn`  <a name="InstanceConnectEndpointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the EC2 Instance Connect Endpoint.

`NetworkInterfaceIds`  <a name="NetworkInterfaceIds-fn::getatt"></a>
The ID of the elastic network interface that Amazon EC2 automatically created when creating the EC2 Instance Connect Endpoint.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that created the EC2 Instance Connect Endpoint.

`State`  <a name="State-fn::getatt"></a>
The current state of the EC2 Instance Connect Endpoint.

`StateMessage`  <a name="StateMessage-fn::getatt"></a>
The message for the current state of the EC2 Instance Connect Endpoint. Can include a failure message.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC in which the EC2 Instance Connect Endpoint was created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
