---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html
---

# EntityFilter

The values to use to filter results from the [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) operation.

## Contents
<a name="API_EntityFilter_Contents"></a>

 ** eventArns **   <a name="AWSHealth-Type-EntityFilter-eventArns"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: Yes

 ** entityArns **   <a name="AWSHealth-Type-EntityFilter-entityArns"></a>
A list of entity ARNs (unique identifiers).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1600.
Pattern: `.{0,1600}`
Required: No

 ** entityValues **   <a name="AWSHealth-Type-EntityFilter-entityValues"></a>
A list of IDs for affected entities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Maximum length of 1224.
Pattern: `.{0,1224}`
Required: No

 ** lastUpdatedTimes **   <a name="AWSHealth-Type-EntityFilter-lastUpdatedTimes"></a>
A list of the most recent dates and times that the entity was updated.
Type: Array of [DateTimeRange](API_DateTimeRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** statusCodes **   <a name="AWSHealth-Type-EntityFilter-statusCodes"></a>
A list of entity status codes (`IMPAIRED`, `UNIMPAIRED`, or `UNKNOWN`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

 ** tags **   <a name="AWSHealth-Type-EntityFilter-tags"></a>
A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. The filter matches when at least one key in the map matches.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 127.
Key Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{0,255}`
Required: No

## See Also
<a name="API_EntityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EntityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EntityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EntityFilter)
