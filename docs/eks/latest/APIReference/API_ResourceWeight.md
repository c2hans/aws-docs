---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ResourceWeight.html
---

# ResourceWeight
<a name="API_ResourceWeight"></a>

A resource weight entry for the scheduler scoring strategy.

## Contents
<a name="API_ResourceWeight_Contents"></a>

 ** name **   <a name="AmazonEKS-Type-ResourceWeight-name"></a>
The name of the resource (for example, `cpu` or `memory`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Required: No

 ** weight **   <a name="AmazonEKS-Type-ResourceWeight-weight"></a>
The weight assigned to the resource for scoring. Must be between 1 and 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_ResourceWeight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ResourceWeight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ResourceWeight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ResourceWeight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
