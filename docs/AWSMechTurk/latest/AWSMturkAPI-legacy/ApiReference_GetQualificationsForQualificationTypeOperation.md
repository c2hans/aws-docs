---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetQualificationsForQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetQualificationsForQualificationType
<a name="ApiReference_GetQualificationsForQualificationTypeOperation"></a>

## Description
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-description"></a>

 The `GetQualificationsForQualificationType` operation returns all of the Qualifications granted to Workers for a given Qualification type.

 This operations divides the results into numbered pages and returns a single page of results. You can control pagination with parameters to the operation.

## Request Parameters
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-request-parameters"></a>

 The `GetQualificationsForQualificationType` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetQualificationsForQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetQualificationForQualificationType<br />Default: None | Yes |
|  `QualificationTypeId`  | The ID of the Qualification type of the Qualifications to return.<br />Type: String<br />Default: None | Yes |
|  `Status`  | The status of the Qualifications to return.<br />Type: String<br />Valid Values: Granted \| Revoked<br />Default: Granted | No |
|  `PageSize`  |  The number of Qualifications to include in a page of results. The operation divides the complete result set into pages of this many Qualifications. <br />Type: positive integer<br /> Valid Values: any number between 1 and 100 <br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. Once the operation divides the Qualifications into pages of size `PageSize`, it returns the page corresponding to `PageNumber`. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-response-elements"></a>

 A successful request for the `GetQualificationsForQualificationType` operation returns a `GetQualificationsForQualificationTypeResult` element in the response.

 The `GetQualificationsForQualificationTypeResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `PageNumber`  |  The page of results to return. Once the operation divides the Qualifications into pages of size `PageSize`, the operation returns the page corresponding to `PageNumber`. <br />Type: positive integer |
|  `NumResults`  |  The number of Qualifications on this page in the filtered results list, equivalent to the number of Qualifications being returned by this call. <br />Type: non-negative integer |
|  `TotalNumResults`  |  The total number of Qualifications in the filtered results list based on this call. <br />Type: non-negative integer |
|  `Qualification`  |  The Qualification. The response includes one `Qualification` element for each Qualification returned by the query. <br /> Type: a [Qualification](ApiReference_QualificationDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-examples"></a>

The following example shows how to use the `GetQualificationsForQualificationType` operation.

### Sample Request
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-examples-sample-request"></a>

 The following example returns the Qualifications assigned to Workers for the given Qualification type.

```
https://mechanicalturk.amazonaws.com/onca/xml?
Service=AWSMechanicalTurkRequester
&Operation=GetQualificationsForQualificationType
&Version=2008-08-02
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Signature={{[signature for this request]}}
&Timestamp=2009-07-15T01:21:28.186Z
&QualificationTypeId=ZSPJXD4F1SFZP7YNJWR0
```

### Sample Response
<a name="ApiReference_GetQualificationsForQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<GetQualificationsForQualificationTypeResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>1</NumResults>
  <TotalNumResults>1</TotalNumResults>
  <PageNumber>1</PageNumber>
    <QualificationRequest>
    <QualificationRequestId>789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE
    </QualificationRequestId>
    <QualificationTypeId>ZSPJXD4F1SFZP7YNJWR0</QualificationTypeId>
      <SubjectId>AZ3456EXAMPLE</SubjectId>
      <Test>
        &lt;QuestionForm&gt;
        [XML-encoded question data]
        &lt;/QuestionForm&gt;
      </Test>
      <Answer>
        &lt;QuestionFormAnswers&gt;
        [XML-encoded answer data]
        &lt;/QuestionFormAnswers&gt;
      </Answer>
      <SubmitTime>2009-07-15T01:21:28.296Z</SubmitTime>
    </QualificationRequest>
</GetQualificationsForQualificationTypeResult>
```
