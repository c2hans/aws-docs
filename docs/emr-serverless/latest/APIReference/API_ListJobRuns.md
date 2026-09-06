---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRuns.html
---

# ListJobRuns
<a name="API_ListJobRuns"></a>

Lists job runs based on a set of parameters.

## Request Syntax
<a name="API_ListJobRuns_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/jobruns?createdAtAfter={{createdAtAfter}}&createdAtBefore={{createdAtBefore}}&maxResults={{maxResults}}&mode={{mode}}&nextToken={{nextToken}}&states={{states}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-applicationId"></a>
The ID of the application for which to list the job run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [createdAtAfter](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-createdAtAfter"></a>
The lower bound of the option to filter by creation date and time.

 ** [createdAtBefore](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-createdAtBefore"></a>
The upper bound of the option to filter by creation date and time.

 ** [maxResults](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-maxResults"></a>
The maximum number of job runs that can be listed.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [mode](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-mode"></a>
The mode of the job runs to list.
Valid Values: `BATCH | STREAMING`

 ** [nextToken](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-nextToken"></a>
The token for the next set of job run results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

 ** [states](#API_ListJobRuns_RequestSyntax) **   <a name="emrserverless-ListJobRuns-request-uri-states"></a>
An optional filter for job run states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Valid Values: `SUBMITTED | PENDING | SCHEDULED | RUNNING | SUCCESS | FAILED | CANCELLING | CANCELLED | QUEUED`

## Request Body
<a name="API_ListJobRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobRuns": [
      {
         "applicationId": "string",
         "arn": "string",
         "attempt": number,
         "attemptCreatedAt": number,
         "attemptUpdatedAt": number,
         "createdAt": number,
         "createdBy": "string",
         "executionRole": "string",
         "id": "string",
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
<a name="API_ListJobRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobRuns](#API_ListJobRuns_ResponseSyntax) **   <a name="emrserverless-ListJobRuns-response-jobRuns"></a>
The output lists information about the specified job runs.
Type: Array of [JobRunSummary](API_JobRunSummary.md) objects

 ** [nextToken](#API_ListJobRuns_ResponseSyntax) **   <a name="emrserverless-ListJobRuns-response-nextToken"></a>
The output displays the token for the next set of job run results. This is required for pagination and is available as a response of the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

## Errors
<a name="API_ListJobRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListJobRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/ListJobRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ListJobRuns)
