---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_SMSSandboxPhoneNumber.html
---

# SMSSandboxPhoneNumber
<a name="API_SMSSandboxPhoneNumber"></a>

A verified or pending destination phone number in the SMS sandbox.

When you start using Amazon SNS to send SMS messages, your AWS account is in the *SMS sandbox*. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your AWS account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) in the *Amazon SNS Developer Guide*.

## Contents
<a name="API_SMSSandboxPhoneNumber_Contents"></a>

 ** PhoneNumber **
The destination phone number.
Type: String
Length Constraints: Maximum length of 20.
Pattern: `^(\+[0-9]{8,}|[0-9]{0,9})$`
Required: No

 ** Status **
The destination phone number's verification status.
Type: String
Valid Values: `Pending | Verified`
Required: No

## See Also
<a name="API_SMSSandboxPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SMSSandboxPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SMSSandboxPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/SMSSandboxPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
