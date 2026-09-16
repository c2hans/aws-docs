---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateRotation.html
---

# CreateRotation
<a name="API_SSMContacts_CreateRotation"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Creates a rotation in an on-call schedule.

## Request Syntax
<a name="API_SSMContacts_CreateRotation_RequestSyntax"></a>

```
{
   "ContactIds": [ "{{string}}" ],
   "IdempotencyToken": "{{string}}",
   "Name": "{{string}}",
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
   "StartTime": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimeZoneId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_CreateRotation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactIds](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-ContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts to add to the rotation.
Only the `PERSONAL` contact type is supported. The contact types `ESCALATION` and `ONCALL_SCHEDULE` are not supported for this operation.
The order that you list the contacts in is their shift order in the rotation schedule. To change the order of the contact's shifts, use the [UpdateRotation](API_SSMContacts_UpdateRotation.md) operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [IdempotencyToken](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-IdempotencyToken"></a>
A token that ensures that the operation is called only once with the specified details.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [Name](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-Name"></a>
The name of the rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\s\.]*$`
Required: Yes

 ** [Recurrence](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-Recurrence"></a>
Information about the rule that specifies when a shift's team members rotate.
Type: [RecurrenceSettings](API_SSMContacts_RecurrenceSettings.md) object
Required: Yes

 ** [StartTime](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-StartTime"></a>
The date and time that the rotation goes into effect.
Type: Timestamp
Required: No

 ** [Tags](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-Tags"></a>
Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see [Tagging Incident Manager resources](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html) in the *Incident Manager User Guide*.
Type: Array of [Tag](API_SSMContacts_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TimeZoneId](#API_SSMContacts_CreateRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-request-TimeZoneId"></a>
The time zone to base the rotation’s activity on in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Designators for time zones that don’t support Daylight Savings Time rules, such as Pacific Standard Time (PST), are not supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_CreateRotation_ResponseSyntax"></a>

```
{
   "RotationArn": "string"
}
```

## Response Elements
<a name="API_SSMContacts_CreateRotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RotationArn](#API_SSMContacts_CreateRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotation-response-RotationArn"></a>
The Amazon Resource Name (ARN) of the created rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

## Errors
<a name="API_SSMContacts_CreateRotation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SSMContacts_CreateRotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/CreateRotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/CreateRotation)
