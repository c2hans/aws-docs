---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_PhoneNumber.html
---

# PhoneNumber
<a name="API_PhoneNumber"></a>

The phone number associated with the user.

## Contents
<a name="API_PhoneNumber_Contents"></a>

 ** Primary **   <a name="singlesignon-Type-PhoneNumber-Primary"></a>
A Boolean value representing whether this is the primary phone number for the associated resource.
Type: Boolean
Required: No

 ** Type **   <a name="singlesignon-Type-PhoneNumber-Type"></a>
A string representing the type of a phone number. For example, "Mobile."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Value **   <a name="singlesignon-Type-PhoneNumber-Value"></a>
A string containing a phone number. For example, "8675309" or "\+1 (800) 123-4567".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## See Also
<a name="API_PhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/PhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/PhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/PhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Identity Store. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
