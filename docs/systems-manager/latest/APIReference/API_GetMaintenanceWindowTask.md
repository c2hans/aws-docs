---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowTask.html
---

# GetMaintenanceWindowTask
<a name="API_GetMaintenanceWindowTask"></a>

Retrieves the details of a maintenance window task.

**Note**
For maintenance window tasks without a specified target, you can't supply values for `--max-errors` and `--max-concurrency`. Instead, the system inserts a placeholder value of `1`, which may be reported in the response to this command. These values don't affect the running of your task and can be ignored.

To retrieve a list of tasks in a maintenance window, instead use the [DescribeMaintenanceWindowTasks](API_DescribeMaintenanceWindowTasks.md) command.

## Request Syntax
<a name="API_GetMaintenanceWindowTask_RequestSyntax"></a>

```
{
   "WindowId": "{{string}}",
   "WindowTaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMaintenanceWindowTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WindowId](#API_GetMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-request-WindowId"></a>
The maintenance window ID that includes the task to retrieve.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

 ** [WindowTaskId](#API_GetMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-request-WindowTaskId"></a>
The maintenance window task ID to retrieve.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetMaintenanceWindowTask_ResponseSyntax"></a>

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
   "CutoffBehavior": "string",
   "Description": "string",
   "LoggingInfo": {
      "S3BucketName": "string",
      "S3KeyPrefix": "string",
      "S3Region": "string"
   },
   "MaxConcurrency": "string",
   "MaxErrors": "string",
   "Name": "string",
   "Priority": number,
   "ServiceRoleArn": "string",
   "Targets": [
      {
         "Key": "string",
         "Values": [ "string" ]
      }
   ],
   "TaskArn": "string",
   "TaskInvocationParameters": {
      "Automation": {
         "DocumentVersion": "string",
         "Parameters": {
            "string" : [ "string" ]
         }
      },
      "Lambda": {
         "ClientContext": "string",
         "Payload": blob,
         "Qualifier": "string"
      },
      "RunCommand": {
         "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "string",
            "CloudWatchOutputEnabled": boolean
         },
         "Comment": "string",
         "DocumentHash": "string",
         "DocumentHashType": "string",
         "DocumentVersion": "string",
         "NotificationConfig": {
            "NotificationArn": "string",
            "NotificationEvents": [ "string" ],
            "NotificationType": "string"
         },
         "OutputS3BucketName": "string",
         "OutputS3KeyPrefix": "string",
         "Parameters": {
            "string" : [ "string" ]
         },
         "ServiceRoleArn": "string",
         "TimeoutSeconds": number
      },
      "StepFunctions": {
         "Input": "string",
         "Name": "string"
      }
   },
   "TaskParameters": {
      "string" : {
         "Values": [ "string" ]
      }
   },
   "TaskType": "string",
   "WindowId": "string",
   "WindowTaskId": "string"
}
```

## Response Elements
<a name="API_GetMaintenanceWindowTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlarmConfiguration](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-AlarmConfiguration"></a>
The details for the CloudWatch alarm you applied to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object

 ** [CutoffBehavior](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-CutoffBehavior"></a>
The action to take on tasks when the maintenance window cutoff time is reached. `CONTINUE_TASK` means that tasks continue to run. For Automation, AWS Lambda, AWS Step Functions tasks, `CANCEL_TASK` means that currently running task invocations continue, but no new task invocations are started. For Run Command tasks, `CANCEL_TASK` means the system attempts to stop the task by sending a `CancelCommand` operation.
Type: String
Valid Values: `CONTINUE_TASK | CANCEL_TASK`

 ** [Description](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-Description"></a>
The retrieved task description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [LoggingInfo](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-LoggingInfo"></a>
The location in Amazon Simple Storage Service (Amazon S3) where the task results are logged.
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: [LoggingInfo](API_LoggingInfo.md) object

 ** [MaxConcurrency](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-MaxConcurrency"></a>
The maximum number of targets allowed to run this task in parallel.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`, which may be reported in the response to this command. This value doesn't affect the running of your task and can be ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`

 ** [MaxErrors](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-MaxErrors"></a>
The maximum number of errors allowed before the task stops being scheduled.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`, which may be reported in the response to this command. This value doesn't affect the running of your task and can be ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`

 ** [Name](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-Name"></a>
The retrieved task name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [Priority](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-Priority"></a>
The priority of the task when it runs. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ServiceRoleArn](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String

 ** [Targets](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-Targets"></a>
The targets where the task should run.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [TaskArn](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-TaskArn"></a>
The resource that the task used during execution. For `RUN_COMMAND` and `AUTOMATION` task types, the value of `TaskArn` is the SSM document name/ARN. For `LAMBDA` tasks, the value is the function name/ARN. For `STEP_FUNCTIONS` tasks, the value is the state machine ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [TaskInvocationParameters](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-TaskInvocationParameters"></a>
The parameters to pass to the task when it runs.
Type: [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md) object

 ** [TaskParameters](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-TaskParameters"></a>
The parameters to pass to the task when it runs.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: String to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [TaskType](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-TaskType"></a>
The type of task to run.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`

 ** [WindowId](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-WindowId"></a>
The retrieved maintenance window ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

 ** [WindowTaskId](#API_GetMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindowTask-response-WindowTaskId"></a>
The retrieved maintenance window task ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetMaintenanceWindowTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetMaintenanceWindowTask_Examples"></a>

### Example
<a name="API_GetMaintenanceWindowTask_Example_1"></a>

This example illustrates one usage of GetMaintenanceWindowTask.

#### Sample Request
<a name="API_GetMaintenanceWindowTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetMaintenanceWindowTask
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T002532Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 92

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE"
}
```

#### Sample Response
<a name="API_GetMaintenanceWindowTask_Example_1_Response"></a>

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE",
    "Name": "MyRunCommandTask",
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE"
            ]
        }
    ],
    "TaskArn": "AWS-ApplyPatchBaseline",
    "ServiceRoleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
    "TaskType": "RUN_COMMAND",
    "TaskParameters": {},
    "Priority": 1,
    "TaskInvocationParameters": {
        "RunCommand": {
            "Comment": "",
            "Parameters": {
                "Operation": [
                    "Install"
                ],
                "SnapshotId": [
                    ""
                ]
            },
            "TimeoutSeconds": 600
        }
    },
    "MaxConcurrency": "1",
    "MaxErrors": "1"
}
```

## See Also
<a name="API_GetMaintenanceWindowTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetMaintenanceWindowTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetMaintenanceWindowTask)
