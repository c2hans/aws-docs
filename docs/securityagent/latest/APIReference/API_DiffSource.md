---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DiffSource.html
---

# DiffSource
<a name="API_DiffSource"></a>

Source of the diff for a differential code scan.

## Contents
<a name="API_DiffSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3Uri **   <a name="securityagent-Type-DiffSource-s3Uri"></a>
S3 URI pointing to a unified diff file. The file must be in standard unified diff format and stored in an S3 bucket connected to your Agent Space.
Type: String
Required: No

## See Also
<a name="API_DiffSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DiffSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DiffSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DiffSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
