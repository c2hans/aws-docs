---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMaintenanceOptions.html
---

# InstanceMaintenanceOptions
<a name="API_InstanceMaintenanceOptions"></a>

The maintenance options for the instance.

## Contents
<a name="API_InstanceMaintenanceOptions_Contents"></a>

 ** autoRecovery **
Provides information on the current automatic recovery behavior of your instance.
Type: String
Valid Values: `disabled | default`
Required: No

 ** rebootMigration **
Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled `system-reboot` event:
+  `default` - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the `system-reboot` event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
+  `disabled` - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The `system-reboot` event remains scheduled.
This setting only applies to supported instances that have a scheduled reboot event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | default`
Required: No

## See Also
<a name="API_InstanceMaintenanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceMaintenanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceMaintenanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceMaintenanceOptions)
