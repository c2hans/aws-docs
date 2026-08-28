---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AttachmentContent.html
---

# AttachmentContent
<a name="API_AttachmentContent"></a>

A structure that includes attributes that describe a document attachment.

## Contents
<a name="API_AttachmentContent_Contents"></a>

 ** Hash **   <a name="systemsmanager-Type-AttachmentContent-Hash"></a>
The cryptographic hash value of the document content.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** HashType **   <a name="systemsmanager-Type-AttachmentContent-HashType"></a>
The hash algorithm used to calculate the hash value.
Type: String
Valid Values: `Sha256`
Required: No

 ** Name **   <a name="systemsmanager-Type-AttachmentContent-Name"></a>
The name of an attachment.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** Size **   <a name="systemsmanager-Type-AttachmentContent-Size"></a>
The size of an attachment in bytes.
Type: Long
Required: No

 ** Url **   <a name="systemsmanager-Type-AttachmentContent-Url"></a>
The URL location of the attachment content.
Type: String
Required: No

## See Also
<a name="API_AttachmentContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AttachmentContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AttachmentContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AttachmentContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
