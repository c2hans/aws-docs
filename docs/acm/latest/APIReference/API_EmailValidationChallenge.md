---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_EmailValidationChallenge.html
---

# EmailValidationChallenge
<a name="API_EmailValidationChallenge"></a>

Contains the email addresses used for email-based domain validation.

## Contents
<a name="API_EmailValidationChallenge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValidationDomain **   <a name="ACM-Type-EmailValidationChallenge-ValidationDomain"></a>
The domain name that ACM uses to send validation emails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: No

 ** ValidationEmails **   <a name="ACM-Type-EmailValidationChallenge-ValidationEmails"></a>
A list of email addresses that ACM uses to send domain validation emails.
Type: Array of strings
Required: No

## See Also
<a name="API_EmailValidationChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/EmailValidationChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/EmailValidationChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/EmailValidationChallenge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
