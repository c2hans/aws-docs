---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeneratedAnswerResult.html
---

# GeneratedAnswerResult
<a name="API_GeneratedAnswerResult"></a>

The QA result that is made from generated answer.

## Contents
<a name="API_GeneratedAnswerResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnswerId **   <a name="QS-Type-GeneratedAnswerResult-AnswerId"></a>
The ID of the answer.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: No

 ** AnswerStatus **   <a name="QS-Type-GeneratedAnswerResult-AnswerStatus"></a>
The answer status of the generated answer.
Type: String
Valid Values: `ANSWER_GENERATED | ANSWER_RETRIEVED | ANSWER_DOWNGRADE`
Required: No

 ** QuestionId **   <a name="QS-Type-GeneratedAnswerResult-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** QuestionText **   <a name="QS-Type-GeneratedAnswerResult-QuestionText"></a>
The question text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QuestionUrl **   <a name="QS-Type-GeneratedAnswerResult-QuestionUrl"></a>
The URL of the question.
Type: String
Required: No

 ** Restatement **   <a name="QS-Type-GeneratedAnswerResult-Restatement"></a>
The restatement for the answer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** TopicId **   <a name="QS-Type-GeneratedAnswerResult-TopicId"></a>
The ID of the topic.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: No

 ** TopicName **   <a name="QS-Type-GeneratedAnswerResult-TopicName"></a>
The name of the topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_GeneratedAnswerResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeneratedAnswerResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeneratedAnswerResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeneratedAnswerResult)
