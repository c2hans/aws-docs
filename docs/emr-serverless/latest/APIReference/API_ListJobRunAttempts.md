---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRunAttempts.html
---

# ListJobRunAttempts
<a name="API_ListJobRunAttempts"></a>

Lists all attempt of a job run.

## Request Syntax
<a name="API_ListJobRunAttempts_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/jobruns/{{jobRunId}}/attempts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobRunAttempts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListJobRunAttempts_RequestSyntax) **   <a name="emrserverless-ListJobRunAttempts-request-uri-applicationId"></a>
The ID of the application for which to list job runs.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [jobRunId](#API_ListJobRunAttempts_RequestSyntax) **   <a name="emrserverless-ListJobRunAttempts-request-uri-jobRunId"></a>
The ID of the job run to list.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [maxResults](#API_ListJobRunAttempts_RequestSyntax) **   <a name="emrserverless-ListJobRunAttempts-request-uri-maxResults"></a>
The maximum number of job run attempts to list.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListJobRunAttempts_RequestSyntax) **   <a name="emrserverless-ListJobRunAttempts-request-uri-nextToken"></a>
The token for the next set of job run attempt results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

## Request Body
<a name="API_ListJobRunAttempts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobRunAttempts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobRunAttempts": [
      {
         "applicationId": "string",
         "arn": "string",
         "attempt": number,
         "createdAt": number,
         "createdBy": "string",
         "executionRole": "string",
         "id": "string",
         "jobCreatedAt": number,
         "mode": "string",
         "name": "string",
         "releaseLabel": "string",
         "state": "string",
         "stateDetails": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobRunAttempts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobRunAttempts](#API_ListJobRunAttempts_ResponseSyntax) **   <a name="emrserverless-ListJobRunAttempts-response-jobRunAttempts"></a>
The array of the listed job run attempt objects.
Type: Array of [JobRunAttemptSummary](API_JobRunAttemptSummary.md) objects

 ** [nextToken](#API_ListJobRunAttempts_ResponseSyntax) **   <a name="emrserverless-ListJobRunAttempts-response-nextToken"></a>
The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

## Errors
<a name="API_ListJobRunAttempts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListJobRunAttempts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/ListJobRunAttempts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ListJobRunAttempts)
