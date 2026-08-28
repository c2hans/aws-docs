---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ArtifactDetails.html
---

# ArtifactDetails
<a name="API_ArtifactDetails"></a>

Details about a generated artifact including location and status

## Contents
<a name="API_ArtifactDetails_Contents"></a>

 ** failureReason **   <a name="connecthealth-Type-ArtifactDetails-failureReason"></a>
The reason for failure if the artifact generation failed
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** outputLocation **   <a name="connecthealth-Type-ArtifactDetails-outputLocation"></a>

Type: String
Length Constraints: Minimum length of 1.
Pattern: `.*(s3://|http(s*)://).+.*`
Required: No

 ** status **   <a name="connecthealth-Type-ArtifactDetails-status"></a>
The generation status of the artifact
Type: String
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`
Required: No

## See Also
<a name="API_ArtifactDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/ArtifactDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/ArtifactDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/ArtifactDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
