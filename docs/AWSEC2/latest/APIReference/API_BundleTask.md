---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleTask.html
---

# BundleTask
<a name="API_BundleTask"></a>

Describes a bundle task.

## Contents
<a name="API_BundleTask_Contents"></a>

 ** bundleId **
The ID of the bundle task.
Type: String
Required: No

 ** error **
If the task fails, a description of the error.
Type: [BundleTaskError](API_BundleTaskError.md) object
Required: No

 ** instanceId **
The ID of the instance associated with this bundle task.
Type: String
Required: No

 ** progress **
The level of task completion, as a percent (for example, 20%).
Type: String
Required: No

 ** startTime **
The time this task started.
Type: Timestamp
Required: No

 ** state **
The state of the task.
Type: String
Valid Values: `pending | waiting-for-shutdown | bundling | storing | cancelling | complete | failed`
Required: No

 ** storage **
The Amazon S3 storage locations.
Type: [Storage](API_Storage.md) object
Required: No

 ** updateTime **
The time of the most recent update for the task.
Type: Timestamp
Required: No

## See Also
<a name="API_BundleTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BundleTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BundleTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BundleTask)
