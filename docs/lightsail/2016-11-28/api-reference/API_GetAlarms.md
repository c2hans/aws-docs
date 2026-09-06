---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetAlarms.html
---

# GetAlarms
<a name="API_GetAlarms"></a>

Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about all alarms for a specific resource.

An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms).

## Request Syntax
<a name="API_GetAlarms_RequestSyntax"></a>

```
{
   "alarmName": "{{string}}",
   "monitoredResourceName": "{{string}}",
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAlarms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [alarmName](#API_GetAlarms_RequestSyntax) **   <a name="Lightsail-GetAlarms-request-alarmName"></a>
The name of the alarm.
Specify an alarm name to return information about a specific alarm.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [monitoredResourceName](#API_GetAlarms_RequestSyntax) **   <a name="Lightsail-GetAlarms-request-monitoredResourceName"></a>
The name of the Lightsail resource being monitored by the alarm.
Specify a monitored resource name to return information about all alarms for a specific resource.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [pageToken](#API_GetAlarms_RequestSyntax) **   <a name="Lightsail-GetAlarms-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetAlarms` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetAlarms_ResponseSyntax"></a>

```
{
   "alarms": [
      {
         "arn": "string",
         "comparisonOperator": "string",
         "contactProtocols": [ "string" ],
         "createdAt": number,
         "datapointsToAlarm": number,
         "evaluationPeriods": number,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "metricName": "string",
         "monitoredResourceInfo": {
            "arn": "string",
            "name": "string",
            "resourceType": "string"
         },
         "name": "string",
         "notificationEnabled": boolean,
         "notificationTriggers": [ "string" ],
         "period": number,
         "resourceType": "string",
         "state": "string",
         "statistic": "string",
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "threshold": number,
         "treatMissingData": "string",
         "unit": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetAlarms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alarms](#API_GetAlarms_ResponseSyntax) **   <a name="Lightsail-GetAlarms-response-alarms"></a>
An array of objects that describe the alarms.
Type: Array of [Alarm](API_Alarm.md) objects

 ** [nextPageToken](#API_GetAlarms_ResponseSyntax) **   <a name="Lightsail-GetAlarms-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetAlarms` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetAlarms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetAlarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetAlarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetAlarms)
