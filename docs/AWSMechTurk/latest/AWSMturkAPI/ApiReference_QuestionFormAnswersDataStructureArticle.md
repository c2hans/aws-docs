---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QuestionFormAnswersDataStructureArticle.html
---

# QuestionFormAnswers
<a name="ApiReference_QuestionFormAnswersDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_QuestionFormAnswersDataStructureArticle-description)
+ [The Structure of Answers](#ApiReference_QuestionFormAnswersDataStructureArticle-the-structure-of-answers)
+ [Example](#ApiReference_QuestionFormAnswersDataStructureArticle-example)

## Description
<a name="ApiReference_QuestionFormAnswersDataStructureArticle-description"></a>

 The `QuestionFormAnswers` data format describes answers submitted by a Worker for a HIT, or for a Qualification test.

 A `QuestionFormAnswers` data structure is a string value that consists of XML data. The XML data must conform to the QuestionForm schema. See [Schema Locations](ApiReference_SchemaLocationArticle.md) for the location of this schema. For more information about using XML data as parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

**Note**
 Answer data is *not* guaranteed by the Amazon Mechanical Turk Service to conform to the answer specifications described in a QuestionForm. MTS only guarantees that answer data returned by the service will conform to the `QuestionFormAnswers` schema. Your application should check that the answer data sufficiently answers the question.

 The `QuestionFormAnswers` data structure is used as a response element for the following operations:
+  `GetAssignmentsForHIT`
+  `GetQualificationRequests`

 All elements in a `QuestionFormAnswers` belong to a namespace whose name is identical to the URL of the `QuestionFormAnswers` schema document for the version of the API you are using.

## The Structure of Answers
<a name="ApiReference_QuestionFormAnswersDataStructureArticle-the-structure-of-answers"></a>

 A `QuestionFormAnswers` element contains an `Answer` element for each question in the HIT or Qualification test for which the Worker provided an answer. Each `Answer` contains a `QuestionIdentifier` element whose value corresponds to the `QuestionIdentifier` of a `Question` in the QuestionForm. See [the QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md) for more information about questions and answer specifications.

 If the question expects a free-text answer, the `Answer` element contains a `FreeText` element. This element contains the Worker's answer.

 If the question expects a multiple-choice answer, the `Answer` element contains a `SelectionIdentifier` element for each option the Worker selected. If the Worker did not make any selections, the `Answer` will contain zero `SelectionIdentifier` elements. The identifier corresponds to the `SelectionIdentifier` for the selection provided in the answer specification for the question.

 If the multiple-choice question includes an `OtherSelection` field, and the Worker enters data into this field, that data appears in the `Answer` in an `OtherSelectionText` element. If the Worker both selects an option from the list and provides text in this field, both values will be present in the answer.

 If the question expects an uploaded file as an answer, the `Answer` element contains an `UploadedFileSizeInBytes` element, and an `UploadedFileKey` element. `UploadedFileSizeInBytes` indicates the size of the file the Worker uploaded. `UploadedFileKey` is a unique identifier for the file, unique with respect to other files that Workers may have uploaded. To retrieve an uploaded file, your application calls the `GetFileUploadURL` operation, which returns a temporary URL your application can use to download the file. See the `GetFileUploadURL` operation for more information on retrieving uploaded files.

 Answer data will always conform to the answer specification provided in the HIT question, or in the Qualification test question.

## Example
<a name="ApiReference_QuestionFormAnswersDataStructureArticle-example"></a>

 The following is an example of a complete `QuestionFormAnswers` data structure. Remember that this value will be returned as a single return value, XML escaped in the response.

```
<QuestionFormAnswers xmlns="{{[the QuestionFormAnswers schema URL]}}">
  <Answer>
    <QuestionIdentifier>nextmove</QuestionIdentifier>
    <FreeText>C3</FreeText>
  </Answer>
  <Answer>
    <QuestionIdentifier>likelytowin</QuestionIdentifier>
    <SelectionIdentifier>notlikely</SelectionIdentifier>
  </Answer>
</QuestionFormAnswers>
```

When using [Crowd HTML Elements](ApiReference_HTMLCustomElementsArticle.md) in your form, they will output JSON formatted data in the `<FreeText>` field. For example, the output for a [crowd-bounding-box](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-crowd-bounding-box.html) with three boxes on the image would contain a text string similar to the one below.

```
<FreeText>
  {
    'annotatedResult':
    {
      'boundingBoxes':
      [
        {
          'height': 902,
          'label': 'human',
          'left': 53,
          'top': 174,
          'width': 619
        },
        {
          'height': 936,
          'label': 'human',
          'left': 734,
          'top': 73,
          'width': 684
        },
        {
          'height': 686,
          'label': 'human',
          'left': 1174,
          'top': 121,
          'width': 556
        }
      ],
      'inputImageProperties':
      {
        'height': 1080,
        'width': 1920
      }
    }
  }
</FreeText>
```
