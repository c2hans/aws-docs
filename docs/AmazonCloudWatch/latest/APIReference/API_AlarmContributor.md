---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmContributor.html
---

# AlarmContributor
<a name="API_AlarmContributor"></a>

Represents an individual contributor to a multi-timeseries alarm, containing information about a specific time series and its contribution to the alarm's state.

## Contents
<a name="API_AlarmContributor_Contents"></a>

 ** ContributorAttributes **   <a name="ACW-Type-AlarmContributor-ContributorAttributes"></a>
A map of attributes that describe the contributor, such as metric dimensions and other identifying characteristics.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 150 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ContributorId **   <a name="ACW-Type-AlarmContributor-ContributorId"></a>
The unique identifier for this alarm contributor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: Yes

 ** StateReason **   <a name="ACW-Type-AlarmContributor-StateReason"></a>
An explanation for the contributor's current state, providing context about why it is in its current condition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: Yes

 ** StateTransitionedTimestamp **   <a name="ACW-Type-AlarmContributor-StateTransitionedTimestamp"></a>
The timestamp when the contributor last transitioned to its current state.
Type: Timestamp
Required: No

## See Also
<a name="API_AlarmContributor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmContributor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmContributor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmContributor)
