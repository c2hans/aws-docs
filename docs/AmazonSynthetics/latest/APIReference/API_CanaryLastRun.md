---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryLastRun.html
---

# CanaryLastRun
<a name="API_CanaryLastRun"></a>

This structure contains information about the most recent run of a single canary.

## Contents
<a name="API_CanaryLastRun_Contents"></a>

 ** CanaryName **   <a name="synthetics-Type-CanaryLastRun-CanaryName"></a>
The name of the canary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: No

 ** LastRun **   <a name="synthetics-Type-CanaryLastRun-LastRun"></a>
The results from this canary's most recent run.
Type: [CanaryRun](API_CanaryRun.md) object
Required: No

## See Also
<a name="API_CanaryLastRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryLastRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryLastRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryLastRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
