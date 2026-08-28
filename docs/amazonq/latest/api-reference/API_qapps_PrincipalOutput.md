---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PrincipalOutput.html
---

# PrincipalOutput
<a name="API_qapps_PrincipalOutput"></a>

The principal for which the permission applies.

## Contents
<a name="API_qapps_PrincipalOutput_Contents"></a>

 ** email **   <a name="qbusiness-Type-qapps_PrincipalOutput-email"></a>
The email address associated with the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** userId **   <a name="qbusiness-Type-qapps_PrincipalOutput-userId"></a>
The unique identifier of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** userType **   <a name="qbusiness-Type-qapps_PrincipalOutput-userType"></a>
The type of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Valid Values: `owner | user`
Required: No

## See Also
<a name="API_qapps_PrincipalOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/PrincipalOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/PrincipalOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/PrincipalOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
