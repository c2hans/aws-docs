---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindowTask.html
---

# UpdateMaintenanceWindowTask
<a name="API_UpdateMaintenanceWindowTask"></a>

Modifies a task assigned to a maintenance window. You can't change the task type, but you can change the following values:
+  `TaskARN`. For example, you can change a `RUN_COMMAND` task from `AWS-RunPowerShellScript` to `AWS-RunShellScript`.
+  `ServiceRoleArn`
+  `TaskInvocationParameters`
+  `Priority`
+  `MaxConcurrency`
+  `MaxErrors`

**Note**
One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, AWS Lambda, and AWS Step Functions). For more information about running tasks that don't specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the * AWS Systems Manager User Guide*.

If the value for a parameter in `UpdateMaintenanceWindowTask` is null, then the corresponding field isn't modified. If you set `Replace` to true, then all fields required by the [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) operation are required for this request. Optional fields that aren't specified are set to null.

**Important**
When you update a maintenance window task that has options specified in `TaskInvocationParameters`, you must provide again all the `TaskInvocationParameters` values that you want to retain. The values you don't specify again are removed. For example, suppose that when you registered a Run Command task, you specified `TaskInvocationParameters` values for `Comment`, `NotificationConfig`, and `OutputS3BucketName`. If you update the maintenance window task and specify only a different `OutputS3BucketName` value, the values for `Comment` and `NotificationConfig` are removed.

## Request Syntax
<a name="API_UpdateMaintenanceWindowTask_RequestSyntax"></a>

```
{
   "AlarmConfiguration": {
      "Alarms": [
         {
            "Name": "{{string}}"
         }
      ],
      "IgnorePollAlarmFailure": {{boolean}}
   },
   "CutoffBehavior": "{{string}}",
   "Description": "{{string}}",
   "LoggingInfo": {
      "S3BucketName": "{{string}}",
      "S3KeyPrefix": "{{string}}",
      "S3Region": "{{string}}"
   },
   "MaxConcurrency": "{{string}}",
   "MaxErrors": "{{string}}",
   "Name": "{{string}}",
   "Priority": {{number}},
   "Replace": {{boolean}},
   "ServiceRoleArn": "{{string}}",
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "TaskArn": "{{string}}",
   "TaskInvocationParameters": {
      "Automation": {
         "DocumentVersion": "{{string}}",
         "Parameters": {
            "{{string}}" : [ "{{string}}" ]
         }
      },
      "Lambda": {
         "ClientContext": "{{string}}",
         "Payload": {{blob}},
         "Qualifier": "{{string}}"
      },
      "RunCommand": {
         "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "{{string}}",
            "CloudWatchOutputEnabled": {{boolean}}
         },
         "Comment": "{{string}}",
         "DocumentHash": "{{string}}",
         "DocumentHashType": "{{string}}",
         "DocumentVersion": "{{string}}",
         "NotificationConfig": {
            "NotificationArn": "{{string}}",
            "NotificationEvents": [ "{{string}}" ],
            "NotificationType": "{{string}}"
         },
         "OutputS3BucketName": "{{string}}",
         "OutputS3KeyPrefix": "{{string}}",
         "Parameters": {
            "{{string}}" : [ "{{string}}" ]
         },
         "ServiceRoleArn": "{{string}}",
         "TimeoutSeconds": {{number}}
      },
      "StepFunctions": {
         "Input": "{{string}}",
         "Name": "{{string}}"
      }
   },
   "TaskParameters": {
      "{{string}}" : {
         "Values": [ "{{string}}" ]
      }
   },
   "WindowId": "{{string}}",
   "WindowTaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMaintenanceWindowTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmConfiguration](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-AlarmConfiguration"></a>
The CloudWatch alarm you want to apply to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [CutoffBehavior](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-CutoffBehavior"></a>
Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
+  `CONTINUE_TASK`: When the cutoff time is reached, any tasks that are running continue. The default value.
+  `CANCEL_TASK`:
  + For Automation, AWS Lambda, AWS Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.
  + For Run Command tasks: When the cutoff time is reached, the system sends a [CancelCommand](API_CancelCommand.md) operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.

  The status for tasks that are not completed is `TIMED_OUT`.
Type: String
Valid Values: `CONTINUE_TASK | CANCEL_TASK`
Required: No

 ** [Description](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-Description"></a>
The new task description to specify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [LoggingInfo](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-LoggingInfo"></a>
The new logging location in Amazon S3 to specify.
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: [LoggingInfo](API_LoggingInfo.md) object
Required: No

 ** [MaxConcurrency](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-MaxConcurrency"></a>
The new `MaxConcurrency` value you want to specify. `MaxConcurrency` is the number of targets that are allowed to run this task, in parallel.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** [MaxErrors](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-MaxErrors"></a>
The new `MaxErrors` value to specify. `MaxErrors` is the maximum number of errors that are allowed before the task stops being scheduled.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** [Name](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-Name"></a>
The new task name to specify.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [Priority](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-Priority"></a>
The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Replace](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-Replace"></a>
If True, then all fields that are required by the [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) operation are also required for this API request. Optional fields that aren't specified are set to null.
Type: Boolean
Required: No

 ** [ServiceRoleArn](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String
Required: No

 ** [Targets](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-Targets"></a>
The targets (either managed nodes or tags) to modify. Managed nodes are specified using the format `Key=instanceids,Values=instanceID_1,instanceID_2`. Tags are specified using the format ` Key=tag_name,Values=tag_value`.
One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, AWS Lambda, and AWS Step Functions). For more information about running tasks that don't specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the * AWS Systems Manager User Guide*.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [TaskArn](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-TaskArn"></a>
The task ARN to modify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** [TaskInvocationParameters](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-TaskInvocationParameters"></a>
The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
When you update a maintenance window task that has options specified in `TaskInvocationParameters`, you must provide again all the `TaskInvocationParameters` values that you want to retain. The values you don't specify again are removed. For example, suppose that when you registered a Run Command task, you specified `TaskInvocationParameters` values for `Comment`, `NotificationConfig`, and `OutputS3BucketName`. If you update the maintenance window task and specify only a different `OutputS3BucketName` value, the values for `Comment` and `NotificationConfig` are removed.
Type: [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md) object
Required: No

 ** [TaskParameters](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-TaskParameters"></a>
The parameters to modify.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
The map has the following format:
Key: string, between 1 and 255 characters
Value: an array of strings, each string is between 1 and 255 characters
Type: String to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [WindowId](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-WindowId"></a>
The maintenance window ID that contains the task to modify.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

 ** [WindowTaskId](#API_UpdateMaintenanceWindowTask_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-request-WindowTaskId"></a>
The task ID to modify.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_UpdateMaintenanceWindowTask_ResponseSyntax"></a>

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
   "WindowId": "string",
   "WindowTaskId": "string"
}
```

