---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eks-certificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::CertificateAuthority
<a name="aws-resource-eks-certificateauthority"></a>

<a name="aws-resource-eks-certificateauthority-description"></a>The `AWS::EKS::CertificateAuthority` resource Property description not available. for EKS.

## Syntax
<a name="aws-resource-eks-certificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eks-certificateauthority-syntax.json"></a>

```
{
  "Type" : "AWS::EKS::CertificateAuthority",
  "Properties" : {
      "[ClusterName](#cfn-eks-certificateauthority-clustername)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-eks-certificateauthority-syntax.yaml"></a>

```
Type: AWS::EKS::CertificateAuthority
Properties:
  [ClusterName](#cfn-eks-certificateauthority-clustername): {{String}}
```

## Properties
<a name="aws-resource-eks-certificateauthority-properties"></a>

`ClusterName`  <a name="cfn-eks-certificateauthority-clustername"></a>
The name of your cluster.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-eks-certificateauthority-return-values"></a>

### Ref
<a name="aws-resource-eks-certificateauthority-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-eks-certificateauthority-return-values-fn--getatt"></a>

####
<a name="aws-resource-eks-certificateauthority-return-values-fn--getatt-fn--getatt"></a>

`ActivatedAt`  <a name="ActivatedAt-fn::getatt"></a>
Property description not available.

`ActivatedBy`  <a name="ActivatedBy-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`Data`  <a name="Data-fn::getatt"></a>
Property description not available.

`DistributionStatus`  <a name="DistributionStatus-fn::getatt"></a>
Property description not available.

`RollbackAvailable`  <a name="RollbackAvailable-fn::getatt"></a>
Property description not available.

`ScheduledEvents.FinalAutoActivation`  <a name="ScheduledEvents.FinalAutoActivation-fn::getatt"></a>
Property description not available.

`ScheduledEvents.FirstAutoActivation`  <a name="ScheduledEvents.FirstAutoActivation-fn::getatt"></a>
Property description not available.

`SigningStatus`  <a name="SigningStatus-fn::getatt"></a>
Property description not available.

`Validity.NotAfter`  <a name="Validity.NotAfter-fn::getatt"></a>
Property description not available.

`Validity.NotBefore`  <a name="Validity.NotBefore-fn::getatt"></a>
Property description not available.
