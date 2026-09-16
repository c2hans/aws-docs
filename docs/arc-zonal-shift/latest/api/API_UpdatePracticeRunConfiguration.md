---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdatePracticeRunConfiguration.html
---

# UpdatePracticeRunConfiguration
<a name="API_UpdatePracticeRunConfiguration"></a>

Update a practice run configuration to change one or more of the following: add, change, or remove the blocking alarm; change the outcome alarm; or add, change, or remove blocking dates or time windows.

## Request Syntax
<a name="API_UpdatePracticeRunConfiguration_RequestSyntax"></a>

```
PATCH /configuration/{{resourceIdentifier}} HTTP/1.1
Content-type: application/json

{
   "allowedWindows": [ "{{string}}" ],
   "blockedDates": [ "{{string}}" ],
   "blockedWindows": [ "{{string}}" ],
   "blockingAlarms": [
      {
         "alarmIdentifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "outcomeAlarms": [
      {
         "alarmIdentifier": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdatePracticeRunConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-uri-resourceIdentifier"></a>
The identifier for the resource that you want to update the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Request Body
<a name="API_UpdatePracticeRunConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedWindows](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-allowedWindows"></a>
Add, change, or remove windows of days and times for when you can, optionally, allow ARC to start a practice run for a resource.
The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.
For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: `Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00`.
The `allowedWindows` have to start and end on the same day. Windows that span multiple days aren't supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** [blockedDates](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-blockedDates"></a>
Add, change, or remove blocked dates for a practice run in zonal autoshift.
Optionally, you can block practice runs for specific calendar dates. The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.
For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 10.
Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}`
Required: No

 ** [blockedWindows](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-blockedWindows"></a>
Add, change, or remove windows of days and times for when you can, optionally, block ARC from starting a practice run for a resource.
The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.
For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** [blockingAlarms](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-blockingAlarms"></a>
Add, change, or remove the Amazon CloudWatch alarms that you optionally specify as the blocking alarms for practice runs.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [outcomeAlarms](#API_UpdatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-request-outcomeAlarms"></a>
Specify one or more Amazon CloudWatch alarms as the outcome alarms for practice runs.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_UpdatePracticeRunConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "name": "string",
   "practiceRunConfiguration": {
      "allowedWindows": [ "string" ],
      "blockedDates": [ "string" ],
      "blockedWindows": [ "string" ],
      "blockingAlarms": [
         {
            "alarmIdentifier": "string",
            "type": "string"
         }
      ],
      "outcomeAlarms": [
         {
            "alarmIdentifier": "string",
            "type": "string"
         }
      ]
   },
   "zonalAutoshiftStatus": "string"
}
```

## Response Elements
<a name="API_UpdatePracticeRunConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource that you updated the practice run for.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `arn:.*`

 ** [name](#API_UpdatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-response-name"></a>
The name of the resource that you updated the practice run for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [practiceRunConfiguration](#API_UpdatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-response-practiceRunConfiguration"></a>
The practice run configuration that was updated.
Type: [PracticeRunConfiguration](API_PracticeRunConfiguration.md) object

 ** [zonalAutoshiftStatus](#API_UpdatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-UpdatePracticeRunConfiguration-response-zonalAutoshiftStatus"></a>
The zonal autoshift status for the resource that you updated the practice run for.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdatePracticeRunConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** reason **
The reason for the conflict exception.
 ** zonalShiftId **
The zonal shift ID associated with the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The input requested a resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePracticeRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)
