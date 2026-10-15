---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmTagsPropagation.html
---

# AlarmTagsPropagation
<a name="API_AlarmTagsPropagation"></a>

Includes the alarm's tags in the notifications that the alarm sends to Amazon SNS topics and Lambda functions. The tags are also included in the alarm's state-change events in Amazon EventBridge. Other types of alarm actions don't receive the tags.

By default, the alarm's tags aren't included.

Use this to route or filter notifications and events by tag, such as by team or environment. You can also use it to read the alarm's tags without looking them up separately.

To limit which tags are included, specify either `IncludedTagKeys` or `ExcludedTagKeys`. You can't specify both. If you specify neither, all of the alarm's tags are included. This includes tags that you add to the alarm later.

## Contents
<a name="API_AlarmTagsPropagation_Contents"></a>

 ** Enabled **   <a name="ACW-Type-AlarmTagsPropagation-Enabled"></a>
Set to `true` to include the alarm's tags. Set to `false` to stop including them.
When this is `true`, you must have the `cloudwatch:ListTagsForResource` permission on the alarm to create or update it.
Type: Boolean
Required: Yes

 ** ExcludedTagKeys **   <a name="ACW-Type-AlarmTagsPropagation-ExcludedTagKeys"></a>
The tag keys to exclude. All of the alarm's tags except those with these keys are included.
You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.
You can't specify both `IncludedTagKeys` and `ExcludedTagKeys`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** IncludedTagKeys **   <a name="ACW-Type-AlarmTagsPropagation-IncludedTagKeys"></a>
The tag keys to include. Only the alarm's tags with these keys are included.
You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.
You can't specify both `IncludedTagKeys` and `ExcludedTagKeys`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AlarmTagsPropagation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmTagsPropagation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmTagsPropagation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmTagsPropagation)
