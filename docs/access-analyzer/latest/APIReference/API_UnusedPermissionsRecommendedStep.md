---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedPermissionsRecommendedStep.html
---

# UnusedPermissionsRecommendedStep
<a name="API_UnusedPermissionsRecommendedStep"></a>

Contains information about the action to take for a policy in an unused permissions finding.

## Contents
<a name="API_UnusedPermissionsRecommendedStep_Contents"></a>

 ** recommendedAction **   <a name="accessanalyzer-Type-UnusedPermissionsRecommendedStep-recommendedAction"></a>
A recommendation of whether to create or detach a policy for an unused permissions finding.
Type: String
Valid Values: `CREATE_POLICY | DETACH_POLICY`
Required: Yes

 ** existingPolicyId **   <a name="accessanalyzer-Type-UnusedPermissionsRecommendedStep-existingPolicyId"></a>
If the recommended action for the unused permissions finding is to detach a policy, the ID of an existing policy to be detached.
Type: String
Required: No

 ** policyUpdatedAt **   <a name="accessanalyzer-Type-UnusedPermissionsRecommendedStep-policyUpdatedAt"></a>
The time at which the existing policy for the unused permissions finding was last updated.
Type: Timestamp
Required: No

 ** recommendedPolicy **   <a name="accessanalyzer-Type-UnusedPermissionsRecommendedStep-recommendedPolicy"></a>
If the recommended action for the unused permissions finding is to replace the existing policy, the contents of the recommended policy to replace the policy specified in the `existingPolicyId` field.
Type: String
Required: No

## See Also
<a name="API_UnusedPermissionsRecommendedStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
