---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_TriggerConfig.html
---

# TriggerConfig
<a name="API_TriggerConfig"></a>

 The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

## Contents
<a name="API_TriggerConfig_Contents"></a>

 ** triggerType **   <a name="appflow-Type-TriggerConfig-triggerType"></a>
 Specifies the type of flow trigger. This can be `OnDemand`, `Scheduled`, or `Event`.
Type: String
Valid Values: `Scheduled | Event | OnDemand`
Required: Yes

 ** triggerProperties **   <a name="appflow-Type-TriggerConfig-triggerProperties"></a>
 Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the `Scheduled` trigger type.
Type: [TriggerProperties](API_TriggerProperties.md) object
Required: No

## See Also
<a name="API_TriggerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/TriggerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/TriggerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/TriggerConfig)
