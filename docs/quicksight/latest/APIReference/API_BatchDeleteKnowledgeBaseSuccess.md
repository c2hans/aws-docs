---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDeleteKnowledgeBaseSuccess.html
---

# BatchDeleteKnowledgeBaseSuccess
<a name="API_BatchDeleteKnowledgeBaseSuccess"></a>

Information about a knowledge base that was successfully deleted in a batch operation.

## Contents
<a name="API_BatchDeleteKnowledgeBaseSuccess_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KnowledgeBaseArn **   <a name="QS-Type-BatchDeleteKnowledgeBaseSuccess-KnowledgeBaseArn"></a>
The ARN of the successfully deleted knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** KnowledgeBaseId **   <a name="QS-Type-BatchDeleteKnowledgeBaseSuccess-KnowledgeBaseId"></a>
The unique identifier of the successfully deleted knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## See Also
<a name="API_BatchDeleteKnowledgeBaseSuccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDeleteKnowledgeBaseSuccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDeleteKnowledgeBaseSuccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDeleteKnowledgeBaseSuccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
