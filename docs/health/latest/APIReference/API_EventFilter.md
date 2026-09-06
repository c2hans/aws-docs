---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html
---

# EventFilter
<a name="API_EventFilter"></a>

The values to use to filter results from the [DescribeEvents](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html) and [DescribeEventAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html) operations.

## Contents
<a name="API_EventFilter_Contents"></a>

 ** actionabilities **   <a name="AWSHealth-Type-EventFilter-actionabilities"></a>
A list of actionability values to filter events. Use this to filter events based on whether they require action (`ACTION_REQUIRED`), may require action (`ACTION_MAY_BE_REQUIRED`) or are informational (`INFORMATIONAL`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** availabilityZones **   <a name="AWSHealth-Type-EventFilter-availabilityZones"></a>
A list of AWS Availability Zones.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 18.
Pattern: `[a-z]{2}\-[0-9a-z\-]{4,16}`
Required: No

 ** endTimes **   <a name="AWSHealth-Type-EventFilter-endTimes"></a>
A list of dates and times that the event ended.
Type: Array of [DateTimeRange](API_DateTimeRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** entityArns **   <a name="AWSHealth-Type-EventFilter-entityArns"></a>
A list of entity ARNs (unique identifiers).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1600.
Pattern: `.{0,1600}`
Required: No

 ** entityValues **   <a name="AWSHealth-Type-EventFilter-entityValues"></a>
A list of entity identifiers, such as EC2 instance IDs (`i-34ab692e`) or EBS volumes (`vol-426ab23e`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1224.
Pattern: `.{0,1224}`
Required: No

 ** eventArns **   <a name="AWSHealth-Type-EventFilter-eventArns"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** eventStatusCodes **   <a name="AWSHealth-Type-EventFilter-eventStatusCodes"></a>
A list of event status codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Valid Values: `open | closed | upcoming`
Required: No

 ** eventTypeCategories **   <a name="AWSHealth-Type-EventFilter-eventTypeCategories"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** eventTypeCodes **   <a name="AWSHealth-Type-EventFilter-eventTypeCodes"></a>
A list of unique identifiers for event types. For example, `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED".`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[^:/]{3,100}`
Required: No

 ** lastUpdatedTimes **   <a name="AWSHealth-Type-EventFilter-lastUpdatedTimes"></a>
A list of dates and times that the event was last updated.
Type: Array of [DateTimeRange](API_DateTimeRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** personas **   <a name="AWSHealth-Type-EventFilter-personas"></a>
A list of persona values to filter events. Use this to filter events based on their target audience: `OPERATIONS`, `SECURITY`, or `BILLING`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** regions **   <a name="AWSHealth-Type-EventFilter-regions"></a>
A list of AWS Regions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[^:/]{2,25}`
Required: No

 ** services **   <a name="AWSHealth-Type-EventFilter-services"></a>
The AWS services associated with the event. For example, `EC2`, `RDS`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

 ** startTimes **   <a name="AWSHealth-Type-EventFilter-startTimes"></a>
A list of dates and times that the event began.
Type: Array of [DateTimeRange](API_DateTimeRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** tags **   <a name="AWSHealth-Type-EventFilter-tags"></a>
A map of entity tags attached to the affected entity.
Currently, the `tags` property isn't supported.
Type: Array of string to string maps
Array Members: Maximum number of 50 items.
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 127.
Key Pattern: `.{0,127}`
Value Length Constraints: Maximum length of 255.
Value Pattern: `.{0,255}`
Required: No

## See Also
<a name="API_EventFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventFilter)
