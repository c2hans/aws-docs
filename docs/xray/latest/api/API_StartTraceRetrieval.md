---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_StartTraceRetrieval.html
---

# StartTraceRetrieval
<a name="API_StartTraceRetrieval"></a>

 Initiates a trace retrieval process using the specified time range and for the given trace IDs in the Transaction Search generated CloudWatch log group. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).

API returns a `RetrievalToken`, which can be used with `ListRetrievedTraces` or `GetRetrievedTracesGraph` to fetch results. Retrievals will time out after 60 minutes. To execute long time ranges, consider segmenting into multiple retrievals.

If you are using [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html), you can use this operation in a monitoring account to retrieve data from a linked source account, as long as both accounts have transaction search enabled.

For retrieving data from X-Ray directly as opposed to the Transaction-Search Log group, see [BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html).

## Request Syntax
<a name="API_StartTraceRetrieval_RequestSyntax"></a>

```
POST /StartTraceRetrieval HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "StartTime": {{number}},
   "TraceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartTraceRetrieval_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTraceRetrieval_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_StartTraceRetrieval_RequestSyntax) **   <a name="xray-StartTraceRetrieval-request-EndTime"></a>
 The end of the time range to retrieve traces. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.
Type: Timestamp
Required: Yes

 ** [StartTime](#API_StartTraceRetrieval_RequestSyntax) **   <a name="xray-StartTraceRetrieval-request-StartTime"></a>
 The start of the time range to retrieve traces. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.
Type: Timestamp
Required: Yes

 ** [TraceIds](#API_StartTraceRetrieval_RequestSyntax) **   <a name="xray-StartTraceRetrieval-request-TraceIds"></a>
 Specify the trace IDs of the traces to be retrieved.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: Yes

## Response Syntax
<a name="API_StartTraceRetrieval_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RetrievalToken": "string"
}
```

## Response Elements
<a name="API_StartTraceRetrieval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RetrievalToken](#API_StartTraceRetrieval_ResponseSyntax) **   <a name="xray-StartTraceRetrieval-response-RetrievalToken"></a>
 Retrieval token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1020.

## Errors
<a name="API_StartTraceRetrieval_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.
HTTP Status Code: 404

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_StartTraceRetrieval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/StartTraceRetrieval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/StartTraceRetrieval)
