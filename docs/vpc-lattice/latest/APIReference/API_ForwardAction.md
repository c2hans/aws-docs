---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ForwardAction.html
---

# ForwardAction
<a name="API_ForwardAction"></a>

Describes a forward action. You can use forward actions to route requests to one or more target groups.

## Contents
<a name="API_ForwardAction_Contents"></a>

 ** targetGroups **   <a name="vpclattice-Type-ForwardAction-targetGroups"></a>
The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.
The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.
Type: Array of [WeightedTargetGroup](API_WeightedTargetGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_ForwardAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ForwardAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ForwardAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ForwardAction)
