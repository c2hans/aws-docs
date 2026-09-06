---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-certificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster CertificateAuthority
<a name="aws-properties-eks-cluster-certificateauthority"></a>

An object representing a certificate authority (CA) for an Amazon EKS cluster.

## Syntax
<a name="aws-properties-eks-cluster-certificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-certificateauthority-syntax.json"></a>

```
{
  "[Active](#cfn-eks-cluster-certificateauthority-active)" : {{ActiveCertificateAuthority}},
  "[Data](#cfn-eks-cluster-certificateauthority-data)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-certificateauthority-syntax.yaml"></a>

```
  [Active](#cfn-eks-cluster-certificateauthority-active): {{
    ActiveCertificateAuthority}}
  [Data](#cfn-eks-cluster-certificateauthority-data): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-certificateauthority-properties"></a>

`Active`  <a name="cfn-eks-cluster-certificateauthority-active"></a>
Property description not available.
*Required*: No
*Type*: [ActiveCertificateAuthority](aws-properties-eks-cluster-activecertificateauthority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Data`  <a name="cfn-eks-cluster-certificateauthority-data"></a>
The Base64-encoded public certificate of the certificate authority.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
