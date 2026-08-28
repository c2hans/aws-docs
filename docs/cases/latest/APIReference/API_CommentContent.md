---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CommentContent.html
---

# CommentContent
<a name="API_connect-cases_CommentContent"></a>

Represents the content of a `Comment` to be returned to agents.

## Contents
<a name="API_connect-cases_CommentContent_Contents"></a>

 ** body **   <a name="connect-Type-connect-cases_CommentContent-body"></a>
Text in the body of a `Comment` on a case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15000.
Required: Yes

 ** contentType **   <a name="connect-Type-connect-cases_CommentContent-contentType"></a>
Type of the text in the box of a `Comment` on a case.
Type: String
Valid Values: `Text/Plain`
Required: Yes

## See Also
<a name="API_connect-cases_CommentContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CommentContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CommentContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CommentContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
