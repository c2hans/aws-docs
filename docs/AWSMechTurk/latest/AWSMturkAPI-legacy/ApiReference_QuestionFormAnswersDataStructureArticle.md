---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_QuestionFormAnswersDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# QuestionFormAnswers
<a name="ApiReference_QuestionFormAnswersDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_QuestionFormAnswersDataStructureArticle-description)
+ [The Structure of Answers](#ApiReference_QuestionFormAnswersDataStructureArticle-the-structure-of-answers)
+ [Example](#ApiReference_QuestionFormAnswersDataStructureArticle-example)

## Description
<a name="ApiReference_QuestionFormAnswersDataStructureArticle-description"></a>

 The `QuestionFormAnswers` data format describes answers submitted by a Worker for a HIT, or for a Qualification test.

 A `QuestionFormAnswers` data structure is a string value that consists of XML data. The XML data must conform to the QuestionForm schema. See [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md) for the location of this schema. For more information about using XML data as parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

**Note**
 Answer data is *not* guaranteed by the Amazon Mechanical Turk Service to conform to the answer specifications described in a QuestionForm. MTS only guarantees that answer data returned by the service will conform to the `QuestionFormAnswers` schema. Your application should check that the answer data sufficiently answers the question.

 The `QuestionFormAnswers` data structure is used as a response element for the following operations:
+  `GetAssignmentsForHIT`
+  `GetQualificationRequests`

 The `QuestionFormAnswers` data structure is a value in an [Assignment data structure](ApiReference_AssignmentDataStructureArticle.md), and a value in a [QualificationRequest data structure](ApiReference_QualificationRequestDataStructureArticle.md).

 All elements in a `QuestionFormAnswers` belong to a namespace whose name is identical to the URL of the `QuestionFormAnswers` schema document for the version of the API you are using.

## The Structure of Answers
<a name="ApiReference_QuestionFormAnswersDataStructureArticle-the-structure-of-answers"></a>

 A `QuestionFormAnswers` element contains an `Answer` element for each question in the HIT or Qualification test for which the Worker provided an answer. Each `Answer` contains a `QuestionIdentifier` element whose value corresponds to the `QuestionIdentifier` of a `Question` in the QuestionForm. See [the QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md) for more information about questions and answer specifications.

 If the question expects a free-text answer, the `Answer` element contains a `FreeText` element. This element contains the Worker's answer.

 If the question expects a multiple-choice answer, the `Answer` element contains a `SelectionIdentifier` element for each option the Worker selected. If the Worker did not make any selections, the `Answer` will contain zero `SelectionIdentifier` elements. The identifier corresponds to the `SelectionIdentifier` for the selection provided in the answer specification for the question.

 If the multiple-choice question includes an `OtherSelection` field, and the Worker enters data into this field, that data appears in the `Answer` in an `OtherSelectionText` element. If the Worker both selects an option from the list and provides text in this field, both values will be present in the answer.

 If the question expects an uploaded file as an answer, the `Answer` element contains an `UploadedFileSizeInBytes` element, and an `UploadedFileKey` element. `UploadedFileSizeInBytes` indicates the size of the file the Worker uploaded. `UploadedFileKey` is a unique identifier for the file, unique with respect to other files that Workers may have uploaded. To retrieve an uploaded file, your application calls the `GetFileUploadURL` operation, which returns a temporary URL your application can use to download the file. See [the GetFileUploadURL operation](ApiReference_GetFileUploadURLOperation.md) for more information on retrieving uploaded files.

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
