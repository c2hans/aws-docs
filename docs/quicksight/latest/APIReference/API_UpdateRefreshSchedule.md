---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateRefreshSchedule.html
---

# UpdateRefreshSchedule
<a name="API_UpdateRefreshSchedule"></a>

Updates a refresh schedule for a dataset.

## Request Syntax
<a name="API_UpdateRefreshSchedule_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/refresh-schedules HTTP/1.1
Content-type: application/json

{
   "Schedule": {
      "Arn": "{{string}}",
      "RefreshType": "{{string}}",
      "ScheduleFrequency": {
         "Interval": "{{string}}",
         "RefreshOnDay": {
            "DayOfMonth": "{{string}}",
            "DayOfWeek": "{{string}}"
         },
         "TimeOfTheDay": "{{string}}",
         "Timezone": "{{string}}"
      },
      "ScheduleId": "{{string}}",
      "StartAfterDateTime": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateRefreshSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateRefreshSchedule-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DataSetId](#API_UpdateRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateRefreshSchedule-request-uri-DataSetId"></a>
The ID of the dataset.
Required: Yes

## Request Body
<a name="API_UpdateRefreshSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Schedule](#API_UpdateRefreshSchedule_RequestSyntax) **   <a name="QS-UpdateRefreshSchedule-request-Schedule"></a>
The refresh schedule.
Type: [RefreshSchedule](API_RefreshSchedule.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateRefreshSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "ScheduleId": "string"
}
```

## Response Elements
<a name="API_UpdateRefreshSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateRefreshSchedule-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateRefreshSchedule-response-Arn"></a>
The Amazon Resource Name (ARN) for the refresh schedule.
Type: String

 ** [RequestId](#API_UpdateRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateRefreshSchedule-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [ScheduleId](#API_UpdateRefreshSchedule_ResponseSyntax) **   <a name="QS-UpdateRefreshSchedule-response-ScheduleId"></a>
The ID of the refresh schedule.
Type: String

## Errors
<a name="API_UpdateRefreshSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_UpdateRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateRefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateRefreshSchedule)