## Response Elements
<a name="API_UpdateMaintenanceWindowTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlarmConfiguration](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-AlarmConfiguration"></a>
The details for the CloudWatch alarm you applied to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object

 ** [CutoffBehavior](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-CutoffBehavior"></a>
The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
Type: String
Valid Values: `CONTINUE_TASK | CANCEL_TASK`

 ** [Description](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-Description"></a>
The updated task description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [LoggingInfo](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-LoggingInfo"></a>
The updated logging information in Amazon S3.
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: [LoggingInfo](API_LoggingInfo.md) object

 ** [MaxConcurrency](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-MaxConcurrency"></a>
The updated `MaxConcurrency` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`

 ** [MaxErrors](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-MaxErrors"></a>
The updated `MaxErrors` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`

 ** [Name](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-Name"></a>
The updated task name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [Priority](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-Priority"></a>
The updated priority value.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ServiceRoleArn](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String

 ** [Targets](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-Targets"></a>
The updated target values.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [TaskArn](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-TaskArn"></a>
The updated task ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [TaskInvocationParameters](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-TaskInvocationParameters"></a>
The updated parameter values.
Type: [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md) object

 ** [TaskParameters](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-TaskParameters"></a>
The updated parameter values.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: String to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [WindowId](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-WindowId"></a>
The ID of the maintenance window that was updated.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

 ** [WindowTaskId](#API_UpdateMaintenanceWindowTask_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTask-response-WindowTaskId"></a>
The task ID of the maintenance window that was updated.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_UpdateMaintenanceWindowTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_UpdateMaintenanceWindowTask_Examples"></a>

### Example
<a name="API_UpdateMaintenanceWindowTask_Example_1"></a>

This example illustrates one usage of UpdateMaintenanceWindowTask.

#### Sample Request
<a name="API_UpdateMaintenanceWindowTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateMaintenanceWindowTask
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T010531Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 244

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE",
    "Priority": 2,
    "MaxConcurrency": "10",
    "MaxErrors": "3",
    "Name": "MyRevisedMaintenanceWindowTask",
    "Description": "My updated maintenance window task",
    "ServiceRoleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/MyCustomMaintenanceWindowTaskRole"
}
```

#### Sample Response
<a name="API_UpdateMaintenanceWindowTask_Example_1_Response"></a>

```
{
    "Description": "My updated maintenance window task",
    "MaxConcurrency": "10",
    "MaxErrors": "3",
    "Name": "MyRevisedMaintenanceWindowTask",
    "Priority": 2,
    "ServiceRoleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/MyCustomMaintenanceWindowTaskRole",
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE"
            ]
        }
    ],
    "TaskArn": "AWS-ApplyPatchBaseline",
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
    "TaskParameters": {},
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE"
}
```

## See Also
<a name="API_UpdateMaintenanceWindowTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateMaintenanceWindowTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateMaintenanceWindowTask)
