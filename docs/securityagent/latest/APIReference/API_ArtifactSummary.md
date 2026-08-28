---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ArtifactSummary.html
---

# ArtifactSummary
<a name="API_ArtifactSummary"></a>

Contains summary information about an artifact.

## Contents
<a name="API_ArtifactSummary_Contents"></a>

 ** artifactId **   <a name="securityagent-Type-ArtifactSummary-artifactId"></a>
The unique identifier of the artifact.
Type: String
Required: Yes

 ** artifactType **   <a name="securityagent-Type-ArtifactSummary-artifactType"></a>
The file type of the artifact.
Type: String
Valid Values: `TXT | PNG | JPEG | MD | PDF | DOCX | DOC | JSON | YAML`
Required: Yes

 ** fileName **   <a name="securityagent-Type-ArtifactSummary-fileName"></a>
The file name of the artifact.
Type: String
Required: Yes

## See Also
<a name="API_ArtifactSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ArtifactSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ArtifactSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ArtifactSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
