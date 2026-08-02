---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRootVolumeTask.html
---

# ReplaceRootVolumeTask
<a name="API_ReplaceRootVolumeTask"></a>

Information about a root volume replacement task.

## Contents
<a name="API_ReplaceRootVolumeTask_Contents"></a>

 ** completeTime **
The time the task completed.
Type: String
Required: No

 ** deleteReplacedRootVolume **
Indicates whether the original root volume is to be deleted after the root volume replacement task completes.
Type: Boolean
Required: No

 ** imageId **
The ID of the AMI used to create the replacement root volume.
Type: String
Required: No

 ** instanceId **
The ID of the instance for which the root volume replacement task was created.
Type: String
Required: No

 ** replaceRootVolumeTaskId **
The ID of the root volume replacement task.
Type: String
Required: No

 ** snapshotId **
The ID of the snapshot used to create the replacement root volume.
Type: String
Required: No

 ** startTime **
The time the task was started.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** taskState **
The state of the task. The task can be in one of the following states:
+  `pending` - the replacement volume is being created.
+  `in-progress` - the original volume is being detached and the replacement volume is being attached.
+  `succeeded` - the replacement volume has been successfully attached to the instance and the instance is available.
+  `failing` - the replacement task is in the process of failing.
+  `failed` - the replacement task has failed but the original root volume is still attached.
+  `failing-detached` - the replacement task is in the process of failing. The instance might have no root volume attached.
+  `failed-detached` - the replacement task has failed and the instance has no root volume attached.
Type: String
Valid Values: `pending | in-progress | failing | succeeded | failed | failed-detached`
Required: No

## See Also
<a name="API_ReplaceRootVolumeTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReplaceRootVolumeTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReplaceRootVolumeTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReplaceRootVolumeTask)
