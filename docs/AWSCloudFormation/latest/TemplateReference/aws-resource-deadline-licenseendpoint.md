---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-licenseendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::LicenseEndpoint
<a name="aws-resource-deadline-licenseendpoint"></a>

Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.

## Syntax
<a name="aws-resource-deadline-licenseendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-licenseendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::LicenseEndpoint",
  "Properties" : {
      "[SecurityGroupIds](#cfn-deadline-licenseendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetIds](#cfn-deadline-licenseendpoint-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-deadline-licenseendpoint-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-deadline-licenseendpoint-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-licenseendpoint-syntax.yaml"></a>

```
Type: AWS::Deadline::LicenseEndpoint
Properties:
  [SecurityGroupIds](#cfn-deadline-licenseendpoint-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-deadline-licenseendpoint-subnetids): {{
    - String}}
  [Tags](#cfn-deadline-licenseendpoint-tags): {{
    - Tag}}
  [VpcId](#cfn-deadline-licenseendpoint-vpcid): {{String}}
```

## Properties
<a name="aws-resource-deadline-licenseendpoint-properties"></a>

`SecurityGroupIds`  <a name="cfn-deadline-licenseendpoint-securitygroupids"></a>
The identifier of the Amazon EC2 security group that controls access to the license endpoint.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-deadline-licenseendpoint-subnetids"></a>
Identifies the VPC subnets that can connect to a license endpoint.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `32 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-deadline-licenseendpoint-tags"></a>
The tags to add to your license endpoint. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-licenseendpoint-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-deadline-licenseendpoint-vpcid"></a>
The VPC (virtual private cloud) ID associated with the license endpoint.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-licenseendpoint-return-values"></a>

### Ref
<a name="aws-resource-deadline-licenseendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the license endpoint.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-licenseendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-licenseendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the license endpoint.

`DnsName`  <a name="DnsName-fn::getatt"></a>
The DNS name of the license server endpoint.

`LicenseEndpointId`  <a name="LicenseEndpointId-fn::getatt"></a>
The license endpoint ID.

`Status`  <a name="Status-fn::getatt"></a>
The status of the license endpoint.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
The status message of the license endpoint.
