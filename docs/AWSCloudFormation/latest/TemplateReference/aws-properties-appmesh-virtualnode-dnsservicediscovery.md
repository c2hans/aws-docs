---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-dnsservicediscovery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode DnsServiceDiscovery
<a name="aws-properties-appmesh-virtualnode-dnsservicediscovery"></a>

An object that represents the DNS service discovery information for your virtual node.

## Syntax
<a name="aws-properties-appmesh-virtualnode-dnsservicediscovery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-dnsservicediscovery-syntax.json"></a>

```
{
  "[Hostname](#cfn-appmesh-virtualnode-dnsservicediscovery-hostname)" : {{String}},
  "[IpPreference](#cfn-appmesh-virtualnode-dnsservicediscovery-ippreference)" : {{String}},
  "[ResponseType](#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-dnsservicediscovery-syntax.yaml"></a>

```
  [Hostname](#cfn-appmesh-virtualnode-dnsservicediscovery-hostname): {{String}}
  [IpPreference](#cfn-appmesh-virtualnode-dnsservicediscovery-ippreference): {{String}}
  [ResponseType](#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-dnsservicediscovery-properties"></a>

`Hostname`  <a name="cfn-appmesh-virtualnode-dnsservicediscovery-hostname"></a>
Specifies the DNS service discovery hostname for the virtual node.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpPreference`  <a name="cfn-appmesh-virtualnode-dnsservicediscovery-ippreference"></a>
The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.
*Required*: No
*Type*: String
*Allowed values*: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseType`  <a name="cfn-appmesh-virtualnode-dnsservicediscovery-responsetype"></a>
Specifies the DNS response type for the virtual node.
*Required*: No
*Type*: String
*Allowed values*: `LOADBALANCER | ENDPOINTS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
