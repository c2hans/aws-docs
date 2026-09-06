---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-vpcconnectivity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster VpcConnectivity
<a name="aws-properties-msk-cluster-vpcconnectivity"></a>

VPC connection control settings for brokers.

## Syntax
<a name="aws-properties-msk-cluster-vpcconnectivity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-vpcconnectivity-syntax.json"></a>

```
{
  "[ClientAuthentication](#cfn-msk-cluster-vpcconnectivity-clientauthentication)" : {{VpcConnectivityClientAuthentication}}
}
```

### YAML
<a name="aws-properties-msk-cluster-vpcconnectivity-syntax.yaml"></a>

```
  [ClientAuthentication](#cfn-msk-cluster-vpcconnectivity-clientauthentication): {{
    VpcConnectivityClientAuthentication}}
```

## Properties
<a name="aws-properties-msk-cluster-vpcconnectivity-properties"></a>

`ClientAuthentication`  <a name="cfn-msk-cluster-vpcconnectivity-clientauthentication"></a>
VPC connection control settings for brokers.
*Required*: No
*Type*: [VpcConnectivityClientAuthentication](aws-properties-msk-cluster-vpcconnectivityclientauthentication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
