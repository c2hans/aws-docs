---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CreatePracticeRunConfiguration.html
---

# CreatePracticeRunConfiguration
<a name="API_CreatePracticeRunConfiguration"></a>

A practice run configuration for zonal autoshift is required when you enable zonal autoshift. A practice run configuration includes specifications for blocked dates and blocked time windows, and for Amazon CloudWatch alarms that you create to use with practice runs. The alarms that you specify are an *outcome alarm*, to monitor application health during practice runs and, optionally, a *blocking alarm*, to block practice runs from starting.

When a resource has a practice run configuration, ARC starts zonal shifts for the resource weekly, to shift traffic for practice runs. Practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.

For more information, see [ Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Application Recovery Controller Developer Guide.

## Request Syntax
<a name="API_CreatePracticeRunConfiguration_RequestSyntax"></a>

```
POST /configuration HTTP/1.1
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
   ],
   "resourceIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePracticeRunConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePracticeRunConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedWindows](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-allowedWindows"></a>
Optionally, you can allow ARC to start practice runs for specific windows of days and times.
The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.
For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: `Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00`.
The `allowedWindows` have to start and end on the same day. Windows that span multiple days aren't supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** [blockedDates](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-blockedDates"></a>
Optionally, you can block ARC from starting practice runs for a resource on specific calendar dates.
The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.
For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 10.
Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}`
Required: No

 ** [blockedWindows](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-blockedWindows"></a>
Optionally, you can block ARC from starting practice runs for specific windows of days and times.
The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.
For example, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example: `Mon:00:00-Mon:10:00 Wed-20:30-Wed:21:30 Fri-20:30-Fri:21:30`.
The `blockedWindows` have to start and end on the same day. Windows that span multiple days aren't supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** [blockingAlarms](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-blockingAlarms"></a>
 *Blocking alarms* for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an `ALARM` state.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [outcomeAlarms](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-outcomeAlarms"></a>
 *Outcome alarms* for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an `ALARM` state.
Configure one or more of these alarms to monitor the health of your application when traffic is shifted away from an Availability Zone during each practice run. You should configure these alarms to go into an `ALARM` state if you want to stop a zonal shift, to let traffic for the resource return to the original Availability Zone.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [resourceIdentifier](#API_CreatePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-request-resourceIdentifier"></a>
The identifier of the resource that AWS shifts traffic for with a practice run zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.
Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:
+  [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html)
+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html)
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_CreatePracticeRunConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreatePracticeRunConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource that you configured the practice run for.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `arn:.*`

 ** [name](#API_CreatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-response-name"></a>
The name of the resource that you configured the practice run for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [practiceRunConfiguration](#API_CreatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-response-practiceRunConfiguration"></a>
A practice run configuration for a resource. Configurations include the outcome alarm that you specify for practice runs, and, optionally, a blocking alarm and blocking dates and windows.
Type: [PracticeRunConfiguration](API_PracticeRunConfiguration.md) object

 ** [zonalAutoshiftStatus](#API_CreatePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-CreatePracticeRunConfiguration-response-zonalAutoshiftStatus"></a>
The status for zonal autoshift for a resource. When you specify `ENABLED` for the autoshift status, AWS shifts traffic away from shifts away application resource traffic from an Availability Zone, on your behalf, when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers.
When you enable zonal autoshift, you must also configure practice runs for the resource.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_CreatePracticeRunConfiguration_Errors"></a>

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
<a name="API_CreatePracticeRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
