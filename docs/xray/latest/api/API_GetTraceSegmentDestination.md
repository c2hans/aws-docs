---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSegmentDestination.html
---

# GetTraceSegmentDestination
<a name="API_GetTraceSegmentDestination"></a>

 Retrieves the current destination of data sent to `PutTraceSegments` and *OpenTelemetry protocol (OTLP)* endpoint. The Transaction Search feature requires a CloudWatchLogs destination. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) and [OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html).

## Request Syntax
<a name="API_GetTraceSegmentDestination_RequestSyntax"></a>

```
POST /GetTraceSegmentDestination HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTraceSegmentDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTraceSegmentDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTraceSegmentDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Destination": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetTraceSegmentDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Destination](#API_GetTraceSegmentDestination_ResponseSyntax) **   <a name="xray-GetTraceSegmentDestination-response-Destination"></a>
 Retrieves the current destination.
Type: String
Valid Values: `XRay | CloudWatchLogs`

 ** [Status](#API_GetTraceSegmentDestination_ResponseSyntax) **   <a name="xray-GetTraceSegmentDestination-response-Status"></a>
 Status of the retrieval.
Type: String
Valid Values: `PENDING | ACTIVE`

## Errors
<a name="API_GetTraceSegmentDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetTraceSegmentDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetTraceSegmentDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetTraceSegmentDestination)
