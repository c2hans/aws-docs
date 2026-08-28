---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAccountAuditConfiguration.html
---

# UpdateAccountAuditConfiguration
<a name="API_UpdateAccountAuditConfiguration"></a>

Configures or reconfigures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.

Requires permission to access the [UpdateAccountAuditConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateAccountAuditConfiguration_RequestSyntax"></a>

```
PATCH /audit/configuration HTTP/1.1
Content-type: application/json

{
   "auditCheckConfigurations": {
      "{{string}}" : {
         "configuration": {
            "{{string}}" : "{{string}}"
         },
         "enabled": {{boolean}}
      }
   },
   "auditNotificationTargetConfigurations": {
      "{{string}}" : {
         "enabled": {{boolean}},
         "roleArn": "{{string}}",
         "targetArn": "{{string}}"
      }
   },
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccountAuditConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAccountAuditConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [auditCheckConfigurations](#API_UpdateAccountAuditConfiguration_RequestSyntax) **   <a name="iot-UpdateAccountAuditConfiguration-request-auditCheckConfigurations"></a>
Specifies which audit checks are enabled and disabled for this account. Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are currently enabled.
Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted.
You cannot disable a check if it's used by any scheduled audit. You must first delete the check from the scheduled audit or delete the scheduled audit itself.
On the first call to `UpdateAccountAuditConfiguration`, this parameter is required and must specify at least one enabled check.
Type: String to [AuditCheckConfiguration](API_AuditCheckConfiguration.md) object map
Required: No

 ** [auditNotificationTargetConfigurations](#API_UpdateAccountAuditConfiguration_RequestSyntax) **   <a name="iot-UpdateAccountAuditConfiguration-request-auditNotificationTargetConfigurations"></a>
Information about the targets to which audit notifications are sent.
Type: String to [AuditNotificationTarget](API_AuditNotificationTarget.md) object map
Valid Keys: `SNS`
Required: No

 ** [roleArn](#API_UpdateAccountAuditConfiguration_RequestSyntax) **   <a name="iot-UpdateAccountAuditConfiguration-request-roleArn"></a>
The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateAccountAuditConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAccountAuditConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAccountAuditConfiguration_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccountAuditConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateAccountAuditConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateAccountAuditConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
