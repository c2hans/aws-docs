---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ReviewPolicyUseCases.html
---

# Review Policy Use Cases
<a name="ApiReference_ReviewPolicyUseCases"></a>

The following use cases show you how to apply ScoreYourKnownAnswers and SimplePlurality policies when you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation.

## Photo Moderation Use Case – Single Worker with Known Answers
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-single-worker-with-known-answers"></a>

In this scenario, you want Workers to moderate photos and screen the photos for inappropriate content. You place 20 photos in a single HIT and 5 of the 20 photos are your known answers. You are using Master Workers and have created the HIT with only one initial assignment. You want to use the answers based on the Worker getting at least 4 of the 5 known answers (80% Answer Agreement Score) correct. If the first Worker does not meet the Answer Agreement score of 80%, then you want to extend the HIT to another Worker. But, in this scenario, you only want to extend the HIT to a maximum of three Workers.

### Elements and Parameters
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-single-worker-with-known-answers-elements-and-parameters"></a>

The following is a list of elements and parameters you need to specify in the [CreateHIT](ApiReference_CreateHITOperation.md) operation to execute the above scenario and allow Mechanical Turk to automatically calculate the known answer score. Note that this `CreateHIT` example assumes you have already created a HIT Type.

| Element | Parameter | Value |
| --- | --- | --- |
|  `AssignmentReviewPolicy`  | PolicyName | ScoreMyKnownAnswers/2011/09/01 |
|  `AssignmentReviewPolicy`  | AnswerKey | List of questionIDs and answers. |
|  `AssignmentReviewPolicy`  | ExtendIfKnownAnswerScoreIsLessThan | 80 |
|  `AssignmentReviewPolicy`  | ExtendMaximumAssignments | 3 |

### Examples
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-single-worker-with-known-answers-examples"></a>

The following example shows how to use the above elements and parameters with the `CreateHIT` operation.

#### Sample CreateHIT Request
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-single-worker-with-known-answers-examples-sample-createhit-request"></a>

The following example shows a `CreateHIT` request.

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

## Photo Moderation Use Case – Multiple Workers with Agreement
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-multiple-workers-with-agreement"></a>

In this scenario, you want Workers to moderate photos and screen the photos for inappropriate content. You place 20 photos in a single HIT and 5 of the 20 photos are your known answers. You want to approve the assignment if the Worker completes at least 4 of the 5 known answers correct (at least 80% Answer Agreement Score).

You want 3 Workers to complete each HIT and you want to calculate the HIT Agreement Score for the 15 photos you don’t know the answer to. Also, you want to disregard the Worker's answer in the Agreement Score if they don't get 4 of 5 of the known answers correct.

### Elements and Parameters
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-multiple-workers-with-agreement-elements-and-parameters"></a>

The following is a list of elements and parameters you need to specify in the [CreateHIT](ApiReference_CreateHITOperation.md) operation to execute the above scenario and allow Mechanical Turk to automatically approve the assignments. Note that this CreateHIT example assumes you have already created a HIT Type.

| Element | Parameter | Value |
| --- | --- | --- |
|  `AssignmentReviewPolicy`  | PolicyName | ScoreMyKnownAnswers/2011/09/01 |
|  `AssignmentReviewPolicy`  | Answer | List of questionIDs and answers. |
|  `AssignmentReviewPolicy`  | ApproveIfKnownAnswerScoreIsAtLeast  | 80 |
|  `AssignmentReviewPolicy`  | ExtendIfKnownAnswerScoreIsLessThan | 80 |
|  `AssignmentReviewPolicy`  | ExtendMaximumAssignments | 3 |
|  `HITReviewPolicy`  | PolicyName | SimplePlurality/2011-09-01  |
|  `HITReviewPolicy`  | QuestionIDs | Your list of 15 question IDs. |
|  `HITReviewPolicy`  | QuestionAgreementThreshold | 100  |
|  `HITReviewPolicy`  | DisregardAssignmentIfKnownAnswerScoreIsLessThan | 80 |

### Examples
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-multiple-workers-with-agreement-examples"></a>

The following example shows how to use the above elements and parameters with the `CreateHIT` operation.

#### Sample CreateHIT Request
<a name="ApiReference_ReviewPolicyUseCases-photo-moderation-use-case-multiple-workers-with-agreement-examples-sample-createhit-request"></a>

