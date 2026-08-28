---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FormOutput.html
---

# FormOutput
<a name="API_FormOutput"></a>

The details of a metadata form.

## Contents
<a name="API_FormOutput_Contents"></a>

 ** formName **   <a name="datazone-Type-FormOutput-formName"></a>
The name of the metadata form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** content **   <a name="datazone-Type-FormOutput-content"></a>
The content of the metadata form.
Type: String
Required: No

 ** typeName **   <a name="datazone-Type-FormOutput-typeName"></a>
The name of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: No

 ** typeRevision **   <a name="datazone-Type-FormOutput-typeRevision"></a>
The revision of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_FormOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FormOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FormOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FormOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
