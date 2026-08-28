---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MetricDataResult.html
---

# MetricDataResult
<a name="API_MetricDataResult"></a>

The result of a single metric data query.

## Contents
<a name="API_MetricDataResult_Contents"></a>

 ** Id **   <a name="SES-Type-MetricDataResult-Id"></a>
The query identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Timestamps **   <a name="SES-Type-MetricDataResult-Timestamps"></a>
A list of timestamps for the metric data results.
Type: Array of timestamps
Required: No

 ** Values **   <a name="SES-Type-MetricDataResult-Values"></a>
A list of values (cumulative / sum) for the metric data results.
Type: Array of longs
Required: No

## See Also
<a name="API_MetricDataResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MetricDataResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MetricDataResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MetricDataResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
