---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageGroup.html
---

# ModelPackageGroup
<a name="API_ModelPackageGroup"></a>

A group of versioned models in the Model Registry.

## Contents
<a name="API_ModelPackageGroup_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-ModelPackageGroup-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ModelPackageGroup-CreationTime"></a>
The time that the model group was created.
Type: Timestamp
Required: No

 ** ModelPackageGroupArn **   <a name="sagemaker-Type-ModelPackageGroup-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`
Required: No

 ** ModelPackageGroupDescription **   <a name="sagemaker-Type-ModelPackageGroup-ModelPackageGroupDescription"></a>
The description for the model group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ModelPackageGroup-ModelPackageGroupName"></a>
The name of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelPackageGroupStatus **   <a name="sagemaker-Type-ModelPackageGroup-ModelPackageGroupStatus"></a>
The status of the model group. This can be one of the following values.
+  `PENDING` - The model group is pending being created.
+  `IN_PROGRESS` - The model group is in the process of being created.
+  `COMPLETED` - The model group was successfully created.
+  `FAILED` - The model group failed.
+  `DELETING` - The model group is in the process of being deleted.
+  `DELETE_FAILED` - SageMaker failed to delete the model group.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting | DeleteFailed`
Required: No

 ** Tags **   <a name="sagemaker-Type-ModelPackageGroup-Tags"></a>
A list of the tags associated with the model group. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ModelPackageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageGroup)
