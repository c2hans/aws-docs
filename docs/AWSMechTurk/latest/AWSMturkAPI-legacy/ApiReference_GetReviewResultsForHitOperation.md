---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetReviewResultsForHitOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetReviewResultsForHIT
<a name="ApiReference_GetReviewResultsForHitOperation"></a>

## Description
<a name="ApiReference_GetReviewResultsForHitOperation-description"></a>

The `GetReviewResultsForHIT` operation retrieves the computed results and the actions taken in the course of executing your Review Policies during a [CreateHIT](ApiReference_CreateHITOperation.md) operation. For information about how to apply Review Policies when you call `CreateHIT`, see [Review Policies](ApiReference_ReviewPoliciesArticle.md). The `GetReviewResultsForHIT` operation can return results for both Assignment-level and HIT-level review results. You can also specify to only return results pertaining to a particular Assignment.

## Request Parameters
<a name="ApiReference_GetReviewResultsForHitOperation-request-parameters"></a>

 The `GetReviewResultsForHIT` operation accepts parameters common to all operations. Some common parameters are required. For more information, see [Common Parameters](ApiReference_CommonParametersArticle.md).

The following parameters are specific to the `GetReviewResultsForHIT` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetReveiwResultsForHIT<br />Default: None | Yes |
|  `HITId`  | The unique identifier of the HIT to retrieve review results for.<br />Type: String<br />Default: None | Yes |
|  `PolicyLevel`  | The Policy Level(s) to retrieve review results for.<br />Type: String<br />Default: HIT and Assignments<br />Constraints: HIT and Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).  | No |
|  `AssignmentId`  | If supplied, the results are limited to those pertaining directly to this Assignment ID.<br />Type: String<br />Default: None<br />Note: Both the HIT-level and the Assignment-level Review Policies may take actions and return results concerning an Assignment, so both will be reported unless filtered by the `PolicyLevel` parameter. | No |
|  `RetrieveActions`  | Retrieves a list of the actions taken executing the Review Policies and their outcomes. <br />Type: String<br />Default: T<br />Constraints: T or F | No |
|  `RetrieveResults`  | Retrieves a list of the results computed by the Review Policies.<br />Type: String<br />Default: T<br />Constraints: T or F | No |
|  `PageSize`  |  The number of results to include in a page of results. The complete results set is divided into pages of this many `HITs`. <br />Type: positive integer<br />Valid Values: any integer between 100 and 65535<br />Default: 400 | Optional |
|  `PageNumber`  |  The page of results to return. After the results are divided into pages of size `PageSize`, the operation returns the page corresponding to the `PageNumber`. <br />Type: positive integer<br />Default: 1 | Optional |

## Response Elements
<a name="ApiReference_GetReviewResultsForHitOperation-response-elements"></a>

A successful request for the `GetReviewResultsForHIT` operation has a `GetReviewResultsForHITResult` element in the response. The `GetReviewResultsForHITResult` element contains the name of the Review Policy applied as well as the `AssignmentReviewReport` element and the `HITReviewReport` element. Additional elements called `ReviewAction` and `ReviewResult` provide the results of Review Policy specified when the HIT was created.

 The `GetReviewResultsForHITResult` element contains the following elements:

| Name | Description |
| --- | --- |
| `HITId` | The HIT ID.<br />Type: String |
| `AssignmentReviewPolicy` | The name of the Assignment-level Review Policy. This contains only the `PolicyName` element.<br />Type: String<br />Constraint: Name of the applied policy. For a list of available named policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).  |
| `HITReviewPolicy` | The name of the HIT-level Review Policy. This contains only the `PolicyName` element.<br />Type: String<br />Constraint: Name of the applied policy. For a list of available named policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).  |
| `AssignmentReviewReport` | Contains both `ReviewResult` and `ReviewAction` elements for an Assignment.<br />Type: `ReviewResult` data structure and `ReviewAction` data structure. See below for details. |
| `HITReviewReport` | Contains both`ReviewResult` and `ReviewAction` elements for a particular HIT.<br />Type: `ReviewResult` data structure and `ReviewAction` data structure. See below for details. |

## ReviewResult Data Structure
<a name="ApiReference_GetReviewResultsForHitOperation-reviewresult-data-structure"></a>

Both the `AssignmentReviewReport` element and the`HITReviewReport` element contain the ReviewResult data structure. The ReviewResult structure is returned multiple times for each result specified in the Review Policy.

**Note**
A HIT-level Review Policy may be enacted multiple times if the HIT is extended by the Review Policy or by extending a reviewable HIT using the [ExtendHIT](ApiReference_ExtendHITOperation.md) operation.

