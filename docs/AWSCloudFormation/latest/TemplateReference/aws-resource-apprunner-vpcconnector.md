---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apprunner-vpcconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::VpcConnector
<a name="aws-resource-apprunner-vpcconnector"></a>

The `AWS::AppRunner::VpcConnector` resource is an AWS App Runner resource type that specifies an App Runner VPC connector.

App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud (Amazon VPC).

## Syntax
<a name="aws-resource-apprunner-vpcconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apprunner-vpcconnector-syntax.json"></a>

```
{
  "Type" : "AWS::AppRunner::VpcConnector",
  "Properties" : {
      "[SecurityGroups](#cfn-apprunner-vpcconnector-securitygroups)" : {{[ String, ... ]}},
      "[Subnets](#cfn-apprunner-vpcconnector-subnets)" : {{[ String, ... ]}},
      "[Tags](#cfn-apprunner-vpcconnector-tags)" : {{[ Tag, ... ]}},
      "[VpcConnectorName](#cfn-apprunner-vpcconnector-vpcconnectorname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-apprunner-vpcconnector-syntax.yaml"></a>

```
Type: AWS::AppRunner::VpcConnector
Properties:
  [SecurityGroups](#cfn-apprunner-vpcconnector-securitygroups): {{
    - String}}
  [Subnets](#cfn-apprunner-vpcconnector-subnets): {{
    - String}}
  [Tags](#cfn-apprunner-vpcconnector-tags): {{
    - Tag}}
  [VpcConnectorName](#cfn-apprunner-vpcconnector-vpcconnectorname): {{String}}
```

## Properties
<a name="aws-resource-apprunner-vpcconnector-properties"></a>

`SecurityGroups`  <a name="cfn-apprunner-vpcconnector-securitygroups"></a>
A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-apprunner-vpcconnector-subnets"></a>
A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
 App Runner only supports subnets of IP address type *IPv4* and *dual stack* (IPv4 and IPv6).
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-apprunner-vpcconnector-tags"></a>
A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
A `VpcConnector` is immutable, so you cannot update its tags. To change the tags, replace the resource. To replace a `VpcConnector`, you must provide a new combination of security groups.
*Required*: No
*Type*: Array of [Tag](aws-properties-apprunner-vpcconnector-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConnectorName`  <a name="cfn-apprunner-vpcconnector-vpcconnectorname"></a>
A name for the VPC connector.
If you don't specify a name, CloudFormation generates a name for your VPC connector.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9-\\_]{3,39}$`
*Minimum*: `4`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-apprunner-vpcconnector-return-values"></a>

### Ref
<a name="aws-resource-apprunner-vpcconnector-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apprunner-vpcconnector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apprunner-vpcconnector-return-values-fn--getatt-fn--getatt"></a>

`VpcConnectorArn`  <a name="VpcConnectorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of this VPC connector.

`VpcConnectorRevision`  <a name="VpcConnectorRevision-fn::getatt"></a>
The revision of this VPC connector. It's unique among all the active connectors (`"Status": "ACTIVE"`) that share the same `Name`.
At this time, App Runner supports only one revision per name.

## Examples
<a name="aws-resource-apprunner-vpcconnector--examples"></a>

### VPC connector
<a name="aws-resource-apprunner-vpcconnector--examples--VPC_connector"></a>

This example illustrates creating a VPC connector with two subnets and two security groups.

#### JSON
<a name="aws-resource-apprunner-vpcconnector--examples--VPC_connector--json"></a>

```
{
  "Type" : "AWS::AppRunner::VpcConnector",
  "Properties" : {
    "VpcConnectorName": "my-vpc-connector",
    "Subnets": ["subnet-123", "subnet-456"],
    "SecurityGroups": ["sg-123", "sg-456"]
  }
}
```

#### YAML
<a name="aws-resource-apprunner-vpcconnector--examples--VPC_connector--yaml"></a>

```
Type: AWS::AppRunner::VpcConnector
Properties:
  VpcConnectorName: my-vpc-connector
  Subnets:
    - subnet-123
    - subnet-456
  SecurityGroups:
    - sg-123
    - sg-456
```

## See also
<a name="aws-resource-apprunner-vpcconnector--seealso"></a>
+ [Enabling Amazon VPC access for your service](https://docs.aws.amazon.com/apprunner/latest/dg/network-vpc.html) in the *AWS App Runner Developer Guide*
