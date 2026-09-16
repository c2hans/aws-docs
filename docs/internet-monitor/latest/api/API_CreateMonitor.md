---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_CreateMonitor.html
---

# CreateMonitor
<a name="API_CreateMonitor"></a>

Creates a monitor in Internet Monitor. A monitor is built based on information from the application resources that you add: VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, and Amazon WorkSpaces directories. Internet Monitor then publishes internet measurements from AWS that are specific to the *city-networks*. That is, the locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see [Using Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) in the *Amazon CloudWatch User Guide*.

When you create a monitor, you choose the percentage of traffic that you want to monitor. You can also set a maximum limit for the number of city-networks where client traffic is monitored, that caps the total traffic that Internet Monitor monitors. A city-network maximum is the limit of city-networks, but you only pay for the number of city-networks that are actually monitored. You can update your monitor at any time to change the percentage of traffic to monitor or the city-networks maximum. For more information, see [Choosing a city-network maximum value](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the *Amazon CloudWatch User Guide*.

## Request Syntax
<a name="API_CreateMonitor_RequestSyntax"></a>

```
POST /v20210603/Monitors HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "HealthEventsConfig": {
      "AvailabilityLocalHealthEventsConfig": {
         "HealthScoreThreshold": {{number}},
         "MinTrafficImpact": {{number}},
         "Status": "{{string}}"
      },
      "AvailabilityScoreThreshold": {{number}},
      "PerformanceLocalHealthEventsConfig": {
         "HealthScoreThreshold": {{number}},
         "MinTrafficImpact": {{number}},
         "Status": "{{string}}"
      },
      "PerformanceScoreThreshold": {{number}}
   },
   "InternetMeasurementsLogDelivery": {
      "S3Config": {
         "BucketName": "{{string}}",
         "BucketPrefix": "{{string}}",
         "LogDeliveryStatus": "{{string}}"
      }
   },
   "MaxCityNetworksToMonitor": {{number}},
   "MonitorName": "{{string}}",
   "Resources": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TrafficPercentageToMonitor": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateMonitor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-ClientToken"></a>
A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.
Type: String
Required: No

 ** [HealthEventsConfig](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-HealthEventsConfig"></a>
Defines the threshold percentages and other configuration information for when Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.
If you don't set a health event threshold, the default value is 95%.
For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: [HealthEventsConfig](API_HealthEventsConfig.md) object
Required: No

 ** [InternetMeasurementsLogDelivery](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-InternetMeasurementsLogDelivery"></a>
Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.
Type: [InternetMeasurementsLogDelivery](API_InternetMeasurementsLogDelivery.md) object
Required: No

 ** [MaxCityNetworksToMonitor](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-MaxCityNetworksToMonitor"></a>
The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.
To learn more, see [Choosing a city-network maximum value ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500000.
Required: No

 ** [MonitorName](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-MonitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Resources](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-Resources"></a>
The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.
You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.
If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [Tags](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-Tags"></a>
The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [TrafficPercentageToMonitor](#API_CreateMonitor_RequestSyntax) **   <a name="internetmonitor-CreateMonitor-request-TrafficPercentageToMonitor"></a>
The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.
To learn more, see [Choosing an application traffic percentage to monitor ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_CreateMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateMonitor_ResponseSyntax) **   <a name="internetmonitor-CreateMonitor-response-Arn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [Status](#API_CreateMonitor_ResponseSyntax) **   <a name="internetmonitor-CreateMonitor-response-Status"></a>
The status of a monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR`

## Errors
<a name="API_CreateMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested resource is in use.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
The request exceeded a service quota.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_CreateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/CreateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/CreateMonitor)
