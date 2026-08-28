---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_FormatOptions.html
---

# FormatOptions
<a name="API_FormatOptions"></a>

Formatting options for a file.

## Contents
<a name="API_FormatOptions_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** tsvOptions **   <a name="omics-Type-FormatOptions-tsvOptions"></a>
Options for a TSV file.
Type: [TsvOptions](API_TsvOptions.md) object
Required: No

 ** vcfOptions **   <a name="omics-Type-FormatOptions-vcfOptions"></a>
Options for a VCF file.
Type: [VcfOptions](API_VcfOptions.md) object
Required: No

## See Also
<a name="API_FormatOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/FormatOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/FormatOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/FormatOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
