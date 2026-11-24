---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-storagevirtualmachinepeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::StorageVirtualMachinePeer

Describes an Amazon FSx for NetApp ONTAP storage virtual machine (SVM) peer relationship.

## Syntax
<a name="aws-resource-fsx-storagevirtualmachinepeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-storagevirtualmachinepeer-syntax.json"></a>

```json
{
  "Type" : "AWS::FSx::StorageVirtualMachinePeer",
  "Properties" : {
      "[Applications](#cfn-fsx-storagevirtualmachinepeer-applications)" : {{[ String, ... ]}},
      "[PeerClusterName](#cfn-fsx-storagevirtualmachinepeer-peerclustername)" : {{String}},
      "[PeerSvmAlias](#cfn-fsx-storagevirtualmachinepeer-peersvmalias)" : {{String}},
      "[PeerSvmName](#cfn-fsx-storagevirtualmachinepeer-peersvmname)" : {{String}},
      "[StorageVirtualMachineId](#cfn-fsx-storagevirtualmachinepeer-storagevirtualmachineid)" : {{String}},
      "[Tags](#cfn-fsx-storagevirtualmachinepeer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fsx-storagevirtualmachinepeer-syntax.yaml"></a>

```yaml
Type: AWS::FSx::StorageVirtualMachinePeer
Properties:
  [Applications](#cfn-fsx-storagevirtualmachinepeer-applications): {{
    - String}}
  [PeerClusterName](#cfn-fsx-storagevirtualmachinepeer-peerclustername): {{String}}
  [PeerSvmAlias](#cfn-fsx-storagevirtualmachinepeer-peersvmalias): {{String}}
  [PeerSvmName](#cfn-fsx-storagevirtualmachinepeer-peersvmname): {{String}}
  [StorageVirtualMachineId](#cfn-fsx-storagevirtualmachinepeer-storagevirtualmachineid): {{String}}
  [Tags](#cfn-fsx-storagevirtualmachinepeer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fsx-storagevirtualmachinepeer-properties"></a>

`Applications`  <a name="cfn-fsx-storagevirtualmachinepeer-applications"></a>
The applications that the SVM peer relationship authorizes. The applications can be one or more of the following:
+ `SNAPMIRROR` – SnapMirror replication.
+ `FILE_COPY` – File copy.
+ `LUN_COPY` – LUN copy.
+ `FLEXCACHE` – FlexCache.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `SNAPMIRROR | FILE_COPY | LUN_COPY | FLEXCACHE`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerClusterName`  <a name="cfn-fsx-storagevirtualmachinepeer-peerclustername"></a>
The name of the peer cluster that the peer SVM is on.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
*Minimum*: `1`
*Maximum*: `44`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerSvmAlias`  <a name="cfn-fsx-storagevirtualmachinepeer-peersvmalias"></a>
The name that the local cluster uses to identify the peer SVM.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,41}$`
*Minimum*: `1`
*Maximum*: `41`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerSvmName`  <a name="cfn-fsx-storagevirtualmachinepeer-peersvmname"></a>
The name of the SVM on the peer cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageVirtualMachineId`  <a name="cfn-fsx-storagevirtualmachinepeer-storagevirtualmachineid"></a>
The ID of the SVM on the file system that the SVM peer relationship belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^(svm-[0-9a-f]{17,})$`
*Minimum*: `21`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-storagevirtualmachinepeer-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-storagevirtualmachinepeer-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-storagevirtualmachinepeer-return-values"></a>

### Ref
<a name="aws-resource-fsx-storagevirtualmachinepeer-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-storagevirtualmachinepeer-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-storagevirtualmachinepeer-return-values-fn--getatt-fn--getatt"></a>

`FileSystemId`  <a name="FileSystemId-fn::getatt"></a>
The globally unique ID of the file system, assigned by Amazon FSx.

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the SVM peer can be one of the following:
+ `CREATED` – The SVM peer is fully available for use.
+ `CREATING` – Amazon FSx is creating the SVM peer.
+ `DELETING` – Amazon FSx is deleting the SVM peer.
+ `FAILED` – Amazon FSx was unable to create the SVM peer.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`State`  <a name="State-fn::getatt"></a>
The state of the SVM peer relationship in ONTAP can be one of the following:
+ `PEERED` – The SVM peer relationship is established.
+ `INITIATED` – The local cluster sent a peering request to the peer SVM.
+ `PENDING` – A peering request from the peer SVM is waiting for acceptance.
+ `INITIALIZING` – ONTAP is setting up the SVM peer relationship.
+ `SUSPENDED` – The SVM peer relationship is suspended.
+ `REJECTED` – The peering request was rejected.

`StorageVirtualMachinePeerId`  <a name="StorageVirtualMachinePeerId-fn::getatt"></a>
The system-generated, unique ID of the SVM peer.

`UUID`  <a name="UUID-fn::getatt"></a>
The SVM peer's universally unique identifier (UUID).