`GetReviewResultsForHITResult` includes the results from each of the review steps, in chronological order. The first-produced results appear first in the list, while other results with the same SubjectId/QuestionId/Key may appear later in the list, reflecting later reviews. Assignment-level review policies are enabled precisely once per submitted Assignment, so the Assignment-level results will only contain duplicate SubjectId/QuestionId/Key elements if the Assignment-level policy contains information about the HIT itself.

### ReviewResult Elements
<a name="ApiReference_GetReviewResultsForHitOperation-reviewresult-data-structure-reviewresult-elements"></a>

 The `ReviewResult` data structure contains the following elements:

| Name | Description |
| --- | --- |
| `ActionId` | A unique identifier of the Review action result.<br />Type: String |
| `SubjectId` | The HITID or AssignmentId about which this result was taken. <br />Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself.<br />Type: String |
| `ObjectType` | The type of the object from the SubjectId field.<br />Type: String<br />Constraint: Assignment or HIT |
| `QuestionId` | Specifies the QuestionId the result is describing. Depending on whether the ObjectType is a HIT or Assignment this results could specify multiple values. See the next table for possible values and their meaning.<br />If ObjectType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Worker's performance on the HIT.<br />Type: String |
| `Key` | Key identifies the particular piece of reviewed information. See the next table for details. <br />Type: String |
| `Value` | The values of *Key* provided by the review policies you have selected.<br />Type: String |

#### Result Keys
<a name="ApiReference_GetReviewResultsForHitOperation-reviewresult-data-structure-reviewresult-elements-result-keys"></a>

 The `QuestionId` element can contain the following result values:

| Key | SubjectType | Meaning |
| --- | --- | --- |
| AgreedAnswerFound | Question | A boolean to describe whether an agreed answer was found. <br />Constraints: true or false |
| AgreedAnswer | Question | If AgreedAnswerFound is true, contains the agreed answer for the question. If no agreed answer is found then this value is not returned. |
| AnswerAgreementScore | Question | If AgreedAnswerFound is true, contains the Agreement Score for the question. If no agreed answer is found then this value is not returned. |
| WorkerAgreementScore  | Assignment  | Contains the computed Worker Agreement Score for the Worker that completed the assignment.  |
| PluralityAnswersCorrect | Assignment | Contains the number of answers in the assignment that agreed with the majority.  |
| PluralityAnswersIncorrect | Assignment | Contains the number of answers in the assignment that disagreed with the majority. |
| HitAgreementScore | HIT | Contains the computed HIT Agreement Score for the HIT.  |

## ReviewAction Data Structure
<a name="ApiReference_GetReviewResultsForHitOperation-reviewaction-data-structure"></a>

Both the `AssignmentReviewReport` and the `HITReviewReport` elements contains the `ReviewAction` data structure. This structure is returned multiple times for each action specified in the Review Policy.

### ReviewAction Elements
<a name="ApiReference_GetReviewResultsForHitOperation-reviewaction-data-structure-reviewaction-elements"></a>

The `ReviewAction` data structure element contains the following elements:

| Name | Description |
| --- | --- |
| `ActionId` | The unique identifier for the action.<br />Type: String |
| `ActionName` | The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary. <br />Type: String<br />Constraints: Approve, Reject, or Extend  |
| `ObjectId` | The specific HITId or AssignmentID targeted by the action.<br />Type: String<br />Constraint: none |
| `ObjectType` | The type of object in ObjectId.<br />Type: String<br />Constraint: AssignmentID or HITID |
| `Status` | The current disposition of the action. See below for a description of the statuses.<br />Type: String<br />Constraints: INTENDED, SUCCEEDED, FAILED, or CANCELLED |
| `CompleteTime` | The date when the action was completed.<br />Type: Date/Time<br />Constraints: none |
| `Results` | A description of the outcome of the review. Do not to make assumptions about the format of this string or the data it contains. <br />Type: String |
| `ErrorCode` | Present only when the Results have a FAILED Status.<br />Type: String |

### ReviewAction Elements Returned Status Values
<a name="ApiReference_GetReviewResultsForHitOperation-reviewaction-data-structure-reviewaction-elements-returned-status-values"></a>

The following table lists the types of Status values returned in the `ReviewAction` Status element:

| Status | Description |
| --- | --- |
| INTENDED | The action is either queued for execution or currently being worked on. |
| SUCCEEDED | The action was taken successfully. Note that the SUCCESS of an action does not necessarily imply that the object has actually been acted upon. For example, an action trying to approve an already-approved Assignment will report itself as SUCCESSFUL even though the Assignment was not further altered by the second approval. <br />Similarly, if the policy was configured to extend a HIT to a maximum of 5 assignments, then an extend action attempted when the HIT has already been extended to have a maximum of 5 assignments will take no action and report SUCCESS, because it has successfully performed the action in accordance with the configured limits of the Review Policy.  |
| FAILED  | The action could not be taken because of the state of its object. For example, an Assignment that is already approved cannot later be rejected or a HIT cannot be extended if the Requester lacks sufficient funds to cover the increased liability. Whenever an action is "FAILED", an additional ErrorCode element is present.  |
| CANCELLED | The action was prevented by the intervention of Mechanical Turk. |

