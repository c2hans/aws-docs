---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetAssignmentOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetAssignment
<a name="ApiReference_GetAssignmentOperation"></a>

## Description
<a name="ApiReference_GetAssignmentOperation-description"></a>

The `GetAssignment` operation retrieves an assignment with an `AssignmentStatus` value of `Submitted`, `Approved`, or `Rejected`, using the assignment's ID. Requesters can only retrieve their own assignments for HITs that they have not disposed of. For more information about the `AssignmentStatus` element, see the [Assignment](ApiReference_AssignmentDataStructureArticle.md) data structure. For more information about assignments, see [Creating and Managing Assignments](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_AssignmentsArticle.html).

## Request Parameters
<a name="ApiReference_GetAssignmentOperation-request-parameters"></a>

 The `GetAssignment` operation accepts parameters common to all operations. Some common parameters are required. For more information, see [Common Parameters](ApiReference_CommonParametersArticle.md).

 The following parameters are specific to the `GetAssignment` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetAssignment<br />Default: None | Yes |
|  `AssignmentId`  | The ID of the assignment that is being requested. <br />Type: String<br />Default: None.  | Yes |

## Response Elements
<a name="ApiReference_GetAssignmentOperation-response-elements"></a>

 A successful request for the `GetAssignment` operation has a `GetAssignmentResult` element in the response.

The `GetAssignmentResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `Request`  | This element is present only if the **Request** `ResponseGroup` is specified. |
|  `Assignment`  | The assignment. The response includes one `Assignment` element. <br />Type: An [Assignment](ApiReference_AssignmentDataStructureArticle.md) data structure |
|  `HIT`  | The HIT associated with this assignment. The response includes one `HIT` element.<br />Type: A [HIT](ApiReference_HITDataStructureArticle.md) data structure |

## Examples
<a name="ApiReference_GetAssignmentOperation-examples"></a>

The following example shows how to use the `GetAssignment` operation.

### Sample Request
<a name="ApiReference_GetAssignmentOperation-examples-sample-request"></a>

The following example retrieves an assignment using the assignment's ID.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetAssignment
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&AssignmentId=GYFTRHZ5J3DZREY48WNZE38ZR9RR1ZPMXGWE7WE0
```

### Sample Response
<a name="ApiReference_GetAssignmentOperation-examples-sample-response"></a>

The following is an example response.

```
<GetAssignmentResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <Assignment>
    <AssignmentId>GYFTRHZ5J3DZREY48WNZE38ZR9RR1ZPMXGWE7WE0</AssignmentId>
    <WorkerId>AD20WXZZP9XXK</WorkerId>
    <HITId>GYFTRHZ5J3DZREY48WNZ</HITId>
    <AssignmentStatus>Approved</AssignmentStatus>
    <AutoApprovalTime>2012-08-12T19:21:54Z</AutoApprovalTime>
    <AcceptTime>2012-07-13T19:21:40Z</AcceptTime>
    <SubmitTime>2012-07-13T19:21:54Z</SubmitTime>
    <ApprovalTime>2012-07-13T19:27:54Z</ApprovalTime>
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
  <HIT>
    <HITId>GYFTRHZ5J3DZREY48WNZ</HITId>
    <HITTypeId>NYVZTQ1QVKJZXCYZCZVZ</HITTypeId>
    <CreationTime>2012-07-07T00:56:40Z</CreationTime>
    <Title>Location</Title>
    <Description>Answer this Question</Description>
    <Question>
      <QuestionForm xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd">
        <Question>
          <QuestionIdentifier>Question100</QuestionIdentifier>
          <DisplayName>My Question</DisplayName>
          <IsRequired>true</IsRequired>
          <QuestionContent>
            <Binary>
              <MimeType>
                <Type>image</Type>
                <SubType>gif</SubType>
              </MimeType>
              <DataURL>http://tictactoe.amazon.com/game/01523/board.gif</DataURL>
              <AltText>The game board, with "X" to move.</AltText>
            </Binary>
          </QuestionContent>
          <AnswerSpecification><FreeTextAnswer/></AnswerSpecification>
        </Question>
      </QuestionForm>
    </Question>
    <HITStatus>Assignable</HITStatus>
    <MaxAssignments>1</MaxAssignments>
    <Reward>
      <Amount>5.00</Amount>
      <CurrencyCode>USD</CurrencyCode>
      <FormattedPrice>$5.00</FormattedPrice>
    </Reward>
    <AutoApprovalDelayInSeconds>2592000</AutoApprovalDelayInSeconds>
    <Expiration>2012-07-14T00:56:40Z</Expiration>
    <AssignmentDurationInSeconds>30</AssignmentDurationInSeconds>
    <HITReviewStatus>NotReviewed</HITReviewStatus>
  </HIT>
</GetAssignment>
```

## Related Operations
<a name="ApiReference_GetAssignmentOperation-related-operations"></a>
+ [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md)
