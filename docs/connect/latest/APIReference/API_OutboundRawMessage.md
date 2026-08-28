---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundRawMessage.html
---

# OutboundRawMessage
<a name="API_OutboundRawMessage"></a>

Information about the raw email body content.

## Contents
<a name="API_OutboundRawMessage_Contents"></a>

 ** Body **   <a name="connect-Type-OutboundRawMessage-Body"></a>
The email message body.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: Yes

 ** ContentType **   <a name="connect-Type-OutboundRawMessage-ContentType"></a>
Type of content, that is, `text/plain` or `text/html`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Subject **   <a name="connect-Type-OutboundRawMessage-Subject"></a>
The email subject.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 998.
Required: Yes

## See Also
<a name="API_OutboundRawMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/OutboundRawMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/OutboundRawMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/OutboundRawMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
