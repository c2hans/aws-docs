---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekspersistentvolumeclaim.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksPersistentVolumeClaim
<a name="aws-properties-batch-jobdefinition-ekspersistentvolumeclaim"></a>

A `persistentVolumeClaim` volume is used to mount a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) into a Pod. PersistentVolumeClaims are a way for users to "claim" durable storage without knowing the details of the particular cloud environment. See the information about [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekspersistentvolumeclaim-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekspersistentvolumeclaim-syntax.json"></a>

```
{
  "[ClaimName](#cfn-batch-jobdefinition-ekspersistentvolumeclaim-claimname)" : {{String}},
  "[ReadOnly](#cfn-batch-jobdefinition-ekspersistentvolumeclaim-readonly)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekspersistentvolumeclaim-syntax.yaml"></a>

```
  [ClaimName](#cfn-batch-jobdefinition-ekspersistentvolumeclaim-claimname): {{String}}
  [ReadOnly](#cfn-batch-jobdefinition-ekspersistentvolumeclaim-readonly): {{Boolean}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekspersistentvolumeclaim-properties"></a>

`ClaimName`  <a name="cfn-batch-jobdefinition-ekspersistentvolumeclaim-claimname"></a>
The name of the `persistentVolumeClaim` bounded to a `persistentVolume`. For more information, see [ Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnly`  <a name="cfn-batch-jobdefinition-ekspersistentvolumeclaim-readonly"></a>
An optional boolean value indicating if the mount is read only. Default is false. For more information, see [ Read Only Mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) in the *Kubernetes documentation*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
