---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ResponseSpecification.html
---

# ResponseSpecification
<a name="API_ResponseSpecification"></a>

Specifies a list of message groups that Amazon Lex uses to respond the user input.

## Contents
<a name="API_ResponseSpecification_Contents"></a>

 ** messageGroups **   <a name="lexv2-Type-ResponseSpecification-messageGroups"></a>
A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.
Type: Array of [MessageGroup](API_MessageGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** allowInterrupt **   <a name="lexv2-Type-ResponseSpecification-allowInterrupt"></a>
Indicates whether the user can interrupt a speech response from Amazon Lex.
Type: Boolean
Required: No

## See Also
<a name="API_ResponseSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ResponseSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ResponseSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ResponseSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
