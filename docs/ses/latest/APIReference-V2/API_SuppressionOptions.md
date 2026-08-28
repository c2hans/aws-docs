---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressionOptions.html
---

# SuppressionOptions
<a name="API_SuppressionOptions"></a>

An object that contains information about the suppression list preferences for your account or for a specific tenant.

## Contents
<a name="API_SuppressionOptions_Contents"></a>

 ** SuppressedReasons **   <a name="SES-Type-SuppressionOptions-SuppressedReasons"></a>
A list that contains the reasons that email addresses are automatically added to the suppression list for your account or for a specific tenant. This list can contain any or all of the following:
+  `COMPLAINT` – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a complaint.
+  `BOUNCE` – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a hard bounce.
Type: Array of strings
Valid Values: `BOUNCE | COMPLAINT`
Required: No

 ** SuppressionScope **   <a name="SES-Type-SuppressionOptions-SuppressionScope"></a>
The suppression scope for the configuration set. This overrides the tenant or account suppression scope for emails sent using this configuration set. Can be one of the following:
+  `TENANT` – Use the tenant's suppression list.
+  `ACCOUNT` – Use the account-level suppression list.
Type: String
Valid Values: `ACCOUNT | TENANT`
Required: No

 ** ValidationOptions **   <a name="SES-Type-SuppressionOptions-ValidationOptions"></a>
Contains validation options for email address suppression.
Type: [SuppressionValidationOptions](API_SuppressionValidationOptions.md) object
Required: No

## See Also
<a name="API_SuppressionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
