---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_AssignmentDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Assignment
<a name="ApiReference_AssignmentDataStructureArticle"></a>

## Description
<a name="ApiReference_AssignmentDataStructureArticle-description"></a>

 The Assignment data structure represents a single assignment of a HIT to a Worker. The assignment tracks the Worker's efforts to complete the HIT, and contains the results for later retrieval.

 The Assignment data structure is used as a response element for the following operations:
+ [GetAssignment](ApiReference_GetAssignmentOperation.md)
+ [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md)

## Elements
<a name="ApiReference_AssignmentDataStructureArticle-elements"></a>

 The Assignment structure can contain the following elements.

| Name | Description | Required |
| --- | --- | --- |
|  `AssignmentId`  | A unique identifier for the assignment<br />Type: String<br />Default: None | No |
|  `WorkerId`  |  The ID of the Worker who accepted the HIT. <br />Type: String<br />Default: None | No |
|  `HITId`  | The ID of the HIT<br />Type: String<br />Default: None | No |
|  `AssignmentStatus`  | The status of the assignment<br />Type: String<br />Valid Values: Submitted \| Approved \| Rejected<br />Default: None | No |
|  `AutoApprovalTime`  |  If results have been submitted, `AutoApprovalTime` is the date and time the results of the assignment results are considered **Approved** automatically if they have not already been explicitly approved or rejected by the Requester. This value is derived from the auto-approval delay specified by the Requester in the HIT. This value is omitted from the assignment if the Worker has not yet submitted results. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `AcceptTime`  | The date and time the Worker accepted the assignment.<br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `SubmitTime`  |  If the Worker has submitted results, `SubmitTime` is the date and time the assignment was submitted. This value is omitted from the assignment if the Worker has not yet submitted results. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `ApprovalTime`  |  If the Worker has submitted results and the Requester has approved the results, `ApprovalTime` is the date and time the Requester approved the results. This value is omitted from the assignment if the Requester has not yet approved the results. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `RejectionTime`  |  If the Worker has submitted results and the Requester has rejected the results, `RejectionTime` is the date and time the Requester rejected the results. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br /> Default: None. This value is omitted from the assignment if the Requester has not yet rejected the results.  | No |
|  `Deadline`  |  The date and time of the deadline for the assignment. This value is derived from the deadline specification for the HIT and the date and time the Worker accepted the HIT. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | No |
|  `Answer`  |  The Worker's answers submitted for the HIT contained in a `QuestionFormAnswers` document, if the Worker provides an answer. If the Worker does not provide any answers, `Answer` may contain a `QuestionFormAnswers` document, or `Answer` may be empty.<br /> Type: a [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md) data structure <br />Default: None | No |
|  `RequesterFeedback`  |  The feedback string included with the call to the [ ApproveAssignment](ApiReference_ApproveAssignmentOperation.md) operation or the[ RejectAssignment](ApiReference_RejectAssignmentOperation.md) operation, if the Requester approved or rejected the assignment and specified feedback. <br />Type: String<br /> Default: None. This field is not returned with assignment data by default. To request this field, specify a response group of **AssignmentFeedback**. For information about response groups, see [Common Parameters](ApiReference_CommonParametersArticle.md). | No |

## Example
<a name="ApiReference_AssignmentDataStructureArticle-example"></a>

 The following example shows an Assignment data structure returned by the [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation. The [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation returns zero or more `Assignment` elements for a **Reviewable** HIT.

```
<Assignment>
  <AssignmentId>123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE</AssignmentId>
  <WorkerId>AZ3456EXAMPLE</WorkerId>
  <HITId>123RVWYBAZW00EXAMPLE</HITId>
  <AssignmentStatus>Submitted</AssignmentStatus>
  <Deadline>2005-12-01T23:59:59Z</Deadline>
  <AcceptTime>2005-12-01T12:00:00Z</AcceptTime>
  <SubmitTime>2005-12-07T23:59:59Z</SubmitTime>
  <Answer>
    &lt;QuestionFormAnswers&gt;
      {{[XML-encoded Answer data]}}
    &lt;/QuestionFormAnswers&gt;
  </Answer>
</Assignment>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
