---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ReplacePermissionAssociationsWork.html
---

# ReplacePermissionAssociationsWork
<a name="API_ReplacePermissionAssociationsWork"></a>

A structure that represents the background work that AWS RAM performs when you invoke the [ReplacePermissionAssociations](API_ReplacePermissionAssociations.md) operation.

## Contents
<a name="API_ReplacePermissionAssociationsWork_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** creationTime **   <a name="ram-Type-ReplacePermissionAssociationsWork-creationTime"></a>
The date and time when this asynchronous background task was created.
Type: Timestamp
Required: No

 ** fromPermissionArn **   <a name="ram-Type-ReplacePermissionAssociationsWork-fromPermissionArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission that this background task is replacing.
Type: String
Required: No

 ** fromPermissionVersion **   <a name="ram-Type-ReplacePermissionAssociationsWork-fromPermissionVersion"></a>
The version of the managed permission that this background task is replacing.
Type: String
Required: No

 ** id **   <a name="ram-Type-ReplacePermissionAssociationsWork-id"></a>
The unique identifier for the background task associated with one [ReplacePermissionAssociations](API_ReplacePermissionAssociations.md) request.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-ReplacePermissionAssociationsWork-lastUpdatedTime"></a>
The date and time when the status of this background task was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="ram-Type-ReplacePermissionAssociationsWork-status"></a>
Specifies the current status of the background tasks for the specified ID. The output is one of the following strings:
+  `IN_PROGRESS`
+  `COMPLETED`
+  `FAILED`
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** statusMessage **   <a name="ram-Type-ReplacePermissionAssociationsWork-statusMessage"></a>
Specifies the reason for a `FAILED` status. This field is present only when there `status` is `FAILED`.
Type: String
Required: No

 ** toPermissionArn **   <a name="ram-Type-ReplacePermissionAssociationsWork-toPermissionArn"></a>
The ARN of the managed permission that this background task is associating with the resource shares in place of the managed permission and version specified in `fromPermissionArn` and `fromPermissionVersion`.
Type: String
Required: No

 ** toPermissionVersion **   <a name="ram-Type-ReplacePermissionAssociationsWork-toPermissionVersion"></a>
The version of the managed permission that this background task is associating with the resource shares. This is always the version that is currently the default for this managed permission.
Type: String
Required: No

## See Also
<a name="API_ReplacePermissionAssociationsWork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ReplacePermissionAssociationsWork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ReplacePermissionAssociationsWork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ReplacePermissionAssociationsWork)
