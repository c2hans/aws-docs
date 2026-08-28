---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesTrendsMetricsResult.html
---

# ResourcesTrendsMetricsResult
<a name="API_ResourcesTrendsMetricsResult"></a>

Contains the resource trend metrics data for a specific time point in the requested time period.

## Contents
<a name="API_ResourcesTrendsMetricsResult_Contents"></a>

 ** Timestamp **   <a name="securityhub-Type-ResourcesTrendsMetricsResult-Timestamp"></a>
The timestamp for this data point in the resources trend metrics.
Type: Timestamp
Required: Yes

 ** TrendsValues **   <a name="securityhub-Type-ResourcesTrendsMetricsResult-TrendsValues"></a>
The resource trend metric values associated with this timestamp, including resource counts.
Type: [ResourcesTrendsValues](API_ResourcesTrendsValues.md) object
Required: Yes

## See Also
<a name="API_ResourcesTrendsMetricsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesTrendsMetricsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesTrendsMetricsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesTrendsMetricsResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
