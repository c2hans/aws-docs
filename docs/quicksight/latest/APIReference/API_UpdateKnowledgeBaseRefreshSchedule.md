---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKnowledgeBaseRefreshSchedule.html
---

# UpdateKnowledgeBaseRefreshSchedule

Updates the refresh schedule for an Amazon Quick Sight knowledge base. Use this operation to change how often the knowledge base refreshes, or to enable or disable the schedule. Specify the schedule by its `ScheduleId`. The operation changes only the fields that you provide. Any field that you omit keeps its existing value.

## Request Syntax
<a name="API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax"></a>

```
PUT /v1/accounts/{{AwsAccountId}}/knowledge-bases/{{KnowledgeBaseId}}/kb-refresh-schedules/{{ScheduleId}} HTTP/1.1
Content-type: application/json

{
   "ScheduleFrequency": {
      "Interval": "{{string}}",
      "RefreshOnDay": {
         "DayOfMonth": "{{string}}",
         "DayOfWeek": "{{string}}"
      }
   },
   "StartTime": {{number}},
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateKnowledgeBaseRefreshSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

 ** [KnowledgeBaseId](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-uri-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** [ScheduleId](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-uri-ScheduleId"></a>
The unique identifier for the refresh schedule to update.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z_=-][0-9a-zA-Z_=.-]*`
Required: Yes

## Request Body
<a name="API_UpdateKnowledgeBaseRefreshSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ScheduleFrequency](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-ScheduleFrequency"></a>
The frequency configuration for the refresh schedule. The frequency configuration specifies how often the schedule runs and, for weekly or monthly schedules, the day on which it runs. If you don't specify this parameter, the schedule keeps its existing frequency.
Type: [KnowledgeBaseRefreshFrequency](API_KnowledgeBaseRefreshFrequency.md) object
Required: No

 ** [StartTime](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-StartTime"></a>
The date and time, in ISO 8601 format, after which the schedule can start refreshing the knowledge base. The first refresh runs at the next scheduled time after this date and time. If you don't specify this parameter, the schedule keeps its existing start time.
Type: Timestamp
Required: No

 ** [State](#API_UpdateKnowledgeBaseRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-request-State"></a>
The state of the refresh schedule. A schedule that isn't `ENABLED` doesn't run refreshes. If you don't specify this parameter, the schedule keeps its existing state.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateKnowledgeBaseRefreshSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "KnowledgeBaseArn": "string",
   "RequestId": "string",
   "ScheduleId": "string"
}
```

## Response Elements
<a name="API_UpdateKnowledgeBaseRefreshSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [KnowledgeBaseArn](#API_UpdateKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-response-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base that the schedule applies to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ScheduleId](#API_UpdateKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-response-ScheduleId"></a>
The unique identifier for the refresh schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z_=-][0-9a-zA-Z_=.-]*`

 ** [RequestId](#API_UpdateKnowledgeBaseRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBaseRefreshSchedule-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateKnowledgeBaseRefreshSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateKnowledgeBaseRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateKnowledgeBaseRefreshSchedule)
