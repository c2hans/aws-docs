---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDeleteKnowledgeBaseFailure.html
---

# BatchDeleteKnowledgeBaseFailure
<a name="API_BatchDeleteKnowledgeBaseFailure"></a>

Information about a knowledge base that failed to be deleted in a batch operation.

## Contents
<a name="API_BatchDeleteKnowledgeBaseFailure_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="QS-Type-BatchDeleteKnowledgeBaseFailure-ErrorCode"></a>
The error code for the deletion failure.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="QS-Type-BatchDeleteKnowledgeBaseFailure-ErrorMessage"></a>
The error message for the deletion failure.
Type: String
Required: Yes

 ** KnowledgeBaseId **   <a name="QS-Type-BatchDeleteKnowledgeBaseFailure-KnowledgeBaseId"></a>
The unique identifier of the knowledge base that failed to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## See Also
<a name="API_BatchDeleteKnowledgeBaseFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDeleteKnowledgeBaseFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDeleteKnowledgeBaseFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDeleteKnowledgeBaseFailure)
