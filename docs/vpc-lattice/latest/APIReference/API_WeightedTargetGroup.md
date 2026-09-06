---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_WeightedTargetGroup.html
---

# WeightedTargetGroup
<a name="API_WeightedTargetGroup"></a>

Describes the weight of a target group.

## Contents
<a name="API_WeightedTargetGroup_Contents"></a>

 ** targetGroupIdentifier **   <a name="vpclattice-Type-WeightedTargetGroup-targetGroupIdentifier"></a>
The ID or ARN of the target group.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))`
Required: Yes

 ** weight **   <a name="vpclattice-Type-WeightedTargetGroup-weight"></a>
Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: No

## See Also
<a name="API_WeightedTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/WeightedTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/WeightedTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/WeightedTargetGroup)
