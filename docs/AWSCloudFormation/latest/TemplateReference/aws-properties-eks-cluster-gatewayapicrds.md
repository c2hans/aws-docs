---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-gatewayapicrds.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster GatewayApiCrds
<a name="aws-properties-eks-cluster-gatewayapicrds"></a>

Indicates the current configuration of Gateway API custom resource definition (CRD) management on your EKS Auto Mode cluster. For example, if CRD management is enabled or disabled. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-gatewayapicrds-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-gatewayapicrds-syntax.json"></a>

```
{
  "[Managed](#cfn-eks-cluster-gatewayapicrds-managed)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-gatewayapicrds-syntax.yaml"></a>

```
  [Managed](#cfn-eks-cluster-gatewayapicrds-managed): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-gatewayapicrds-properties"></a>

`Managed`  <a name="cfn-eks-cluster-gatewayapicrds-managed"></a>
Indicates if Gateway API CRD management is enabled on your EKS Auto Mode cluster. If CRD management is enabled, EKS Auto Mode will create and update the Gateway API CRDs in your EKS Auto Mode cluster.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
