---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateScheduledAudit.html
---

# UpdateScheduledAudit
<a name="API_UpdateScheduledAudit"></a>

Updates a scheduled audit, including which checks are performed and how often the audit takes place.

Requires permission to access the [UpdateScheduledAudit](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateScheduledAudit_RequestSyntax"></a>

```
PATCH /audit/scheduledaudits/{{scheduledAuditName}} HTTP/1.1
Content-type: application/json

{
   "dayOfMonth": "{{string}}",
   "dayOfWeek": "{{string}}",
   "frequency": "{{string}}",
   "targetCheckNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateScheduledAudit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scheduledAuditName](#API_UpdateScheduledAudit_RequestSyntax) **   <a name="iot-UpdateScheduledAudit-request-uri-scheduledAuditName"></a>
The name of the scheduled audit. (Max. 128 chars)
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_UpdateScheduledAudit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dayOfMonth](#API_UpdateScheduledAudit_RequestSyntax) **   <a name="iot-UpdateScheduledAudit-request-dayOfMonth"></a>
The day of the month on which the scheduled audit takes place. This can be `1` through `31` or `LAST`. This field is required if the `frequency` parameter is set to `MONTHLY`. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
Type: String
Pattern: `^([1-9]|[12][0-9]|3[01])$|^LAST$`
Required: No

 ** [dayOfWeek](#API_UpdateScheduledAudit_RequestSyntax) **   <a name="iot-UpdateScheduledAudit-request-dayOfWeek"></a>
The day of the week on which the scheduled audit takes place. This can be one of `SUN`, `MON`, `TUE`, `WED`, `THU`, `FRI`, or `SAT`. This field is required if the "frequency" parameter is set to `WEEKLY` or `BIWEEKLY`.
Type: String
Valid Values: `SUN | MON | TUE | WED | THU | FRI | SAT`
Required: No

 ** [frequency](#API_UpdateScheduledAudit_RequestSyntax) **   <a name="iot-UpdateScheduledAudit-request-frequency"></a>
How often the scheduled audit takes place, either `DAILY`, `WEEKLY`, `BIWEEKLY`, or `MONTHLY`. The start time of each audit is determined by the system.
Type: String
Valid Values: `DAILY | WEEKLY | BIWEEKLY | MONTHLY`
Required: No

 ** [targetCheckNames](#API_UpdateScheduledAudit_RequestSyntax) **   <a name="iot-UpdateScheduledAudit-request-targetCheckNames"></a>
Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateScheduledAudit_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scheduledAuditArn": "string"
}
```

## Response Elements
<a name="API_UpdateScheduledAudit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledAuditArn](#API_UpdateScheduledAudit_ResponseSyntax) **   <a name="iot-UpdateScheduledAudit-response-scheduledAuditArn"></a>
The ARN of the scheduled audit.
Type: String

## Errors
<a name="API_UpdateScheduledAudit_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateScheduledAudit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateScheduledAudit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateScheduledAudit)
