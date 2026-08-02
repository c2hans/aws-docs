---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogObject.html
---

# GetLogObject
<a name="API_GetLogObject"></a>

Retrieves a large logging object (LLO) and streams it back. This API is used to fetch the content of large portions of log events that have been ingested through the PutOpenTelemetryLogs API. When log events contain fields that would cause the total event size to exceed 1MB, CloudWatch Logs automatically processes up to 10 fields, starting with the largest fields. Each field is truncated as needed to keep the total event size as close to 1MB as possible. The excess portions are stored as Large Log Objects (LLOs) and these fields are processed separately and LLO reference system fields (in the format `@ptr.$[path.to.field]`) are added. The path in the reference field reflects the original JSON structure where the large field was located. For example, this could be `@ptr.$['input']['message']`, `@ptr.$['AAA']['BBB']['CCC']['DDD']`, `@ptr.$['AAA']`, or any other path matching your log structure.

**Note**
The `GetLogObject` API routes requests using SDK host prefix injection. SDK versions released before April 1, 2026 route to `streaming-logs.Region.amazonaws.com`, which does not support VPC endpoints. SDK versions released on or after April 1, 2026 route to `stream-logs.Region.amazonaws.com`, which supports VPC endpoints. To set up a VPC endpoint for this API, see [Creating a VPC endpoint for CloudWatch Logs ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html#create-VPC-endpoint-for-CloudWatchLogs).

## Request Syntax
<a name="API_GetLogObject_RequestSyntax"></a>

```
{
   "logObjectPointer": "{{string}}",
   "unmask": {{boolean}}
}
```

## Request Parameters
<a name="API_GetLogObject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logObjectPointer](#API_GetLogObject_RequestSyntax) **   <a name="CWL-GetLogObject-request-logObjectPointer"></a>
A pointer to the specific log object to retrieve. This is a required parameter that uniquely identifies the log object within CloudWatch Logs. The pointer is typically obtained from a previous query or filter operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [unmask](#API_GetLogObject_RequestSyntax) **   <a name="CWL-GetLogObject-request-unmask"></a>
A boolean flag that indicates whether to unmask sensitive log data. When set to true, any masked or redacted data in the log object will be displayed in its original form. Default is false.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetLogObject_ResponseSyntax"></a>

```
{
   "fieldStream": {
      "fields": {
         "data": blob
      },
      "InternalStreamingException": {
      }
   }
}
```

## Response Elements
<a name="API_GetLogObject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fieldStream](#API_GetLogObject_ResponseSyntax) **   <a name="CWL-GetLogObject-response-fieldStream"></a>
A stream of structured log data returned by the GetLogObject operation. This stream contains log events with their associated metadata and extracted fields.
Type: [GetLogObjectResponseStream](API_GetLogObjectResponseStream.md) object

## Errors
<a name="API_GetLogObject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

## See Also
<a name="API_GetLogObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetLogObject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetLogObject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLogObject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetLogObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLogObject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetLogObject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetLogObject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetLogObject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetLogObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLogObject)
