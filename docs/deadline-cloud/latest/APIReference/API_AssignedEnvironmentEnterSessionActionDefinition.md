---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedEnvironmentEnterSessionActionDefinition.html
---

# AssignedEnvironmentEnterSessionActionDefinition
<a name="API_AssignedEnvironmentEnterSessionActionDefinition"></a>

The assigned starting environment for a worker during session.

## Contents
<a name="API_AssignedEnvironmentEnterSessionActionDefinition_Contents"></a>

 ** environmentId **   <a name="deadlinecloud-Type-AssignedEnvironmentEnterSessionActionDefinition-environmentId"></a>
The environment ID of the assigned environment at the start of a session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

## See Also
<a name="API_AssignedEnvironmentEnterSessionActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedEnvironmentEnterSessionActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedEnvironmentEnterSessionActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedEnvironmentEnterSessionActionDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
