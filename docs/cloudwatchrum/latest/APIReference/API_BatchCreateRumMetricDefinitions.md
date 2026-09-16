---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html
---

# BatchCreateRumMetricDefinitions
<a name="API_BatchCreateRumMetricDefinitions"></a>

Specifies the extended metrics and custom metrics that you want a CloudWatch RUM app monitor to send to a destination. Valid destinations include CloudWatch and Evidently.

By default, RUM app monitors send some metrics to CloudWatch. These default metrics are listed in [CloudWatch metrics that you can collect with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html).

In addition to these default metrics, you can choose to send extended metrics, custom metrics, or both.
+ Extended metrics let you send metrics with additional dimensions that aren't included in the default metrics. You can also send extended metrics to both Evidently and CloudWatch. The valid dimension names for the additional dimensions for extended metrics are `BrowserName`, `CountryCode`, `DeviceType`, `FileType`, `OSName`, and `PageId`. For more information, see [ Extended metrics that you can send to CloudWatch and CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html).
+ Custom metrics are metrics that you define. You can send custom metrics to CloudWatch. CloudWatch Evidently, or both. With custom metrics, you can use any metric name and namespace. To derive the metrics, you can use any custom events, built-in events, custom attributes, or default attributes.

  You can't send custom metrics to the `AWS/RUM` namespace. You must send custom metrics to a custom namespace that you define. The namespace that you use can't start with `AWS/`. CloudWatch RUM prepends `RUM/CustomMetrics/` to the custom namespace that you define, so the final namespace for your metrics in CloudWatch is `RUM/CustomMetrics/your-custom-namespace `.

The maximum number of metric definitions that you can specify in one `BatchCreateRumMetricDefinitions` operation is 200.

The maximum number of metric definitions that one destination can contain is 2000.

Extended metrics sent to CloudWatch and RUM custom metrics are charged as CloudWatch custom metrics. Each combination of additional dimension name and dimension value counts as a custom metric. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

You must have already created a destination for the metrics before you send them. For more information, see [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html).

If some metric definitions specified in a `BatchCreateRumMetricDefinitions` operations are not valid, those metric definitions fail and return errors, but all valid metric definitions in the same operation still succeed.

## Request Syntax
<a name="API_BatchCreateRumMetricDefinitions_RequestSyntax"></a>

```
POST /rummetrics/{{AppMonitorName}}/metrics HTTP/1.1
Content-type: application/json

{
   "Destination": "{{string}}",
   "DestinationArn": "{{string}}",
   "MetricDefinitions": [
      {
         "DimensionKeys": {
            "{{string}}" : "{{string}}"
         },
         "EventPattern": "{{string}}",
         "Name": "{{string}}",
         "Namespace": "{{string}}",
         "UnitLabel": "{{string}}",
         "ValueKey": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateRumMetricDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_BatchCreateRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-request-uri-AppMonitorName"></a>
The name of the CloudWatch RUM app monitor that is to send the metrics.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_BatchCreateRumMetricDefinitions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Destination](#API_BatchCreateRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-request-Destination"></a>
The destination to send the metrics to. Valid values are `CloudWatch` and `Evidently`. If you specify `Evidently`, you must also specify the Amazon Resource Name (ARN) of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.
Type: String
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_BatchCreateRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-request-DestinationArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, do not use this parameter.
This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** [MetricDefinitions](#API_BatchCreateRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-request-MetricDefinitions"></a>
An array of structures which define the metrics that you want to send.
Type: Array of [MetricDefinitionRequest](API_MetricDefinitionRequest.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchCreateRumMetricDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "MetricDefinition": {
            "DimensionKeys": {
               "string" : "string"
            },
            "EventPattern": "string",
            "Name": "string",
            "Namespace": "string",
            "UnitLabel": "string",
            "ValueKey": "string"
         }
      }
   ],
   "MetricDefinitions": [
      {
         "DimensionKeys": {
            "string" : "string"
         },
         "EventPattern": "string",
         "MetricDefinitionId": "string",
         "Name": "string",
         "Namespace": "string",
         "UnitLabel": "string",
         "ValueKey": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateRumMetricDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchCreateRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-response-Errors"></a>
An array of error objects, if the operation caused any errors.
Type: Array of [BatchCreateRumMetricDefinitionsError](API_BatchCreateRumMetricDefinitionsError.md) objects

 ** [MetricDefinitions](#API_BatchCreateRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchCreateRumMetricDefinitions-response-MetricDefinitions"></a>
An array of structures that define the extended metrics.
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects

## Errors
<a name="API_BatchCreateRumMetricDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_BatchCreateRumMetricDefinitions_Examples"></a>

### Example
<a name="API_BatchCreateRumMetricDefinitions_Example_1"></a>

The following example creates extended metrics with dimensions `Browser:Chrome`, `Browser:Safari`, and `CountryCode=US`.

```
{
  AppMonitorName: "app-monitor-name",
  Destination: "CloudWatch",
  MetricDefinitionId: "guid2",
  MetricDefinition: {
    Name: "NavigationToleratedTransaction",
    DimensionKeys: [{
      Key: "metadata.browserName",
      Value: "BrowserName"
    },{
      Key: "metadata.countryCode",
      Value: "CountryCode"
    }],
    EventPattern: '{
      "event_type": ["com.amazon.rum.performance_navigation_event"],
      "metadata": {
        "browserName": [ "Chrome", "Safari" ],
        "countryCode": [ "US" ]
      },
      "event_details": {
        "duration": [{
          "numeric": [ ">=", 2000, "<", 8000 ]
        }]
      }
    }',
    UnitLabel: 'Count'
  }
}
```

## See Also
<a name="API_BatchCreateRumMetricDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/BatchCreateRumMetricDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/BatchCreateRumMetricDefinitions)
