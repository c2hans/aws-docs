---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AssociatedAlarm.html
---

# AssociatedAlarm
<a name="API_AssociatedAlarm"></a>

An Amazon CloudWatch alarm associated with a Region switch plan. These alarms can be used to trigger automatic execution of the plan.

## Contents
<a name="API_AssociatedAlarm_Contents"></a>

 ** alarmType **   <a name="regionswitch-Type-AssociatedAlarm-alarmType"></a>
The alarm type for an associated alarm. An associated CloudWatch alarm can be an application health alarm or a trigger alarm.
Type: String
Valid Values: `applicationHealth | trigger`
Required: Yes

 ** resourceIdentifier **   <a name="regionswitch-Type-AssociatedAlarm-resourceIdentifier"></a>
The resource identifier for alarms that you associate with a plan.
Type: String
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-AssociatedAlarm-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-AssociatedAlarm-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

## See Also
<a name="API_AssociatedAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/AssociatedAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/AssociatedAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/AssociatedAlarm)
