---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SuppressionPeriod.html
---

# SuppressionPeriod
<a name="API_SuppressionPeriod"></a>

If you are suppressing an anomaly temporariliy, this structure defines how long the suppression period is to be.

## Contents
<a name="API_SuppressionPeriod_Contents"></a>

 ** suppressionUnit **   <a name="CWL-Type-SuppressionPeriod-suppressionUnit"></a>
Specifies whether the value of `value` is in seconds, minutes, or hours.
Type: String
Valid Values: `SECONDS | MINUTES | HOURS`
Required: No

 ** value **   <a name="CWL-Type-SuppressionPeriod-value"></a>
Specifies the number of seconds, minutes or hours to suppress this anomaly. There is no maximum.
Type: Integer
Required: No

## See Also
<a name="API_SuppressionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SuppressionPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SuppressionPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SuppressionPeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
