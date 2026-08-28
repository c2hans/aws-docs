---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListRotations.html
---

# ListRotations
<a name="API_SSMContacts_ListRotations"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves a list of on-call rotations.

## Request Syntax
<a name="API_SSMContacts_ListRotations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RotationNamePrefix": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListRotations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_SSMContacts_ListRotations_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotations-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListRotations_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotations-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [RotationNamePrefix](#API_SSMContacts_ListRotations_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotations-request-RotationNamePrefix"></a>
A filter to include rotations in list results based on their common prefix. For example, entering prod returns a list of all rotation names that begin with `prod`, such as `production` and `prod-1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\s\.]*$`
Required: No

## Response Syntax
<a name="API_SSMContacts_ListRotations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Rotations": [
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
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListRotations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListRotations_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListRotations-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [Rotations](#API_SSMContacts_ListRotations_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListRotations-response-Rotations"></a>
Information about rotations that meet the filter criteria.
Type: Array of [Rotation](API_SSMContacts_Rotation.md) objects

## Errors
<a name="API_SSMContacts_ListRotations_Errors"></a>

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
<a name="API_SSMContacts_ListRotations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListRotations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListRotations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
