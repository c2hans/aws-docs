---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_RawMessageContent.html
---

# RawMessageContent
<a name="API_messageflow_RawMessageContent"></a>

Provides the MIME content of the updated email message as an S3 object. All MIME content must meet the following criteria:
+ Each part of a multipart MIME message must be formatted properly.
+ Attachments must be of a content type that Amazon SES supports. For more information, see [Unsupported Attachment Types](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types-appendix.html).
+ If any of the MIME parts in a message contain content that is outside of the 7-bit ASCII character range, we recommend encoding that content.
+ Per [RFC 5321](https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6), the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.
+ The message must contain all the required header fields. Check the returned error message for more information.
+ The value of immutable headers must remain unchanged. Check the returned error message for more information.
+ Certain unique headers can only appear once. Check the returned error message for more information.

## Contents
<a name="API_messageflow_RawMessageContent_Contents"></a>

 ** s3Reference **   <a name="workmail-Type-messageflow_RawMessageContent-s3Reference"></a>
The S3 reference of an email message.
Type: [S3Reference](API_messageflow_S3Reference.md) object
Required: Yes

## See Also
<a name="API_messageflow_RawMessageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmailmessageflow-2019-05-01/RawMessageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmailmessageflow-2019-05-01/RawMessageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmailmessageflow-2019-05-01/RawMessageContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
