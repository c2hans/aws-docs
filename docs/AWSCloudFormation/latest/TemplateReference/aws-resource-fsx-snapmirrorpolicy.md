---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-snapmirrorpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapmirrorPolicy

Describes an Amazon FSx for NetApp ONTAP SnapMirror policy.

## Syntax
<a name="aws-resource-fsx-snapmirrorpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-snapmirrorpolicy-syntax.json"></a>

```json
{
  "Type" : "AWS::FSx::SnapmirrorPolicy",
  "Properties" : {
      "[FileSystemId](#cfn-fsx-snapmirrorpolicy-filesystemid)" : {{String}},
      "[Name](#cfn-fsx-snapmirrorpolicy-name)" : {{String}},
      "[NetworkCompressionEnabled](#cfn-fsx-snapmirrorpolicy-networkcompressionenabled)" : {{Boolean}},
      "[RetentionRules](#cfn-fsx-snapmirrorpolicy-retentionrules)" : {{[ RetentionRule, ... ]}},
      "[SnapshotCopyMode](#cfn-fsx-snapmirrorpolicy-snapshotcopymode)" : {{String}},
      "[StorageVirtualMachineId](#cfn-fsx-snapmirrorpolicy-storagevirtualmachineid)" : {{String}},
      "[Tags](#cfn-fsx-snapmirrorpolicy-tags)" : {{[ Tag, ... ]}},
      "[ThrottleInKbps](#cfn-fsx-snapmirrorpolicy-throttleinkbps)" : {{Integer}},
      "[TransferSchedule](#cfn-fsx-snapmirrorpolicy-transferschedule)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fsx-snapmirrorpolicy-syntax.yaml"></a>

```yaml
Type: AWS::FSx::SnapmirrorPolicy
Properties:
  [FileSystemId](#cfn-fsx-snapmirrorpolicy-filesystemid): {{String}}
  [Name](#cfn-fsx-snapmirrorpolicy-name): {{String}}
  [NetworkCompressionEnabled](#cfn-fsx-snapmirrorpolicy-networkcompressionenabled): {{Boolean}}
  [RetentionRules](#cfn-fsx-snapmirrorpolicy-retentionrules): {{
    - RetentionRule}}
  [SnapshotCopyMode](#cfn-fsx-snapmirrorpolicy-snapshotcopymode): {{String}}
  [StorageVirtualMachineId](#cfn-fsx-snapmirrorpolicy-storagevirtualmachineid): {{String}}
  [Tags](#cfn-fsx-snapmirrorpolicy-tags): {{
    - Tag}}
  [ThrottleInKbps](#cfn-fsx-snapmirrorpolicy-throttleinkbps): {{Integer}}
  [TransferSchedule](#cfn-fsx-snapmirrorpolicy-transferschedule): {{String}}
```

## Properties
<a name="aws-resource-fsx-snapmirrorpolicy-properties"></a>

`FileSystemId`  <a name="cfn-fsx-snapmirrorpolicy-filesystemid"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
*Required*: No
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-fsx-snapmirrorpolicy-name"></a>
The name of the SnapMirror policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkCompressionEnabled`  <a name="cfn-fsx-snapmirrorpolicy-networkcompressionenabled"></a>
Specifies whether SnapMirror compresses data when it transfers the data over the network. This value defaults to `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionRules`  <a name="cfn-fsx-snapmirrorpolicy-retentionrules"></a>
The rules that determine which snapshots SnapMirror retains on the destination volume.
*Required*: No
*Type*: Array of [RetentionRule](aws-properties-fsx-snapmirrorpolicy-retentionrule.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotCopyMode`  <a name="cfn-fsx-snapmirrorpolicy-snapshotcopymode"></a>
The snapshot copy mode of the SnapMirror policy, which determines which snapshots SnapMirror transfers to the destination volume.
*Required*: No
*Type*: String
*Allowed values*: `COPY_ALL_SOURCE_SNAPSHOTS | COPY_LATEST_SOURCE_SNAPSHOT | NO_CREATE_SNAPSHOT_ON_SOURCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageVirtualMachineId`  <a name="cfn-fsx-snapmirrorpolicy-storagevirtualmachineid"></a>
The ID of the SnapMirror policy's storage virtual machine, if you created the SnapMirror policy on a storage virtual machine.
*Required*: No
*Type*: String
*Pattern*: `^(svm-[0-9a-f]{17,})$`
*Minimum*: `21`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-snapmirrorpolicy-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-snapmirrorpolicy-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottleInKbps`  <a name="cfn-fsx-snapmirrorpolicy-throttleinkbps"></a>
The maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data. A value of `0` means that the bandwidth is unlimited.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransferSchedule`  <a name="cfn-fsx-snapmirrorpolicy-transferschedule"></a>
The name of the ONTAP schedule that determines when SnapMirror transfers data.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_:.-]{0,256}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-snapmirrorpolicy-return-values"></a>

### Ref
<a name="aws-resource-fsx-snapmirrorpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-snapmirrorpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-snapmirrorpolicy-return-values-fn--getatt-fn--getatt"></a>

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the SnapMirror policy can be one of the following:
+ `CREATED` – The SnapMirror policy is fully available for use.
+ `CREATING` – Amazon FSx is creating the SnapMirror policy.
+ `DELETING` – Amazon FSx is deleting the SnapMirror policy.
+ `FAILED` – Amazon FSx was unable to create the SnapMirror policy.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`Scope`  <a name="Scope-fn::getatt"></a>
The scope of the SnapMirror policy can be one of the following:
+ `FILESYSTEM` – The SnapMirror policy was created on the file system.
+ `SVM` – The SnapMirror policy was created on an SVM.

`SnapmirrorPolicyId`  <a name="SnapmirrorPolicyId-fn::getatt"></a>
The system-generated, unique ID of the SnapMirror policy.

`UUID`  <a name="UUID-fn::getatt"></a>
The SnapMirror policy's universally unique identifier (UUID).
