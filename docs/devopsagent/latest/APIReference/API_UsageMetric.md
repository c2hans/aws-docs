---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UsageMetric.html
---

# UsageMetric
<a name="API_UsageMetric"></a>

Represents a usage metric with its configured limit and current usage value.

## Contents
<a name="API_UsageMetric_Contents"></a>

 ** limit **   <a name="devopsagent-Type-UsageMetric-limit"></a>
Configured limit for this metric. A value of -1 indicates no limit is enforced.
Type: Integer
Required: Yes

 ** usage **   <a name="devopsagent-Type-UsageMetric-usage"></a>
Current usage for this metric
Type: Double
Required: Yes

## See Also
<a name="API_UsageMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UsageMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UsageMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UsageMetric)
