---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListJobRuns.html
---

# ListJobRuns
<a name="API_ListJobRuns"></a>

Lists job runs.

## Request Syntax
<a name="API_ListJobRuns_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/jobs/{{jobIdentifier}}/runs?maxResults={{maxResults}}&nextToken={{nextToken}}&sortOrder={{sortOrder}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list job runs.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [jobIdentifier](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-jobIdentifier"></a>
The ID of the job run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-maxResults"></a>
The maximum number of job runs to return in a single call to ListJobRuns. When the number of job runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListJobRuns to list the next set of job runs.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-nextToken"></a>
When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [sortOrder](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-sortOrder"></a>
Specifies the order in which job runs are to be sorted.
Valid Values: `ASCENDING | DESCENDING`

 ** [status](#API_ListJobRuns_RequestSyntax) **   <a name="datazone-ListJobRuns-request-uri-status"></a>
The status of a job run.
Valid Values: `SCHEDULED | IN_PROGRESS | SUCCESS | PARTIALLY_SUCCEEDED | FAILED | ABORTED | TIMED_OUT | CANCELED`

## Request Body
<a name="API_ListJobRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "createdBy": "string",
         "domainId": "string",
         "endTime": number,
         "error": {
            "message": "string"
         },
         "jobId": "string",
         "jobType": "string",
         "runId": "string",
         "runMode": "string",
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListJobRuns_ResponseSyntax) **   <a name="datazone-ListJobRuns-response-items"></a>
The results of the ListJobRuns action.
Type: Array of [JobRunSummary](API_JobRunSummary.md) objects

 ** [nextToken](#API_ListJobRuns_ResponseSyntax) **   <a name="datazone-ListJobRuns-response-nextToken"></a>
When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListJobRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListJobRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListJobRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListJobRuns)
