---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html
---

# ConfigSnapshotDeliveryProperties
<a name="API_ConfigSnapshotDeliveryProperties"></a>

Provides options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket in your delivery channel.

The frequency for a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot is set by one of two values, depending on which is less frequent:
+ The value for the `deliveryFrequency` parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for AWS Config rules.
+ The value for the `MaximumExecutionFrequency` parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see [ConfigRule](API_ConfigRule.md).

If the `deliveryFrequency` value is less frequent than the `MaximumExecutionFrequency` value for a rule, AWS Config invokes the rule only as often as the `deliveryFrequency` value.

1. For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.

1. You specify the `MaximumExecutionFrequency` value for `Six_Hours`.

1. You then specify the delivery channel `deliveryFrequency` value for `TwentyFour_Hours`.

1. Because the value for `deliveryFrequency` is less frequent than `MaximumExecutionFrequency`, AWS Config invokes evaluations for the rule every 24 hours.

You should set the `MaximumExecutionFrequency` value to be at least as frequent as the `deliveryFrequency` value. You can view the `deliveryFrequency` value by using the `DescribeDeliveryChannnels` action.

To update the `deliveryFrequency` with which AWS Config delivers your configuration snapshots, use the `PutDeliveryChannel` action.

## Contents
<a name="API_ConfigSnapshotDeliveryProperties_Contents"></a>

 ** deliveryFrequency **   <a name="config-Type-ConfigSnapshotDeliveryProperties-deliveryFrequency"></a>
The frequency with which AWS Config delivers configuration snapshots.
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

## See Also
<a name="API_ConfigSnapshotDeliveryProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigSnapshotDeliveryProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigSnapshotDeliveryProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigSnapshotDeliveryProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
