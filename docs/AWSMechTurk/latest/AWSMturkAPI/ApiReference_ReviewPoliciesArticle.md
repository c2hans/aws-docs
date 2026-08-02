---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ReviewPoliciesArticle.html
---

# Review Policies
<a name="ApiReference_ReviewPoliciesArticle"></a>

Using Amazon Mechanical Turk Review Policies you can evaluate Worker submissions against a defined set of criteria. You specify the Review Policy(s) that you want to use when you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation.

There are two types of Review Policies, Assignment-level and HIT-level:

+ An Assignment-level Review Policy is applied as soon as a Worker submits an assignment. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md).
+ A HIT-level Review Policy is applied when a HIT becomes reviewable. For more information, see [HIT Review Policies](ApiReference_HITReviewPolicies.md).

You can select from a set of pre-defined Review Policies. One Review Policy leverages *known answers* or *gold standards* within a Human Intelligence Task (HIT) and has Mechanical Turk calculate a Worker’s performance on these known answers. You can specify an action for Mechanical Turk to take automatically based on Worker performance against the known answer.

Mechanical Turk has Review Policies that calculate consensus/agreement among multiple Workers performing the same HITs. For instance, you can specify a Review Policy that measures agreement on work items within the HIT and authorizes Mechanical Turk to keep asking additional Workers to work on the HIT, until a certain level of agreement is achieved. Once the required level of agreement is achieved, the results are returned to you for immediate use.

Review Policies that track Worker performance on your known answers and agreement with other Workers give you information you can use to manage your Workers. For more information about using Review Policies, see [Review Policy Use Cases](ApiReference_ReviewPolicyUseCases.md).
