---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecutionTaskInvocation.html
---

# GetMaintenanceWindowExecutionTaskInvocation
<a name="API_GetMaintenanceWindowExecutionTaskInvocation"></a>

Retrieves information about a specific task running on a specific target.

## Request Syntax
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_RequestSyntax"></a>

```
{
   "InvocationId": "{{string}}",
   "TaskId": "{{string}}",
   "WindowExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InvocationId](#API_GetMaintenanceWindowExecutionTaskInvocation_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-request-InvocationId"></a>
The invocation ID to retrieve.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

 ** [TaskId](#API_GetMaintenanceWindowExecutionTaskInvocation_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-request-TaskId"></a>
The ID of the specific task in the maintenance window task that should be retrieved.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecutionTaskInvocation_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-request-WindowExecutionId"></a>
The ID of the maintenance window execution for which the task is a part.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax"></a>

```
{
   "EndTime": number,
   "ExecutionId": "string",
   "InvocationId": "string",
   "OwnerInformation": "string",
   "Parameters": "string",
   "StartTime": number,
   "Status": "string",
   "StatusDetails": "string",
   "TaskExecutionId": "string",
   "TaskType": "string",
   "WindowExecutionId": "string",
   "WindowTargetId": "string"
}
```

## Response Elements
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-EndTime"></a>
The time that the task finished running on the target.
Type: Timestamp

 ** [ExecutionId](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-ExecutionId"></a>
The execution ID.
Type: String

 ** [InvocationId](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-InvocationId"></a>
The invocation ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

 ** [OwnerInformation](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-OwnerInformation"></a>
User-provided value to be included in any Amazon CloudWatch Events or Amazon EventBridge events raised while running tasks for these targets in this maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Parameters](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-Parameters"></a>
The parameters used at the time that the task ran.
Type: String

 ** [StartTime](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-StartTime"></a>
The time that the task started running on the target.
Type: Timestamp

 ** [Status](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-Status"></a>
The task status for an invocation.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`

 ** [StatusDetails](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-StatusDetails"></a>
The details explaining the status. Details are only available for certain status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.

 ** [TaskExecutionId](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-TaskExecutionId"></a>
The task execution ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

 ** [TaskType](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-TaskType"></a>
Retrieves the task type for a maintenance window.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-WindowExecutionId"></a>
The maintenance window execution ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

 ** [WindowTargetId](#API_GetMaintenanceWindowExecutionTaskInvocation_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTaskInvocation-response-WindowTargetId"></a>
The maintenance window target ID.
Type: String
Length Constraints: Maximum length of 36.

## Errors
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_Examples"></a>

### Example
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_Example_1"></a>

This example illustrates one usage of GetMaintenanceWindowExecutionTaskInvocation.

#### Sample Request
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetMaintenanceWindowExecutionTaskInvocation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T001923Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 167

{
    "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef4EXAMPLE",
    "TaskId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE",
    "InvocationId": "0e466033-290b-4d74-9ae0-f33e3EXAMPLE"
}
```

#### Sample Response
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_Example_1_Response"></a>

```
{
    "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef4EXAMPLE",
    "TaskExecutionId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE",
    "InvocationId": "0e466033-290b-4d74-9ae0-f33e3EXAMPLE",
    "ExecutionId": "1203cf98-5a79-4ec3-97e9-12e0bEXAMPLE",
    "TaskType": "RUN_COMMAND",
    "Parameters": "{\"comment\":\"\",\"documentName\":\"AWS-ApplyPatchBaseline\",\"instanceIds\":[\"i-02573cafcfEXAMPLE\",\"i-0471e04240EXAMPLE\"],\"maxConcurrency\":\"1\",\"maxErrors\":\"1\",\"parameters\":{\"SnapshotId\":[\"\"],\"Operation\":[\"Install\"]},\"timeoutSeconds\":600}",
    "Status": "SUCCESS",
    "StatusDetails": "Success",
    "StartTime": "2024-08-04T11:45:35.141000-07:00",
    "EndTime": "2024-08-04T11:48:08.960000-07:00"
}
```

## See Also
<a name="API_GetMaintenanceWindowExecutionTaskInvocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation)
