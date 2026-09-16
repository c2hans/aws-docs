---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListTestCaseExecutionRecords.html
---

# ListTestCaseExecutionRecords
<a name="API_ListTestCaseExecutionRecords"></a>

Lists detailed steps of test case execution that includes all observations along with actions taken and data associated in the specified Amazon Connect instance.

## Request Syntax
<a name="API_ListTestCaseExecutionRecords_RequestSyntax"></a>

```
GET /test-cases/{{InstanceId}}/{{TestCaseId}}/{{TestCaseExecutionId}}/records?maxResults={{MaxResults}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTestCaseExecutionRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [Status](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-Status"></a>
Filter execution records by status.
Valid Values: `INITIATED | PASSED | FAILED | IN_PROGRESS | STOPPED`

 ** [TestCaseExecutionId](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-TestCaseExecutionId"></a>
The identifier of the test case execution.
Length Constraints: Maximum length of 500.
Required: Yes

 ** [TestCaseId](#API_ListTestCaseExecutionRecords_RequestSyntax) **   <a name="connect-ListTestCaseExecutionRecords-request-uri-TestCaseId"></a>
The identifier of the test case.
Length Constraints: Maximum length of 500.
Required: Yes

## Request Body
<a name="API_ListTestCaseExecutionRecords_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTestCaseExecutionRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExecutionRecords": [
      {
         "ObservationId": "string",
         "Record": "string",
         "Status": "string",
         "Timestamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListTestCaseExecutionRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExecutionRecords](#API_ListTestCaseExecutionRecords_ResponseSyntax) **   <a name="connect-ListTestCaseExecutionRecords-response-ExecutionRecords"></a>
An array of test case execution record objects.
Type: Array of [ExecutionRecord](API_ExecutionRecord.md) objects

 ** [NextToken](#API_ListTestCaseExecutionRecords_ResponseSyntax) **   <a name="connect-ListTestCaseExecutionRecords-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

## Errors
<a name="API_ListTestCaseExecutionRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListTestCaseExecutionRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListTestCaseExecutionRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListTestCaseExecutionRecords)
