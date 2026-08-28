---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UserFeedback.html
---

# UserFeedback
<a name="API_UserFeedback"></a>

Feedback that can be submitted for each instance of an anomaly by the user. Feedback is be used for improvements in generating recommendations for the application.

## Contents
<a name="API_UserFeedback_Contents"></a>

 ** type **   <a name="profiler-Type-UserFeedback-type"></a>
Optional `Positive` or `Negative` feedback submitted by the user about whether the recommendation is useful or not.
Type: String
Valid Values: `Positive | Negative`
Required: Yes

## See Also
<a name="API_UserFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/UserFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/UserFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/UserFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
