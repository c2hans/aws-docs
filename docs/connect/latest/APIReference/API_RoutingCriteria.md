---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingCriteria.html
---

# RoutingCriteria
<a name="API_RoutingCriteria"></a>

Latest routing criteria on the contact.

## Contents
<a name="API_RoutingCriteria_Contents"></a>

 ** ActivationTimestamp **   <a name="connect-Type-RoutingCriteria-ActivationTimestamp"></a>
The timestamp indicating when the routing criteria is set to active. A routing criteria is activated when contact is transferred to a queue. ActivationTimestamp will be set on routing criteria for contacts in agent queue even though Routing criteria is never activated for contacts in agent queue.
Type: Timestamp
Required: No

 ** Index **   <a name="connect-Type-RoutingCriteria-Index"></a>
Information about the index of the routing criteria.
Type: Integer
Required: No

 ** Steps **   <a name="connect-Type-RoutingCriteria-Steps"></a>
List of routing steps. When Connect Customer does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.
Type: Array of [Step](API_Step.md) objects
Required: No

## See Also
<a name="API_RoutingCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
