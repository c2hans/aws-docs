---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_WorkloadProfile.html
---

# WorkloadProfile
<a name="API_WorkloadProfile"></a>

The profile associated with a workload.

## Contents
<a name="API_WorkloadProfile_Contents"></a>

 ** ProfileArn **   <a name="wellarchitected-Type-WorkloadProfile-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ProfileVersion **   <a name="wellarchitected-Type-WorkloadProfile-ProfileVersion"></a>
The profile version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[A-Za-z0-9-]+$`
Required: No

## See Also
<a name="API_WorkloadProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/WorkloadProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/WorkloadProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/WorkloadProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
