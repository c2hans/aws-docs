---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressionAttributes.html
---

# SuppressionAttributes
<a name="API_SuppressionAttributes"></a>

An object that contains information about the email address suppression preferences for your account in the current AWS Region.

## Contents
<a name="API_SuppressionAttributes_Contents"></a>

 ** SuppressedReasons **   <a name="SES-Type-SuppressionAttributes-SuppressedReasons"></a>
A list that contains the reasons that email addresses will be automatically added to the suppression list for your account. This list can contain any or all of the following:
+  `COMPLAINT` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.
+  `BOUNCE` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.
Type: Array of strings
Valid Values: `BOUNCE | COMPLAINT`
Required: No

 ** ValidationAttributes **   <a name="SES-Type-SuppressionAttributes-ValidationAttributes"></a>
Structure containing validation attributes used for suppressing sending to specific destination on account level.
Type: [SuppressionValidationAttributes](API_SuppressionValidationAttributes.md) object
Required: No

## See Also
<a name="API_SuppressionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressionAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
