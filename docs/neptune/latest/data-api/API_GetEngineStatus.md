---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_GetEngineStatus.html
---

# GetEngineStatus
<a name="API_GetEngineStatus"></a>

Retrieves the status of the graph database on the host.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetEngineStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getenginestatus) IAM action in that cluster.

## Request Syntax
<a name="API_GetEngineStatus_RequestSyntax"></a>

```
GET /status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEngineStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEngineStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEngineStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dbEngineVersion": "string",
   "dfeQueryEngine": "string",
   "features": {
      "string" : JSON value
   },
   "gremlin": {
      "version": "string"
   },
   "labMode": {
      "string" : "string"
   },
   "opencypher": {
      "version": "string"
   },
   "role": "string",
   "rollingBackTrxCount": number,
   "rollingBackTrxEarliestStartTime": "string",
   "settings": {
      "string" : "string"
   },
   "sparql": {
      "version": "string"
   },
   "startTime": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetEngineStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbEngineVersion](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-dbEngineVersion"></a>
Set to the Neptune engine version running on your DB cluster. If this engine version has been manually patched since it was released, the version number is prefixed by `Patch-`.
Type: String

 ** [dfeQueryEngine](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-dfeQueryEngine"></a>
Set to `enabled` if the DFE engine is fully enabled, or to `viaQueryHint` (the default) if the DFE engine is only used with queries that have the `useDFE` query hint set to `true`.
Type: String

 ** [features](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-features"></a>
Contains status information about the features enabled on your DB cluster.
Type: String to JSON value map

 ** [gremlin](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-gremlin"></a>
Contains information about the Gremlin query language available on your cluster. Specifically, it contains a version field that specifies the current TinkerPop version being used by the engine.
Type: [QueryLanguageVersion](API_QueryLanguageVersion.md) object

 ** [labMode](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-labMode"></a>
Contains Lab Mode settings being used by the engine.
Type: String to string map

 ** [opencypher](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-opencypher"></a>
Contains information about the openCypher query language available on your cluster. Specifically, it contains a version field that specifies the current operCypher version being used by the engine.
Type: [QueryLanguageVersion](API_QueryLanguageVersion.md) object

 ** [role](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-role"></a>
Set to `reader` if the instance is a read-replica, or to `writer` if the instance is the primary instance.
Type: String

 ** [rollingBackTrxCount](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-rollingBackTrxCount"></a>
If there are transactions being rolled back, this field is set to the number of such transactions. If there are none, the field doesn't appear at all.
Type: Integer

 ** [rollingBackTrxEarliestStartTime](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-rollingBackTrxEarliestStartTime"></a>
Set to the start time of the earliest transaction being rolled back. If no transactions are being rolled back, the field doesn't appear at all.
Type: String

 ** [settings](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-settings"></a>
Contains information about the current settings on your DB cluster. For example, contains the current cluster query timeout setting (`clusterQueryTimeoutInMs`).
Type: String to string map

 ** [sparql](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-sparql"></a>
Contains information about the SPARQL query language available on your cluster. Specifically, it contains a version field that specifies the current SPARQL version being used by the engine.
Type: [QueryLanguageVersion](API_QueryLanguageVersion.md) object

 ** [startTime](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-startTime"></a>
Set to the UTC time at which the current server process started.
Type: String

 ** [status](#API_GetEngineStatus_ResponseSyntax) **   <a name="neptunedata-GetEngineStatus-response-status"></a>
Set to `healthy` if the instance is not experiencing problems. If the instance is recovering from a crash or from being rebooted and there are active transactions running from the latest server shutdown, status is set to `recovery`.
Type: String

## Errors
<a name="API_GetEngineStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientTimeoutException **
Raised when a request timed out in the client.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 408

 ** ConstraintViolationException **
Raised when a value in a request field did not satisfy required constraints.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** IllegalArgumentException **
Raised when an argument in a request is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InternalFailureException **
Raised when the processing of the request failed unexpectedly.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

 ** InvalidArgumentException **
Raised when an argument in a request has an invalid value.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** PreconditionsFailedException **
Raised when a precondition for processing a request is not satisfied.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** TooManyRequestsException **
Raised when the number of requests being processed exceeds the limit.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 429

 ** UnsupportedOperationException **
Raised when a request attempts to initiate an operation that is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

## See Also
<a name="API_GetEngineStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/GetEngineStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/GetEngineStatus)
