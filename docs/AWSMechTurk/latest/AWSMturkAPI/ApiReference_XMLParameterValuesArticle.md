---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_XMLParameterValuesArticle.html
---

# Using XML Parameter Values
<a name="ApiReference_XMLParameterValuesArticle"></a>

 The [HTMLQuestion](ApiReference_HTMLQuestionArticle.md#ApiReference_HTMLQuestionArticle.title),[ExternalQuestion](ApiReference_ExternalQuestionArticle.md#ApiReference_ExternalQuestionArticle.title), [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md#ApiReference_QuestionFormDataStructureArticle.title), [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md#ApiReference_QuestionFormAnswersDataStructureArticle.title), and [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md#ApiReference_AnswerKeyDataStructureArticle.title) data structures are used as parameter values in service requests, and as return values in service responses. Unlike other data structures described in this API reference, these XML structures are not part of the service API directly, but rather are used as string values going in and out of the service. This article describes the encoding methods needed to use XML data as parameter and return values.

## XML Data as a Parameter
<a name="ApiReference_XMLParameterValuesArticle-xml-data-as-a-parameter"></a>

 Data must be *URL encoded* to appear as a single parameter value in the request. Characters that are part of URL syntax, such as question marks (**?**) and ampersands (**&**), must be replaced with the corresponding URL character codes.

**Note**
 XML data should only be URL encoded, *not* XML escaped.

 In service responses, this data will be XML escaped.

## Namespaces for XML Parameter Values
<a name="ApiReference_XMLParameterValuesArticle-namespaces-for-xml-parameter-values"></a>

 XML data in parameter values must have a namespace specified for all elements. The easiest way to do this is to include an `xmlns` attribute in the root element equal to the appropriate namespace.

 The namespace for a `HTMLQuestion`,`ExternalQuestion`, `QuestionForm`, `QuestionFormAnswers`, or `AnswerKey` element is identical to the URL of the corresponding schema document, including the version date. While XML namespaces need not be URLs according to the XML specification, this convention ensures that the consumer of the value knows which version of the schema is being used for the data.

 For the locations of the schema documents, as well as instructions on how to include the version date in the URL, see [Schema Locations](ApiReference_SchemaLocationArticle.md#ApiReference_SchemaLocationArticle.title).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
