---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetMonitor.html
---

# GetMonitor
<a name="API_GetMonitor"></a>

Gets information about a monitor in Internet Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.

## Request Syntax
<a name="API_GetMonitor_RequestSyntax"></a>

```
GET /v20210603/Monitors/{{MonitorName}}?LinkedAccountId={{LinkedAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LinkedAccountId](#API_GetMonitor_RequestSyntax) **   <a name="internetmonitor-GetMonitor-request-uri-LinkedAccountId"></a>
The account ID for an account that you've set up cross-account sharing for in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Internet Monitor User Guide.
Length Constraints: Fixed length of 12.

 ** [MonitorName](#API_GetMonitor_RequestSyntax) **   <a name="internetmonitor-GetMonitor-request-uri-MonitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_GetMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": "string",
   "HealthEventsConfig": {
      "AvailabilityLocalHealthEventsConfig": {
         "HealthScoreThreshold": number,
         "MinTrafficImpact": number,
         "Status": "string"
      },
      "AvailabilityScoreThreshold": number,
      "PerformanceLocalHealthEventsConfig": {
         "HealthScoreThreshold": number,
         "MinTrafficImpact": number,
         "Status": "string"
      },
      "PerformanceScoreThreshold": number
   },
   "InternetMeasurementsLogDelivery": {
      "S3Config": {
         "BucketName": "string",
         "BucketPrefix": "string",
         "LogDeliveryStatus": "string"
      }
   },
   "MaxCityNetworksToMonitor": number,
   "ModifiedAt": "string",
   "MonitorArn": "string",
   "MonitorName": "string",
   "ProcessingStatus": "string",
   "ProcessingStatusInfo": "string",
   "Resources": [ "string" ],
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "TrafficPercentageToMonitor": number
}
```

## Response Elements
<a name="API_GetMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-CreatedAt"></a>
The time when the monitor was created.
Type: Timestamp

 ** [HealthEventsConfig](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-HealthEventsConfig"></a>
The list of health event threshold configurations. The threshold percentage for a health score determines, along with other configuration information, when Internet Monitor creates a health event when there's an internet issue that affects your application end users.
For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: [HealthEventsConfig](API_HealthEventsConfig.md) object

 ** [InternetMeasurementsLogDelivery](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-InternetMeasurementsLogDelivery"></a>
Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.
Type: [InternetMeasurementsLogDelivery](API_InternetMeasurementsLogDelivery.md) object

 ** [MaxCityNetworksToMonitor](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-MaxCityNetworksToMonitor"></a>
The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. This limit can help control billing costs.
To learn more, see [Choosing a city-network maximum value ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500000.

 ** [ModifiedAt](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-ModifiedAt"></a>
The last time that the monitor was modified.
Type: Timestamp

 ** [MonitorArn](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [MonitorName](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-MonitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ProcessingStatus](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-ProcessingStatus"></a>
The health of the data processing for the monitor.
Type: String
Valid Values: `OK | INACTIVE | COLLECTING_DATA | INSUFFICIENT_DATA | FAULT_SERVICE | FAULT_ACCESS_CLOUDWATCH`

 ** [ProcessingStatusInfo](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-ProcessingStatusInfo"></a>
Additional information about the health of the data processing for the monitor.
Type: String

 ** [Resources](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-Resources"></a>
The resources monitored by the monitor. Resources are listed by their Amazon Resource Names (ARNs).
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [Status](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-Status"></a>
The status of the monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR`

 ** [Tags](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-Tags"></a>
The tags that have been added to monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [TrafficPercentageToMonitor](#API_GetMonitor_ResponseSyntax) **   <a name="internetmonitor-GetMonitor-response-TrafficPercentageToMonitor"></a>
The percentage of the internet-facing traffic for your application to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.
To learn more, see [Choosing an application traffic percentage to monitor ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

## Errors
<a name="API_GetMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_GetMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/GetMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/GetMonitor)
