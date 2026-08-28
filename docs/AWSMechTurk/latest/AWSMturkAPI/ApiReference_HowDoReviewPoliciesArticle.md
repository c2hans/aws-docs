---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HowDoReviewPoliciesArticle.html
---

# How Review Policies Work
<a name="ApiReference_HowDoReviewPoliciesArticle"></a>

You specify the Review Policy(s) that you want Mechanical Turk to apply when you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation. You must specify Review Policies when you create a HIT. You cannot apply a Review Policy to an existing HIT.

As assignments are submitted, Mechanical Turk applies the Review Policy(s) that you specify. You call the ListReviewPolicyResultsForHIT operation to gather the results from the application of the Review Policy.

There are two types of Review Policies, Assignment-level Review Policies that are applied as soon as a Worker submits an assignment and HIT-level Review Policies that are applied when a HIT becomes reviewable. For more information, see [Assignment Review Policies](ApiReference_AssignmentReviewPolicies.md) and [HIT Review Policies](ApiReference_HITReviewPolicies.md).

You can specify one Assignment-level Review Policy and one HIT-level Review Policy when you call `CreateHIT` using the [HIT Review Policy](ApiReference_HITReviewPolicyDataStructureArticle.md) data structure. The Assignment-level Review Policy ScoreMyKnownAnswer/2011-09-01 and the HIT-level Review Policy SimplePlurality/2011-09-01 can be used in the same call to `CreateHIT`.

Once an Assignment-level Review Policy is applied, the Assignment's status is changed to *Submitted* and optionally an event notification can be sent. Assignments with *Submitted* status are returned by the ListAssignmentsForHIT operation and the results of applying the Review Policy are available by using the ListReviewPolicyResultsForHIToperation.

You can use different Review Policies on distinct HITs in a HIT type. For example, you may wish to apply the ScoreMyKnownAnswers/2011-09-01 policy to a small number of HITs that have known answers in them, but apply the SimplePlurality/2011-09-01 policy to all HITs in a group. Workers do not have access on the Worker User Interface to information about whether a Review Policy has been applied to a HIT.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
