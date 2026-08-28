---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ExtensionField.html
---

# ExtensionField
<a name="API_ExtensionField"></a>

Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html).

## Contents
<a name="API_ExtensionField_Contents"></a>

 ** Name **
The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
Type: String
Required: Yes

 ** Value **
The value of the header to add. Must contain 2048 characters or fewer, and must not contain newline characters ("\\r" or "\\n").
Type: String
Required: Yes

## See Also
<a name="API_ExtensionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ExtensionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ExtensionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ExtensionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
