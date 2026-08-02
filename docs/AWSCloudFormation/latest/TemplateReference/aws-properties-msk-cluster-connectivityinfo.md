---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-connectivityinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster ConnectivityInfo
<a name="aws-properties-msk-cluster-connectivityinfo"></a>

Broker access controls.

## Syntax
<a name="aws-properties-msk-cluster-connectivityinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-connectivityinfo-syntax.json"></a>

```
{
  "[NetworkType](#cfn-msk-cluster-connectivityinfo-networktype)" : {{String}},
  "[PublicAccess](#cfn-msk-cluster-connectivityinfo-publicaccess)" : {{PublicAccess}},
  "[VpcConnectivity](#cfn-msk-cluster-connectivityinfo-vpcconnectivity)" : {{VpcConnectivity}}
}
```

### YAML
<a name="aws-properties-msk-cluster-connectivityinfo-syntax.yaml"></a>

```
  [NetworkType](#cfn-msk-cluster-connectivityinfo-networktype): {{String}}
  [PublicAccess](#cfn-msk-cluster-connectivityinfo-publicaccess): {{
    PublicAccess}}
  [VpcConnectivity](#cfn-msk-cluster-connectivityinfo-vpcconnectivity): {{
    VpcConnectivity}}
```

## Properties
<a name="aws-properties-msk-cluster-connectivityinfo-properties"></a>

`NetworkType`  <a name="cfn-msk-cluster-connectivityinfo-networktype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicAccess`  <a name="cfn-msk-cluster-connectivityinfo-publicaccess"></a>
Access control settings for the cluster's brokers.
*Required*: No
*Type*: [PublicAccess](aws-properties-msk-cluster-publicaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConnectivity`  <a name="cfn-msk-cluster-connectivityinfo-vpcconnectivity"></a>
VPC connection control settings for brokers.
*Required*: No
*Type*: [VpcConnectivity](aws-properties-msk-cluster-vpcconnectivity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
