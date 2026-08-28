---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_RelatedItemUpdateContent.html
---

# RelatedItemUpdateContent
<a name="API_connect-cases_RelatedItemUpdateContent"></a>

Represents the content of a related item to be updated. This is a union type that can contain either comment content or custom content.

## Contents
<a name="API_connect-cases_RelatedItemUpdateContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** comment **   <a name="connect-Type-connect-cases_RelatedItemUpdateContent-comment"></a>
Represents the updated content of a `Comment` related item.
Type: [CommentUpdateContent](API_connect-cases_CommentUpdateContent.md) object
Required: No

 ** custom **   <a name="connect-Type-connect-cases_RelatedItemUpdateContent-custom"></a>
Represents the updated content of a `Custom` related item.
Type: [CustomUpdateContent](API_connect-cases_CustomUpdateContent.md) object
Required: No

## See Also
<a name="API_connect-cases_RelatedItemUpdateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RelatedItemUpdateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RelatedItemUpdateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RelatedItemUpdateContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
