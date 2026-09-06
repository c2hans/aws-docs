---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListWorkspaceInstances.html
---

# ListWorkspaceInstances
<a name="API_ListWorkspaceInstances"></a>

Retrieves a collection of WorkSpaces Instances based on specified filters.

## Request Parameters
<a name="API_ListWorkspaceInstances_RequestParameters"></a>

 ** MaxResults **
Maximum number of WorkSpaces Instances to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** NextToken **
Pagination token for retrieving subsequent pages of WorkSpaces Instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ProvisionStates **
Filter WorkSpaces Instances by their current provisioning states.
Type: Array of strings
Valid Values: `ALLOCATING | ALLOCATED | DEALLOCATING | DEALLOCATED | ERROR_ALLOCATING | ERROR_DEALLOCATING`
Required: No

## Response Elements
<a name="API_ListWorkspaceInstances_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
Token for retrieving additional WorkSpaces Instances if the result set is paginated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** WorkspaceInstances **
Collection of WorkSpaces Instances returned by the query.
Type: Array of [WorkspaceInstance](API_WorkspaceInstance.md) objects

## Errors
<a name="API_ListWorkspaceInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 403

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

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
<a name="API_ListWorkspaceInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/ListWorkspaceInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ListWorkspaceInstances)
