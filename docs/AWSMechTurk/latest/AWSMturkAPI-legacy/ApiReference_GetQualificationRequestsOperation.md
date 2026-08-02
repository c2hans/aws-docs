---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetQualificationRequestsOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetQualificationRequests
<a name="ApiReference_GetQualificationRequestsOperation"></a>

## Description
<a name="ApiReference_GetQualificationRequestsOperation-description"></a>

 The `GetQualificationRequests` operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and grants Qualifications based on the requests using the [GrantQualification](ApiReference_GrantQualificationOperation.md) operation.

 The `GetQualificationRequests` operation returns only those Qualifications that require the type owner's attention. The operation does not return requests awaiting Qualification test answers and requests that have already been granted.

 Only the owner of the Qualification type can retrieve its requests.

 The operation sorts the results, divides them into numbered pages, and returns a single page of results. You can control sorting and pagination with parameters to the operation.

## Request Parameters
<a name="ApiReference_GetQualificationRequestsOperation-request-parameters"></a>

 The `GetQualificationRequests` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetQualificationRequests` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetQualificationRequests<br />Default: None | Yes |
|  `QualificationTypeId`  |  The ID of the Qualification type, as returned by the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation. <br />Type: String<br /> Default: None. If not specified, all requests for all of your Qualification types are considered for the results.  | No |
|  `SortProperty`  |  The field on which to sort the returned results. <br />Type: String<br />Valid Values: QualificationTypeId \| SubmitTime<br />Default: SubmitTime | No |
|  `SortDirection`  |  The direction of the sort. <br />Type: String<br />Valid Values: Ascending \| Descending<br />Default: Ascending | No |
|  `PageSize`  |  The number of Qualification requests to include in a page of results. The operation divides the complete sorted result set into pages of this many Qualification requests. <br />Type: positive integer<br />Valid Values: any number between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. When the operation has filtered the Qualification requests, sorted them, and divided them into pages of size `PageSize`, the operation returns the page corresponding to the `PageNumber` parameter. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetQualificationRequestsOperation-response-elements"></a>

 A successful request for the `GetQualificationRequests` operation returns a `GetQualificationRequestsResult` element in the response.

 The `GetQualificationRequestsResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `NumResults`  |  The number of Qualification requests on this page in the filtered results list, equivalent to the number of Qualification requests being returned by this call. <br />Type: non-negative integer |
|  `PageNumber`  | The number of this page in the filtered results list.<br />Type: positive integer |
|  `TotalNumResults`  | The total number of Qualification requests in the filtered results list based on this call.<br />Type: non-negative integer |
|  `QualificationRequest`  |  The Qualification request. The response includes one `QualificationRequest` element for each Qualification request returned by the query. <br /> Type: a [ QualificationRequest](ApiReference_QualificationRequestDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_GetQualificationRequestsOperation-examples"></a>

The following example shows how to use the `GetQualificationRequests` operation.

### Sample Request
<a name="ApiReference_GetQualificationRequestsOperation-examples-sample-request"></a>

 The following example retrieves Qualification requests for a specified Qualification type.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetQualificationRequests
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&QualificationTypeId=789RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_GetQualificationRequestsOperation-examples-sample-response"></a>

The following is an example response.

```
<GetQualificationRequestsResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>1</NumResults>
  <TotalNumResults>1</TotalNumResults>
  <PageNumber>1</PageNumber>
  <QualificationRequest>
    <QualificationRequestId>789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE
    </QualificationRequestId>
    <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
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
    <SubmitTime>2005-12-01T23:59:59Z</SubmitTime>
  </QualificationRequest>
</GetQualificationRequestsResult>
```
