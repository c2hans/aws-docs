---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StartOnDemandAuditTask.html
---

# StartOnDemandAuditTask
<a name="API_StartOnDemandAuditTask"></a>

Starts an on-demand Device Defender audit.

Requires permission to access the [StartOnDemandAuditTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_StartOnDemandAuditTask_RequestSyntax"></a>

```
POST /audit/tasks HTTP/1.1
Content-type: application/json

{
   "targetCheckNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartOnDemandAuditTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartOnDemandAuditTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetCheckNames](#API_StartOnDemandAuditTask_RequestSyntax) **   <a name="iot-StartOnDemandAuditTask-request-targetCheckNames"></a>
Which checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or `UpdateAccountAuditConfiguration` to select which checks are enabled.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_StartOnDemandAuditTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskId": "string"
}
```

## Response Elements
<a name="API_StartOnDemandAuditTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_StartOnDemandAuditTask_ResponseSyntax) **   <a name="iot-StartOnDemandAuditTask-response-taskId"></a>
The ID of the on-demand audit you started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`

## Errors
<a name="API_StartOnDemandAuditTask_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartOnDemandAuditTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/StartOnDemandAuditTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StartOnDemandAuditTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
