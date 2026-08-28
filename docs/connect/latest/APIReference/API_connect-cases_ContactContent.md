---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ContactContent.html
---

# ContactContent
<a name="API_connect-cases_ContactContent"></a>

An object that represents a content of an Connect Customer contact object.

## Contents
<a name="API_connect-cases_ContactContent_Contents"></a>

 ** channel **   <a name="connect-Type-connect-cases_ContactContent-channel"></a>
A list of channels to filter on for related items of type `Contact`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** connectedToSystemTime **   <a name="connect-Type-connect-cases_ContactContent-connectedToSystemTime"></a>
The difference between the `InitiationTimestamp` and the `DisconnectTimestamp` of the contact.
Type: Timestamp
Required: Yes

 ** contactArn **   <a name="connect-Type-connect-cases_ContactContent-contactArn"></a>
A unique identifier of a contact in Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## See Also
<a name="API_connect-cases_ContactContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/ContactContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/ContactContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/ContactContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
