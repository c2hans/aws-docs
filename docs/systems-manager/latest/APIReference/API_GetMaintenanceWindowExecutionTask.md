---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecutionTask.html
---

# GetMaintenanceWindowExecutionTask
<a name="API_GetMaintenanceWindowExecutionTask"></a>

Retrieves the details about a specific task run as part of a maintenance window execution.

## Request Syntax
<a name="API_GetMaintenanceWindowExecutionTask_RequestSyntax"></a>

```
{
   "TaskId": "{{string}}",
   "WindowExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMaintenanceWindowExecutionTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskId](#API_GetMaintenanceWindowExecutionTask_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-request-TaskId"></a>
The ID of the specific task execution in the maintenance window task that should be retrieved.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecutionTask_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-request-WindowExecutionId"></a>
The ID of the maintenance window execution that includes the task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetMaintenanceWindowExecutionTask_ResponseSyntax"></a>

```
{
   "AlarmConfiguration": {
      "Alarms": [
         {
            "Name": "string"
         }
      ],
      "IgnorePollAlarmFailure": boolean
   },
   "EndTime": number,
   "MaxConcurrency": "string",
   "MaxErrors": "string",
   "Priority": number,
   "ServiceRole": "string",
   "StartTime": number,
   "Status": "string",
   "StatusDetails": "string",
   "TaskArn": "string",
   "TaskExecutionId": "string",
   "TaskParameters": [
      {
         "string" : {
            "Values": [ "string" ]
         }
      }
   ],
   "TriggeredAlarms": [
      {
         "Name": "string",
         "State": "string"
      }
   ],
   "Type": "string",
   "WindowExecutionId": "string"
}
```

## Response Elements
<a name="API_GetMaintenanceWindowExecutionTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlarmConfiguration](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-AlarmConfiguration"></a>
The details for the CloudWatch alarm you applied to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object

 ** [EndTime](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-EndTime"></a>
The time the task execution completed.
Type: Timestamp

 ** [MaxConcurrency](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-MaxConcurrency"></a>
The defined maximum number of task executions that could be run in parallel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`

 ** [MaxErrors](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-MaxErrors"></a>
The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`

 ** [Priority](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-Priority"></a>
The priority of the task.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ServiceRole](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-ServiceRole"></a>
The role that was assumed when running the task.
Type: String

 ** [StartTime](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-StartTime"></a>
The time the task execution started.
Type: Timestamp

 ** [Status](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-Status"></a>
The status of the task.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`

 ** [StatusDetails](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-StatusDetails"></a>
The details explaining the status. Not available for all status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.

 ** [TaskArn](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the task that ran.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [TaskExecutionId](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-TaskExecutionId"></a>
The ID of the specific task execution in the maintenance window task that was retrieved.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

 ** [TaskParameters](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-TaskParameters"></a>
The parameters passed to the task when it was run.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
The map has the following format:
+  `Key`: string, between 1 and 255 characters
+  `Value`: an array of strings, each between 1 and 255 characters
Type: Array of string to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object maps
Key Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [TriggeredAlarms](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-TriggeredAlarms"></a>
The CloudWatch alarms that were invoked by the maintenance window task.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.

 ** [Type](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-Type"></a>
The type of task that was run.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`

 ** [WindowExecutionId](#API_GetMaintenanceWindowExecutionTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowExecutionTask-response-WindowExecutionId"></a>
The ID of the maintenance window execution that includes the task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetMaintenanceWindowExecutionTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetMaintenanceWindowExecutionTask_Examples"></a>

### Example
<a name="API_GetMaintenanceWindowExecutionTask_Example_1"></a>

This example illustrates one usage of GetMaintenanceWindowExecutionTask.

#### Sample Request
<a name="API_GetMaintenanceWindowExecutionTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetMaintenanceWindowExecutionTask
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T001515Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 111

{
    "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef436EXAMPLE",
    "TaskId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE"
}
```

#### Sample Response
<a name="API_GetMaintenanceWindowExecutionTask_Example_1_Response"></a>

```
{
    "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef436EXAMPLE",
    "TaskExecutionId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE",
    "TaskArn": "AWS-RunPatchBaseline",
    "ServiceRole": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
    "Type": "RUN_COMMAND",
    "TaskParameters": [
        {
            "BaselineOverride": {
                "Values": [
                    ""
                ]
            },
            "InstallOverrideList": {
                "Values": [
                    ""
                ]
            },
            "Operation": {
                "Values": [
                    "Scan"
                ]
            },
            "RebootOption": {
                "Values": [
                    "RebootIfNeeded"
                ]
            },
            "SnapshotId": {
                "Values": [
                    "{{ aws:ORCHESTRATION_ID }}"
                ]
            },
            "aws:InstanceId": {
                "Values": [
                    "i-02573cafcfEXAMPLE",
                    "i-0471e04240EXAMPLE",
                    "i-07782c72faEXAMPLE"
                ]
            }
        }
    ],
    "Priority": 1,
    "MaxConcurrency": "1",
    "MaxErrors": "3",
    "Status": "SUCCESS",
    "StartTime": "2024-08-04T11:45:35.088000-07:00",
    "EndTime": "2024-08-04T11:48:09.079000-07:00"
}
```

## See Also
<a name="API_GetMaintenanceWindowExecutionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetMaintenanceWindowExecutionTask)
