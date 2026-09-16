---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetHITsForQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetHITsForQualificationType
<a name="ApiReference_GetHITsForQualificationTypeOperation"></a>

## Description
<a name="ApiReference_GetHITsForQualificationTypeOperation-description"></a>

 The `GetHITsForQualificationType` operation returns the HITs that use the given Qualification type for a Qualification requirement.

 The operation returns HITs of any status, except for HITs that have been disposed with the [DisposeHIT](ApiReference_DisposeHITOperation.md) operation.

 This operation returns only HITs that you created.

**Note**
 For reasons internal to the service, there may be a delay between when a HIT is created and when the HIT will be returned from a call to `GetHITsForQualificationType`.

 The operation divides the results into numbered pages and returns a single page of results. You can control pagination with parameters to the operation.

## Request Parameters
<a name="ApiReference_GetHITsForQualificationTypeOperation-request-parameters"></a>

 The `GetHITsForQualificationType` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetHITsForQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetHITsForQualificationType<br />Default: None | Yes |
|  `QualificationTypeId`  |  The ID of the Qualification type to use when querying HITs, as returned by the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation. The operation returns HITs that require that a Worker have a Qualification of this type. <br />Type: String<br />Default: None | Yes |
|  `PageSize`  |  The number of HITs to include in a page of results. The complete results set is divided into pages of this many HITs. <br />Type: positive integer<br />Valid Values: any integer between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. After the HITs are divided into pages of size `PageSize`, the operation returns the page corresponding to the `PageNumber`. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetHITsForQualificationTypeOperation-response-elements"></a>

 A successful request for the `GetHITsForQualificationType` operation returns a `GetHITsForQualificationTypeResult` element in the response.

 The `GetHITsForQualificationTypeResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `NumResults`  |  The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call. <br />Type: non-negative integer |
|  `PageNumber`  |  The number of this page in the filtered results list. <br />Type: positive integer |
|  `TotalNumResults`  |  The total number of HITs in the filtered results list based on this call. <br />Type: non-negative integer |
|  `HIT`  |  The HIT. The response includes one `HIT` element for each HIT returned by the query. <br /> Type: [ HIT](ApiReference_HITDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_GetHITsForQualificationTypeOperation-examples"></a>

The following example shows how to use the `GetHITsForQualificationType` operation.

### Sample Request
<a name="ApiReference_GetHITsForQualificationTypeOperation-examples-sample-request"></a>

 The following example returns HITs that use the specified Qualification type for a Qualification requirement.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetHITsForQualificationType
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&QualificationTypeId=789RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_GetHITsForQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<GetHITsForQualificationTypeResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>1</NumResults>
  <TotalNumResults>1</TotalNumResults>
  <PageNumber>1</PageNumber>
  <HIT>
    <HITId>123RVWYBAZW00EXAMPLE</HITId>
    <HITTypeId>T100CN9P324W00EXAMPLE</HITTypeId>
    <CreationTime>2009-06-15T12:00:01</CreationTime>
    <HITStatus>Assignable</HITStatus>
    <MaxAssignments>5</MaxAssignments>
    <AutoApprovalDelayInSeconds>86400</AutoApprovalDelayInSeconds>
    <LifetimeInSeconds>86400</LifetimeInSeconds>
    <AssignmentDurationInSeconds>300</AssignmentDurationInSeconds>
    <Reward>
      <Amount>25</Amount>
      <CurrencyCode>USD</CurrencyCode>
      <FormattedPrice>$0.25</FormattedPrice>
    </Reward>
    <Title>Location and Photograph Identification</Title>
    <Description>Select the image that best represents...</Description>
    <Keywords>location, photograph, image, identification, opinion</Keywords>
    <Question>
      &lt;QuestionForm&gt;
      [XML-encoded Question data]
      &lt;/QuestionForm&gt;
    </Question>
    <QualificationRequirement>
      <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
      <Comparator>GreaterThan</Comparator>
      <Value>18</Value>
    </QualificationRequirement>
  <HITReviewStatus>NotReviewed</HITReviewStatus>
</HIT>
</GetHITsForQualificationTypeResult>
```
