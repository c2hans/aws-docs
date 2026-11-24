---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-snapshotpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapshotPolicy

Describes an Amazon FSx for NetApp ONTAP snapshot policy.

## Syntax
<a name="aws-resource-fsx-snapshotpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-snapshotpolicy-syntax.json"></a>

```json
{
  "Type" : "AWS::FSx::SnapshotPolicy",
  "Properties" : {
      "[Enabled](#cfn-fsx-snapshotpolicy-enabled)" : {{Boolean}},
      "[FileSystemId](#cfn-fsx-snapshotpolicy-filesystemid)" : {{String}},
      "[Name](#cfn-fsx-snapshotpolicy-name)" : {{String}},
      "[Schedules](#cfn-fsx-snapshotpolicy-schedules)" : {{[ SnapshotPolicySchedule, ... ]}},
      "[StorageVirtualMachineId](#cfn-fsx-snapshotpolicy-storagevirtualmachineid)" : {{String}},
      "[Tags](#cfn-fsx-snapshotpolicy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fsx-snapshotpolicy-syntax.yaml"></a>

```yaml
Type: AWS::FSx::SnapshotPolicy
Properties:
  [Enabled](#cfn-fsx-snapshotpolicy-enabled): {{Boolean}}
  [FileSystemId](#cfn-fsx-snapshotpolicy-filesystemid): {{String}}
  [Name](#cfn-fsx-snapshotpolicy-name): {{String}}
  [Schedules](#cfn-fsx-snapshotpolicy-schedules): {{
    - SnapshotPolicySchedule}}
  [StorageVirtualMachineId](#cfn-fsx-snapshotpolicy-storagevirtualmachineid): {{String}}
  [Tags](#cfn-fsx-snapshotpolicy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fsx-snapshotpolicy-properties"></a>

`Enabled`  <a name="cfn-fsx-snapshotpolicy-enabled"></a>
Specifies whether the snapshot policy is enabled. This value defaults to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemId`  <a name="cfn-fsx-snapshotpolicy-filesystemid"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
*Required*: No
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-fsx-snapshotpolicy-name"></a>
The name of the snapshot policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedules`  <a name="cfn-fsx-snapshotpolicy-schedules"></a>
The schedules on which ONTAP creates snapshots for the snapshot policy.
*Required*: Yes
*Type*: Array of [SnapshotPolicySchedule](aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageVirtualMachineId`  <a name="cfn-fsx-snapshotpolicy-storagevirtualmachineid"></a>
The ID of the snapshot policy's storage virtual machine, if you created the snapshot policy on a storage virtual machine.
*Required*: No
*Type*: String
*Pattern*: `^(svm-[0-9a-f]{17,})$`
*Minimum*: `21`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-snapshotpolicy-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-snapshotpolicy-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-snapshotpolicy-return-values"></a>

### Ref
<a name="aws-resource-fsx-snapshotpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-snapshotpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-snapshotpolicy-return-values-fn--getatt-fn--getatt"></a>

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the snapshot policy can be one of the following:
+ `CREATED` – The snapshot policy is fully available for use.
+ `CREATING` – Amazon FSx is creating the snapshot policy.
+ `DELETING` – Amazon FSx is deleting the snapshot policy.
+ `FAILED` – Amazon FSx was unable to create the snapshot policy.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`Scope`  <a name="Scope-fn::getatt"></a>
The scope of the snapshot policy can be one of the following:
+ `FILESYSTEM` – The snapshot policy was created on the file system.
+ `SVM` – The snapshot policy was created on an SVM.

`SnapshotPolicyId`  <a name="SnapshotPolicyId-fn::getatt"></a>
The system-generated, unique ID of the snapshot policy.

`UUID`  <a name="UUID-fn::getatt"></a>
The snapshot policy's universally unique identifier (UUID).