The following example shows a `CreateHIT` request.

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
14.                 <Key>QuestionId4</Key>  <!—correct answer is “A” -->
15.                 <Value>A</Value>
16.             </MapEntry>
17.             <MapEntry>
18.                 <Key>QuestionId13</Key>   <!—correct answer is “F” -->
19.                 <Value>F</Value>
20.             </MapEntry>
21.             <MapEntry>
22.                 <Key>QuestionId14</Key>   <!—correct answer is “C” -->
23.                 <Value>C</Value>
24.             </MapEntry>
25.             <MapEntry>
26.                 <Key>QuestionId19</Key>   <!—correct answer is “A” -->
27.                 <Value>A</Value>
28.             </MapEntry>
29.          </Parameter>
30.         <Parameter>
31.            <Key>ApproveIfKnownAnswerScoreIsAtLeast</Key>
32.            <Value>80</Value>
33.         </Parameter>
34.         <Parameter>
35.            <Key>ExtendIfKnownAnswerScoreIsLessThan</Key>
36.            <Value>80</Value>
37.         </Parameter>
38.         <Parameter>
39.            <Key>ExtendMaximumAssignments</Key>
40.            <Value>3</Value>
41.         </Parameter>
42.     </AssignmentReviewPolicy>
43.     <HITReviewPolicy>
44.         <PolicyName>SimplePlurality/2011-09-01</PolicyName>
45.         <Parameter>
46.            <Key>QuestionIDs</Key>
47.            <Value>questionid1</Value>
48.            <Value>questionid2</Value>
49.            <Value>questionid5</Value>
50.            <Value>questionid6</Value>
51.            <Value>questionid7</Value>
52.                  ..... <! Add your additional 10 questionIDs for a total of 15 questions. Different from your known answer questionIDs.>
53.         </Parameter>
54.         <Parameter>
55.            <Key>QuestionAgreementThreshold</Key>
56.            <Value>100</Value>
57.         </Parameter>
58.         <Parameter>
59.            <Key>DisregardAssignmentIfKnownAnswerScoreIsLessThan</Key>
60.            <Value>80</Value>
61.         </Parameter>
62.     </HITReviewPolicy>
63. </CreateHITRequest>
```

## Categorization and Tagging Use Case – Multiple Workers
<a name="ApiReference_ReviewPolicyUseCases-categorization-and-tagging-use-case-multiple-workers"></a>

In this scenario, you want Workers to categorize a product and provide multiple tags for the product in a HIT. You also want the Workers to be able to comment on your HIT and give you feedback.

You want to calculate the Answer Agreement Score for only the categorization question. If two Workers do not agree on the product categorization question, you want to extend the HIT to a third Worker. Also, you want to extend the assignment by an hour so the third Worker has time to work on the assignment.

### Elements and Parameters
<a name="ApiReference_ReviewPolicyUseCases-categorization-and-tagging-use-case-multiple-workers-elements-and-parameters"></a>

The following is a list of elements and parameters you need to specify in the [CreateHIT](ApiReference_CreateHITOperation.md) operation to execute the above scenario and allow Mechanical Turk to automatically calculate agreement and approve or reject the assignments. Note that this CreateHIT example assumes you have already created a HIT Type.

| Element | Parameter | Value |
| --- | --- | --- |
|  `HITReviewPolicy`  | PolicyName | SimplePlurality/2011-09-01 |
|  `HITReviewPolicy`  | QuestionIDs | questionID1 |
|  `HITReviewPolicy`  | QuestionAgreementThreshold | 100 |
|  `HITReviewPolicy`  | ExtendMinimumTimeInSeconds | 3600 |
|  `HITReviewPolicy`  | ExtendMaximumAssignments | 3 |

### Examples
<a name="ApiReference_ReviewPolicyUseCases-categorization-and-tagging-use-case-multiple-workers-examples"></a>

The following example shows how to use the above elements and parameters with the `CreateHIT` operation.

#### Sample CreateHIT Request
<a name="ApiReference_ReviewPolicyUseCases-categorization-and-tagging-use-case-multiple-workers-examples-sample-createhit-request"></a>

The following example shows a CreateHIT request.

```
 1. <CreateHITRequest>
 2.     <HITTypeId>T100CN9P324W00EXAMPLE</HITTypeId>
 3.     <Question>[CDATA block or XML Entity encoded]</Question>
 4.     <LifetimeInSeconds>604800</LifetimeInSeconds>
 5.     <HITReviewPolicy>
 6.         <PolicyName>SimplePlurality/2011-09-01</PolicyName>
 7.         <Parameter>
 8.            <Key>QuestionIDs</Key>
 9.            <Value>questionID1</Value>
10.         </Parameter>
11.         <Parameter>
12.            <Key>QuestionAgreementThreshold</Key>
13.            <Value>100</Value>
14.         </Parameter>
15.         <Parameter>
16.            <Key>ExtendMaximumAssignments</Key>
17.            <Value>3</Value>
18.         </Parameter>
19.         <Parameter>
20.            <Key>ExtendMinimumTimeInSeconds</Key>
21.            <Value>3600</Value>
22.         </Parameter>
23.     </HITReviewPolicy>
24. </CreateHITRequest>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
