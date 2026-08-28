---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-respondergateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway
<a name="aws-resource-rtbfabric-respondergateway"></a>

Creates a responder gateway.

**Important**
A domain name or managed endpoint is required.

## Syntax
<a name="aws-resource-rtbfabric-respondergateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-respondergateway-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::ResponderGateway",
  "Properties" : {
      "[AcmCertificateArn](#cfn-rtbfabric-respondergateway-acmcertificatearn)" : {{String}},
      "[Description](#cfn-rtbfabric-respondergateway-description)" : {{String}},
      "[DomainName](#cfn-rtbfabric-respondergateway-domainname)" : {{String}},
      "[GatewayType](#cfn-rtbfabric-respondergateway-gatewaytype)" : {{String}},
      "[ListenerConfig](#cfn-rtbfabric-respondergateway-listenerconfig)" : {{ListenerConfig}},
      "[ManagedEndpointConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration)" : {{ManagedEndpointConfiguration}},
      "[Port](#cfn-rtbfabric-respondergateway-port)" : {{Integer}},
      "[Protocol](#cfn-rtbfabric-respondergateway-protocol)" : {{String}},
      "[SecurityGroupIds](#cfn-rtbfabric-respondergateway-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetIds](#cfn-rtbfabric-respondergateway-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-rtbfabric-respondergateway-tags)" : {{[ Tag, ... ]}},
      "[TrustStoreConfiguration](#cfn-rtbfabric-respondergateway-truststoreconfiguration)" : {{TrustStoreConfiguration}},
      "[VpcId](#cfn-rtbfabric-respondergateway-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-respondergateway-syntax.yaml"></a>

```
Type: AWS::RTBFabric::ResponderGateway
Properties:
  [AcmCertificateArn](#cfn-rtbfabric-respondergateway-acmcertificatearn): {{String}}
  [Description](#cfn-rtbfabric-respondergateway-description): {{String}}
  [DomainName](#cfn-rtbfabric-respondergateway-domainname): {{String}}
  [GatewayType](#cfn-rtbfabric-respondergateway-gatewaytype): {{String}}
  [ListenerConfig](#cfn-rtbfabric-respondergateway-listenerconfig): {{
    ListenerConfig}}
  [ManagedEndpointConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration): {{
    ManagedEndpointConfiguration}}
  [Port](#cfn-rtbfabric-respondergateway-port): {{Integer}}
  [Protocol](#cfn-rtbfabric-respondergateway-protocol): {{String}}
  [SecurityGroupIds](#cfn-rtbfabric-respondergateway-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-rtbfabric-respondergateway-subnetids): {{
    - String}}
  [Tags](#cfn-rtbfabric-respondergateway-tags): {{
    - Tag}}
  [TrustStoreConfiguration](#cfn-rtbfabric-respondergateway-truststoreconfiguration): {{
    TrustStoreConfiguration}}
  [VpcId](#cfn-rtbfabric-respondergateway-vpcid): {{String}}
```

## Properties
<a name="aws-resource-rtbfabric-respondergateway-properties"></a>

`AcmCertificateArn`  <a name="cfn-rtbfabric-respondergateway-acmcertificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-cn|aws-us-gov):acm:([a-z0-9-]+):[0-9]{12}:certificate/.{1,2048}`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Description`  <a name="cfn-rtbfabric-respondergateway-description"></a>
An optional description for the responder gateway.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9 ]+$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DomainName`  <a name="cfn-rtbfabric-respondergateway-domainname"></a>
The domain name for the responder gateway.
*Required*: No
*Type*: String
*Pattern*: `^(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(?:\.(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?))+$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`GatewayType`  <a name="cfn-rtbfabric-respondergateway-gatewaytype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `EXTERNAL | INTERNAL`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ListenerConfig`  <a name="cfn-rtbfabric-respondergateway-listenerconfig"></a>
Property description not available.
*Required*: No
*Type*: [ListenerConfig](aws-properties-rtbfabric-respondergateway-listenerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedEndpointConfiguration`  <a name="cfn-rtbfabric-respondergateway-managedendpointconfiguration"></a>
The configuration for the managed endpoint.
*Required*: No
*Type*: [ManagedEndpointConfiguration](aws-properties-rtbfabric-respondergateway-managedendpointconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Port`  <a name="cfn-rtbfabric-respondergateway-port"></a>
The networking port to use.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Protocol`  <a name="cfn-rtbfabric-respondergateway-protocol"></a>
The networking protocol to use.
*Required*: Yes
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroupIds`  <a name="cfn-rtbfabric-respondergateway-securitygroupids"></a>
The unique identifiers of the security groups.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SubnetIds`  <a name="cfn-rtbfabric-respondergateway-subnetids"></a>
Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rtbfabric-respondergateway-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-respondergateway-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustStoreConfiguration`  <a name="cfn-rtbfabric-respondergateway-truststoreconfiguration"></a>
The configuration of the trust store.
*Required*: No
*Type*: [TrustStoreConfiguration](aws-properties-rtbfabric-respondergateway-truststoreconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VpcId`  <a name="cfn-rtbfabric-respondergateway-vpcid"></a>
The unique identifier of the Virtual Private Cloud (VPC).
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `50`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-rtbfabric-respondergateway-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-respondergateway-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-respondergateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rtbfabric-respondergateway-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CertificateAssociationStatus`  <a name="CertificateAssociationStatus-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`ExternalInboundEndpoint`  <a name="ExternalInboundEndpoint-fn::getatt"></a>
Property description not available.

`GatewayId`  <a name="GatewayId-fn::getatt"></a>
Property description not available.

`ResponderGatewayStatus`  <a name="ResponderGatewayStatus-fn::getatt"></a>
Property description not available.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
