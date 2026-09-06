---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_DeleteWorkspaceInstance.html
---

# DeleteWorkspaceInstance
<a name="API_DeleteWorkspaceInstance"></a>

Deletes the specified WorkSpace

**Important**
Usage of this API will result in deletion of the resource in question.

## Request Parameters
<a name="API_DeleteWorkspaceInstance_RequestParameters"></a>

 ** WorkspaceInstanceId **
Unique identifier of the WorkSpaces Instance targeted for deletion.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 70.
Pattern: `wsinst-[0-9a-zA-Z]{8,63}`
Required: Yes

## Errors
<a name="API_DeleteWorkspaceInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 403

 ** ConflictException **
Signals a conflict with the current state of the resource.
 ** Message **
Description of the conflict encountered.
 ** ResourceId **
Identifier of the conflicting resource.
 ** ResourceType **
Type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates the requested resource could not be found.
 ** Message **
Details about the missing resource.
 ** ResourceId **
Identifier of the resource that was not found.
 ** ResourceType **
Type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 429

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkspaceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/DeleteWorkspaceInstance)
