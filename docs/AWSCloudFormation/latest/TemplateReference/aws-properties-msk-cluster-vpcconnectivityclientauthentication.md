---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster VpcConnectivityClientAuthentication
<a name="aws-properties-msk-cluster-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

## Syntax
<a name="aws-properties-msk-cluster-vpcconnectivityclientauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-vpcconnectivityclientauthentication-syntax.json"></a>

```
{
  "[Sasl](#cfn-msk-cluster-vpcconnectivityclientauthentication-sasl)" : {{VpcConnectivitySasl}},
  "[Tls](#cfn-msk-cluster-vpcconnectivityclientauthentication-tls)" : {{VpcConnectivityTls}}
}
```

### YAML
<a name="aws-properties-msk-cluster-vpcconnectivityclientauthentication-syntax.yaml"></a>

```
  [Sasl](#cfn-msk-cluster-vpcconnectivityclientauthentication-sasl): {{
    VpcConnectivitySasl}}
  [Tls](#cfn-msk-cluster-vpcconnectivityclientauthentication-tls): {{
    VpcConnectivityTls}}
```

## Properties
<a name="aws-properties-msk-cluster-vpcconnectivityclientauthentication-properties"></a>

`Sasl`  <a name="cfn-msk-cluster-vpcconnectivityclientauthentication-sasl"></a>
Details for VpcConnectivity ClientAuthentication using SASL.
*Required*: No
*Type*: [VpcConnectivitySasl](aws-properties-msk-cluster-vpcconnectivitysasl.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tls`  <a name="cfn-msk-cluster-vpcconnectivityclientauthentication-tls"></a>
Details for VpcConnectivity ClientAuthentication using TLS.
*Required*: No
*Type*: [VpcConnectivityTls](aws-properties-msk-cluster-vpcconnectivitytls.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
