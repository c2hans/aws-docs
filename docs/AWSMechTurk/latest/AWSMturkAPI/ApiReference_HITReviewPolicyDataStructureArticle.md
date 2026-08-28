---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITReviewPolicyDataStructureArticle.html
---

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
|  `Key`  | The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy. Can be up to 255 bytes in length.<br />Type: String none  |  |
|  `Value`  | The answer to the question specified in the MapEntry `Key` element. <br />Note: You can provide multiple `Value` elements, but the Worker must match all values in order for the answer to be scored correctly.<br />Type: String  |  |

## Examples
<a name="ApiReference_HITReviewPolicyDataStructureArticle-examples"></a>

The following example request shows the structure of a `CreateHIT` request using HIT Review Policy data structures. The example request is followed by an example response.

### Sample Request
<a name="ApiReference_HITReviewPolicyDataStructureArticle-examples-sample-request"></a>

 The following is an example `CreateHIT` request.

```
{	HITTypeId:"T100CN9P324W00EXAMPLE",
    Question:{{URL-encoded question data}},
    LifetimeInSeconds:604800,
    AssignmentReviewPolicy:{
        PolicyName:"ScoreMyKnownAnswers/2011-09-01",
        Parameters:[
			{ Key:"AnswerKey",
		  		MapEntries:[
					{Key: "QuestionId1", Values:["B"]},
					{Key: "QuestionId2", Value:["A"]},
					{Key: "QuestionId3", Value:["C"]},
					{Key: "QuestionId4", Value:["A"]}
					]
			},
			{ Key: "ApproveIfKnownAnswerScoreIsAtLeast",
			  Values:["79"]
			}
			{ Key: "ExtendIfKnownAnswerScoreIsLessThan",
			  Values:["79"]
			}
			{ Key: "ExtendMaximumAssignments",
			  Values:["3"]
			}
		]
	},
    HITReviewPolicy:{
        PolicyName:"SimplePlurality/2011-09-01",
        Parameters:[
			{
				Key:"QuestionIDs",
				// Add upto 15 questions
				Values:["questionid1", "questionid2", "questionid3", "questionid4", "questionid5"]
			},
			{
				Key:"QuestionAgreementThreshold",
				Values:["100"]
			}
		]
	}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
