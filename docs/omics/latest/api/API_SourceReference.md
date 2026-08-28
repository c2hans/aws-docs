---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_SourceReference.html
---

# SourceReference
<a name="API_SourceReference"></a>

Contains information about the source reference in a code repository, such as a branch, tag, or commit.

## Contents
<a name="API_SourceReference_Contents"></a>

 ** type **   <a name="omics-Type-SourceReference-type"></a>
The type of source reference, such as branch, tag, or commit.
Type: String
Valid Values: `BRANCH | TAG | COMMIT`
Required: Yes

 ** value **   <a name="omics-Type-SourceReference-value"></a>
The value of the source reference, such as the branch name, tag name, or commit ID.
Type: String
Required: Yes

## See Also
<a name="API_SourceReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/SourceReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/SourceReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/SourceReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
