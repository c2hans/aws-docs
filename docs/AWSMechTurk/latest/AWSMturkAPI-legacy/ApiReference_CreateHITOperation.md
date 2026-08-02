---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_CreateHITOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# CreateHIT
<a name="ApiReference_CreateHITOperation"></a>

## Description
<a name="ApiReference_CreateHITOperation-description"></a>

The `CreateHIT` operation creates a new Human Intelligence Task (HIT). The new HIT is made available for Workers to find and accept on the Amazon Mechanical Turk website.

There are two ways to specify HIT properties when calling the `CreateHIT` operation: with the HIT type ID, or with the common property values. If the `HITTypeId` parameter is specified, the `CreateHIT` operation assumes the syntax with a HIT type ID is what you intended. If you provide both a HIT type ID and values for the common properties, the common property values are ignored.

CreateHIT also supports several ways to provide question data: by providing a value for the `Question` parameter that fully specifies the contents of the HIT, or by providing a HitLayoutId and associated HitLayoutParameters. If you are providing a data structure, it may be a [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) structure, an [ExternalQuestion](ApiReference_ExternalQuestionArticle.md) structure, or an [HTMLQuestion](ApiReference_HTMLQuestionArticle.md) structure. For more information, see the `Question` parameter.

Using Review Policies with `CreateHIT` you can specify how you want Mechanical Turk to take action on the HITs you create. Using Review Policies removes the need for you to manually take action and determine Worker accuracy after the HIT has been completed. For more information about Review Policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).

You must specify review policies when you create a HIT. You cannot apply a Review Policy to an existing HIT. There are two types of Review Policies, Assignment-level and HIT-level:
+ An Assignment-level Review Policy is applied as soon as a Worker submits an assignment. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md).
+ A HIT-level Review Policy is applied when a HIT becomes reviewable. For more information, see [HIT Review Policies](ApiReference_HITReviewPolicies.md).

You can specify one Assignment-level Review Policy and one HIT-level Review Policy when you call `CreateHIT` using the [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md) data structure. The Assignment-level Review Policy ScoreMyKnownAnswer/2011-09-01 and the HIT-level Review Policy SimplePlurality/2011-09-01 can be used in the same call to `CreateHIT`.

+ Use the ScoreMyKnownAnswers/2011-09-01 policy parameters to compare a known answer you provide with the answer a Worker provides. Mechanical Turk will automatically compare the answer and take action based on your requirements.
+ Use the SimplePlurality/2011-09-01 policy parameters to automatically compare answers received from multiple workers and detect if there is a majority or consensus answer.

For more information about how to get the results you need from Workers, see [Review Policy Use Cases](ApiReference_ReviewPolicyUseCases.md).

