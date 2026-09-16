---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UpdateWorkflowVersion.html
---

# UpdateWorkflowVersion
<a name="API_UpdateWorkflowVersion"></a>

Updates information about the workflow version. For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_UpdateWorkflowVersion_RequestSyntax"></a>

```
POST /workflow/{{workflowId}}/version/{{versionName}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "readmeMarkdown": "{{string}}",
   "storageCapacity": {{number}},
   "storageType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkflowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [versionName](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-uri-versionName"></a>
The name of the workflow version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

 ** [workflowId](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-uri-workflowId"></a>
The workflow's ID. The `workflowId` is not the UUID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkflowVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-description"></a>
Description of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeMarkdown](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-readmeMarkdown"></a>
The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.
Type: String
Required: No

 ** [storageCapacity](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-storageCapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow version. The `storageCapacity` can be overwritten at run time. The storage capacity is not required for runs with a `DYNAMIC` storage type.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [storageType](#API_UpdateWorkflowVersion_RequestSyntax) **   <a name="omics-UpdateWorkflowVersion-request-storageType"></a>
The default storage type for runs that use this workflow version. The `storageType` can be overridden at run time. `DYNAMIC` storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see [Run storage types](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html) in the *in the * AWS HealthOmics User Guide* *.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

## Response Syntax
<a name="API_UpdateWorkflowVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_UpdateWorkflowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkflowVersion_Errors"></a>

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
<a name="API_UpdateWorkflowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UpdateWorkflowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UpdateWorkflowVersion)
