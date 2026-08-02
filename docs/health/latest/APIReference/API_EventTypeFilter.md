---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventTypeFilter.html
---

# EventTypeFilter
<a name="API_EventTypeFilter"></a>

The values to use to filter results from the [DescribeEventTypes](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html) operation.

## Contents
<a name="API_EventTypeFilter_Contents"></a>

 ** actionabilities **   <a name="AWSHealth-Type-EventTypeFilter-actionabilities"></a>
A list of actionability values to filter event types. Possible values are `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED` and `INFORMATIONAL`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** eventTypeCategories **   <a name="AWSHealth-Type-EventTypeFilter-eventTypeCategories"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** eventTypeCodes **   <a name="AWSHealth-Type-EventTypeFilter-eventTypeCodes"></a>
A list of event type codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9\_\-]{3,100}`
Required: No

 ** personas **   <a name="AWSHealth-Type-EventTypeFilter-personas"></a>
A list of persona classifications to filter event types. Possible values are `OPERATIONS`, `SECURITY`, and `BILLING`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** services **   <a name="AWSHealth-Type-EventTypeFilter-services"></a>
The AWS services associated with the event. For example, `EC2`, `RDS`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

## See Also
<a name="API_EventTypeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventTypeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventTypeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventTypeFilter)
