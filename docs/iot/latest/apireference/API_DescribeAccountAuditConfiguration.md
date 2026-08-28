---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAccountAuditConfiguration.html
---

# DescribeAccountAuditConfiguration
<a name="API_DescribeAccountAuditConfiguration"></a>

Gets information about the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.

Requires permission to access the [DescribeAccountAuditConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeAccountAuditConfiguration_RequestSyntax"></a>

```
GET /audit/configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccountAuditConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAccountAuditConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccountAuditConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "auditCheckConfigurations": {
      "string" : {
         "configuration": {
            "string" : "string"
         },
         "enabled": boolean
      }
   },
   "auditNotificationTargetConfigurations": {
      "string" : {
         "enabled": boolean,
         "roleArn": "string",
         "targetArn": "string"
      }
   },
   "roleArn": "string"
}
```

## Response Elements
<a name="API_DescribeAccountAuditConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [auditCheckConfigurations](#API_DescribeAccountAuditConfiguration_ResponseSyntax) **   <a name="iot-DescribeAccountAuditConfiguration-response-auditCheckConfigurations"></a>
Which audit checks are enabled and disabled for this account.
Type: String to [AuditCheckConfiguration](API_AuditCheckConfiguration.md) object map

 ** [auditNotificationTargetConfigurations](#API_DescribeAccountAuditConfiguration_ResponseSyntax) **   <a name="iot-DescribeAccountAuditConfiguration-response-auditNotificationTargetConfigurations"></a>
Information about the targets to which audit notifications are sent for this account.
Type: String to [AuditNotificationTarget](API_AuditNotificationTarget.md) object map
Valid Keys: `SNS`

 ** [roleArn](#API_DescribeAccountAuditConfiguration_ResponseSyntax) **   <a name="iot-DescribeAccountAuditConfiguration-response-roleArn"></a>
The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
On the first call to `UpdateAccountAuditConfiguration`, this parameter is required.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_DescribeAccountAuditConfiguration_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccountAuditConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeAccountAuditConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeAccountAuditConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
