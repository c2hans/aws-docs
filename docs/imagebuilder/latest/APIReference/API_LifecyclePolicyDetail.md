---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetail.html
---

# LifecyclePolicyDetail
<a name="API_LifecyclePolicyDetail"></a>

The configuration details for a lifecycle policy resource.

## Contents
<a name="API_LifecyclePolicyDetail_Contents"></a>

 ** action **   <a name="imagebuilder-Type-LifecyclePolicyDetail-action"></a>
Configuration details for the policy action.
Type: [LifecyclePolicyDetailAction](API_LifecyclePolicyDetailAction.md) object
Required: Yes

 ** filter **   <a name="imagebuilder-Type-LifecyclePolicyDetail-filter"></a>
Specifies the resources that the lifecycle policy applies to.
Type: [LifecyclePolicyDetailFilter](API_LifecyclePolicyDetailFilter.md) object
Required: Yes

 ** exclusionRules **   <a name="imagebuilder-Type-LifecyclePolicyDetail-exclusionRules"></a>
Additional rules to specify resources that should be exempt from policy actions.
Type: [LifecyclePolicyDetailExclusionRules](API_LifecyclePolicyDetailExclusionRules.md) object
Required: No

## See Also
<a name="API_LifecyclePolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
