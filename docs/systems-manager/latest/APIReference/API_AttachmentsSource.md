---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AttachmentsSource.html
---

# AttachmentsSource
<a name="API_AttachmentsSource"></a>

Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.

## Contents
<a name="API_AttachmentsSource_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-AttachmentsSource-Key"></a>
The key of a key-value pair that identifies the location of an attachment to a document.
Type: String
Valid Values: `SourceUrl | S3FileUrl | AttachmentReference`
Required: No

 ** Name **   <a name="systemsmanager-Type-AttachmentsSource-Name"></a>
The name of the document attachment file.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** Values **   <a name="systemsmanager-Type-AttachmentsSource-Values"></a>
The value of a key-value pair that identifies the location of an attachment to a document. The format for **Value** depends on the type of key you specify.
+ For the key *SourceUrl*, the value is an S3 bucket location. For example:

   `"Values": [ "s3://amzn-s3-demo-bucket/my-prefix" ]`
+ For the key *S3FileUrl*, the value is a file in an S3 bucket. For example:

   `"Values": [ "s3://amzn-s3-demo-bucket/my-prefix/my-file.py" ]`
+ For the key *AttachmentReference*, the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example:

   `"Values": [ "MyOtherDocument/3/my-other-file.py" ]`

  However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example:

   `"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]`
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_AttachmentsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AttachmentsSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AttachmentsSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AttachmentsSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
