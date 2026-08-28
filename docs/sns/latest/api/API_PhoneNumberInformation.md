---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_PhoneNumberInformation.html
---

# PhoneNumberInformation
<a name="API_PhoneNumberInformation"></a>

A list of phone numbers and their metadata.

## Contents
<a name="API_PhoneNumberInformation_Contents"></a>

 ** CreatedAt **
The date and time when the phone number was created.
Type: Timestamp
Required: No

 ** Iso2CountryCode **
The two-character code for the country or region, in ISO 3166-1 alpha-2 format.
Type: String
Length Constraints: Maximum length of 2.
Pattern: `^[A-Za-z]{2}$`
Required: No

 ** NumberCapabilities.member.N **
The capabilities of each phone number.
Type: Array of strings
Valid Values: `SMS | MMS | VOICE`
Required: No

 ** PhoneNumber **
The phone number.
Type: String
Required: No

 ** RouteType **
The list of supported routes.
Type: String
Valid Values: `Transactional | Promotional | Premium`
Required: No

 ** Status **
The status of the phone number.
Type: String
Required: No

## See Also
<a name="API_PhoneNumberInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/PhoneNumberInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/PhoneNumberInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/PhoneNumberInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
