---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateScheduledAudit.html
---

# CreateScheduledAudit
<a name="API_CreateScheduledAudit"></a>

Creates a scheduled audit that is run at a specified time interval.

Requires permission to access the [CreateScheduledAudit](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateScheduledAudit_RequestSyntax"></a>

```
POST /audit/scheduledaudits/{{scheduledAuditName}} HTTP/1.1
Content-type: application/json

{
   "dayOfMonth": "{{string}}",
   "dayOfWeek": "{{string}}",
   "frequency": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "targetCheckNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateScheduledAudit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scheduledAuditName](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-uri-scheduledAuditName"></a>
The name you want to give to the scheduled audit. (Max. 128 chars)
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateScheduledAudit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dayOfMonth](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-dayOfMonth"></a>
The day of the month on which the scheduled audit takes place. This can be "1" through "31" or "LAST". This field is required if the "frequency" parameter is set to `MONTHLY`. If days 29 to 31 are specified, and the month doesn't have that many days, the audit takes place on the `LAST` day of the month.
Type: String
Pattern: `^([1-9]|[12][0-9]|3[01])$|^LAST$`
Required: No

 ** [dayOfWeek](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-dayOfWeek"></a>
The day of the week on which the scheduled audit takes place, either `SUN`, `MON`, `TUE`, `WED`, `THU`, `FRI`, or `SAT`. This field is required if the `frequency` parameter is set to `WEEKLY` or `BIWEEKLY`.
Type: String
Valid Values: `SUN | MON | TUE | WED | THU | FRI | SAT`
Required: No

 ** [frequency](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-frequency"></a>
How often the scheduled audit takes place, either `DAILY`, `WEEKLY`, `BIWEEKLY` or `MONTHLY`. The start time of each audit is determined by the system.
Type: String
Valid Values: `DAILY | WEEKLY | BIWEEKLY | MONTHLY`
Required: Yes

 ** [tags](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-tags"></a>
Metadata that can be used to manage the scheduled audit.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [targetCheckNames](#API_CreateScheduledAudit_RequestSyntax) **   <a name="iot-CreateScheduledAudit-request-targetCheckNames"></a>
Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_CreateScheduledAudit_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scheduledAuditArn": "string"
}
```

## Response Elements
<a name="API_CreateScheduledAudit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledAuditArn](#API_CreateScheduledAudit_ResponseSyntax) **   <a name="iot-CreateScheduledAudit-response-scheduledAuditArn"></a>
The ARN of the scheduled audit.
Type: String

## Errors
<a name="API_CreateScheduledAudit_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduledAudit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateScheduledAudit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateScheduledAudit)
