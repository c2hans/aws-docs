---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_BounceAction.html
---

# BounceAction
<a name="API_BounceAction"></a>

The action to send a bounce response for the email. When executed, this action generates a non-delivery report (bounce) back to the sender.

## Contents
<a name="API_BounceAction_Contents"></a>

 ** DiagnosticMessage **   <a name="sesmailmanager-Type-BounceAction-DiagnosticMessage"></a>
The diagnostic message included in the Diagnostic-Code header of the bounce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x20-\x7e]+`
Required: Yes

 ** RoleArn **   <a name="sesmailmanager-Type-BounceAction-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to use to send the bounce message.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** Sender **   <a name="sesmailmanager-Type-BounceAction-Sender"></a>
The sender email address of the bounce message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 254.
Pattern: `[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+`
Required: Yes

 ** SmtpReplyCode **   <a name="sesmailmanager-Type-BounceAction-SmtpReplyCode"></a>
The SMTP reply code for the bounce, as defined by RFC 5321.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[45][0-9][0-9]`
Required: Yes

 ** StatusCode **   <a name="sesmailmanager-Type-BounceAction-StatusCode"></a>
The enhanced status code for the bounce, in the format of x.y.z (e.g. 5.1.1).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 9.
Pattern: `[45]\.[0-9]{1,3}\.[0-9]{1,3}`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-BounceAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the SendBounce API.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

 ** Message **   <a name="sesmailmanager-Type-BounceAction-Message"></a>
The human-readable text to include in the bounce message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[\r\n\x20-\x7e]+`
Required: No

## See Also
<a name="API_BounceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/BounceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/BounceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/BounceAction)
