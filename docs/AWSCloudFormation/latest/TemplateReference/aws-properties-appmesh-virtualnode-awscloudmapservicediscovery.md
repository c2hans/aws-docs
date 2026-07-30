---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode AwsCloudMapServiceDiscovery
<a name="aws-properties-appmesh-virtualnode-awscloudmapservicediscovery"></a>

An object that represents the AWS Cloud Map service discovery information for your virtual node.

**Note**
AWS Cloud Map is not available in the eu-south-1 Region.

## Syntax
<a name="aws-properties-appmesh-virtualnode-awscloudmapservicediscovery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-awscloudmapservicediscovery-syntax.json"></a>

```
{
  "[Attributes](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes)" : {{[ AwsCloudMapInstanceAttribute, ... ]}},
  "[IpPreference](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-ippreference)" : {{String}},
  "[NamespaceName](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename)" : {{String}},
  "[ServiceName](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-awscloudmapservicediscovery-syntax.yaml"></a>

```
  [Attributes](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes): {{
    - AwsCloudMapInstanceAttribute}}
  [IpPreference](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-ippreference): {{String}}
  [NamespaceName](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename): {{String}}
  [ServiceName](#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-awscloudmapservicediscovery-properties"></a>

`Attributes`  <a name="cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes"></a>
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
*Required*: No
*Type*: Array of [AwsCloudMapInstanceAttribute](aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpPreference`  <a name="cfn-appmesh-virtualnode-awscloudmapservicediscovery-ippreference"></a>
The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.
*Required*: No
*Type*: String
*Allowed values*: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename"></a>
The HTTP name of the AWS Cloud Map namespace to use.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename"></a>
The name of the AWS Cloud Map service to use.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
