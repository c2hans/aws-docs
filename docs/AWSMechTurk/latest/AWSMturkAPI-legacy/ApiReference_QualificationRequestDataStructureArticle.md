---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_QualificationRequestDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# QualificationRequest
<a name="ApiReference_QualificationRequestDataStructureArticle"></a>

## Description
<a name="ApiReference_QualificationRequestDataStructureArticle-description"></a>

 The QualificationRequest data structure represents a request a Worker has made for a Qualification.

 The QualificationRequest data structure is used as a response element for the following operations:
+  [GetQualificationRequests](ApiReference_GetQualificationRequestsOperation.md)

## Elements
<a name="ApiReference_QualificationRequestDataStructureArticle-elements"></a>

 The QualificationRequest structure can contain the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `QualificationRequestId`  |  The ID of the Qualification request, a unique identifier generated when the request was submitted. <br />Type: String<br />Default: None | No |
|  `QualificationTypeId`  |  The ID of the Qualification type the Worker is requesting, as returned by the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation. <br />Type: String<br />Default: None | No |
|  `SubjectId`  |  The ID of the Worker requesting the Qualification. This ID corresponds to the `WorkerId` returned with assignment results when the Worker performs a HIT. <br />Type: String<br />Default: None | No |
|  `Test`  |  The contents of the Qualification test that was presented to the Worker, if the type has a test and the Worker has submitted answers. This value is identical to the QuestionForm associated with the Qualification type at the time the Worker requests the Qualification. <br />Type: a [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure <br />Default: None | No |
|  `Answer`  |  The Worker's answers for the Qualification type's test contained in a `QuestionFormAnswers` document, if the type has a test and the Worker has submitted answers. If the Worker does not provide any answers, `Answer` may be empty. <br /> Type: a [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md) data structure <br />Default: None | No |
|  `SubmitTime`  |  The date and time the Qualification request had a status of **Submitted**. This is either the time the Worker submitted answers for a Qualification test, or the time the Worker requested the Qualification if the Qualification type does not have a test. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z** <br />Default: None | No |

## Example
<a name="ApiReference_QualificationRequestDataStructureArticle-example"></a>

 The following example shows a QualificationRequest data structure returned by the [GetQualificationRequests](ApiReference_GetQualificationRequestsOperation.md) operation. This operation returns the requests for Qualifications of a Qualification type to the owner of the type.

```
<QualificationRequest>
  <QualificationRequestId>789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE</QualificationRequestId>
  <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
  <SubjectId>AZ3456EXAMPLE</SubjectId>
  <Test>
    &lt;QuestionForm&gt;
      {{[XML-encoded question data]}}
    &lt;/QuestionForm&gt;
  </Test>
  <Answer>
    &lt;QuestionFormAnswers&gt;
      {{[XML-encoded answer data]}}
    &lt;/QuestionFormAnswers&gt;
  </Answer>
  <SubmitTime>2005-12-01T23:59:59Z</SubmitTime>
</QualificationRequest>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
