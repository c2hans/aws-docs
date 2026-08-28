---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EffectivePreferredResource.html
---

# EffectivePreferredResource
<a name="API_EffectivePreferredResource"></a>

 Describes the effective preferred resources that Compute Optimizer considers as rightsizing recommendation candidates.

**Note**
Compute Optimizer only supports Amazon EC2 instance types.

## Contents
<a name="API_EffectivePreferredResource_Contents"></a>

 ** effectiveIncludeList **   <a name="computeoptimizer-Type-EffectivePreferredResource-effectiveIncludeList"></a>
 The expanded version of your preferred resource's include list.
Type: Array of strings
Required: No

 ** excludeList **   <a name="computeoptimizer-Type-EffectivePreferredResource-excludeList"></a>
 The list of preferred resources values that you want excluded from rightsizing recommendation candidates.
Type: Array of strings
Required: No

 ** includeList **   <a name="computeoptimizer-Type-EffectivePreferredResource-includeList"></a>
 The list of preferred resource values that you want considered as rightsizing recommendation candidates.
Type: Array of strings
Required: No

 ** name **   <a name="computeoptimizer-Type-EffectivePreferredResource-name"></a>
 The name of the preferred resource list.
Type: String
Valid Values: `Ec2InstanceTypes`
Required: No

## See Also
<a name="API_EffectivePreferredResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EffectivePreferredResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EffectivePreferredResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EffectivePreferredResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
