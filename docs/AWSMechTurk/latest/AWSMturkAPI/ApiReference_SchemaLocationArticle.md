---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_SchemaLocationArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# Data Structure Schema Locations
<a name="ApiReference_SchemaLocationArticle"></a>

**Topics**

 The Amazon Mechanical Turk uses several XML data structures to help you define your tasks flexibly. These data structures are specified using schemas that are versioned. This allows MTurk to add new versions of task types while preserving backwards compatibility.

 When constructing an XML object for any of these structures, you must declare a namespace that matches the target namespace for the schema for the structure. The namespace is defined using the URL to the schema definition. For example, here is how to declare your namespace when constructing an HTMLQuestion:

```
<HTMLQuestion
xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
{{[...]}}
</HTMLQuestion>
```

 If the service returns an error message about data not validating against the schema, make sure your namespace declaration matches the target namespace specified in the schema.

**Important**
Beginning Tuesday, December 12th 2017 the [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) structure will **no longer support the `FileUploadAnswer` element and the `Application` element.** The **2017-11-06** version of the QuestionForm schema has been updated to reflect these changes. If you don't use the deprecated elements in your QuestionForm, the **2005-10-01** schema will continue to work.

 You can find the schema namespace values for all of the question and answer data structures below:

|  Type of Schema  |  Latest Version  |  Schema Namespace |
| --- | --- | --- |
|  The [HTMLQuestion](ApiReference_HTMLQuestionArticle.md) schema  |  2011-11-11  |  [Download HTMLQuestion.zip](samples/HTMLQuestion.zip)  |
|  The [ExternalQuestion](ApiReference_ExternalQuestionArticle.md) schema  |  2006-07-14  |  [Download ExternalQuestion.zip](samples/ExternalQuestion.zip)  |
|  The [Formatted Content: XHTML](ApiReference_FormattedContentXHTMLArticle.md) subset |  2006-07-14  |  [Download FormattedContentXHTMLSubset.zip](samples/FormattedContentXHTMLSubset.zip)  |
| The [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) schemas  | 2017-11-06 |  [Download QuestionForm.zip](samples/QuestionForm.zip) |
|  The [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md) schemas  |  2005-10-01  |  [Download QuestionFormAnswers.zip](samples/QuestionFormAnswers.zip)  |
|  The [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md) schemas schemas  |  2005-10-01  |  [Download AnswerKey.zip](samples/AnswerKey.zip)  |
