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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
