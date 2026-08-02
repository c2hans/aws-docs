---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_SourceDetail.html
---

# SourceDetail
<a name="API_SourceDetail"></a>

Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for `SourceDetail` only for custom rules.

## Contents
<a name="API_SourceDetail_Contents"></a>

 ** EventSource **   <a name="config-Type-SourceDetail-EventSource"></a>
The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
Type: String
Valid Values: `aws.config`
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-SourceDetail-MaximumExecutionFrequency"></a>
The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for `MaximumExecutionFrequency`, then `MessageType` must use the `ScheduledNotification` value.
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.
Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose `Three_Hours`, AWS Config runs evaluations once every three hours. In this case, `Three_Hours` is the frequency of this rule.
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** MessageType **   <a name="config-Type-SourceDetail-MessageType"></a>
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
+  `ConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
+  `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
+  `ScheduledNotification` - Triggers a periodic evaluation at the frequency specified for `MaximumExecutionFrequency`.
+  `ConfigurationSnapshotDeliveryCompleted` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.
If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for `ConfigurationItemChangeNotification` and one for `OversizedConfigurationItemChangeNotification`.
Type: String
Valid Values: `ConfigurationItemChangeNotification | ConfigurationSnapshotDeliveryCompleted | ScheduledNotification | OversizedConfigurationItemChangeNotification`
Required: No

## See Also
<a name="API_SourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/SourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/SourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/SourceDetail)