## Examples
<a name="ApiReference_GetReviewResultsForHitOperation-examples"></a>

The following example shows how to use the `GetReviewResultsForHIT` operation.

### Sample Request
<a name="ApiReference_GetReviewResultsForHitOperation-examples-sample-request"></a>

The following is an example request.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId=[{{the Requester's Access Key ID}}]
&Version=2011-XX-XX
&Operation=GetReviewResultsForHIT
&Signature=[{{signature for this request}}]
&Timestamp=[{{your system's local time}}]
&HITId=1AAAAAAAAABBBBBBBBBBCCCCCCCCCC
```

### Sample Response
<a name="ApiReference_GetReviewResultsForHitOperation-examples-sample-response"></a>

The following is an example response.

```
<GetReviewResultsForHITResult>
  <HITId>1AAAAAAAAABBBBBBBBBBCCCCCCCCCC</HITId>
  <AssignmentReviewPolicy>
    <PolicyName>ScoreMyKnownAnswers/2011-09-01</PolicyName>
  </AssignmentReviewPolicy>
  <HITReviewPolicy>
    <PolicyName>SimplePlurality/2011-09-01</PolicyName>
  </HITReviewPolicy>
  <AssignmentReviewReport>
    <ReviewResult>
      <SubjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <QuestionId>Question_2</QuestionId>
      <Key>KnownAnswerCorrect</Key>
      <Value>1</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <Key>KnownAnswerScore</Key>
      <Value>100</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <QuestionId>Question_2</QuestionId>
      <Key>KnownAnswerCorrect</Key>
      <Value>0</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <Key>KnownAnswerScore</Key>
      <Value>0</Value>
    </ReviewResult>
    <ReviewAction>
      <ActionName>review</ActionName>
      <ObjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>SUCCEEDED</Status>
      <Result>Reviewed one known answer; 1/1 correct</Result>
    </ReviewAction>
    <ReviewAction>
      <ActionName>approve</ActionName>
      <ObjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>SUCCEEDED</Status>
      <Result>Approved</Result>
    </ReviewAction>
    <ReviewAction>
      <ActionName>review</ActionName>
      <ObjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>SUCCEEDED</Status>
      <Result>Reviewed one known answer; 0/1 correct</Result>
    </ReviewAction>
    <ReviewAction>
      <ActionName>reject</ActionName>
      <ObjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>SUCCEEDED</Status>
      <Result>Rejected</Result>
    </ReviewAction>
  </AssignmentReviewReport>
  <HITReviewReport>
    <ReviewResult>
      <SubjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <QuestionId>Question_1</QuestionId>
      <Key>AgreedWithPlurality</Key>
      <Value>1</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</SubjectId>
      <ObjectType>Assignment</ObjectType>
      <QuestionId>Question_1</QuestionId>
      <Key>AgreedWithPlurality</Key>
      <Value>1</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1AAAAAAAAABBBBBBBBBBCCCCCCCCCC</SubjectId>
      <ObjectType>HIT</ObjectType>
      <QuestionId>Question_1</QuestionId>
      <Key>PluralityAnswer</Key>
      <Value>true</Value>
    </ReviewResult>
    <ReviewResult>
      <SubjectId>1AAAAAAAAABBBBBBBBBBCCCCCCCCCC</SubjectId>
      <ObjectType>HIT</ObjectType>
      <QuestionId>Question_1</QuestionId>
      <Key>PluralityLevel</Key>
      <Value>100</Value>
    </ReviewResult>
    <ReviewAction>
      <ActionName>approve</ActionName>
      <ObjectId>1DDDDDDDDDEEEEEEEEEEFFFFFFFFFF</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>SUCCEEDED</Status>
      <Result>Already approved</Result>
    </ReviewAction>
    <ReviewAction>
      <ActionName>approve</ActionName>
      <ObjectId>1GGGGGGGGGHHHHHHHHHHIIIIIIIIII</ObjectId>
      <ObjectType>Assignment</ObjectType>
      <Status>FAILED</Status>
      <Result>Assignment was in an invalid state for this operation.</Result>
      <ErrorCode>AWS.MechanicalTurk.InvalidAssignmentState</ErrorCode>
    </ReviewAction>
  </HITReviewReport>
</GetReviewResultsForHITResult>
```
