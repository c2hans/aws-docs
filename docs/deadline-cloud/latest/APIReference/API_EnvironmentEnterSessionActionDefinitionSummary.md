---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_EnvironmentEnterSessionActionDefinitionSummary.html
---

# EnvironmentEnterSessionActionDefinitionSummary
<a name="API_EnvironmentEnterSessionActionDefinitionSummary"></a>

Defines the environment a session action enters in.

## Contents
<a name="API_EnvironmentEnterSessionActionDefinitionSummary_Contents"></a>

 ** environmentId **   <a name="deadlinecloud-Type-EnvironmentEnterSessionActionDefinitionSummary-environmentId"></a>
The environment ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

## See Also
<a name="API_EnvironmentEnterSessionActionDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentEnterSessionActionDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentEnterSessionActionDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentEnterSessionActionDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
