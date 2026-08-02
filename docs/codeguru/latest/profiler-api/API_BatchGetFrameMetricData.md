---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_BatchGetFrameMetricData.html
---

# BatchGetFrameMetricData
<a name="API_BatchGetFrameMetricData"></a>

 Returns the time series of values for a requested list of frame metrics from a time period.

## Request Syntax
<a name="API_BatchGetFrameMetricData_RequestSyntax"></a>

```
POST /profilingGroups/{{profilingGroupName}}/frames/-/metrics?endTime={{endTime}}&period={{period}}&startTime={{startTime}}&targetResolution={{targetResolution}} HTTP/1.1
Content-type: application/json

{
   "frameMetrics": [
      {
         "frameName": "{{string}}",
         "threadStates": [ "{{string}}" ],
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetFrameMetricData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-uri-endTime"></a>
 The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

 ** [period](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-uri-period"></a>
 The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (`PT24H` or `P1D`).
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [profilingGroupName](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-uri-profilingGroupName"></a>
 The name of the profiling group associated with the the frame metrics used to return the time series values.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [startTime](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-uri-startTime"></a>
 The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

 ** [targetResolution](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-uri-targetResolution"></a>
The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values.
+  `P1D` — 1 day
+  `PT1H` — 1 hour
+  `PT5M` — 5 minutes
Valid Values: `PT5M | PT1H | P1D`

## Request Body
<a name="API_BatchGetFrameMetricData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [frameMetrics](#API_BatchGetFrameMetricData_RequestSyntax) **   <a name="profiler-BatchGetFrameMetricData-request-frameMetrics"></a>
 The details of the metrics that are used to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.
Type: Array of [FrameMetric](API_FrameMetric.md) objects
Required: No

## Response Syntax
<a name="API_BatchGetFrameMetricData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": "string",
   "endTimes": [
      {
         "value": "string"
      }
   ],
   "frameMetricData": [
      {
         "frameMetric": {
            "frameName": "string",
            "threadStates": [ "string" ],
            "type": "string"
         },
         "values": [ number ]
      }
   ],
   "resolution": "string",
   "startTime": "string",
   "unprocessedEndTimes": {
      "string" : [
         {
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_BatchGetFrameMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-endTime"></a>
 The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [endTimes](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-endTimes"></a>
 List of instances, or time steps, in the time series. For example, if the `period` is one day (`PT24H)`), and the `resolution` is five minutes (`PT5M`), then there are 288 `endTimes` in the list that are each five minutes appart.
Type: Array of [TimestampStructure](API_TimestampStructure.md) objects

 ** [frameMetricData](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-frameMetricData"></a>
Details of the metrics to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.
Type: Array of [FrameMetricDatum](API_FrameMetricDatum.md) objects

 ** [resolution](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-resolution"></a>
Resolution or granularity of the profile data used to generate the time series. This is the value used to jump through time steps in a time series. There are 3 valid values.
+  `P1D` — 1 day
+  `PT1H` — 1 hour
+  `PT5M` — 5 minutes
Type: String
Valid Values: `PT5M | PT1H | P1D`

 ** [startTime](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-startTime"></a>
 The start time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [unprocessedEndTimes](#API_BatchGetFrameMetricData_ResponseSyntax) **   <a name="profiler-BatchGetFrameMetricData-response-unprocessedEndTimes"></a>
List of instances which remained unprocessed. This will create a missing time step in the list of end times.
Type: String to array of [TimestampStructure](API_TimestampStructure.md) objects map

## Errors
<a name="API_BatchGetFrameMetricData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetFrameMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)
