---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateRotation.html
---

# UpdateRotation
<a name="API_SSMContacts_UpdateRotation"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Updates the information specified for an on-call rotation.

## Request Syntax
<a name="API_SSMContacts_UpdateRotation_RequestSyntax"></a>

```
{
   "ContactIds": [ "{{string}}" ],
   "Recurrence": {
      "DailySettings": [
         {
            "HourOfDay": {{number}},
            "MinuteOfHour": {{number}}
         }
      ],
      "MonthlySettings": [
         {
            "DayOfMonth": {{number}},
            "HandOffTime": {
               "HourOfDay": {{number}},
               "MinuteOfHour": {{number}}
            }
         }
      ],
      "NumberOfOnCalls": {{number}},
      "RecurrenceMultiplier": {{number}},
      "ShiftCoverages": {
         "{{string}}" : [
            {
               "End": {
                  "HourOfDay": {{number}},
                  "MinuteOfHour": {{number}}
               },
               "Start": {
                  "HourOfDay": {{number}},
                  "MinuteOfHour": {{number}}
               }
            }
         ]
      },
      "WeeklySettings": [
         {
            "DayOfWeek": "{{string}}",
            "HandOffTime": {
               "HourOfDay": {{number}},
               "MinuteOfHour": {{number}}
            }
         }
      ]
   },
   "RotationId": "{{string}}",
   "StartTime": {{number}},
   "TimeZoneId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_UpdateRotation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactIds](#API_SSMContacts_UpdateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateRotation-request-ContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts to include in the updated rotation.
Only the `PERSONAL` contact type is supported. The contact types `ESCALATION` and `ONCALL_SCHEDULE` are not supported for this operation.
The order in which you list the contacts is their shift order in the rotation schedule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

 ** [Recurrence](#API_SSMContacts_UpdateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateRotation-request-Recurrence"></a>
Information about how long the updated rotation lasts before restarting at the beginning of the shift order.
Type: [RecurrenceSettings](API_SSMContacts_RecurrenceSettings.md) object
Required: Yes

 ** [RotationId](#API_SSMContacts_UpdateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateRotation-request-RotationId"></a>
The Amazon Resource Name (ARN) of the rotation to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [StartTime](#API_SSMContacts_UpdateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateRotation-request-StartTime"></a>
The date and time the rotation goes into effect.
Type: Timestamp
Required: No

 ** [TimeZoneId](#API_SSMContacts_UpdateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateRotation-request-TimeZoneId"></a>
The time zone to base the updated rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Designators for time zones that don’t support Daylight Savings Time Rules, such as Pacific Standard Time (PST), aren't supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
Required: No

## Response Elements
<a name="API_SSMContacts_UpdateRotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_UpdateRotation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SSMContacts_UpdateRotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/UpdateRotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/UpdateRotation)
