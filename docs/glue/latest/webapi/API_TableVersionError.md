---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableVersionError.html
---

# TableVersionError
<a name="API_TableVersionError"></a>

An error record for table-version operations.

## Contents
<a name="API_TableVersionError_Contents"></a>

 ** ErrorDetail **   <a name="Glue-Type-TableVersionError-ErrorDetail"></a>
The details about the error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** TableName **   <a name="Glue-Type-TableVersionError-TableName"></a>
The name of the table in question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** VersionId **   <a name="Glue-Type-TableVersionError-VersionId"></a>
The ID value of the version in question. A `VersionID` is a string representation of an integer. Each version is incremented by 1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TableVersionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableVersionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableVersionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableVersionError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
