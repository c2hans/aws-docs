---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnusedPermissionsRecommendationStep.html
---

# UnusedPermissionsRecommendationStep
<a name="API_UnusedPermissionsRecommendationStep"></a>

Contains information about the action to take for a policy in an unused permissions finding.

## Contents
<a name="API_UnusedPermissionsRecommendationStep_Contents"></a>

 ** ExistingPolicy **   <a name="securityhub-Type-UnusedPermissionsRecommendationStep-ExistingPolicy"></a>
The contents of the existing policy identified by `ExistingPolicyId` which needs to be replaced, when the `RecommendedAction` is `CREATE_POLICY`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExistingPolicyId **   <a name="securityhub-Type-UnusedPermissionsRecommendationStep-ExistingPolicyId"></a>
The ID of an existing policy to be replaced or detached.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PolicyUpdatedAt **   <a name="securityhub-Type-UnusedPermissionsRecommendationStep-PolicyUpdatedAt"></a>
The time at which the existing policy for the unused permissions finding was last updated.
Type: Timestamp
Required: No

 ** RecommendedAction **   <a name="securityhub-Type-UnusedPermissionsRecommendationStep-RecommendedAction"></a>
A recommendation of whether to create or detach a policy for an unused permissions finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RecommendedPolicy **   <a name="securityhub-Type-UnusedPermissionsRecommendationStep-RecommendedPolicy"></a>
The contents of the least-privileged recommended replacement for `ExistingPolicyId`, when the `RecommendedAction` is `CREATE_POLICY`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnusedPermissionsRecommendationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnusedPermissionsRecommendationStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnusedPermissionsRecommendationStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnusedPermissionsRecommendationStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
