---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITReviewPolicies.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# HIT Review Policies
<a name="ApiReference_HITReviewPolicies"></a>

A HIT-level Review Policy is applied when a Human Intelligence Task (HIT) becomes reviewable.

## SimplePlurality/2011-09-01
<a name="PluralityHITReview_2011-09-01"></a>

SimplePlurality/2011-09-01 is a HIT-level Review Policy.

### Description
<a name="PluralityHITReview_2011-09-01-description"></a>

The SimplePlurality/2011-09-01 policy allows you to automatically compare answers received from multiple Workers and detect if there is a majority or consensus answer. The results can optionally trigger additional actions, such as approving the assignments that matched the majority answer. The results of this comparison are available as a part of the ListReviewPolicyResultsForHIT operation.

Mechanical Turk evaluates answers and considers the following answers as not matching:
+ The Worker provides an answer that is the wrong case or incorrect punctuation that doesn't match the answer exactly to another Worker. You can either use structured HTML form elements to restrict the values a Worker can submit, or use JavaScript to validate and normalize the submitted values.
+ One Worker's answer is A and B, but another Worker's value is A.
+ One Worker's answer is A, but another Worker selected both A and B.

When comparing answers for a match, Mechanical Turk removes any whitespace from before and after the Worker's answer.

**Note**
Answers that are longer than 256 characters are not used in the computation of HIT review policies.

### Parameters
<a name="PluralityHITReview_2011-09-01-parameters"></a>

The following parameters are specified in the HITReviewPolicy element when calling the [CreateHIT](ApiReference_CreateHITOperation.md) operation. You must also specify the PolicyName *SimplePlurality/2011-09-01* as part of the HitReviewPolicy element. For an example, see [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md) data structure.

| Name | Description | Required |
| --- | --- | --- |
|  `QuestionIds`  | A comma-separated list of questionIds used to determine agreement.<br />Type: String<br />Constraints: none | Yes |
|  `QuestionAgreementThreshold`  | If the Question Agreement Score is greater than this value, the questionId is considered to have an *agreed answer*.<br />Type: Integer<br />Constraints: none | Yes |
|  `DisregardAssignmentIfRejected`  | Excludes rejected assignments from agreement calculation.<br />Type: Boolean<br />Constraints: T or F  | Yes |
|  `DisregardAssignmentIfKnownAnswerScoreIsLessThan`  | Excludes answers from agreement calculation if the KnownAnswerScore is present and less than the provided value. <br />Type: Integer<br />Constraints: none  | No |
|  `ExtendIfHITAgreementScoreIsLessThan `  | If the HIT Agreement Score is less than this value, extend the HIT to another Worker to complete. If omitted, extending on failure is disabled.<br />Type: Integer<br />Constraints: 1-100  | No |
|  `ExtendMaximumAssignments`  | If the ExtendIfHITAgreementScoreIsLessThan is provided, this sets the total maximum number of assignments for the HIT. <br />If you use ExtendHIT operation and specify the maximum assignment count greater than this value, ScoreMyKnownAnswers will not extend the HIT. <br />**Note**: If a HIT is created with fewer than 10 assignments, it will not extend to have 10 or more assignments.<br />Type: Integer<br />Constraints: none<br />Conditions: Required if ExtendIfHITAgreementScoreIsLessThan is provided. | Conditional |
|  `ExtendMinimumTimeInSeconds`  | If the ExtendIfHITAgreementScoreIsLessThan is provided, this sets the additional time that the HIT will be extended by. <br />Type: Integer<br />Constraints: Minimum of 60 (one minute), Maximum of 31536000 (365 days) <br />Conditions: Required if ExtendIfHITAgreementScoreIsLessThan is provided. | Conditional |
|  `ApproveIfWorkerAgreementScoreIsAtLeast`  | If the Worker Agreement Score is not less than this value, approve the Worker's assignment.<br />If omitted, assignment will not be approved or rejected.<br />Type: Integer<br />Constraints: none | No |
|  `RejectIfWorkerAgreementScoreIsLessThan`  | If the Worker Agreement Score is less than this value, reject the Worker's assignment.<br />If omitted, assignment will not be approved or rejected.<br />Type: Integer<br />Constraints: none | No |
|  `RejectReason`  | If the RejectIfWorkerAgreementIsScoreLessThan value is provided, this value sets the reason for any automated rejections.<br />Type: String<br />Constraints: none | Optional |

### Scores
<a name="PluralityHITReview_2011-09-01-scores"></a>

The following scores are calculated data from the SimplePlurality/2011-09-01 policy. Based on the value of these scores, Mechanical Turk can take various actions that you specify in the `CreateHIT` operation. It is important to understand how these scores are calculated so you can specify the appropriate actions to take, including approving or rejecting assignments, or extending HITs. The following chart describes how the scores are calculated.

| Score | Description |
| --- | --- |
| Question Agreement Score  | Percentage of Workers who provided the agreed-upon answer for a HIT.<br />Note: Answer values are not normalized for case, whitespace, or punctuation before comparison. Answers can contain multiple values (such as in a set of check boxes); two answers agree with each other if they have the same values present and absent. We don't recommend using free format answers because values are not normalized. |
|  HIT Agreement Score  | Percentage of questions within the HIT with an agreed-upon answer. The number of questions within the HIT with an agreed-upon answer, divided by the number of questions evaluated.  |
|  Worker Agreement Score  | The percentage of questions to which a Worker's answer agreed with other Workers' answers in the same HIT. If a question does not have an agreed upon answer the question is disregarded in this calculation. |

The example chart below describes how the Answer Agreement Score and Worker Agreement Score is calculated for a HIT with 4 questions and answers from 3 Workers.

| QuestionId | Worker1's answers | Worker2's answers  | Worker3's answers  | Has Agreed-upon value? | Agreed-upon value | Question Agreement Score |
| --- | --- | --- | --- | --- | --- | --- |
| A | coat | sweater | coat | Yes | coat | 66% |
| B | blue | blue | green | Yes | blue | 66% |
| C | large | large | large | Yes | large | 100% |
| D | Furry | fur | furr | No | n/a | n/a |
| Worker Agreement Score | 100% | 66% | 66% |  |  |  |

The Question Agreement Score for questions A and B are 66% because two Workers agreed on the same answer. The HIT Agreement Score for this HIT is 75%. The HIT had four questions, and three of them had an agreed-upon answer for a percentage of 75%. The Worker Agreement Score for Worker 1 is 100% because this Worker agreed with the other Workers for each answer, except Question D where there was no conclusive answer.
