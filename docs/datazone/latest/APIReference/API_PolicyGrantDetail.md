---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PolicyGrantDetail.html
---

# PolicyGrantDetail
<a name="API_PolicyGrantDetail"></a>

The details of the policy grant.

## Contents
<a name="API_PolicyGrantDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** addToProjectMemberPool **   <a name="datazone-Type-PolicyGrantDetail-addToProjectMemberPool"></a>
Specifies that the policy grant is to be added to the members of the project.
Type: [AddToProjectMemberPoolPolicyGrantDetail](API_AddToProjectMemberPoolPolicyGrantDetail.md) object
Required: No

 ** createAssetType **   <a name="datazone-Type-PolicyGrantDetail-createAssetType"></a>
Specifies that this is a create asset type policy.
Type: [CreateAssetTypePolicyGrantDetail](API_CreateAssetTypePolicyGrantDetail.md) object
Required: No

 ** createDomainUnit **   <a name="datazone-Type-PolicyGrantDetail-createDomainUnit"></a>
Specifies that this is a create domain unit policy.
Type: [CreateDomainUnitPolicyGrantDetail](API_CreateDomainUnitPolicyGrantDetail.md) object
Required: No

 ** createEnvironment **   <a name="datazone-Type-PolicyGrantDetail-createEnvironment"></a>
Specifies that this is a create environment policy.
Type: [Unit](API_Unit.md) object
Required: No

 ** createEnvironmentFromBlueprint **   <a name="datazone-Type-PolicyGrantDetail-createEnvironmentFromBlueprint"></a>
The details of the policy of creating an environment.
Type: [Unit](API_Unit.md) object
Required: No

 ** createEnvironmentProfile **   <a name="datazone-Type-PolicyGrantDetail-createEnvironmentProfile"></a>
Specifies that this is a create environment profile policy.
Type: [CreateEnvironmentProfilePolicyGrantDetail](API_CreateEnvironmentProfilePolicyGrantDetail.md) object
Required: No

 ** createFormType **   <a name="datazone-Type-PolicyGrantDetail-createFormType"></a>
Specifies that this is a create form type policy.
Type: [CreateFormTypePolicyGrantDetail](API_CreateFormTypePolicyGrantDetail.md) object
Required: No

 ** createGlossary **   <a name="datazone-Type-PolicyGrantDetail-createGlossary"></a>
 Specifies that this is a create glossary policy.
Type: [CreateGlossaryPolicyGrantDetail](API_CreateGlossaryPolicyGrantDetail.md) object
Required: No

 ** createProject **   <a name="datazone-Type-PolicyGrantDetail-createProject"></a>
Specifies that this is a create project policy.
Type: [CreateProjectPolicyGrantDetail](API_CreateProjectPolicyGrantDetail.md) object
Required: No

 ** createProjectFromProjectProfile **   <a name="datazone-Type-PolicyGrantDetail-createProjectFromProjectProfile"></a>
Specifies whether to create a project from project profile.
Type: [CreateProjectFromProjectProfilePolicyGrantDetail](API_CreateProjectFromProjectProfilePolicyGrantDetail.md) object
Required: No

 ** delegateCreateEnvironmentProfile **   <a name="datazone-Type-PolicyGrantDetail-delegateCreateEnvironmentProfile"></a>
Specifies that this is the delegation of the create environment profile policy.
Type: [Unit](API_Unit.md) object
Required: No

 ** overrideDomainUnitOwners **   <a name="datazone-Type-PolicyGrantDetail-overrideDomainUnitOwners"></a>
Specifies whether to override domain unit owners.
Type: [OverrideDomainUnitOwnersPolicyGrantDetail](API_OverrideDomainUnitOwnersPolicyGrantDetail.md) object
Required: No

 ** overrideProjectOwners **   <a name="datazone-Type-PolicyGrantDetail-overrideProjectOwners"></a>
Specifies whether to override project owners.
Type: [OverrideProjectOwnersPolicyGrantDetail](API_OverrideProjectOwnersPolicyGrantDetail.md) object
Required: No

 ** useAssetType **   <a name="datazone-Type-PolicyGrantDetail-useAssetType"></a>
 Specifies the domain unit(s) whose projects can use this asset type while creating asset or asset revisions.
Type: [UseAssetTypePolicyGrantDetail](API_UseAssetTypePolicyGrantDetail.md) object
Required: No

## See Also
<a name="API_PolicyGrantDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PolicyGrantDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PolicyGrantDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PolicyGrantDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
