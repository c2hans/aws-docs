---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-activecertificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ActiveCertificateAuthority
<a name="aws-properties-eks-cluster-activecertificateauthority"></a>

Identifies the certificate authority that is currently signing certificates for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-activecertificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-activecertificateauthority-syntax.json"></a>

```
{
  "[ActivatedBy](#cfn-eks-cluster-activecertificateauthority-activatedby)" : {{String}},
  "[Id](#cfn-eks-cluster-activecertificateauthority-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-activecertificateauthority-syntax.yaml"></a>

```
  [ActivatedBy](#cfn-eks-cluster-activecertificateauthority-activatedby): {{String}}
  [Id](#cfn-eks-cluster-activecertificateauthority-id): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-activecertificateauthority-properties"></a>

`ActivatedBy`  <a name="cfn-eks-cluster-activecertificateauthority-activatedby"></a>
The entity that activated the current signing certificate authority, either `CUSTOMER` or `EKS`.
*Required*: No
*Type*: String
*Allowed values*: `EKS | CUSTOMER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-eks-cluster-activecertificateauthority-id"></a>
The unique identifier of the certificate authority that is currently signing certificates for the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
