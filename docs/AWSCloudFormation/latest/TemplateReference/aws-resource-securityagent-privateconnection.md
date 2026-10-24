---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-privateconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::PrivateConnection
<a name="aws-resource-securityagent-privateconnection"></a>

Creates a private connection for reaching a self-hosted provider instance over private networking using Amazon VPC Lattice.

## Syntax
<a name="aws-resource-securityagent-privateconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-privateconnection-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::PrivateConnection",
  "Properties" : {
      "[Certificate](#cfn-securityagent-privateconnection-certificate)" : {{String}},
      "[Mode](#cfn-securityagent-privateconnection-mode)" : {{Mode}},
      "[PrivateConnectionName](#cfn-securityagent-privateconnection-privateconnectionname)" : {{String}},
      "[Tags](#cfn-securityagent-privateconnection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-privateconnection-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::PrivateConnection
Properties:
  [Certificate](#cfn-securityagent-privateconnection-certificate): {{String}}
  [Mode](#cfn-securityagent-privateconnection-mode): {{
    Mode}}
  [PrivateConnectionName](#cfn-securityagent-privateconnection-privateconnectionname): {{String}}
  [Tags](#cfn-securityagent-privateconnection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-securityagent-privateconnection-properties"></a>

`Certificate`  <a name="cfn-securityagent-privateconnection-certificate"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-securityagent-privateconnection-mode"></a>
Property description not available.
*Required*: No
*Type*: [Mode](aws-properties-securityagent-privateconnection-mode.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateConnectionName`  <a name="cfn-securityagent-privateconnection-privateconnectionname"></a>
The unique name of a private connection within your account.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-securityagent-privateconnection-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-privateconnection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-privateconnection-return-values"></a>

### Ref
<a name="aws-resource-securityagent-privateconnection-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityagent-privateconnection-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityagent-privateconnection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CertificateExpiryTime`  <a name="CertificateExpiryTime-fn::getatt"></a>
Property description not available.

`DnsResolution`  <a name="DnsResolution-fn::getatt"></a>
Property description not available.

`HostAddress`  <a name="HostAddress-fn::getatt"></a>
The IP address or DNS name of a target resource.

`ResourceConfigurationId`  <a name="ResourceConfigurationId-fn::getatt"></a>
The identifier or ARN of a VPC Lattice resource configuration.

`ResourceGatewayId`  <a name="ResourceGatewayId-fn::getatt"></a>
The identifier or ARN of a VPC Lattice resource gateway.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`Type`  <a name="Type-fn::getatt"></a>
Property description not available.

`VpcId`  <a name="VpcId-fn::getatt"></a>
Property description not available.
