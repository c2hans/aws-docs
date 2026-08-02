---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventFilter.html
---

# OrganizationEventFilter
<a name="API_OrganizationEventFilter"></a>

The values to filter results from the [DescribeEventsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html) operation.

## Contents
<a name="API_OrganizationEventFilter_Contents"></a>

 ** actionabilities **   <a name="AWSHealth-Type-OrganizationEventFilter-actionabilities"></a>
A list of actionability values to filter events. Use this to filter events based on whether they require action (`ACTION_REQUIRED`), may require action (`ACTION_MAY_BE_REQUIRED`) or are informational (`INFORMATIONAL`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** awsAccountIds **   <a name="AWSHealth-Type-OrganizationEventFilter-awsAccountIds"></a>
A list of 12-digit AWS account numbers that contains the affected entities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** endTime **   <a name="AWSHealth-Type-OrganizationEventFilter-endTime"></a>
A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from`. If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to`.
Type: [DateTimeRange](API_DateTimeRange.md) object
Required: No

 ** entityArns **   <a name="AWSHealth-Type-OrganizationEventFilter-entityArns"></a>
A list of entity ARNs (unique identifiers).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1600.
Pattern: `.{0,1600}`
Required: No

 ** entityValues **   <a name="AWSHealth-Type-OrganizationEventFilter-entityValues"></a>
A list of entity identifiers, such as EC2 instance IDs (i-34ab692e) or EBS volumes (vol-426ab23e).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1224.
Pattern: `.{0,1224}`
Required: No

 ** eventStatusCodes **   <a name="AWSHealth-Type-OrganizationEventFilter-eventStatusCodes"></a>
A list of event status codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Valid Values: `open | closed | upcoming`
Required: No

 ** eventTypeCategories **   <a name="AWSHealth-Type-OrganizationEventFilter-eventTypeCategories"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** eventTypeCodes **   <a name="AWSHealth-Type-OrganizationEventFilter-eventTypeCodes"></a>
A list of unique identifiers for event types. For example, `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED".`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[^:/]{3,100}`
Required: No

 ** lastUpdatedTime **   <a name="AWSHealth-Type-OrganizationEventFilter-lastUpdatedTime"></a>
A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from`. If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to`.
Type: [DateTimeRange](API_DateTimeRange.md) object
Required: No

 ** personas **   <a name="AWSHealth-Type-OrganizationEventFilter-personas"></a>
A list of persona values to filter events. Use this to filter events based on their target audience: `OPERATIONS`, `SECURITY`, or `BILLING`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** regions **   <a name="AWSHealth-Type-OrganizationEventFilter-regions"></a>
A list of AWS Regions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[^:/]{2,25}`
Required: No

 ** services **   <a name="AWSHealth-Type-OrganizationEventFilter-services"></a>
The AWS services associated with the event. For example, `EC2`, `RDS`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

 ** startTime **   <a name="AWSHealth-Type-OrganizationEventFilter-startTime"></a>
A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from`. If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to`.
Type: [DateTimeRange](API_DateTimeRange.md) object
Required: No

## See Also
<a name="API_OrganizationEventFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationEventFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationEventFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationEventFilter)
