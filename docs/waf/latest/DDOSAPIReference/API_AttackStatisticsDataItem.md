---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackStatisticsDataItem.html
---

# AttackStatisticsDataItem
<a name="API_AttackStatisticsDataItem"></a>

A single attack statistics data record. This is returned by [DescribeAttackStatistics](API_DescribeAttackStatistics.md) along with a time range indicating the time period that the attack statistics apply to.

## Contents
<a name="API_AttackStatisticsDataItem_Contents"></a>

 ** AttackCount **   <a name="AWSShield-Type-AttackStatisticsDataItem-AttackCount"></a>
The number of attacks detected during the time period. This is always present, but might be zero.
Type: Long
Required: Yes

 ** AttackVolume **   <a name="AWSShield-Type-AttackStatisticsDataItem-AttackVolume"></a>
Information about the volume of attacks during the time period. If the accompanying `AttackCount` is zero, this setting might be empty.
Type: [AttackVolume](API_AttackVolume.md) object
Required: No

## See Also
<a name="API_AttackStatisticsDataItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackStatisticsDataItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackStatisticsDataItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackStatisticsDataItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
