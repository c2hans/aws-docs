---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_Evaluation.html
---

# Evaluation
<a name="API_Evaluation"></a>

Represents an individual evaluation for a single action and resource pair. This includes the context, the resulting effect, and any policies that matched.

## Contents
<a name="API_Evaluation_Contents"></a>

 ** action **   <a name="iamtoolbox-Type-Evaluation-action"></a>
The action evaluated for this request (for example, `iam:PassRole`).
Type: String
Required: Yes

 ** resource **   <a name="iamtoolbox-Type-Evaluation-resource"></a>
The resource that the action targeted. This is typically a resource ARN, but can be a wildcard ARN that matches multiple resources, or empty for actions that are not resource-specific.
Type: String
Required: Yes

 ** context **   <a name="iamtoolbox-Type-Evaluation-context"></a>
The context keys and values specific to this evaluation. These are applied on top of the request context.
Type: String to JSON value map
Required: No

 ** evaluatedEffect **   <a name="iamtoolbox-Type-Evaluation-evaluatedEffect"></a>
The result of the evaluation. Valid values:
+  `ALLOW` - The action was allowed.
+  `EXPLICIT_DENY` - The action was explicitly denied by a policy.
+  `IMPLICIT_DENY` - The action was denied because no policy allowed it.
Type: String
Valid Values: `ALLOW | EXPLICIT_DENY | IMPLICIT_DENY`
Required: No

 ** matchedPolicies **   <a name="iamtoolbox-Type-Evaluation-matchedPolicies"></a>
The policies that matched during evaluation of this action and resource. An implicit denial produces no matched policies.
Type: Array of [MatchedPolicy](API_MatchedPolicy.md) objects
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/Evaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Toolbox. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iam-toolbox` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
