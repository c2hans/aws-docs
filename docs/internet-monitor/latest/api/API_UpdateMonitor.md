---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_UpdateMonitor.html
---

# UpdateMonitor
<a name="API_UpdateMonitor"></a>

Updates a monitor. You can update a monitor to change the percentage of traffic to monitor or the maximum number of city-networks (locations and ASNs), to add or remove resources, or to change the status of the monitor. Note that you can't change the name of a monitor.

The city-network maximum that you choose is the limit, but you only pay for the number of city-networks that are actually monitored. For more information, see [Choosing a city-network maximum value](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the *Amazon CloudWatch User Guide*.

## Request Syntax
<a name="API_UpdateMonitor_RequestSyntax"></a>

```
PATCH /v20210603/Monitors/{{MonitorName}} HTTP/1.1
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
   "ResourcesToAdd": [ "{{string}}" ],
   "ResourcesToRemove": [ "{{string}}" ],
   "Status": "{{string}}",
   "TrafficPercentageToMonitor": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MonitorName](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-uri-MonitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_UpdateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-ClientToken"></a>
A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. You should not reuse the same client token for other API requests.
Type: String
Required: No

 ** [HealthEventsConfig](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-HealthEventsConfig"></a>
The list of health score thresholds. A threshold percentage for health scores, along with other configuration information, determines when Internet Monitor creates a health event when there's an internet issue that affects your application end users.
For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: [HealthEventsConfig](API_HealthEventsConfig.md) object
Required: No

 ** [InternetMeasurementsLogDelivery](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-InternetMeasurementsLogDelivery"></a>
Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.
Type: [InternetMeasurementsLogDelivery](API_InternetMeasurementsLogDelivery.md) object
Required: No

 ** [MaxCityNetworksToMonitor](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-MaxCityNetworksToMonitor"></a>
The maximum number of city-networks to monitor for your application. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500000.
Required: No

 ** [ResourcesToAdd](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-ResourcesToAdd"></a>
The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.
You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.
If you add only Amazon Virtual Private Clouds resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [ResourcesToRemove](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-ResourcesToRemove"></a>
The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [Status](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-Status"></a>
The status for a monitor. The accepted values for `Status` with the `UpdateMonitor` API call are the following: `ACTIVE` and `INACTIVE`. The following values are *not* accepted: `PENDING`, and `ERROR`.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR`
Required: No

 ** [TrafficPercentageToMonitor](#API_UpdateMonitor_RequestSyntax) **   <a name="internetmonitor-UpdateMonitor-request-TrafficPercentageToMonitor"></a>
The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.
To learn more, see [Choosing an application traffic percentage to monitor ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_UpdateMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MonitorArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitorArn](#API_UpdateMonitor_ResponseSyntax) **   <a name="internetmonitor-UpdateMonitor-response-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [Status](#API_UpdateMonitor_ResponseSyntax) **   <a name="internetmonitor-UpdateMonitor-response-Status"></a>
The status of a monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR`

## Errors
<a name="API_UpdateMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
The request exceeded a service quota.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The request specifies a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/UpdateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/UpdateMonitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
