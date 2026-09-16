---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DescribeSchedule.html
---

# DescribeSchedule
<a name="API_DescribeSchedule"></a>

Returns the definition of a specific DataBrew schedule.

## Request Syntax
<a name="API_DescribeSchedule_RequestSyntax"></a>

```
GET /schedules/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeSchedule_RequestSyntax) **   <a name="databrew-DescribeSchedule-request-uri-Name"></a>
The name of the schedule to be described.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_DescribeSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": number,
   "CreatedBy": "string",
   "CronExpression": "string",
   "JobNames": [ "string" ],
   "LastModifiedBy": "string",
   "LastModifiedDate": number,
   "Name": "string",
   "ResourceArn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-Name"></a>
The name of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreateDate](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-CreateDate"></a>
The date and time that the schedule was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-CreatedBy"></a>
The identifier (user name) of the user who created the schedule.
Type: String

 ** [CronExpression](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-CronExpression"></a>
The date or dates and time or times when the jobs are to be run for the schedule. For more information, see [Cron expressions](https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html) in the * AWS Glue DataBrew Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [JobNames](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-JobNames"></a>
The name or names of one or more jobs to be run by using the schedule.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 240.

 ** [LastModifiedBy](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-LastModifiedBy"></a>
The identifier (user name) of the user who last modified the schedule.
Type: String

 ** [LastModifiedDate](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-LastModifiedDate"></a>
The date and time that the schedule was last modified.
Type: Timestamp

 ** [ResourceArn](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the schedule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Tags](#API_DescribeSchedule_ResponseSyntax) **   <a name="databrew-DescribeSchedule-response-Tags"></a>
Metadata tags associated with this schedule.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DescribeSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DescribeSchedule)
