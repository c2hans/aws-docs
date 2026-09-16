---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchQuantumTasks.html
---

# SearchQuantumTasks
<a name="API_SearchQuantumTasks"></a>

Searches for tasks that match the specified filter values.

## Request Syntax
<a name="API_SearchQuantumTasks_RequestSyntax"></a>

```
POST /quantum-tasks HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchQuantumTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchQuantumTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchQuantumTasks_RequestSyntax) **   <a name="braket-SearchQuantumTasks-request-filters"></a>
Array of `SearchQuantumTasksFilter` objects to use when searching for quantum tasks.
Type: Array of [SearchQuantumTasksFilter](API_SearchQuantumTasksFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [maxResults](#API_SearchQuantumTasks_RequestSyntax) **   <a name="braket-SearchQuantumTasks-request-maxResults"></a>
Maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchQuantumTasks_RequestSyntax) **   <a name="braket-SearchQuantumTasks-request-nextToken"></a>
A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.
Type: String
Required: No

## Response Syntax
<a name="API_SearchQuantumTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "quantumTasks": [
      {
         "createdAt": "string",
         "deviceArn": "string",
         "endedAt": "string",
         "outputS3Bucket": "string",
         "outputS3Directory": "string",
         "quantumTaskArn": "string",
         "shots": number,
         "status": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchQuantumTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchQuantumTasks_ResponseSyntax) **   <a name="braket-SearchQuantumTasks-response-nextToken"></a>
A token used for pagination of results, or null if there are no additional results. Use the token value in a subsequent request to continue search where the previous request ended.
Type: String

 ** [quantumTasks](#API_SearchQuantumTasks_ResponseSyntax) **   <a name="braket-SearchQuantumTasks-response-quantumTasks"></a>
An array of `QuantumTaskSummary` objects for quantum tasks that match the specified filters.
Type: Array of [QuantumTaskSummary](API_QuantumTaskSummary.md) objects

## Errors
<a name="API_SearchQuantumTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_SearchQuantumTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/SearchQuantumTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchQuantumTasks)
