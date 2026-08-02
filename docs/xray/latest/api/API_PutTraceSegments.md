---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html
---

# PutTraceSegments
<a name="API_PutTraceSegments"></a>

Uploads segment documents to AWS X-Ray. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.

Segments must include the following fields. For the full segment document schema, see [AWS X-Ray Segment Documents](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-api.html#xray-api-segmentdocuments.html) in the * AWS X-Ray Developer Guide*.

**Required segment document fields**
+  `name` - The name of the service that handled the request.
+  `id` - A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.
+  `trace_id` - A unique identifier that connects all segments and subsegments originating from a single client request.
+  `start_time` - Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, `1480615200.010` or `1.480615200010E9`.
+  `end_time` - Time the segment or subsegment was closed. For example, `1480615200.090` or `1.480615200090E9`. Specify either an `end_time` or `in_progress`.
+  `in_progress` - Set to `true` instead of specifying an `end_time` to record that a segment has been started, but is not complete. Send an in-progress segment when your application receives a request that will take a long time to serve, to trace that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.

A `trace_id` consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. For trace IDs created by an X-Ray SDK, or by AWS services integrated with X-Ray, a trace ID includes:

**Trace ID Format**
+ The version number, for instance, `1`.
+ The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is `1480615200` seconds, or `58406520` in hexadecimal.
+ A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.

**Note**
Trace IDs created via OpenTelemetry have a different format based on the [W3C Trace Context specification](https://www.w3.org/TR/trace-context/). A W3C trace ID must be formatted in the X-Ray trace ID format when sending to X-Ray. For example, a W3C trace ID `4efaaf4d1e8720b39541901950019ee5` should be formatted as `1-4efaaf4d-1e8720b39541901950019ee5` when sending to X-Ray. While X-Ray trace IDs include the original request timestamp in Unix epoch time, this is not required or validated.

## Request Syntax
<a name="API_PutTraceSegments_RequestSyntax"></a>

```
POST /TraceSegments HTTP/1.1
Content-type: application/json

{
   "TraceSegmentDocuments": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_PutTraceSegments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutTraceSegments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TraceSegmentDocuments](#API_PutTraceSegments_RequestSyntax) **   <a name="xray-PutTraceSegments-request-TraceSegmentDocuments"></a>
A string containing a JSON document defining one or more segments or subsegments.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_PutTraceSegments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UnprocessedTraceSegments": [
      {
         "ErrorCode": "string",
         "Id": "string",
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutTraceSegments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnprocessedTraceSegments](#API_PutTraceSegments_ResponseSyntax) **   <a name="xray-PutTraceSegments-response-UnprocessedTraceSegments"></a>
Segments that failed processing.
Type: Array of [UnprocessedTraceSegment](API_UnprocessedTraceSegment.md) objects

## Errors
<a name="API_PutTraceSegments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_PutTraceSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/PutTraceSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/PutTraceSegments)
