---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_MetadataFormSummary.html
---

# MetadataFormSummary
<a name="API_MetadataFormSummary"></a>

The summary of the metadata form.

## Contents
<a name="API_MetadataFormSummary_Contents"></a>

 ** typeName **   <a name="datazone-Type-MetadataFormSummary-typeName"></a>
The type name of the metadata form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** typeRevision **   <a name="datazone-Type-MetadataFormSummary-typeRevision"></a>
The type revision of the metadata form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** formName **   <a name="datazone-Type-MetadataFormSummary-formName"></a>
The form name of the metadata form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: No

## See Also
<a name="API_MetadataFormSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/MetadataFormSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/MetadataFormSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/MetadataFormSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
