---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartMatchingJob.html
---

# StartMatchingJob
<a name="API_StartMatchingJob"></a>

Starts the `MatchingJob` of a workflow. The workflow must have previously been created using the `CreateMatchingWorkflow` endpoint.

## Request Syntax
<a name="API_StartMatchingJob_RequestSyntax"></a>

```
POST /matchingworkflows/{{workflowName}}/jobs HTTP/1.1
```

## URI Request Parameters
<a name="API_StartMatchingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_StartMatchingJob_RequestSyntax) **   <a name="API-StartMatchingJob-request-uri-workflowName"></a>
The name of the matching job to be retrieved.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_StartMatchingJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartMatchingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string"
}
```

## Response Elements
<a name="API_StartMatchingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_StartMatchingJob_ResponseSyntax) **   <a name="API-StartMatchingJob-response-jobId"></a>
The ID of the job.
Type: String
Pattern: `[a-f0-9]{32}`

## Errors
<a name="API_StartMatchingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_StartMatchingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/StartMatchingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/StartMatchingJob)
