---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-gatewayapi.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster GatewayApi
<a name="aws-properties-eks-cluster-gatewayapi"></a>

Indicates the current configuration of the Kubernetes Gateway API for the load balancing capability on your EKS Auto Mode cluster. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-gatewayapi-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-gatewayapi-syntax.json"></a>

```
{
  "[Crds](#cfn-eks-cluster-gatewayapi-crds)" : {{GatewayApiCrds}}
}
```

### YAML
<a name="aws-properties-eks-cluster-gatewayapi-syntax.yaml"></a>

```
  [Crds](#cfn-eks-cluster-gatewayapi-crds): {{
    GatewayApiCrds}}
```

## Properties
<a name="aws-properties-eks-cluster-gatewayapi-properties"></a>

`Crds`  <a name="cfn-eks-cluster-gatewayapi-crds"></a>
Indicates the current configuration of Gateway API custom resource definition (CRD) management on your EKS Auto Mode cluster. For example, if CRD management is enabled or disabled.
*Required*: Yes
*Type*: [GatewayApiCrds](aws-properties-eks-cluster-gatewayapicrds.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
