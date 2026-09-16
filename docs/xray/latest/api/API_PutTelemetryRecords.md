---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_PutTelemetryRecords.html
---

# PutTelemetryRecords
<a name="API_PutTelemetryRecords"></a>

Used by the AWS X-Ray daemon to upload telemetry.

## Request Syntax
<a name="API_PutTelemetryRecords_RequestSyntax"></a>

```
POST /TelemetryRecords HTTP/1.1
Content-type: application/json

{
   "EC2InstanceId": "{{string}}",
   "Hostname": "{{string}}",
   "ResourceARN": "{{string}}",
   "TelemetryRecords": [
      {
         "BackendConnectionErrors": {
            "ConnectionRefusedCount": {{number}},
            "HTTPCode4XXCount": {{number}},
            "HTTPCode5XXCount": {{number}},
            "OtherCount": {{number}},
            "TimeoutCount": {{number}},
            "UnknownHostCount": {{number}}
         },
         "SegmentsReceivedCount": {{number}},
         "SegmentsRejectedCount": {{number}},
         "SegmentsSentCount": {{number}},
         "SegmentsSpilloverCount": {{number}},
         "Timestamp": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutTelemetryRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutTelemetryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EC2InstanceId](#API_PutTelemetryRecords_RequestSyntax) **   <a name="xray-PutTelemetryRecords-request-EC2InstanceId"></a>

Type: String
Length Constraints: Maximum length of 20.
Required: No

 ** [Hostname](#API_PutTelemetryRecords_RequestSyntax) **   <a name="xray-PutTelemetryRecords-request-Hostname"></a>

Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [ResourceARN](#API_PutTelemetryRecords_RequestSyntax) **   <a name="xray-PutTelemetryRecords-request-ResourceARN"></a>

Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [TelemetryRecords](#API_PutTelemetryRecords_RequestSyntax) **   <a name="xray-PutTelemetryRecords-request-TelemetryRecords"></a>

Type: Array of [TelemetryRecord](API_TelemetryRecord.md) objects
Required: Yes

## Response Syntax
<a name="API_PutTelemetryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutTelemetryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutTelemetryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_PutTelemetryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/PutTelemetryRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/PutTelemetryRecords)
