---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttachmentReference.html
---

# AttachmentReference
<a name="API_AttachmentReference"></a>

Information about a reference when the `referenceType` is `ATTACHMENT`. Otherwise, null.

## Contents
<a name="API_AttachmentReference_Contents"></a>

 ** Arn **   <a name="connect-Type-AttachmentReference-Arn"></a>
The Amazon Resource Name (ARN) of the attachment reference.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `^[-:/A-Za-z0-9]+`
Required: No

 ** Name **   <a name="connect-Type-AttachmentReference-Name"></a>
Identifier of the attachment reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Status **   <a name="connect-Type-AttachmentReference-Status"></a>
Status of the attachment reference type.
Type: String
Valid Values: `AVAILABLE | DELETED | APPROVED | REJECTED | PROCESSING | FAILED`
Required: No

 ** Value **   <a name="connect-Type-AttachmentReference-Value"></a>
The location path of the attachment reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_AttachmentReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttachmentReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttachmentReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttachmentReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
