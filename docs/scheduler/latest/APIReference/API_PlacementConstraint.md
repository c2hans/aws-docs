---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_PlacementConstraint.html
---

# PlacementConstraint
<a name="API_PlacementConstraint"></a>

An object representing a constraint on task placement.

## Contents
<a name="API_PlacementConstraint_Contents"></a>

 ** expression **   <a name="scheduler-Type-PlacementConstraint-expression"></a>
A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is `distinctInstance`. For more information, see [Cluster query language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon ECS Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** type **   <a name="scheduler-Type-PlacementConstraint-type"></a>
The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.
Type: String
Valid Values: `distinctInstance | memberOf`
Required: No

## See Also
<a name="API_PlacementConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/PlacementConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/PlacementConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/PlacementConstraint)
