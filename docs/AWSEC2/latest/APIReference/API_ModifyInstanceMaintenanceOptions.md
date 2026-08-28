---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMaintenanceOptions.html
---

# ModifyInstanceMaintenanceOptions
<a name="API_ModifyInstanceMaintenanceOptions"></a>

Modifies the recovery behavior of your instance to disable simplified automatic recovery or set the recovery behavior to default. The default configuration will not enable simplified automatic recovery for an unsupported instance type. For more information, see [Simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery).

Modifies the reboot migration behavior during a user-initiated reboot of an instance that has a pending `system-reboot` event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration).

## Request Parameters
<a name="API_ModifyInstanceMaintenanceOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AutoRecovery**
Disables the automatic recovery behavior of your instance or sets it to default.
Type: String
Valid Values: `disabled | default`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **RebootMigration**
Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled `system-reboot` event:
+  `default` - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the `system-reboot` event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
+  `disabled` - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The `system-reboot` event remains scheduled.
This setting only applies to supported instances that have a scheduled reboot event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | default`
Required: No

## Response Elements
<a name="API_ModifyInstanceMaintenanceOptions_ResponseElements"></a>

The following elements are returned by the service.

 **autoRecovery**
Provides information on the current automatic recovery behavior of your instance.
Type: String
Valid Values: `disabled | default`

 **instanceId**
The ID of the instance.
Type: String

 **rebootMigration**
Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled `system-reboot` event:
+  `default` - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the `system-reboot` event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
+  `disabled` - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The `system-reboot` event remains scheduled.
This setting only applies to supported instances that have a scheduled reboot event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | default`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyInstanceMaintenanceOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyInstanceMaintenanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceMaintenanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
