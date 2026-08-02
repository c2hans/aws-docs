---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateSchedule.html
---

# UpdateSchedule
<a name="API_UpdateSchedule"></a>

Modifies the definition of an existing DataBrew schedule.

## Request Syntax
<a name="API_UpdateSchedule_RequestSyntax"></a>

```
PUT /schedules/{{name}} HTTP/1.1
Content-type: application/json

{
   "CronExpression": "{{string}}",
   "JobNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateSchedule_RequestSyntax) **   <a name="databrew-UpdateSchedule-request-uri-Name"></a>
The name of the schedule to update.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_UpdateSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CronExpression](#API_UpdateSchedule_RequestSyntax) **   <a name="databrew-UpdateSchedule-request-CronExpression"></a>
The date or dates and time or times when the jobs are to be run. For more information, see [Cron expressions](https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html) in the * AWS Glue DataBrew Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [JobNames](#API_UpdateSchedule_RequestSyntax) **   <a name="databrew-UpdateSchedule-request-JobNames"></a>
The name or names of one or more jobs to be run for this schedule.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: No

## Response Syntax
<a name="API_UpdateSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateSchedule_ResponseSyntax) **   <a name="databrew-UpdateSchedule-response-Name"></a>
The name of the schedule that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_UpdateSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateSchedule)
