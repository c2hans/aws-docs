---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-replacerootvolumetask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ReplaceRootVolumeTask
<a name="aws-resource-ec2-replacerootvolumetask"></a>

Information about a root volume replacement task.

## Syntax
<a name="aws-resource-ec2-replacerootvolumetask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-replacerootvolumetask-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::ReplaceRootVolumeTask",
  "Properties" : {
      "[DeleteReplacedRootVolume](#cfn-ec2-replacerootvolumetask-deletereplacedrootvolume)" : {{Boolean}},
      "[InstanceId](#cfn-ec2-replacerootvolumetask-instanceid)" : {{String}},
      "[Tags](#cfn-ec2-replacerootvolumetask-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-replacerootvolumetask-syntax.yaml"></a>

```
Type: AWS::EC2::ReplaceRootVolumeTask
Properties:
  [DeleteReplacedRootVolume](#cfn-ec2-replacerootvolumetask-deletereplacedrootvolume): {{Boolean}}
  [InstanceId](#cfn-ec2-replacerootvolumetask-instanceid): {{String}}
  [Tags](#cfn-ec2-replacerootvolumetask-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-replacerootvolumetask-properties"></a>

`DeleteReplacedRootVolume`  <a name="cfn-ec2-replacerootvolumetask-deletereplacedrootvolume"></a>
Indicates whether the original root volume is to be deleted after the root volume replacement task completes.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceId`  <a name="cfn-ec2-replacerootvolumetask-instanceid"></a>
The ID of the instance for which the root volume replacement task was created.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-replacerootvolumetask-tags"></a>
The tags assigned to the task.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-replacerootvolumetask-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-replacerootvolumetask-return-values"></a>

### Ref
<a name="aws-resource-ec2-replacerootvolumetask-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-replacerootvolumetask-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-replacerootvolumetask-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CompleteTime`  <a name="CompleteTime-fn::getatt"></a>
The time the task completed.

`ReplaceRootVolumeTaskId`  <a name="ReplaceRootVolumeTaskId-fn::getatt"></a>
The ID of the root volume replacement task.

`SnapshotId`  <a name="SnapshotId-fn::getatt"></a>
The ID of the snapshot used to create the replacement root volume.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time the task was started.

`TaskState`  <a name="TaskState-fn::getatt"></a>
The state of the task. The task can be in one of the following states:
+ `pending` - the replacement volume is being created.
+ `in-progress` - the original volume is being detached and the replacement volume is being attached.
+ `succeeded` - the replacement volume has been successfully attached to the instance and the instance is available.
+ `failing` - the replacement task is in the process of failing.
+ `failed` - the replacement task has failed but the original root volume is still attached.
+ `failing-detached` - the replacement task is in the process of failing. The instance might have no root volume attached.
+ `failed-detached` - the replacement task has failed and the instance has no root volume attached.
