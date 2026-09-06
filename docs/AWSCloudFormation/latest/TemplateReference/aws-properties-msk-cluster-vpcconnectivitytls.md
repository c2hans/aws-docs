---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-vpcconnectivitytls.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster VpcConnectivityTls
<a name="aws-properties-msk-cluster-vpcconnectivitytls"></a>

Details for client authentication using TLS for VpcConnectivity.

## Syntax
<a name="aws-properties-msk-cluster-vpcconnectivitytls-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-vpcconnectivitytls-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-cluster-vpcconnectivitytls-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-vpcconnectivitytls-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-cluster-vpcconnectivitytls-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-vpcconnectivitytls-properties"></a>

`Enabled`  <a name="cfn-msk-cluster-vpcconnectivitytls-enabled"></a>
TLS authentication is enabled or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
