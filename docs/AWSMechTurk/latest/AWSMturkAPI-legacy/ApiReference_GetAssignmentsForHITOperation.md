---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetAssignmentsForHITOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetAssignmentsForHIT
<a name="ApiReference_GetAssignmentsForHITOperation"></a>

## Description
<a name="ApiReference_GetAssignmentsForHITOperation-description"></a>

 The `GetAssignmentsForHIT` operation retrieves completed assignments for a HIT. You can use this operation to retrieve the results for a HIT.

 You can get assignments for a HIT at any time, even if the HIT is not yet **Reviewable**. If a HIT requested multiple assignments, and has received some results but has not yet become **Reviewable**, you can still retrieve the partial results with this operation.

 Use the `AssignmentStatus` parameter to control which set of assignments for a HIT are returned. The `GetAssignmentsForHIT` operation can return submitted assignments awaiting approval, or it can return assignments that have already been approved or rejected. You can set `AssignmentStatus=Approved,Rejected` to get assignments that have already been approved and rejected together in one result set.

 Only the Requester who created the HIT can retrieve the assignments for that HIT.

 Results are sorted and divided into numbered pages and the operation returns a single page of results. You can use the parameters of the operation to control sorting and pagination.

## Request Parameters
<a name="ApiReference_GetAssignmentsForHITOperation-request-parameters"></a>

 The `GetAssignmentsForHIT` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetAssignmentsForHIT` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetAssignmentsForHIT<br />Default: None | Yes |
|  `HITId`  | The ID of the HIT for which completed assignments are requested.<br />Type: String<br />Default: None | Yes |
|  `AssignmentStatus`  | The status of the assignments to return.<br /> <br />Type: String<br />Valid Values: Submitted \| Approved \| Rejected<br />Default: None. If not specified, the operation returns all assignments that have been submitted, including those that have been approved or rejected. <br />Note: Set `AssignmentStatus=Approved,Rejected` to get assignments that have been approved and rejected together in one result set. | No |
|  `SortProperty`  |  The field on which to sort the results returned by the operation. <br />Type: String<br />Valid Values: AcceptTime \| SubmitTime \| AssignmentStatus<br />Default: SubmitTime |  |
|  `SortDirection`  |  The direction of the sort used with the field specified by the `SortProperty` parameter. <br />Type: String<br />Valid Values: Ascending \| Descending<br />Default: Ascending | No |
|  `PageSize`  |  The number of assignments to include in a page of results. The complete sorted result set is divided into pages of this many assignments. <br />Type: positive integer<br />Valid Values: any integer between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. Once the assignments have been filtered, sorted, and divided into pages of size `PageSize`, the page corresponding to `PageNumber` is returned as the results of the operation. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetAssignmentsForHITOperation-response-elements"></a>

 A successful request for the `GetAssignmentsForHIT` operation has a `GetAssignmentsForHITResult` element in the response.

 The `GetAssignmentsForHITResult` element contains the following elements:

| Name | Description |
| --- | --- |
| NumResults |  The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call. <br />Type: non-negative integer |
| PageNumber | The number of the page in the filtered results list being returned.<br />Type: positive integer |
| TotalNumResults | The total number of HITs in the filtered results list based on this call.<br />Type: positive integer |
| Assignment |  The assignment. The response includes one `Assignment` element for each HIT returned by the query. <br /> Type: an [Assignment](ApiReference_AssignmentDataStructureArticle.md) data structure  |

## Examples
<a name="ApiReference_GetAssignmentsForHITOperation-examples"></a>

The following example shows how to use the `GetAssignmentsForHIT` operation.

### Sample Request
<a name="ApiReference_GetAssignmentsForHITOperation-examples-sample-request"></a>

 The following example retrieves five assignments for a HIT, using the default sort order (`SubmitTime`) and direction (`Ascending`).

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetAssignmentsForHIT
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&HITId=123RVWYBAZW00EXAMPLE
&PageSize=5
&PageNumber=1
```

### Sample Response
<a name="ApiReference_GetAssignmentsForHITOperation-examples-sample-response"></a>

The following is an example response.

```
<GetAssignmentsForHITResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>1</NumResults>
  <TotalNumResults>1</TotalNumResults>
  <PageNumber>1</PageNumber>
  <Assignment>
    <AssignmentId>GYFTRHZ5J3DZREY48WNZE38ZR9RR1ZPMXGWE7WE0</AssignmentId>
    <WorkerId>AD20WXZZP9XXK</WorkerId>
    <HITId>GYFTRHZ5J3DZREY48WNZ</HITId>
    <AssignmentStatus>Approved</AssignmentStatus>
    <AutoApprovalTime>2009-08-12T19:21:54Z</AutoApprovalTime>
    <AcceptTime>2009-07-13T19:21:40Z</AcceptTime>
    <SubmitTime>2009-07-13T19:21:54Z</SubmitTime>
    <ApprovalTime>2009-07-13T19:27:54Z</ApprovalTime>
    <Answer>
      <?xml version="1.0" encoding="UTF-8"?>
      <QuestionFormAnswers xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd">
        <Answer>
          <QuestionIdentifier>Question100</QuestionIdentifier>
          <FreeText>Move to X.</FreeText>
        </Answer>
      </QuestionFormAnswers>
    </Answer>
  </Assignment>
</GetAssignmentsForHITResult>
```

## Related Operations
<a name="ApiReference_GetAssignmentsForHITtOperation-related-operations"></a>
+ [GetAssignment](ApiReference_GetAssignmentOperation.md)
+ [SearchHITs](ApiReference_SearchHITsOperation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
