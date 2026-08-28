---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ScoringStrategyConstraints.html
---

# ScoringStrategyConstraints
<a name="API_ScoringStrategyConstraints"></a>

Constraints for the scoring strategy configuration.

## Contents
<a name="API_ScoringStrategyConstraints_Contents"></a>

 ** resources **   <a name="AmazonEKS-Type-ScoringStrategyConstraints-resources"></a>
The constraints for resource weights.
Type: [ResourceConstraints](API_ResourceConstraints.md) object
Required: No

 ** scoringStrategy **   <a name="AmazonEKS-Type-ScoringStrategyConstraints-scoringStrategy"></a>
The allowed values for the scoring strategy type.
Type: [AllowedValuesConstraint](API_AllowedValuesConstraint.md) object
Required: No

## See Also
<a name="API_ScoringStrategyConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ScoringStrategyConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ScoringStrategyConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ScoringStrategyConstraints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
