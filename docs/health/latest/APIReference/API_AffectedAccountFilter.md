---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_AffectedAccountFilter.html
---

# AffectedAccountFilter

A filter for narrowing down affected accounts in an organization event.

## Contents
<a name="API_AffectedAccountFilter_Contents"></a>

 ** eventArn **   <a name="AWSHealth-Type-AffectedAccountFilter-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** tags **   <a name="AWSHealth-Type-AffectedAccountFilter-tags"></a>
A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. Matching is case sensitive, and the filter matches when at least one key in the map matches.
An account is returned when its own tags, or the tags of one of its affected resources, match.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 127.
Key Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{0,255}`
Required: No

## See Also
<a name="API_AffectedAccountFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/AffectedAccountFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/AffectedAccountFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/AffectedAccountFilter)
