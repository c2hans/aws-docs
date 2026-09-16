---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryState.html
---

# GetQueryState
<a name="API_GetQueryState"></a>

Returns the state of a query previously submitted. Clients are expected to poll `GetQueryState` to monitor the current state of the planning before retrieving the work units. A query state is only visible to the principal that made the initial call to `StartQueryPlanning`.

## Request Syntax
<a name="API_GetQueryState_RequestSyntax"></a>

```
POST /GetQueryState HTTP/1.1
Content-type: application/json

{
   "QueryId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetQueryState_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetQueryState_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryId](#API_GetQueryState_RequestSyntax) **   <a name="lakeformation-GetQueryState-request-QueryId"></a>
The ID of the plan query operation.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

## Response Syntax
<a name="API_GetQueryState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Error": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_GetQueryState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Error](#API_GetQueryState_ResponseSyntax) **   <a name="lakeformation-GetQueryState-response-Error"></a>
An error message when the operation fails.
Type: String

 ** [State](#API_GetQueryState_ResponseSyntax) **   <a name="lakeformation-GetQueryState-response-State"></a>
The state of a query previously submitted. The possible states are:
+ PENDING: the query is pending.
+ WORKUNITS\_AVAILABLE: some work units are ready for retrieval and execution.
+ FINISHED: the query planning finished successfully, and all work units are ready for retrieval and execution.
+ ERROR: an error occurred with the query, such as an invalid query ID or a backend error.
Type: String
Valid Values: `PENDING | WORKUNITS_AVAILABLE | ERROR | FINISHED | EXPIRED`

## Errors
<a name="API_GetQueryState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetQueryState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetQueryState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetQueryState)
