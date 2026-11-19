---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_Evaluation.html
---

# Evaluation

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

 ** checks **   <a name="iamtoolbox-Type-Evaluation-checks"></a>
 `checks` contains the authorization checks that explain an evaluation result. Each check is one authorization requirement and reports its result and policies from the top-level `policies` list with matching statements. The output lists RCP checks from the organization root to the account, then SCP checks from the organization root to the account. It then lists VPC endpoint, resource, principal, permissions boundary, and session checks. When `checks` is present, an `EXPLICIT_DENY` evaluation includes an `EXPLICIT_DENY` check. When `checks` is present for an `IMPLICIT_DENY` evaluation, it includes an `IMPLICIT_DENY` check and no `EXPLICIT_DENY` check. For more information about how IAM evaluates policies, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html).
 `PRINCIPAL`, `PERMISSIONS_BOUNDARY`, and `SESSION` checks appear when they apply to the principal that made the request, even if none of their policies matched. A missing allow produces `IMPLICIT_DENY`, or `NO_IMPACT` when another path already allowed the request.
Returned when the caller is in the request principal's account or organization. The absence of `checks` does not mean no authorization checks applied.
Type: Array of [Check](API_Check.md) objects
Required: No

 ** context **   <a name="iamtoolbox-Type-Evaluation-context"></a>
The context keys and values specific to this evaluation. These are applied on top of the request context.
Type: String to JSON value map
Required: No

 ** evaluatedEffect **   <a name="iamtoolbox-Type-Evaluation-evaluatedEffect"></a>
The result of the evaluation. Valid values:
+  `ALLOW` - The action was allowed.
+  `EXPLICIT_DENY` - The action was explicitly denied by a policy.
+  `IMPLICIT_DENY` - The action was denied because at least one required authorization check had no matching allow statement.
Type: String
Valid Values: `ALLOW | EXPLICIT_DENY | IMPLICIT_DENY`
Required: No

 ** matchedPolicies **   <a name="iamtoolbox-Type-Evaluation-matchedPolicies"></a>
 `matchedPolicies` is deprecated. Use `checks` instead. This value contains the policies that matched during evaluation of this action and resource.
Type: Array of [MatchedPolicy](API_MatchedPolicy.md) objects
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/Evaluation)
