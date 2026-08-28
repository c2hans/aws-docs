---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AssignmentReviewPolicies.html
---

# Assignment Review Policies
<a name="ApiReference_AssignmentReviewPolicies"></a>

Assignment-level Review Policies are applied as soon as a Worker submits an assignment.

## ScoreMyKnownAnswers/2011-09-01
<a name="ScoreMyKnownAnswers_2011-09-01"></a>

ScoreMyKnownAnswers/2011-09-01 is an Assignment-level Review Policy.

### Description
<a name="ScoreMyKnownAnswers_2011-09-01-description"></a>

You can use the ScoreMyKnownAnswers/2011-09-01 Review Policy for QuestionForm (QAP) HITs and for ExternalQuestion (iframe) HITs. You provide an answer key when you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation. The answer key is a collection of QuestionIds, where each QuestionId has a set of zero or more values that represent the correct response for that QuestionId. For more information about QuestionForm and ExternalQuestion HITs, see [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) and [ExternalQuestion](ApiReference_ExternalQuestionArticle.md).

You can specify if one question in your HIT has a known answer or if many questions in your HIT have known answers. When a Worker submits an assignment Mechanical Turk examines the Worker's answers and compares them against the set of known answers that you provide when you create the HIT. Mechanical Turk then calculates a score, for example, 4 out of 10 known answers were correct.

Based on how the Worker's level of agreement with the known answers compares with various configurable thresholds, Mechanical Turk can automatically take actions you requested to approve the assignment, automatically reject the assignment, or automatically extend the HIT to publish an assignment for another Worker.

A Worker’s performance on known answers within a specific assignment are returned from calling the ListReviewPolicyResultsForHIT operation.

Mechanical Turk evaluates answers and considers the following answers as not matching:
+ The Worker left an empty value set in the answer key.
+ The answer key has an empty value set but the Worker supplied an answer.
+ The Worker provides an answer that is the wrong case or has incorrect punctuation that doesn't match the answer exactly. You can either use structured HTML form elements to restrict the values a Worker can submit, or use JavaScript to validate and normalize the submitted values.
+ The answer key says a question's answer is A and B but the Worker's value is A.
+ The answer key says a question's answer is A and the Worker selected both A and B.

When comparing answers for a match, Mechanical Turk removes any whitespace from before and after the Worker's answer, and from before and after the answer you provide.

### Parameters
<a name="ScoreMyKnownAnswers_2011-09-01-parameters"></a>

The following parameters are specified in the AssignmentReviewPolicy element when calling the `CreateHIT` operation. You must also specify the PolicyName *ScoreYourKnownAnswers/2011-09-01* as part of the AssignmentReviewPolicy element. For an example of how to structure the AssignmentReviewPolicy element, see the [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md) data structure.

| Name | Description | Required |
| --- | --- | --- |
|  `AnswerKey`  | Question IDs and the answers to the questions.<br />Type: MapEntry, see the [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md) data structure. <br />Default: None | Yes |
|  `ApproveIfKnownAnswerScoreIsAtLeast`  | Approve the assignment if the KnownAnswerScore is equal to or greater than this value. If not specified, assignments are left in the submitted state and are not approved or rejected. <br />Type: Integer<br />Constraints: Minimum value 0 (always approve), maximum 101 (never approve) | No |
|  `ApproveReason`  | A description provided to the Worker about the reason the assignment was approved. If not specified, the reason is left blank. <br />Type: String | No |
|  `RejectIfKnownAnswerScoreIsLessThan`  | Reject the assignment if the KnownAnswerScore is equal to or less than this value. If not specified, assignments are left in the submitted state and are not approved or rejected. <br />Type: Integer<br />Constraints: Minimum value 0 (never reject), maximum 101 (always reject).  | No |
|  `RejectReason`  | A description provided to the Worker about the reason the assignment was rejected. If not specified, the reason is left blank. <br />Type: String | No |
|  `ExtendIfKnownAnswerScoreIsLessThan`  | Extend the HIT by one assignment to allow one more Worker to complete it if the known answer score is less than this value. Ordinarily this is done to replace an assignment that is being rejected or that is not usable because the Worker didn't answer the known answer correctly. <br />If omitted the HIT is not extended. <br />Type: String<br />Constraint: Minimum value 0 (never extend), maximum 101 (always extend).  | No |
|  `ExtendMaximumAssignments`  | The maximum number of assignments the HIT can be extended. Note that if you use the CreateAdditionalAssignmentsForHIT operation and specify a maximum assignment count greater than this value, ScoreMyKnownAnswers will not extend the HIT.<br />**Note**: If a HIT is created with fewer than 10 assignments, it will not extend to have 10 or more assignments.<br />Type: Integer<br />Constraint: Minimum value 2, maximum 25.<br />Default: 5 | No |
|  `ExtendMinimumTimeInSeconds`  | The additional time in seconds to let other Workers complete the extended assignment. <br />Type: Integer<br />Constraints: Minimum of 60 (one minute), Maximum of 31536000 (one year).<br />Default: 0 | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
