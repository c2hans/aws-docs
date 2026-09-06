---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListMatchingJobs.html
---

# ListMatchingJobs
<a name="API_ListMatchingJobs"></a>

Lists all jobs for a given workflow.

## Request Syntax
<a name="API_ListMatchingJobs_RequestSyntax"></a>

```
GET /matchingworkflows/{{workflowName}}/jobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMatchingJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMatchingJobs_RequestSyntax) **   <a name="API-ListMatchingJobs-request-uri-maxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListMatchingJobs_RequestSyntax) **   <a name="API-ListMatchingJobs-request-uri-nextToken"></a>
The pagination token from the previous API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

 ** [workflowName](#API_ListMatchingJobs_RequestSyntax) **   <a name="API-ListMatchingJobs-request-uri-workflowName"></a>
The name of the workflow to be retrieved.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_ListMatchingJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMatchingJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "endTime": number,
         "jobId": "string",
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMatchingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListMatchingJobs_ResponseSyntax) **   <a name="API-ListMatchingJobs-response-jobs"></a>
A list of `JobSummary` objects, each of which contain the ID, status, start time, and end time of a job.
Type: Array of [JobSummary](API_JobSummary.md) objects

 ** [nextToken](#API_ListMatchingJobs_ResponseSyntax) **   <a name="API-ListMatchingJobs-response-nextToken"></a>
The pagination token from the previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

## Errors
<a name="API_ListMatchingJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_ListMatchingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/ListMatchingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ListMatchingJobs)
