---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_BatchGetCalculatedAttributeForProfileError.html
---

# BatchGetCalculatedAttributeForProfileError
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfileError"></a>

Error object describing why a specific profile and calculated attribute failed.

## Contents
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfileError_Contents"></a>

 ** Code **   <a name="connect-Type-connect-customer-profiles_BatchGetCalculatedAttributeForProfileError-Code"></a>
Status code for why a specific profile and calculated attribute failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Message **   <a name="connect-Type-connect-customer-profiles_BatchGetCalculatedAttributeForProfileError-Message"></a>
Message describing why a specific profile and calculated attribute failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** ProfileId **   <a name="connect-Type-connect-customer-profiles_BatchGetCalculatedAttributeForProfileError-ProfileId"></a>
The profile id that failed.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfileError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfileError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfileError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfileError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
