---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ScoringStrategy.html
---

# ScoringStrategy
<a name="API_ScoringStrategy"></a>

The scoring strategy configuration for the NodeResourcesFit scheduler plugin.

## Contents
<a name="API_ScoringStrategy_Contents"></a>

 ** resources **   <a name="AmazonEKS-Type-ScoringStrategy-resources"></a>
The resource weights used for scoring nodes.
Type: Array of [ResourceWeight](API_ResourceWeight.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** type **   <a name="AmazonEKS-Type-ScoringStrategy-type"></a>
The scoring strategy type. Valid values are `LeastAllocated` or `MostAllocated`.
Type: String
Valid Values: `LeastAllocated | MostAllocated`
Required: No

## See Also
<a name="API_ScoringStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ScoringStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ScoringStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ScoringStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
