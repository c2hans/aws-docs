---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html
---

# PutAccountSettingDefault
<a name="API_PutAccountSettingDefault"></a>

Modifies an account setting for all users on an account for whom no individual account setting has been specified. Account settings are set on a per-Region basis.

## Request Syntax
<a name="API_PutAccountSettingDefault_RequestSyntax"></a>

```
{
   "name": "{{string}}",
   "value": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAccountSettingDefault_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_PutAccountSettingDefault_RequestSyntax) **   <a name="ECS-PutAccountSettingDefault-request-name"></a>
The resource name for which to modify the account setting.
The following are the valid values for the account setting name.
+  `serviceLongArnFormat` - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.
+  `taskLongArnFormat` - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.
+  `containerInstanceLongArnFormat` - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.
+  `awsvpcTrunking` - When modified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If `awsvpcTrunking` is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see [Elastic Network Interface Trunking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html) in the *Amazon Elastic Container Service Developer Guide*.
+  `containerInsights` - Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up.

  To use Container Insights with enhanced observability, set the `containerInsights` account setting to `enhanced`.

  To use Container Insights, set the `containerInsights` account setting to `enabled`.

  For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html) in the *Amazon Elastic Container Service Developer Guide*.
+  `dualStackIPv6` - When turned on, when using a VPC in dual stack mode, your tasks using the `awsvpc` network mode can have an IPv6 address assigned. For more information on using IPv6 with tasks launched on Amazon EC2 instances, see [Using a VPC in dual-stack mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html#task-networking-vpc-dual-stack). For more information on using IPv6 with tasks launched on Fargate, see [Using a VPC in dual-stack mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html#fargate-task-networking-vpc-dual-stack).
+  `fargateFIPSMode` - If you specify `fargateFIPSMode`, AWS Fargate FIPS 140 compliance is affected.
+  `fargateTaskRetirementWaitPeriod` - When AWS determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use `fargateTaskRetirementWaitPeriod` to configure the wait time to retire a Fargate task. For information about the Fargate tasks maintenance, see [AWS Fargate task maintenance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html) in the *Amazon ECS Developer Guide*.
+  `fargateEventWindows` - When AWS determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use `fargateEventWindows` to use EC2 Event Windows associated with Fargate tasks to configure time windows for task retirement.
+  `tagResourceAuthorization` - Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as `ecsCreateCluster`. If tags are specified when you create a resource, AWS performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the `ecs:TagResource` action. For more information, see [Grant permission to tag resources on creation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html) in the *Amazon ECS Developer Guide*.
+  `defaultLogDriverMode` -Amazon ECS supports setting a default delivery mode of log messages from a container to the `logDriver` that you specify in the container's `logConfiguration`. The delivery mode affects application stability when the flow of logs from the container to the log driver is interrupted. The `defaultLogDriverMode` setting supports two values: `blocking` and `non-blocking`. If you don't specify a delivery mode in your container definition's `logConfiguration`, the mode you specify using this account setting will be used as the default. For more information about log delivery modes, see [LogConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html).
**Note**
On June 25, 2025, Amazon ECS changed the default log driver mode from `blocking` to `non-blocking` to prioritize task availability over logging. To continue using the `blocking` mode after this change, do one of the following:
Set the `mode` option in your container definition's `logConfiguration` as `blocking`.
Set the `defaultLogDriverMode` account setting to `blocking`.
+  `guardDutyActivate` - The `guardDutyActivate` parameter is read-only in Amazon ECS and indicates whether Amazon ECS Runtime Monitoring is enabled or disabled by your security administrator in your Amazon ECS account. Amazon GuardDuty controls this account setting on your behalf. For more information, see [Protecting Amazon ECS workloads with Amazon ECS Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html).
Type: String
Valid Values: `serviceLongArnFormat | taskLongArnFormat | containerInstanceLongArnFormat | awsvpcTrunking | containerInsights | fargateFIPSMode | tagResourceAuthorization | fargateTaskRetirementWaitPeriod | guardDutyActivate | defaultLogDriverMode | fargateEventWindows`
Required: Yes

 ** [value](#API_PutAccountSettingDefault_RequestSyntax) **   <a name="ECS-PutAccountSettingDefault-request-value"></a>
The account setting value for the specified principal ARN. Accepted values are `enabled`, `disabled`, `on`, `enhanced`, and `off`.
When you specify `fargateTaskRetirementWaitPeriod` for the `name`, the following are the valid values:
+  `0` - AWS sends the notification, and immediately retires the affected tasks.
+  `7` - AWS sends the notification, and waits 7 calendar days to retire the tasks.
+  `14` - AWS sends the notification, and waits 14 calendar days to retire the tasks.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutAccountSettingDefault_ResponseSyntax"></a>

```
{
   "setting": {
      "name": "string",
      "principalArn": "string",
      "type": "string",
      "value": "string"
   }
}
```

## Response Elements
<a name="API_PutAccountSettingDefault_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [setting](#API_PutAccountSettingDefault_ResponseSyntax) **   <a name="ECS-PutAccountSettingDefault-response-setting"></a>
The current setting for a resource.
Type: [Setting](API_Setting.md) object

## Errors
<a name="API_PutAccountSettingDefault_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## See Also
<a name="API_PutAccountSettingDefault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/PutAccountSettingDefault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/PutAccountSettingDefault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
