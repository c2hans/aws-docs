---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_HITDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# HIT
<a name="ApiReference_HITDataStructureArticle"></a>

## Description
<a name="ApiReference_HITDataStructureArticle-description"></a>

 The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.

The HIT data structure is used as a response element for the following operations:
+ [CreateHIT](ApiReference_CreateHITOperation.md)
+ [DisableHIT](ApiReference_DisableHITOperation.md)
+ [GetHIT](ApiReference_GetHITOperation.md)
+ [GetReviewableHITs](ApiReference_GetReviewableHITsOperation.md)
+ [SearchHITs](ApiReference_SearchHITsOperation.md)

## HITs and Response Groups
<a name="ApiReference_HITDataStructureArticle-hits-and-response-groups"></a>

 Operations that return a HIT data structure use response groups to determine how much information to return. As described in [Common Parameters](ApiReference_CommonParametersArticle.md), the `ResponseGroup` parameter specifies which sets of elements the service should return, as a set of named groups. For example, the `Request` response group includes the contents of the operation request in the response.

For the HIT data structure, the `Minimal` response group returns the `HITId`. For information about the contents of other HIT data structure related response group content, see [Common Parameters](ApiReference_CommonParametersArticle.md).

 The `GetHIT` operation returns the **HITDetail**, **HITQuestion** and **Minimal** response groups by default. The **HITAssignmentSummary** response group is off by default.

 The `SearchHITs` operation includes **HITDetail**, **Minimal**, and **HITAssignmentSummary** as default response groups. You can also specify **HITQuestion** with `SearchHITs`.

 `CreateHIT` and `DisableHIT` can also return additional HIT fields, but their default is **Minimal**.

 Currently, the `GetReviewableHITs` operation only supports the `Minimal` response group. To retrieve additional HIT data for HITs returned by this operation, use the HIT IDs in the results with `GetHIT`.

## Elements
<a name="ApiReference_HITDataStructureArticle-elements"></a>

 The HIT structure can contain the elements described in the following table.

| Name | Description | Required |
| --- | --- | --- |
|  `HITId`  | A unique identifier for the HIT. The [CreateHIT](ApiReference_CreateHITOperation.md) operation gives a HIT the HIT ID and the HIT retains that ID forever. <br />Type: String<br />Default: None | No |
|  `HITTypeId`  | The ID of the HIT type of this HIT<br />Type: String<br />Default: None | No |
|  `HITGroupId`  | The ID of the HIT Group of this HIT<br />Type: String<br />Default: None | No |
|  `HITLayoutId`  | The ID of the HIT Layout of this HIT <br />Type: String<br />Default: None | No |
|  `CreationTime`  | The date and time the HIT was created<br />Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as `2012-01-31T23:59:59Z`. <br />Default: None | No |
|  `Title`  | The title of the HIT<br />Type: String<br />Default: None | No |
|  `Description`  | A general description of the HIT<br />Type: String<br />Default: None | No |
|  `Keywords`  |  One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results. <br />Type: String<br />Default: None | No |
|  `HITStatus`  | The status of the HIT and its assignments<br />Type: String<br />Valid Values: Assignable \| Unassignable \| Reviewable \| Reviewing \| Disposed<br />Default: None | No |
|  `Reward`  | The amount of money the Requester will pay a Worker for successfully completing the HIT.<br /> Type: a [Price](ApiReference_PriceDataStructureArticle.md) data structure <br />Default: None | No |
|  `LifetimeInSeconds`  | The amount of time, in seconds, after which the HIT is no longer available for users to accept. The HIT becomes unavailable even if the requested number of assignments, specified by `MaxAssignments`, has not been completed. <br />Type: positive integer<br />Default: None | No |
|  `AssignmentDurationInSeconds`  | The length of time, in seconds, that a Worker has to complete the HIT after accepting it.<br />Type: positive integer<br />Default: None | No |
|  `MaxAssignments`  | The number of times the HIT can be accepted and completed before the HIT becomes unavailable. <br />Type: positive integer<br />Default: 1 | No |
|  `AutoApprovalDelayInSeconds`  | The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.<br />Type: positive integer<br />Default: None | No |
|  `Expiration`  | The date and time the HIT expires<br />Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as `2012-01-31T23:59:59Z`. <br />Default: None | No |
|  `QualificationRequirement`  | A condition that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met by a Worker's Qualifications for the Worker to accept the HIT. <br /> Type: a [QualificationRequirement](ApiReference_QualificationRequirementDataStructureArticle.md) data structure. <br />Default: None | No |
|  `Question`  | The data the Worker completing the HIT uses produce the results.<br />Type: either a [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) or an [ExternalQuestion ](ApiReference_ExternalQuestionArticle.md) data structure. <br />Default: None | No |
|  `RequesterAnnotation`  | An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT. <br />Type: String<br />Default: None | No |
|  `HITReviewStatus`  | Indicates the review status of the HIT.<br />Type: String<br />Valid Values: NotReviewed \| MarkedForReview \| ReviewedAppropriate \| ReviewedInappropriate <br />Default: None | No |
|  `NumberofAssignmentsPending`  | The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned. <br />Type: non-negative integer<br />Default: None<br />Conditions: This element is returned only if the `HITAssignmentSummary` response group is specified.  | Conditional |
|  `NumberofAssignmentsAvailable`  | The number of assignments for this HIT that are available for Workers to accept<br />Type: non-negative integer<br />Default: None<br />Conditions: This element is returned only if the `HITAssignmentSummary` response group is specified.  | Conditional |
|  `NumberofAssignmentsCompleted`  | The number of assignments for this HIT that have been approved or rejected.<br />Type: non-negative integer<br />Default: None<br />Conditions: This element is returned only if the `HITAssignmentSummary` response group is specified.  | Conditional |

## Example
<a name="ApiReference_HITDataStructureArticle-example"></a>

 The following example shows a HIT data structure returned by the [CreateHIT](ApiReference_CreateHITOperation.md) operation. The [CreateHIT](ApiReference_CreateHITOperation.md) operation returns an element named `HIT` that represents the HIT that was created by the call.

```
<HIT>
  <HITId>123RVWYBAZW00EXAMPLE</HITId>
  <HITTypeId>T100CN9P324W00EXAMPLE</HITTypeId>
  <CreationTime>2005-06-30T23:59:59</CreationTime>
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
      {{[XML-encoded Question data]}}
    &lt;/QuestionForm&gt;
  </Question>
  <QualificationRequirement>
    <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
    <Comparator>GreaterThan</Comparator>
    <Value>18</Value>
  </QualificationRequirement>
  <HITReviewStatus>NotReviewed</HITReviewStatus>
</HIT>
```
