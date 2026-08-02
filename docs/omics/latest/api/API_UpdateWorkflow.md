---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UpdateWorkflow.html
---

# UpdateWorkflow
<a name="API_UpdateWorkflow"></a>

Updates information about a workflow.

You can update the following workflow information:
+ Name
+ Description
+ Default storage type
+ Default storage capacity (with workflow ID)

This operation returns a response with no body if the operation is successful. You can check the workflow updates by calling the `GetWorkflow` API operation.

For more information, see [Update a private workflow](https://docs.aws.amazon.com/omics/latest/dev/update-private-workflow.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_UpdateWorkflow_RequestSyntax"></a>

```
POST /workflow/{{id}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "readmeMarkdown": "{{string}}",
   "storageCapacity": {{number}},
   "storageType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-uri-id"></a>
The workflow's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-description"></a>
A description for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-name"></a>
A name for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeMarkdown](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-readmeMarkdown"></a>
The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
Type: String
Required: No

 ** [storageCapacity](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-storageCapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [storageType](#API_UpdateWorkflow_RequestSyntax) **   <a name="omics-UpdateWorkflow-request-storageType"></a>
The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see [Running workflows](https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

## Response Syntax
<a name="API_UpdateWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_UpdateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkflow_Errors"></a>

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
<a name="API_UpdateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UpdateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UpdateWorkflow)
