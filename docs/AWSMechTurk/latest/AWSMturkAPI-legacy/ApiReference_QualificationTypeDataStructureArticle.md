---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_QualificationTypeDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# QualificationType
<a name="ApiReference_QualificationTypeDataStructureArticle"></a>

## Description
<a name="ApiReference_QualificationTypeDataStructureArticle-description"></a>

 The QualificationType data structure represents a Qualification type, a description of a property of a Worker that must match the requirements of a HIT for the Worker to be able to accept the HIT. The type also describes how a Worker can obtain a Qualification of that type, such as through a Qualification test.

 The QualificationType data structure is used as a response element for the following operations:
+  [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md)
+  [GetQualificationType](ApiReference_GetQualificationTypeOperation.md)
+  [SearchQualificationTypes](ApiReference_SearchQualificationTypesOperation.md)
+  [UpdateQualificationType](ApiReference_UpdateQualificationTypeOperation.md)

## Elements
<a name="ApiReference_QualificationTypeDataStructureArticle-elements"></a>

 The QualificationType structure can contain the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `QualificationTypeId`  | A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation operation, and it retains that ID forever. <br />Type: String<br />Default: None | No |
|  `CreationTime`  | The date and time the Qualification type was created<br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `Name`  |  The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search. <br />Type: String<br />Default: None | No |
|  `Description`  | A long description for the Qualification type.<br />Type: String<br />Default: None | No |
|  `Keywords`  |  One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search. <br />Type: String<br />Default: None | No |
|  `QualificationTypeStatus`  |  The status of the Qualification type. A Qualification type's status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. <br />Type: String<br />Valid Values: Active \| Inactive<br />Default: None | No |
|  `RetryDelayInSeconds`  |  The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. <br />Type: positive integer<br /> Default: None. If not specified, retries are disabled and Workers can request a Qualification only once.  | No |
|  `Test`  |  The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. <br /> Type: a [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure.   A Qualification test cannot use an [ExternalQuestionQuestionForm](ApiReference_ExternalQuestionArticle.md) like a HIT can.  <br />Default: None<br /> Constraints: must be specified if `AnswerKey` is present. A Qualification type cannot have both a specified `Test` parameter and an `AutoGranted` value of **true**.  | No |
|  `TestDurationInSeconds`  |  The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification. <br />Type: positive integer<br />Default: None | No |
|  `AnswerKey`  |  The answers to the Qualification test specified in the `Test` parameter. <br /> Type: an [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md) data structure. <br /> Default: None. If not provided with a test, the Qualification author must process the Qualification request manually.  | No |
|  `AutoGranted`  |  Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. <br />Type: Boolean<br />Valid Values: true \| false<br />Default: None<br /> Constraints: A Qualification type cannot have both a specified `Test` parameter and an `AutoGranted` value of **true**.  | No  |
|  `AutoGrantedValue`  |  The Qualification value to use for automatically granted Qualifications, if `AutoGranted` is `true`. <br />Type: Integer<br />Default: 1 | No  |
|  `IsRequestable`  |  Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is **false** for Qualifications assigned automatically by the system. <br />Type: Boolean<br />Valid Values: true \| false<br />Default: None | No  |

## Example
<a name="ApiReference_QualificationTypeDataStructureArticle-example-"></a>

 The following example shows a QualificationType data structure returned by a call to the [GetQualificationType](ApiReference_GetQualificationTypeOperation.md) operation. The [GetQualificationType](ApiReference_GetQualificationTypeOperation.md) operation returns a `GetQualificationTypeResult` element, which contains a `QualificationType` element.

```
<QualificationType>
  <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
  <CreationTime>2005-01-31T23:59:59Z</CreationTime>
  <Name>EnglishWritingAbility</Name>
  <Description>The ability to write and edit text...</Description>
  <Keywords>English, text, write, edit, language</Keywords>
  <QualificationTypeStatus>Active</QualificationTypeStatus>
  <RetryDelayInSeconds>86400</RetryDelayInSeconds>
  <IsRequestable>true</IsRequestable>
</QualificationType>
```
