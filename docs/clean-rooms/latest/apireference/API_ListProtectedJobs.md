---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListProtectedJobs.html
---

# ListProtectedJobs
<a name="API_ListProtectedJobs"></a>

Lists protected jobs, sorted by most recent job.

## Request Syntax
<a name="API_ListProtectedJobs_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/protectedJobs?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProtectedJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListProtectedJobs_RequestSyntax) **   <a name="API-ListProtectedJobs-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListProtectedJobs_RequestSyntax) **   <a name="API-ListProtectedJobs-request-uri-membershipIdentifier"></a>
The identifier for the membership in the collaboration.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListProtectedJobs_RequestSyntax) **   <a name="API-ListProtectedJobs-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [status](#API_ListProtectedJobs_RequestSyntax) **   <a name="API-ListProtectedJobs-request-uri-status"></a>
A filter on the status of the protected job.
Valid Values: `SUBMITTED | STARTED | CANCELLED | CANCELLING | FAILED | SUCCESS`

## Request Body
<a name="API_ListProtectedJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProtectedJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "protectedJobs": [
      {
         "createTime": number,
         "id": "string",
         "jobComputePayerAccountId": "string",
         "membershipArn": "string",
         "membershipId": "string",
         "receiverConfigurations": [
            {
               "analysisType": "string",
               "configurationDetails": { ... }
            }
         ],
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProtectedJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProtectedJobs_ResponseSyntax) **   <a name="API-ListProtectedJobs-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [protectedJobs](#API_ListProtectedJobs_ResponseSyntax) **   <a name="API-ListProtectedJobs-response-protectedJobs"></a>
A list of protected job summaries.
Type: Array of [ProtectedJobSummary](API_ProtectedJobSummary.md) objects

## Errors
<a name="API_ListProtectedJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListProtectedJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListProtectedJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListProtectedJobs)
