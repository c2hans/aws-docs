---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetRotation.html
---

# GetRotation
<a name="API_SSMContacts_GetRotation"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves information about an on-call rotation.

## Request Syntax
<a name="API_SSMContacts_GetRotation_RequestSyntax"></a>

```
{
   "RotationId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_GetRotation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RotationId](#API_SSMContacts_GetRotation_RequestSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-request-RotationId"></a>
The Amazon Resource Name (ARN) of the on-call rotation to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_GetRotation_ResponseSyntax"></a>

```
{
   "ContactIds": [ "string" ],
   "Name": "string",
   "Recurrence": {
      "DailySettings": [
         {
            "HourOfDay": number,
            "MinuteOfHour": number
         }
      ],
      "MonthlySettings": [
         {
            "DayOfMonth": number,
            "HandOffTime": {
               "HourOfDay": number,
               "MinuteOfHour": number
            }
         }
      ],
      "NumberOfOnCalls": number,
      "RecurrenceMultiplier": number,
      "ShiftCoverages": {
         "string" : [
            {
               "End": {
                  "HourOfDay": number,
                  "MinuteOfHour": number
               },
               "Start": {
                  "HourOfDay": number,
                  "MinuteOfHour": number
               }
            }
         ]
      },
      "WeeklySettings": [
         {
            "DayOfWeek": "string",
            "HandOffTime": {
               "HourOfDay": number,
               "MinuteOfHour": number
            }
         }
      ]
   },
   "RotationArn": "string",
   "StartTime": number,
   "TimeZoneId": "string"
}
```

## Response Elements
<a name="API_SSMContacts_GetRotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactIds](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-ContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts assigned to the on-call rotation team.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [Name](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-Name"></a>
The name of the on-call rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\s\.]*$`

 ** [Recurrence](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-Recurrence"></a>
Specifies how long a rotation lasts before restarting at the beginning of the shift order.
Type: [RecurrenceSettings](API_SSMContacts_RecurrenceSettings.md) object

 ** [RotationArn](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-RotationArn"></a>
The Amazon Resource Name (ARN) of the on-call rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [StartTime](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-StartTime"></a>
The specified start time for the on-call rotation.
Type: Timestamp

 ** [TimeZoneId](#API_SSMContacts_GetRotation_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotation-response-TimeZoneId"></a>
The time zone that the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[:a-zA-Z0-9_\-\s\.\\/]*$`

## Errors
<a name="API_SSMContacts_GetRotation_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SSMContacts_GetRotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/GetRotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/GetRotation)
