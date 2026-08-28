---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WarmTierRetentionPeriod.html
---

# WarmTierRetentionPeriod
<a name="API_WarmTierRetentionPeriod"></a>

Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.

## Contents
<a name="API_WarmTierRetentionPeriod_Contents"></a>

 ** numberOfDays **   <a name="iotsitewise-Type-WarmTierRetentionPeriod-numberOfDays"></a>
The number of days the data is stored in the warm tier.
Type: Integer
Required: No

 ** unlimited **   <a name="iotsitewise-Type-WarmTierRetentionPeriod-unlimited"></a>
If set to true, the data is stored indefinitely in the warm tier.
Type: Boolean
Required: No

## See Also
<a name="API_WarmTierRetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WarmTierRetentionPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WarmTierRetentionPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WarmTierRetentionPeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
