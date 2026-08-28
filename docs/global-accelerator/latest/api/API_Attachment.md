---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_Attachment.html
---

# Attachment
<a name="API_Attachment"></a>

A cross-account attachment in AWS Global Accelerator. A cross-account attachment specifies the *principals* who have permission to work with *resources* in your account, which you also list in the attachment.

## Contents
<a name="API_Attachment_Contents"></a>

 ** AttachmentArn **   <a name="globalaccelerator-Type-Attachment-AttachmentArn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreatedTime **   <a name="globalaccelerator-Type-Attachment-CreatedTime"></a>
The date and time that the cross-account attachment was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="globalaccelerator-Type-Attachment-LastModifiedTime"></a>
The date and time that the cross-account attachment was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="globalaccelerator-Type-Attachment-Name"></a>
The name of the cross-account attachment.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S\s]+`
Required: No

 ** Principals **   <a name="globalaccelerator-Type-Attachment-Principals"></a>
The principals included in the cross-account attachment.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `(^\d{12}$|arn:.*)`
Required: No

 ** Resources **   <a name="globalaccelerator-Type-Attachment-Resources"></a>
The resources included in the cross-account attachment.
Type: Array of [Resource](API_Resource.md) objects
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/Attachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/Attachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/Attachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
