---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_GetSparqlStream.html
---

# GetSparqlStream
<a name="API_GetSparqlStream"></a>

Gets a stream for an RDF graph.

With the Neptune Streams feature, you can generate a complete sequence of change-log entries that record every change made to your graph data as it happens. `GetSparqlStream` lets you collect these change-log entries for an RDF graph.

The Neptune streams feature needs to be enabled on your Neptune DBcluster. To enable streams, set the [neptune\_streams](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html#parameters-db-cluster-parameters-neptune_streams) DB cluster parameter to `1`.

See [Capturing graph changes in real time using Neptune streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetStreamRecords](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstreamrecords) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Sparql](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of SPARQL queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

## Request Syntax
<a name="API_GetSparqlStream_RequestSyntax"></a>

```
GET /sparql/stream?commitNum={{commitNum}}&iteratorType={{iteratorType}}&limit={{limit}}&opNum={{opNum}} HTTP/1.1
Accept-Encoding: {{encoding}}
```

## URI Request Parameters
<a name="API_GetSparqlStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commitNum](#API_GetSparqlStream_RequestSyntax) **   <a name="neptunedata-GetSparqlStream-request-uri-commitNum"></a>
The commit number of the starting record to read from the change-log stream. This parameter is required when `iteratorType` is`AT_SEQUENCE_NUMBER` or `AFTER_SEQUENCE_NUMBER`, and ignored when `iteratorType` is `TRIM_HORIZON` or `LATEST`.

 ** [encoding](#API_GetSparqlStream_RequestSyntax) **   <a name="neptunedata-GetSparqlStream-request-encoding"></a>
If set to TRUE, Neptune compresses the response using gzip encoding.
Valid Values: `gzip`

 ** [iteratorType](#API_GetSparqlStream_RequestSyntax) **   <a name="neptunedata-GetSparqlStream-request-uri-iteratorType"></a>
Can be one of:
+  `AT_SEQUENCE_NUMBER`   –   Indicates that reading should start from the event sequence number specified jointly by the `commitNum` and `opNum` parameters.
+  `AFTER_SEQUENCE_NUMBER`   –   Indicates that reading should start right after the event sequence number specified jointly by the `commitNum` and `opNum` parameters.
+  `TRIM_HORIZON`   –   Indicates that reading should start at the last untrimmed record in the system, which is the oldest unexpired (not yet deleted) record in the change-log stream.
+  `LATEST`   –   Indicates that reading should start at the most recent record in the system, which is the latest unexpired (not yet deleted) record in the change-log stream.
Valid Values: `AT_SEQUENCE_NUMBER | AFTER_SEQUENCE_NUMBER | TRIM_HORIZON | LATEST`

 ** [limit](#API_GetSparqlStream_RequestSyntax) **   <a name="neptunedata-GetSparqlStream-request-uri-limit"></a>
Specifies the maximum number of records to return. There is also a size limit of 10 MB on the response that can't be modified and that takes precedence over the number of records specified in the `limit` parameter. The response does include a threshold-breaching record if the 10 MB limit was reached.
The range for `limit` is 1 to 100,000, with a default of 10.
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [opNum](#API_GetSparqlStream_RequestSyntax) **   <a name="neptunedata-GetSparqlStream-request-uri-opNum"></a>
The operation sequence number within the specified commit to start reading from in the change-log stream data. The default is `1`.

## Request Body
<a name="API_GetSparqlStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSparqlStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "format": "string",
   "lastEventId": {
      "string" : "string"
   },
   "lastTrxTimestamp": number,
   "records": [
      {
         "commitTimestamp": number,
         "data": {
            "stmt": "string"
         },
         "eventId": {
            "string" : "string"
         },
         "isLastOp": boolean,
         "op": "string"
      }
   ],
   "totalRecords": number
}
```

## Response Elements
<a name="API_GetSparqlStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [format](#API_GetSparqlStream_ResponseSyntax) **   <a name="neptunedata-GetSparqlStream-response-format"></a>
Serialization format for the change records being returned. Currently, the only supported value is `NQUADS`.
Type: String

 ** [lastEventId](#API_GetSparqlStream_ResponseSyntax) **   <a name="neptunedata-GetSparqlStream-response-lastEventId"></a>
Sequence identifier of the last change in the stream response.
An event ID is composed of two fields: a `commitNum`, which identifies a transaction that changed the graph, and an `opNum`, which identifies a specific operation within that transaction:
Type: String to string map

 ** [lastTrxTimestamp](#API_GetSparqlStream_ResponseSyntax) **   <a name="neptunedata-GetSparqlStream-response-lastTrxTimestamp"></a>
The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.
Type: Long

 ** [records](#API_GetSparqlStream_ResponseSyntax) **   <a name="neptunedata-GetSparqlStream-response-records"></a>
An array of serialized change-log stream records included in the response.
Type: Array of [SparqlRecord](API_SparqlRecord.md) objects

 ** [totalRecords](#API_GetSparqlStream_ResponseSyntax) **   <a name="neptunedata-GetSparqlStream-response-totalRecords"></a>
The total number of records in the response.
Type: Integer

## Errors
<a name="API_GetSparqlStream_Errors"></a>

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

 ** ExpiredStreamException **
Raised when a request attempts to access an stream that has expired.
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

 ** InvalidArgumentException **
Raised when an argument in a request has an invalid value.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InvalidParameterException **
Raised when a parameter value is not valid.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that includes an invalid parameter.
HTTP Status Code: 400

 ** MemoryLimitExceededException **
Raised when a request fails because of insufficient memory resources. The request can be retried.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that failed.
HTTP Status Code: 500

 ** PreconditionsFailedException **
Raised when a precondition for processing a request is not satisfied.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** StreamRecordsNotFoundException **
Raised when stream records requested by a query cannot be found.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 404

 ** ThrottlingException **
Raised when the rate of requests exceeds the maximum throughput. Requests can be retried after encountering this exception.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 500

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
<a name="API_GetSparqlStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/GetSparqlStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/GetSparqlStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
