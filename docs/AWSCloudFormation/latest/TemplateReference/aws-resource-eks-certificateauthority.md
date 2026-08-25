---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eks-certificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::CertificateAuthority
<a name="aws-resource-eks-certificateauthority"></a>

Appends a successor certificate authority (CA) to your cluster, beginning the CA rotation process.

A cluster certificate authority is the root of trust for your cluster's control plane. It signs the certificates that secure communication between the Kubernetes API server and its clients, and its public certificate is distributed to your cluster's trust bundle so that worker nodes and clients can verify the API server's identity. Each cluster can have at most two certificate authorities at a time: the outgoing CA that's currently signing (its `signingStatus` is `IN_USE`) and one successor CA (`signingStatus` of `NOT_USED`) that you can later activate to complete the rotation.

Appending a successor CA adds its public certificate to the cluster's trust bundle so that the cluster trusts both CAs simultaneously (the dual trust period), but it doesn't begin signing certificates. Amazon EKS then distributes the successor CA to the AWS managed components in your cluster; you can track this through the CA's `distributionStatus`. The successor CA can't be activated until its `distributionStatus` is `COMPLETE`. To activate it as the cluster's signer, use [`ActivateCertificateAuthority`](https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html). This is an asynchronous operation that returns an `update` object. If you don't append a successor CA yourself, Amazon EKS appends one automatically before the outgoing CA approaches expiration.

For more information, see [Rotate the Amazon EKS cluster certificate authority](https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html) in the *Amazon EKS User Guide*.

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

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eks-certificateauthority-return-values-fn--getatt-fn--getatt"></a>

`ActivatedAt`  <a name="ActivatedAt-fn::getatt"></a>
The timestamp when the certificate authority was last activated as the cluster's signer. This value is absent if the certificate authority has never been activated.

`ActivatedBy`  <a name="ActivatedBy-fn::getatt"></a>
The entity that most recently activated the certificate authority, either `CUSTOMER` or `EKS`.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the certificate authority was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The entity that created the certificate authority. Certificate authorities that you create are `CUSTOMER`; those that Amazon EKS provisions on your behalf are `EKS`.

`Data`  <a name="Data-fn::getatt"></a>
The Base64-encoded public certificate of the certificate authority.

`DistributionStatus`  <a name="DistributionStatus-fn::getatt"></a>
The distribution status of the certificate authority, which tracks whether Amazon EKS has distributed its trust to the AWS managed components in the cluster. Valid values are `IN_PROGRESS`, `COMPLETE`, `FAILED`, and `DELETING`. A successor CA can only be activated after its distribution status is `COMPLETE`.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the certificate authority.

`RollbackAvailable`  <a name="RollbackAvailable-fn::getatt"></a>
Indicates whether CA rollback is still available for this certificate authority. After you activate a successor CA, rollback lets you revert to the outgoing CA for a limited period.

`ScheduledEvents.FinalAutoActivation`  <a name="ScheduledEvents.FinalAutoActivation-fn::getatt"></a>
The date by which Amazon EKS automatically activates this certificate authority if you haven't already activated it.

`ScheduledEvents.FirstAutoActivation`  <a name="ScheduledEvents.FirstAutoActivation-fn::getatt"></a>
The earliest date Amazon EKS may automatically activate this certificate authority.

`SigningStatus`  <a name="SigningStatus-fn::getatt"></a>
The signing status of the certificate authority. `IN_USE` means it's currently signing certificates for the cluster, `ACTIVATING` means it's being promoted to the signer, and `NOT_USED` means it's trusted by the cluster but isn't the signer.

`Validity.NotAfter`  <a name="Validity.NotAfter-fn::getatt"></a>
The end of the validity period for the certificate authority.

`Validity.NotBefore`  <a name="Validity.NotBefore-fn::getatt"></a>
The start of the validity period for the certificate authority.
