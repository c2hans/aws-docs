---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EntityAccountFilter.html
---

# EntityAccountFilter

A JSON set of elements including the `awsAccountId`, `eventArn` and a set of `statusCodes`.

## Contents
<a name="API_EntityAccountFilter_Contents"></a>

 ** eventArn **   <a name="AWSHealth-Type-EntityAccountFilter-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: Yes

 ** awsAccountId **   <a name="AWSHealth-Type-EntityAccountFilter-awsAccountId"></a>
The 12-digit AWS account numbers that contains the affected entities.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** statusCodes **   <a name="AWSHealth-Type-EntityAccountFilter-statusCodes"></a>
A list of entity status codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

 ** tags **   <a name="AWSHealth-Type-EntityAccountFilter-tags"></a>
A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. Matching is case sensitive, and the filter matches when at least one key in the map matches.
An entity is returned when the tags of the resource, or of the account it belongs to, match. When you specify several filters in `organizationEntityAccountFilters`, the tags must be identical in every filter.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 127.
Key Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{0,255}`
Required: No

## See Also
<a name="API_EntityAccountFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EntityAccountFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EntityAccountFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EntityAccountFilter)
