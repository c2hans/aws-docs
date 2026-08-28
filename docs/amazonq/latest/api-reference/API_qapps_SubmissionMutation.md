---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_SubmissionMutation.html
---

# SubmissionMutation
<a name="API_qapps_SubmissionMutation"></a>

Represents an action performed on a submission.

## Contents
<a name="API_qapps_SubmissionMutation_Contents"></a>

 ** mutationType **   <a name="qbusiness-Type-qapps_SubmissionMutation-mutationType"></a>
The operation that is performed on a submission.
Type: String
Valid Values: `edit | delete | add`
Required: Yes

 ** submissionId **   <a name="qbusiness-Type-qapps_SubmissionMutation-submissionId"></a>
The unique identifier of the submission.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

## See Also
<a name="API_qapps_SubmissionMutation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/SubmissionMutation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/SubmissionMutation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/SubmissionMutation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
