---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecution.html
---

# GetMaintenanceWindowExecution
<a name="API_GetMaintenanceWindowExecution"></a>

Retrieves details about a specific a maintenance window execution.

## Request Syntax
<a name="API_GetMaintenanceWindowExecution_RequestSyntax"></a>

```
{
   "WindowExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMaintenanceWindowExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecution_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-request-WindowExecutionId"></a>
The ID of the maintenance window execution that includes the task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetMaintenanceWindowExecution_ResponseSyntax"></a>

```
{
   "EndTime": number,
   "StartTime": number,
   "Status": "string",
   "StatusDetails": "string",
   "TaskIds": [ "string" ],
   "WindowExecutionId": "string"
}
```

## Response Elements
<a name="API_GetMaintenanceWindowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-EndTime"></a>
The time the maintenance window finished running.
Type: Timestamp

 ** [StartTime](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-StartTime"></a>
The time the maintenance window started running.
Type: Timestamp

 ** [Status](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-Status"></a>
The status of the maintenance window execution.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`

 ** [StatusDetails](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-StatusDetails"></a>
The details explaining the status. Not available for all status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.

 ** [TaskIds](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-TaskIds"></a>
The ID of the task executions from the maintenance window execution.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecution_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecution-response-WindowExecutionId"></a>
The ID of the maintenance window execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetMaintenanceWindowExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetMaintenanceWindowExecution_Examples"></a>

### Example
<a name="API_GetMaintenanceWindowExecution_Example_1"></a>

This example illustrates one usage of GetMaintenanceWindowExecution.

#### Sample Request
<a name="API_GetMaintenanceWindowExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 61
X-Amz-Target: AmazonSSM.GetMaintenanceWindowExecution
X-Amz-Date: 20240312T205830Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE"
}
```

#### Sample Response
<a name="API_GetMaintenanceWindowExecution_Example_1_Response"></a>

```
{
    "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE",
    "TaskIds": [
        "4b9f371e-a820-422d-b432-8dec9EXAMPLE"
    ],
    "Status": "SUCCESS",
    "StartTime": "2024-08-04T11:45:34.994000-07:00",
    "EndTime": "2024-08-04T11:48:09.123000-07:00"
}
```

## See Also
<a name="API_GetMaintenanceWindowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetMaintenanceWindowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetMaintenanceWindowExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
