---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Reference.html
---

# Reference
<a name="API_Reference"></a>

Well-formed data on a contact, used by agents to complete a contact request. You can have up to 4,096 UTF-8 bytes across all references for a contact.

## Contents
<a name="API_Reference_Contents"></a>

 ** Type **   <a name="connect-Type-Reference-Type"></a>
The type of the reference. `DATE` must be of type Epoch timestamp.
Type: String
Valid Values: `URL | ATTACHMENT | CONTACT_ANALYSIS | NUMBER | STRING | DATE | EMAIL | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | EMAIL_MESSAGE_REDACTED`
Required: Yes

 ** Arn **   <a name="connect-Type-Reference-Arn"></a>
The Amazon Resource Name (ARN) of the reference
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `^[-:/A-Za-z0-9]+`
Required: No

 ** Status **   <a name="connect-Type-Reference-Status"></a>
Status of the attachment reference type.
Type: String
Valid Values: `AVAILABLE | DELETED | APPROVED | REJECTED | PROCESSING | FAILED`
Required: No

 ** StatusReason **   <a name="connect-Type-Reference-StatusReason"></a>
Relevant details why the reference was not successfully created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** Value **   <a name="connect-Type-Reference-Value"></a>
A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_Reference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Reference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Reference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Reference)
