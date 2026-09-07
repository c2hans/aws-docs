---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_HITReviewPolicyDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# HIT Review Policy
<a name="ApiReference_HITReviewPolicyDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_HITReviewPolicyDataStructureArticle-description)
+ [HIT Review Policy Elements](#ApiReference_HITReviewPolicyDataStructureArticle-hit-review-policy-elements)
+ [Parameter Elements](#ApiReference_HITReviewPolicyDataStructureArticle-parameter-elements)
+ [MapEntry Elements](#ApiReference_HITReviewPolicyDataStructureArticle-mapentry-elements)
+ [Examples](#ApiReference_HITReviewPolicyDataStructureArticle-examples)

## Description
<a name="ApiReference_HITReviewPolicyDataStructureArticle-description"></a>

HIT Review Policy data structures represent HIT review policies, which you specify when you create a Human Intelligence Task (HIT). For more information about Review Policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).

The following two types of HIT Review Policy data structures are used when calling the [CreateHIT](ApiReference_CreateHITOperation.md) operation.
+ `AssignmentReviewPolicy` data structures set the review results and actions at the Assignment level. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md).
+  `HITReviewPolicy` data structures set the review results and actions at the HIT-level. For more information, see [HIT Review Policies](ApiReference_HITReviewPolicies.md).

The HIT Review Policy data structure is used in the following operation:
+  `CreateHIT`

## HIT Review Policy Elements
<a name="ApiReference_HITReviewPolicyDataStructureArticle-hit-review-policy-elements"></a>

The HIT Review Policy data structures can contain the following elements.

| Name | Description | Required |
| --- | --- | --- |
|  `PolicyName`  | Name of a Review Policy. For policy names and descriptions, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md) and [HIT Review Policies](ApiReference_HITReviewPolicies.md).<br />Type: String<br />Constraints: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01  | Yes |
|  `Parameter`  | Name of the parameter from the Review policy.<br />Type: Parameter data structure, for a description see the next section Parameter Elements.  |  |

## Parameter Elements
<a name="ApiReference_HITReviewPolicyDataStructureArticle-parameter-elements"></a>

The Parameter data structure contains the elements described in the following table.

| Name | Description | Required |
| --- | --- | --- |
|  `Key `  | Name of the parameter from the list of Review Polices. For a list of valid parameter names, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md) and [HIT Review Policies](ApiReference_HITReviewPolicies.md). <br />Type: String<br />Constraints: none <br />Default: none  |  |
|  `Value`  | Value of the parameter.<br />Type: Varies.  |  |
|  `MapEntry `  | This data structure is the data type for the `AnswerKey` parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md).<br />Type: MapEntry data structure, for a description, see the next section MapEntry Elements.  |  |

## MapEntry Elements
<a name="ApiReference_HITReviewPolicyDataStructureArticle-mapentry-elements"></a>

The MapEntry element contains the elements described in the following table.

| Name | Description | Required |
| --- | --- | --- |
|  `Key`  | The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.<br />Type: String none  |  |
|  `Value`  | The answer to the question specified in the MapEntry `Key` element. <br />Note: You can provide multiple `Value` elements, but the Worker must match all values in order for the answer to be scored correctly.<br />Type: String  |  |

## Examples
<a name="ApiReference_HITReviewPolicyDataStructureArticle-examples"></a>

The following example request shows the structure of a `CreateHIT` request using HIT Review Policy data structures. The example request is followed by an example response.

### Sample Request
<a name="ApiReference_HITReviewPolicyDataStructureArticle-examples-sample-request"></a>

 The following is an example request.

```
 1. <CreateHITRequest>
 2.     <HITTypeId>T100CN9P324W00EXAMPLE</HITTypeId>
 3.     <Question>{{URL-encoded question data}}</Question>
 4.     <LifetimeInSeconds>604800</LifetimeInSeconds>
 5.     <AssignmentReviewPolicy>
 6.         <PolicyName>ScoreMyKnownAnswers/2011-09-01</PolicyName>
 7.         <Parameter>
 8.             <Key>AnswerKey</Key>
 9.             <MapEntry>
10.                 <Key>QuestionId1</Key>   <!—correct answer is “B” -->
11.                 <Value>B</Value>
12.             </MapEntry
13.             <MapEntry>
14.                 <Key>QuestionId2</Key>  <!—correct answer is “A” -->
15.                 <Value>A</Value>
16.             </MapEntry>
17.             <MapEntry>
18.                 <Key>QuestionId1</Key>   <!—correct answer is “F” -->
19.                 <Value>F</Value>
20.             </MapEntry>
21.             <MapEntry>
22.                 <Key>QuestionId1</Key>   <!—correct answer is “C” -->
23.                 <Value>C</Value>
24.             </MapEntry>
25.             <MapEntry>
26.                 <Key>QuestionId1</Key>   <!—correct answer is “A” -->
27.                 <Value>A</Value>
28.             </MapEntry
29.         <Parameter>
30.            <Key>ApproveIfKnownAnswerScoreIsAtLeast</Key>
31.            <Value>79</Value>
32.         </Parameter>
33.         <Parameter>
34.            <Key>ExtendIfKnownAnswerScoreIsLessThan</Key>
35.            <Value>79</Value>
36.         </Parameter>
37.         <Parameter>
38.            <Key>ExtendMaximumAssignments</Key>
39.            <Value>3</Value>
40.         </Parameter>
41.     </AssignmentReviewPolicy>
42.     <HITReviewPolicy>
43.         <PolicyName>SimplePlurality/2011-09-01</PolicyName>
44.         <Parameter>
45.            <Key>QuestionIDs</Key>
46.            <Value>questionid1</Value>
47.            <Value>questionid2</Value>
48.            <Value>questionid3</Value>
49.            <Value>questionid4</Value>
50.            <Value>questionid5</Value>
51.                  ..... <! Add your additional 10 questionIDs for a total of 15 questions>
52.         </Parameter>
53.         <Parameter>
54.            <Key>QuestionAgreementThreshold</Key>
55.            <Value>100</Value>
56.         </Parameter>
57.     </HITReviewPolicy>
58. </CreateHITRequest>
```

### Sample Response
<a name="ApiReference_HITReviewPolicyDataStructureArticle-examples-sample-response"></a>

The following is an example response.

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
