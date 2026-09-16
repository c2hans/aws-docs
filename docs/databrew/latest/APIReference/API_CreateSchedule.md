---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateSchedule.html
---

# CreateSchedule
<a name="API_CreateSchedule"></a>

Creates a new schedule for one or more DataBrew jobs. Jobs can be run at a specific date and time, or at regular intervals.

## Request Syntax
<a name="API_CreateSchedule_RequestSyntax"></a>

```
POST /schedules HTTP/1.1
Content-type: application/json

{
   "CronExpression": "{{string}}",
   "JobNames": [ "{{string}}" ],
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSchedule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CronExpression](#API_CreateSchedule_RequestSyntax) **   <a name="databrew-CreateSchedule-request-CronExpression"></a>
The date or dates and time or times when the jobs are to be run. For more information, see [Cron expressions](https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html) in the * AWS Glue DataBrew Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [Name](#API_CreateSchedule_RequestSyntax) **   <a name="databrew-CreateSchedule-request-Name"></a>
A unique name for the schedule. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [JobNames](#API_CreateSchedule_RequestSyntax) **   <a name="databrew-CreateSchedule-request-JobNames"></a>
The name or names of one or more jobs to be run.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: No

 ** [Tags](#API_CreateSchedule_RequestSyntax) **   <a name="databrew-CreateSchedule-request-Tags"></a>
Metadata tags to apply to this schedule.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateSchedule_ResponseSyntax) **   <a name="databrew-CreateSchedule-response-Name"></a>
The name of the schedule that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateSchedule)