**Note**
 If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see [ Amazon Mechanical Turk Pricing](https://requester.mturk.com/pricing).

## Request Parameters
<a name="ApiReference_CreateHITOperation-request-parameters"></a>

The `CreateHIT` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

The following tables describe the additional parameters required to call the `CreateHIT` operation with an explicit HIT type ID and without a HIT type ID.

### Calling CreateHIT with a HIT Type ID
<a name="ApiReference_CreateHITOperation-request-parameters-calling-createhit-with-a-hit-type-id"></a>

 The following parameters are specific to calling the `CreateHIT` operation with an explicit HIT type ID:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: CreateHIT<br />Default: None | Yes |
|  `HITTypeId`  | The HIT type ID.<br />Type: String<br />Default: None | Yes |
|  `Question`  | The data the person completing the HIT uses to produce the results. <br />Type: String<br />Default: None<br />Constraints: Must be a [ QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure, an [ ExternalQuestion](ApiReference_ExternalQuestionArticle.md) data structure, or an [HTMLQuestion](ApiReference_HTMLQuestionArticle.md) data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.<br />Either a `Question` parameter or a `HITLayoutId` parameter must be provided. | No |
|  `HITLayoutId`  | The `HITLayoutId` allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as `HITLayoutParameters`. For more information, see [HITLayout](ApiReference_HITLayoutArticle.md).<br />Type: String<br />Default: None<br />Constraints: Must be a valid `HITLayoutId`, as obtained from the Amazon Mechanical Turk Requester website. <br />Either a `Question` parameter or a `HITLayoutId` parameter must be provided. | No |
|  `HITLayoutParameter`  | If the `HITLayoutId` is provided, any placeholder values must be filled in with values using the `HITLayoutParameter` structure. For more information, see [HITLayout](ApiReference_HITLayoutArticle.md).<br />Type: [HITLayoutParameter](ApiReference_HITLayoutParameterArticle.md)<br />Default: None | No |
|  `LifetimeInSeconds`  |  The number of seconds after which the HIT is no longer available for users to accept. After the lifetime of the HIT has elapsed, the HIT no longer appears in HIT searches, even if not all of the HIT's assignments have been accepted. <br />Type: positive integer<br /> Valid Values: any integer between 30 (30 seconds) and 31536000 (365 days). <br />Default: None | Yes |
|  `MaxAssignments`  |  The number of times the HIT can be accepted and completed before the HIT becomes unavailable. <br />Type: positive integer<br /> Valid Values: any integer between 1 and 1000000000 (1 billion). <br />Default: 1 | No |
|  `AssignmentReviewPolicy`  | The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md). <br />Type: String<br />Valid Values: Must be a HIT Review Policy data structure, see [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md).<br />Default: none | No |
|  `HITReviewPolicy`  | The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy. For more information, see [HIT Review Policies](ApiReference_HITReviewPolicies.md). <br />Type: String<br />Valid Values: Must be a HIT Review Policy data structure, see [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md).<br />Default: none | No |
|  `RequesterAnnotation`  | An arbitrary data field. The `RequesterAnnotation` parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT. <br />The `RequesterAnnotation` parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester. <br />The `RequesterAnnotation` parameter may be different for each HIT you submit. It does not affect how your HITs are grouped. <br />Type: String<br />Default: None<br />Constraints: must not be longer than 255 characters in length. | No |
|  `UniqueRequestToken`  | A unique identifier for this request. Allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same `UniqueRequestToken`, subsequent calls will return a *AWS.MechanicalTurk.HitAlreadyExists* error with a message containing the HITId.<br />Type: String<br />Default: None<br />Constraints: must not be longer than 64 characters in length.<br />Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same `UniqueRequestToken` made after the 24 hour limit could create duplicate HITs. | No |

### Calling CreateHIT Without a HIT Type ID
<a name="ApiReference_CreateHITOperation-request-parameters-calling-createhit-without-a-hit-type-id"></a>

The following parameters are specific to calling the `CreateHIT` operation without a HIT type ID, letting Amazon Mechanical Turk determine the HIT type from the property values:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: CreateHIT<br />Default: None | Yes |
|  `Title`  |  The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned. <br />Type: String<br />Default: None<br />Constraints: must not be more than 128 characters | Yes |
|  `Description`  |  A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it. <br />Type: String<br />Default: None<br />Constraints: cannot be more than 2,000 characters in length | Yes |
|  `Question`  | The data the person completing the HIT uses to produce the results. <br />Type: String<br />Default: None<br />Constraints: Must be a [ QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure, an [ ExternalQuestion](ApiReference_ExternalQuestionArticle.md) data structure, or an [HTMLQuestion](ApiReference_HTMLQuestionArticle.md) data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.<br />Either a `Question` parameter or a `HITLayoutId` parameter must be provided. | No |
|  `HITLayoutId`  | The `HITLayoutId` allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as `HITLayoutParameters`. For more information, see [HITLayout](ApiReference_HITLayoutArticle.md).<br />Type: String<br />Default: None<br />Constraints: Must be a valid `HITLayoutId`, as obtained from the Amazon Mechanical Turk Requester website. <br />Either a `Question` parameter or a `HITLayoutId` parameter must be provided. | No |
|  `HITLayoutParameter`  | If the `HITLayoutId` is provided, any placeholder values must be filled in with values using the `HITLayoutParameter` structure. For more information, see [HITLayout](ApiReference_HITLayoutArticle.md).<br />Type: [HITLayoutParameter](ApiReference_HITLayoutParameterArticle.md)<br />Default: None | No |
|  `Reward`  |  The amount of money the Requester will pay a Worker for successfully completing the HIT. <br /> Type: [Price](ApiReference_PriceDataStructureArticle.md) data structure. <br />Default: None | Yes |
|  `AssignmentDurationInSeconds`  |  The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept. <br />Type: positive integer<br /> Valid Values: any integer between 30 (30 seconds) and 31536000 (365 days). <br />Default: None | Yes |
|  `LifetimeInSeconds`  |  An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted. <br />Type: positive integer<br /> Valid Values: any integer between 30 (30 seconds) and 31536000 (365 days). <br />Default: None | Yes |
|  `Keywords`  |  One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs. <br />Type: String<br />Default: None<br /> Constraints: The complete string of keywords, including commas and spaces, cannot be more than 1,000 characters.  | No |
|  `MaxAssignments`  |  The number of times the HIT can be accepted and completed before the HIT becomes unavailable. <br />Type: positive integer<br />Valid Values: any integer between 1 and 1000000000 (1 billion).<br />Default: 1 | No |
|  `AutoApprovalDelayInSeconds`  |  The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered **Approved** automatically unless the Requester explicitly rejects it. <br />Type: non-negative integer<br /> Valid Values: any integer between 0 (auto-approve results as soon as they are submitted) and 2592000 (30 days). <br />Default: 2592000 (30 days) | No |
|  `QualificationRequirement`  |  A condition that a Worker's Qualifications must meet before the Worker is allowed to accept and complete the HIT. <br /> Type: a [QualificationRequirement](ApiReference_QualificationRequirementDataStructureArticle.md) data structure. <br />Default: None<br /> Constraints: there can be no more than 10 `QualificationRequirement` data structures for each HIT.  | No |
|  `AssignmentReviewPolicy`  | The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md). <br />Type: String<br />Valid Values: Must be a HIT Review Policy data structure, see [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md).<br />Default: none | No |
|  `HITReviewPolicy`  | The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy. For more information, see [HIT Review Policies](ApiReference_HITReviewPolicies.md). <br />Type: String<br />Valid Values: Must be a HIT Review Policy data structure, see [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md).<br />Default: none | No |
|  `RequesterAnnotation`  | An arbitrary data field. The `RequesterAnnotation` parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, the `RequesterAnnotation` parameter could be an identifier internal to the Requester's application that corresponds with the HIT. <br />Type: String<br />Default: None<br />Constraints: must not be longer than 255 characters in length. | No |
|  `UniqueRequestToken`  | A unique identifier for this request. Allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same `UniqueRequestToken`, subsequent calls will return a *AWS.MechanicalTurk.HitAlreadyExists* error with a message containing the HITId.<br />Type: String<br />Default: None<br />Constraints: must not be longer than 64 characters in length.<br />Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same `UniqueRequestToken` made after the 24 hour limit could create duplicate HITs. | No |

## Response Elements
<a name="ApiReference_CreateHITOperation-response-elements"></a>

 A successful request for the `CreateHIT` operation includes the elements described in the following table.

| Name | Description |
| --- | --- |
|  `HIT`  |  Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the [ HIT Data Structure](ApiReference_HITDataStructureArticle.md).  |

## Examples
<a name="ApiReference_CreateHITOperation-examples"></a>

The following examples show how to use the `CreateHIT` operation.

### Sample Request
<a name="ApiReference_CreateHITOperation-examples-sample-request"></a>

The following are examples of REST requests.

**Example Request (Query) Using CreateHIT with a HIT Type ID**
 The following example creates a simple HIT, using an explicit HIT type ID. The `Question` parameter takes a block of XML data as its value. See the [ QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure and the[ ExternalQuestion](ApiReference_ExternalQuestionArticle.md) data structure for more information.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=CreateHIT
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &HITTypeId=T100CN9P324W00EXAMPLE
8. &Question={{[URL-encoded question data]}}
9. &LifetimeInSeconds=604800
```

**Example Request (Query) Using CreateHIT With a HIT Type ID Using SimplePlurality/2011-09-01 Review Policy**
The following example creates a simple HIT with a SimplePlurality/2011-09-01 Review Policy.

```
 1. <CreateHITRequest>
 2.     <HITTypeId>T100CN9P324W00EXAMPLE</HITTypeId>
 3.     <Question>[CDATA block or XML Entity encoded]</Question>
 4.     <LifetimeInSeconds>604800</LifetimeInSeconds>
 5.     <AssignmentReviewPolicy>
 6.         <PolicyName>ScoreMyKnownAnswers/2011-09-01</PolicyName>
 7.         <Parameter>
 8.             <Key>AnswerKey</Key>
 9.             <MapEntry>
10.                 <Key>QuestionId3</Key>   <!—correct answer is “B” -->
11.                 <Value>B</Value>
12.             </MapEntry
13.             <MapEntry>
14.                 <Key>QuestionId7</Key>  <!—correct answer is “A” -->
15.                 <Value>A</Value>
16.             </MapEntry>
17.             <MapEntry>
18.                 <Key>QuestionId15</Key>   <!—correct answer is “F” -->
19.                 <Value>F</Value>
20.             </MapEntry>
21.             <MapEntry>
22.                 <Key>QuestionId17</Key>   <!—correct answer is “C” -->
23.                 <Value>C</Value>
24.             </MapEntry>
25.             <MapEntry>
26.                 <Key>QuestionId18</Key>   <!—correct answer is “A” -->
27.                 <Value>A</Value>
28.             </MapEntry>
29.         </Parameter>
30.         <Parameter>
31.            <Key>ExtendIfKnownAnswerScoreIsLessThan</Key>
32.            <Value>80</Value>
33.         </Parameter>
34.         <Parameter>
35.            <Key>ExtendMaximumAssignments</Key>
36.            <Value>3</Value>
37.         </Parameter>
38.     </AssignmentReviewPolicy>
39. </CreateHITRequest>
```

**Example Request (Query) Using CreateHIT Without a HIT Type ID**
 The following example creates a simple HIT with some properties, letting Amazon Mechanical Turk determine the HIT type ID from the property values. The `Question` parameter takes a block of XML data as its value. See the [ QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure and the[ ExternalQuestion](ApiReference_ExternalQuestionArticle.md) data structure for more information.

```
 1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
 2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
 3. &Version=2017-01-17
 4. &Operation=CreateHIT
 5. &Signature={{[signature for this request]}}
 6. &Timestamp={{[your system's local time]}}
 7. &Title=Location%20and%20Photograph%20Identification
 8. &Description=Select%20the%20image%20that%20best%20represents...
 9. &Reward.1.Amount=5
10. &Reward.1.CurrencyCode=USD
11. &Question={{[URL-encoded question data]}}
12. &AssignmentDurationInSeconds=30
13. &LifetimeInSeconds=604800
14. &Keywords=location,%20photograph,%20image,%20identification,%20opinion
```

### Sample Response
<a name="ApiReference_CreateHITOperation-examples-sample-response"></a>

Amazon Mechanical Turk might return the following response for the preceding requests.

```
<CreateHITResponse>
  <OperationRequest>
    <RequestId>ece2785b-6292-4b12-a60e-4c34847a7916</RequestId>
  </OperationRequest>
  <HIT>
    <Request>
      <IsValid>True</IsValid>
    </Request>
    <HITId>GBHZVQX3EHXZ2AYDY2T0</HITId>
    <HITTypeId>NYVZTQ1QVKJZXCYZCZVZ</HITTypeId>
  </HIT>
</CreateHITResponse>
```
