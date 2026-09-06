---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DeleteWorkflowVersion.html
---

# DeleteWorkflowVersion
<a name="API_DeleteWorkflowVersion"></a>

Deletes a workflow version. Deleting a workflow version doesn't affect any ongoing runs that are using the workflow version.

For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_DeleteWorkflowVersion_RequestSyntax"></a>

```
DELETE /workflow/{{workflowId}}/version/{{versionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkflowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [versionName](#API_DeleteWorkflowVersion_RequestSyntax) **   <a name="omics-DeleteWorkflowVersion-request-uri-versionName"></a>
The workflow version name.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

 ** [workflowId](#API_DeleteWorkflowVersion_RequestSyntax) **   <a name="omics-DeleteWorkflowVersion-request-uri-workflowId"></a>
The workflow's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteWorkflowVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkflowVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteWorkflowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteWorkflowVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkflowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/DeleteWorkflowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DeleteWorkflowVersion)
