---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTaskWithMaintenanceWindow.html
---

# RegisterTaskWithMaintenanceWindow
<a name="API_RegisterTaskWithMaintenanceWindow"></a>

Adds a new task to a maintenance window.

## Request Syntax
<a name="API_RegisterTaskWithMaintenanceWindow_RequestSyntax"></a>

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
   "ClientToken": "{{string}}",
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
   "TaskType": "{{string}}",
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterTaskWithMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmConfiguration](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-AlarmConfiguration"></a>
The CloudWatch alarm you want to apply to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [ClientToken](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [CutoffBehavior](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-CutoffBehavior"></a>
Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
+  `CONTINUE_TASK`: When the cutoff time is reached, any tasks that are running continue. The default value.
+  `CANCEL_TASK`:
  + For Automation, AWS Lambda, AWS Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.
  + For Run Command tasks: When the cutoff time is reached, the system sends a [CancelCommand](API_CancelCommand.md) operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.

  The status for tasks that are not completed is `TIMED_OUT`.
Type: String
Valid Values: `CONTINUE_TASK | CANCEL_TASK`
Required: No

 ** [Description](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-Description"></a>
An optional description for the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [LoggingInfo](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-LoggingInfo"></a>
A structure containing information about an Amazon Simple Storage Service (Amazon S3) bucket to write managed node-level logs to.
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: [LoggingInfo](API_LoggingInfo.md) object
Required: No

 ** [MaxConcurrency](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-MaxConcurrency"></a>
The maximum number of targets this task can be run for, in parallel.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** [MaxErrors](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-MaxErrors"></a>
The maximum number of errors allowed before this task stops being scheduled.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** [Name](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-Name"></a>
An optional name for the task.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [Priority](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-Priority"></a>
The priority of the task in the maintenance window, the lower the number the higher the priority. Tasks in a maintenance window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [ServiceRoleArn](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String
Required: No

 ** [Targets](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-Targets"></a>
The targets (either managed nodes or maintenance window targets).
One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, AWS Lambda, and AWS Step Functions). For more information about running tasks that don't specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the * AWS Systems Manager User Guide*.
Specify managed nodes using the following format:
 `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`
Specify maintenance window targets using the following format:
 `Key=WindowTargetIds,Values=<window-target-id-1>,<window-target-id-2>`
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [TaskArn](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-TaskArn"></a>
The ARN of the task to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** [TaskInvocationParameters](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-TaskInvocationParameters"></a>
The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
Type: [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md) object
Required: No

 ** [TaskParameters](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-TaskParameters"></a>
The parameters that should be passed to the task when it is run.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: String to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [TaskType](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-TaskType"></a>
The type of task being registered.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`
Required: Yes

 ** [WindowId](#API_RegisterTaskWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window the task should be added to.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_RegisterTaskWithMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowTaskId": "string"
}
```

## Response Elements
<a name="API_RegisterTaskWithMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowTaskId](#API_RegisterTaskWithMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-RegisterTaskWithMaintenanceWindow-response-WindowTaskId"></a>
The ID of the task in the maintenance window.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_RegisterTaskWithMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** FeatureNotAvailableException **
You attempted to register a `LAMBDA` or `STEP_FUNCTIONS` task in a region where the corresponding service isn't available.
HTTP Status Code: 400

 ** IdempotentParameterMismatch **
Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceLimitExceededException **
Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.
For information about resource quotas in Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_RegisterTaskWithMaintenanceWindow_Examples"></a>

### Example
<a name="API_RegisterTaskWithMaintenanceWindow_Example_1"></a>

This example illustrates one usage of RegisterTaskWithMaintenanceWindow.

#### Sample Request
<a name="API_RegisterTaskWithMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.RegisterTaskWithMaintenanceWindow
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T181553Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 362

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "Targets": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-02573cafcfEXAMPLE"
            ]
        }
    ],
    "TaskArn": "AWS-RunShellScript",
    "TaskType": "RUN_COMMAND",
    "TaskInvocationParameters": {
        "RunCommand": {
            "Parameters": {
                "commands": [
                    "df"
                ]
            }
        }
    },
    "Priority": 10,
    "MaxConcurrency": "1",
    "MaxErrors": "1",
    "ClientToken": "8a3f60db-1d39-4938-a566-c2ec2EXAMPLE"
}
```

#### Sample Response
<a name="API_RegisterTaskWithMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowTaskId": "216ae877-0be9-4746-a19d-ed654EXAMPLE"
}
```

## See Also
<a name="API_RegisterTaskWithMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
