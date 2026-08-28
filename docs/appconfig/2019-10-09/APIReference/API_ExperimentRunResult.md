---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExperimentRunResult.html
---

# ExperimentRunResult
<a name="API_ExperimentRunResult"></a>

The result of an experiment run, including the executive summary and launch decision rationale.

## Contents
<a name="API_ExperimentRunResult_Contents"></a>

 ** ExecutiveSummary **   <a name="appconfig-Type-ExperimentRunResult-ExecutiveSummary"></a>
A summary of the experiment outcome and key findings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ReasonsNotToLaunch **   <a name="appconfig-Type-ExperimentRunResult-ReasonsNotToLaunch"></a>
Evidence against launching the treatment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ReasonsToLaunch **   <a name="appconfig-Type-ExperimentRunResult-ReasonsToLaunch"></a>
Evidence in favor of launching the winning treatment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ExperimentRunResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExperimentRunResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExperimentRunResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExperimentRunResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
