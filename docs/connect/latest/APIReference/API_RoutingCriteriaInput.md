---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingCriteriaInput.html
---

# RoutingCriteriaInput
<a name="API_RoutingCriteriaInput"></a>

An object to define the RoutingCriteria.

## Contents
<a name="API_RoutingCriteriaInput_Contents"></a>

 ** Steps **   <a name="connect-Type-RoutingCriteriaInput-Steps"></a>
When Connect Customer does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.
Type: Array of [RoutingCriteriaInputStep](API_RoutingCriteriaInputStep.md) objects
Required: No

## See Also
<a name="API_RoutingCriteriaInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingCriteriaInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingCriteriaInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingCriteriaInput)
