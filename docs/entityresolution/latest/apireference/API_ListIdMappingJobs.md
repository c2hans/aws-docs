---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdMappingJobs.html
---

# ListIdMappingJobs
<a name="API_ListIdMappingJobs"></a>

Lists all ID mapping jobs for a given workflow.

## Request Syntax
<a name="API_ListIdMappingJobs_RequestSyntax"></a>

```
GET /idmappingworkflows/{{workflowName}}/jobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIdMappingJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListIdMappingJobs_RequestSyntax) **   <a name="API-ListIdMappingJobs-request-uri-maxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListIdMappingJobs_RequestSyntax) **   <a name="API-ListIdMappingJobs-request-uri-nextToken"></a>
The pagination token from the previous API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

 ** [workflowName](#API_ListIdMappingJobs_RequestSyntax) **   <a name="API-ListIdMappingJobs-request-uri-workflowName"></a>
The name of the workflow to be retrieved.
Pattern: `[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## Request Body
<a name="API_ListIdMappingJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIdMappingJobs_ResponseSyntax"></a>

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
<a name="API_ListIdMappingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListIdMappingJobs_ResponseSyntax) **   <a name="API-ListIdMappingJobs-response-jobs"></a>
A list of `JobSummary` objects.
Type: Array of [JobSummary](API_JobSummary.md) objects

 ** [nextToken](#API_ListIdMappingJobs_ResponseSyntax) **   <a name="API-ListIdMappingJobs-response-nextToken"></a>
The pagination token from the previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

## Errors
<a name="API_ListIdMappingJobs_Errors"></a>

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
<a name="API_ListIdMappingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/ListIdMappingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ListIdMappingJobs)
