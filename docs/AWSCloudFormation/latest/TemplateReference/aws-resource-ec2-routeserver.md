---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routeserver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServer
<a name="aws-resource-ec2-routeserver"></a>

Specifies a route server to manage dynamic routing in a VPC.

Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads.

For more information see [Dynamic routing in your VPC with VPC Route Server](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-routeserver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-routeserver-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::RouteServer",
  "Properties" : {
      "[AmazonSideAsn](#cfn-ec2-routeserver-amazonsideasn)" : {{Integer}},
      "[PersistRoutes](#cfn-ec2-routeserver-persistroutes)" : {{String}},
      "[PersistRoutesDuration](#cfn-ec2-routeserver-persistroutesduration)" : {{Integer}},
      "[SnsNotificationsEnabled](#cfn-ec2-routeserver-snsnotificationsenabled)" : {{Boolean}},
      "[Tags](#cfn-ec2-routeserver-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-routeserver-syntax.yaml"></a>

```
Type: AWS::EC2::RouteServer
Properties:
  [AmazonSideAsn](#cfn-ec2-routeserver-amazonsideasn): {{Integer}}
  [PersistRoutes](#cfn-ec2-routeserver-persistroutes): {{String}}
  [PersistRoutesDuration](#cfn-ec2-routeserver-persistroutesduration): {{Integer}}
  [SnsNotificationsEnabled](#cfn-ec2-routeserver-snsnotificationsenabled): {{Boolean}}
  [Tags](#cfn-ec2-routeserver-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-routeserver-properties"></a>

`AmazonSideAsn`  <a name="cfn-ec2-routeserver-amazonsideasn"></a>
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4294967294`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersistRoutes`  <a name="cfn-ec2-routeserver-persistroutes"></a>
Indicates whether routes should be persisted after all BGP sessions are terminated.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistRoutesDuration`  <a name="cfn-ec2-routeserver-persistroutesduration"></a>
The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. Value must be in the range of 1-5. The default value is 1. Only valid if `persistRoutesState` is 'enabled'.
If you set the duration to 1 minute, then when your network appliance re-establishes BGP with route server, it has 1 minute to relearn it's adjacent network and advertise those routes to route server before route server resumes normal functionality. In most cases, 1 minute is probably sufficient. If, however, you have concerns that your BGP network may not be capable of fully re-establishing and re-learning everything in 1 minute, you can increase the duration up to 5 minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsNotificationsEnabled`  <a name="cfn-ec2-routeserver-snsnotificationsenabled"></a>
Indicates whether SNS notifications are enabled for the route server. Enabling SNS notifications persists BGP status changes to an SNS topic provisioned by AWS.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-routeserver-tags"></a>
Any tags assigned to the route server.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-routeserver-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-routeserver-return-values"></a>

### Ref
<a name="aws-resource-ec2-routeserver-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the route server ID.

### Fn::GetAtt
<a name="aws-resource-ec2-routeserver-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-routeserver-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the route server.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the route server.
