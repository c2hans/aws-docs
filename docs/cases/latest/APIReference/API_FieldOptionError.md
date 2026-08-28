---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_FieldOptionError.html
---

# FieldOptionError
<a name="API_connect-cases_FieldOptionError"></a>

Object for field Options errors.

## Contents
<a name="API_connect-cases_FieldOptionError_Contents"></a>

 ** errorCode **   <a name="connect-Type-connect-cases_FieldOptionError-errorCode"></a>
Error code from creating or updating field option.
Type: String
Required: Yes

 ** message **   <a name="connect-Type-connect-cases_FieldOptionError-message"></a>
Error message from creating or updating field option.
Type: String
Required: Yes

 ** value **   <a name="connect-Type-connect-cases_FieldOptionError-value"></a>
The field option value that caused the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

## See Also
<a name="API_connect-cases_FieldOptionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldOptionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldOptionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldOptionError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
