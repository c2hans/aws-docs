---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateError.html
---

# UpdateError
<a name="API_UpdateError"></a>

Describes the error(s) encountered with the last update of the environment.

## Contents
<a name="API_UpdateError_Contents"></a>

 ** ErrorCode **   <a name="mwaa-Type-UpdateError-ErrorCode"></a>
The error code that corresponds to the error with the last update.
Type: String
Required: No

 ** ErrorMessage **   <a name="mwaa-Type-UpdateError-ErrorMessage"></a>
The error message that corresponds to the error code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## See Also
<a name="API_UpdateError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/UpdateError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/UpdateError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/UpdateError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MWAA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
