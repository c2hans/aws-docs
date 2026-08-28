---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_MembershipInferenceAttackScore.html
---

# MembershipInferenceAttackScore
<a name="API_MembershipInferenceAttackScore"></a>

A score that measures the vulnerability of synthetic data to membership inference attacks and provides both the numerical score and the version of the attack methodology used for evaluation.

## Contents
<a name="API_MembershipInferenceAttackScore_Contents"></a>

 ** attackVersion **   <a name="API-Type-MembershipInferenceAttackScore-attackVersion"></a>
The version of the membership inference attack, which consists of the attack type and its version number, used to generate this privacy score.
Type: String
Valid Values: `DISTANCE_TO_CLOSEST_RECORD_V1`
Required: Yes

 ** score **   <a name="API-Type-MembershipInferenceAttackScore-score"></a>
The numerical score representing the vulnerability to membership inference attacks.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: Yes

## See Also
<a name="API_MembershipInferenceAttackScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/MembershipInferenceAttackScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/MembershipInferenceAttackScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/MembershipInferenceAttackScore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
