---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ImportSource.html
---

# ImportSource
<a name="API_ImportSource"></a>

The source from which to import security requirements. Currently supports document uploads.

## Contents
<a name="API_ImportSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** documents **   <a name="securityagent-Type-ImportSource-documents"></a>
The list of documents to extract security requirements from.
Type: Array of [SecurityRequirementArtifact](API_SecurityRequirementArtifact.md) objects
Required: No

## See Also
<a name="API_ImportSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ImportSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ImportSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ImportSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
