---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeScheduledAudit.html
---

# DescribeScheduledAudit
<a name="API_DescribeScheduledAudit"></a>

Gets information about a scheduled audit.

Requires permission to access the [DescribeScheduledAudit](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeScheduledAudit_RequestSyntax"></a>

```
GET /audit/scheduledaudits/{{scheduledAuditName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeScheduledAudit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scheduledAuditName](#API_DescribeScheduledAudit_RequestSyntax) **   <a name="iot-DescribeScheduledAudit-request-uri-scheduledAuditName"></a>
The name of the scheduled audit whose information you want to get.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeScheduledAudit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeScheduledAudit_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dayOfMonth": "string",
   "dayOfWeek": "string",
   "frequency": "string",
   "scheduledAuditArn": "string",
   "scheduledAuditName": "string",
   "targetCheckNames": [ "string" ]
}
```

## Response Elements
<a name="API_DescribeScheduledAudit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dayOfMonth](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-dayOfMonth"></a>
The day of the month on which the scheduled audit takes place. This is will be `1` through `31` or `LAST`. If days `29`-`31` are specified, and the month does not have that many days, the audit takes place on the `LAST` day of the month.
Type: String
Pattern: `^([1-9]|[12][0-9]|3[01])$|^LAST$`

 ** [dayOfWeek](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-dayOfWeek"></a>
The day of the week on which the scheduled audit takes place, either one of `SUN`, `MON`, `TUE`, `WED`, `THU`, `FRI`, or `SAT`.
Type: String
Valid Values: `SUN | MON | TUE | WED | THU | FRI | SAT`

 ** [frequency](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-frequency"></a>
How often the scheduled audit takes place, either one of `DAILY`, `WEEKLY`, `BIWEEKLY`, or `MONTHLY`. The start time of each audit is determined by the system.
Type: String
Valid Values: `DAILY | WEEKLY | BIWEEKLY | MONTHLY`

 ** [scheduledAuditArn](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-scheduledAuditArn"></a>
The ARN of the scheduled audit.
Type: String

 ** [scheduledAuditName](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-scheduledAuditName"></a>
The name of the scheduled audit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [targetCheckNames](#API_DescribeScheduledAudit_ResponseSyntax) **   <a name="iot-DescribeScheduledAudit-response-targetCheckNames"></a>
Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: Array of strings

## Errors
<a name="API_DescribeScheduledAudit_Errors"></a>

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
<a name="API_DescribeScheduledAudit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeScheduledAudit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeScheduledAudit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
