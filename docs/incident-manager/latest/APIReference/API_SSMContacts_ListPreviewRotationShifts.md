---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPreviewRotationShifts.html
---

# ListPreviewRotationShifts
<a name="API_SSMContacts_ListPreviewRotationShifts"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Returns a list of shifts based on rotation configuration parameters.

**Note**
The Incident Manager primarily uses this operation to populate the **Preview** calendar. It is not typically run by end users.

## Request Syntax
<a name="API_SSMContacts_ListPreviewRotationShifts_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "MaxResults": {{number}},
   "Members": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "Overrides": [
      {
         "EndTime": {{number}},
         "NewMembers": [ "{{string}}" ],
         "StartTime": {{number}}
      }
   ],
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
   "RotationStartTime": {{number}},
   "StartTime": {{number}},
   "TimeZoneId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListPreviewRotationShifts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-EndTime"></a>
The date and time a rotation shift would end.
Type: Timestamp
Required: Yes

 ** [MaxResults](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that can be specified in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [Members](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-Members"></a>
The contacts that would be assigned to a rotation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: Yes

 ** [NextToken](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-NextToken"></a>
A token to start the list. This token is used to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [Overrides](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-Overrides"></a>
Information about changes that would be made in a rotation override.
Type: Array of [PreviewOverride](API_SSMContacts_PreviewOverride.md) objects
Required: No

 ** [Recurrence](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-Recurrence"></a>
Information about how long a rotation would last before restarting at the beginning of the shift order.
Type: [RecurrenceSettings](API_SSMContacts_RecurrenceSettings.md) object
Required: Yes

 ** [RotationStartTime](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-RotationStartTime"></a>
The date and time a rotation would begin. The first shift is calculated from this date and time.
Type: Timestamp
Required: No

 ** [StartTime](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-StartTime"></a>
Used to filter the range of calculated shifts before sending the response back to the user.
Type: Timestamp
Required: No

 ** [TimeZoneId](#API_SSMContacts_ListPreviewRotationShifts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-request-TimeZoneId"></a>
The time zone the rotation’s activity would be based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_ListPreviewRotationShifts_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RotationShifts": [
      {
         "ContactIds": [ "string" ],
         "EndTime": number,
         "ShiftDetails": {
            "OverriddenContactIds": [ "string" ]
         },
         "StartTime": number,
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListPreviewRotationShifts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListPreviewRotationShifts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-response-NextToken"></a>
The token for the next set of items to return. This token is used to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [RotationShifts](#API_SSMContacts_ListPreviewRotationShifts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPreviewRotationShifts-response-RotationShifts"></a>
Details about a rotation shift, including times, types, and contacts.
Type: Array of [RotationShift](API_SSMContacts_RotationShift.md) objects

## Errors
<a name="API_SSMContacts_ListPreviewRotationShifts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SSMContacts_ListPreviewRotationShifts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListPreviewRotationShifts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListPreviewRotationShifts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
