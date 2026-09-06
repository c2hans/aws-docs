---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-interconnect-connection-provider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Interconnect::Connection Provider
<a name="aws-properties-interconnect-connection-provider"></a>

The partner cloud service provider on the remote side of the connection.

## Syntax
<a name="aws-properties-interconnect-connection-provider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-interconnect-connection-provider-syntax.json"></a>

```
{
  "[CloudServiceProvider](#cfn-interconnect-connection-provider-cloudserviceprovider)" : {{String}},
  "[LastMileProvider](#cfn-interconnect-connection-provider-lastmileprovider)" : {{String}}
}
```

### YAML
<a name="aws-properties-interconnect-connection-provider-syntax.yaml"></a>

```
  [CloudServiceProvider](#cfn-interconnect-connection-provider-cloudserviceprovider): {{String}}
  [LastMileProvider](#cfn-interconnect-connection-provider-lastmileprovider): {{String}}
```

## Properties
<a name="aws-properties-interconnect-connection-provider-properties"></a>

`CloudServiceProvider`  <a name="cfn-interconnect-connection-provider-cloudserviceprovider"></a>
The name of the cloud service provider. Connections to or from this cloud service provider are considered multicloud connections.
*Required*: No
*Type*: String
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastMileProvider`  <a name="cfn-interconnect-connection-provider-lastmileprovider"></a>
The name of the last-mile provider. Connections to or from this last-mile provider are considered last-mile connections.
*Required*: No
*Type*: String
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
