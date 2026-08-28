---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressedDestinationAttributes.html
---

# SuppressedDestinationAttributes
<a name="API_SuppressedDestinationAttributes"></a>

An object that contains additional attributes that are related an email address that is on the suppression list for your account or for a specific tenant.

## Contents
<a name="API_SuppressedDestinationAttributes_Contents"></a>

 ** FeedbackId **   <a name="SES-Type-SuppressedDestinationAttributes-FeedbackId"></a>
A unique identifier that's generated when an email address is added to the suppression list for your account or for a specific tenant.
Type: String
Required: No

 ** MessageId **   <a name="SES-Type-SuppressedDestinationAttributes-MessageId"></a>
The unique identifier of the email message that caused the email address to be added to the suppression list for your account or for a specific tenant.
Type: String
Required: No

## See Also
<a name="API_SuppressedDestinationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressedDestinationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressedDestinationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressedDestinationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
