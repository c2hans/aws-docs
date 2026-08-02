---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-policygrantdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant PolicyGrantDetail
<a name="aws-properties-datazone-policygrant-policygrantdetail"></a>

The details of the policy grant.

## Syntax
<a name="aws-properties-datazone-policygrant-policygrantdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-policygrantdetail-syntax.json"></a>

```
{
  "[AddToProjectMemberPool](#cfn-datazone-policygrant-policygrantdetail-addtoprojectmemberpool)" : {{AddToProjectMemberPoolPolicyGrantDetail}},
  "[CreateAssetType](#cfn-datazone-policygrant-policygrantdetail-createassettype)" : {{CreateAssetTypePolicyGrantDetail}},
  "[CreateDomainUnit](#cfn-datazone-policygrant-policygrantdetail-createdomainunit)" : {{CreateDomainUnitPolicyGrantDetail}},
  "[CreateEnvironment](#cfn-datazone-policygrant-policygrantdetail-createenvironment)" : {{Json}},
  "[CreateEnvironmentFromBlueprint](#cfn-datazone-policygrant-policygrantdetail-createenvironmentfromblueprint)" : {{Json}},
  "[CreateEnvironmentProfile](#cfn-datazone-policygrant-policygrantdetail-createenvironmentprofile)" : {{CreateEnvironmentProfilePolicyGrantDetail}},
  "[CreateFormType](#cfn-datazone-policygrant-policygrantdetail-createformtype)" : {{CreateFormTypePolicyGrantDetail}},
  "[CreateGlossary](#cfn-datazone-policygrant-policygrantdetail-createglossary)" : {{CreateGlossaryPolicyGrantDetail}},
  "[CreateProject](#cfn-datazone-policygrant-policygrantdetail-createproject)" : {{CreateProjectPolicyGrantDetail}},
  "[CreateProjectFromProjectProfile](#cfn-datazone-policygrant-policygrantdetail-createprojectfromprojectprofile)" : {{CreateProjectFromProjectProfilePolicyGrantDetail}},
  "[DelegateCreateEnvironmentProfile](#cfn-datazone-policygrant-policygrantdetail-delegatecreateenvironmentprofile)" : {{Json}},
  "[OverrideDomainUnitOwners](#cfn-datazone-policygrant-policygrantdetail-overridedomainunitowners)" : {{OverrideDomainUnitOwnersPolicyGrantDetail}},
  "[OverrideProjectOwners](#cfn-datazone-policygrant-policygrantdetail-overrideprojectowners)" : {{OverrideProjectOwnersPolicyGrantDetail}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-policygrantdetail-syntax.yaml"></a>

```
  [AddToProjectMemberPool](#cfn-datazone-policygrant-policygrantdetail-addtoprojectmemberpool): {{
    AddToProjectMemberPoolPolicyGrantDetail}}
  [CreateAssetType](#cfn-datazone-policygrant-policygrantdetail-createassettype): {{
    CreateAssetTypePolicyGrantDetail}}
  [CreateDomainUnit](#cfn-datazone-policygrant-policygrantdetail-createdomainunit): {{
    CreateDomainUnitPolicyGrantDetail}}
  [CreateEnvironment](#cfn-datazone-policygrant-policygrantdetail-createenvironment): {{Json}}
  [CreateEnvironmentFromBlueprint](#cfn-datazone-policygrant-policygrantdetail-createenvironmentfromblueprint): {{Json}}
  [CreateEnvironmentProfile](#cfn-datazone-policygrant-policygrantdetail-createenvironmentprofile): {{
    CreateEnvironmentProfilePolicyGrantDetail}}
  [CreateFormType](#cfn-datazone-policygrant-policygrantdetail-createformtype): {{
    CreateFormTypePolicyGrantDetail}}
  [CreateGlossary](#cfn-datazone-policygrant-policygrantdetail-createglossary): {{
    CreateGlossaryPolicyGrantDetail}}
  [CreateProject](#cfn-datazone-policygrant-policygrantdetail-createproject): {{
    CreateProjectPolicyGrantDetail}}
  [CreateProjectFromProjectProfile](#cfn-datazone-policygrant-policygrantdetail-createprojectfromprojectprofile): {{
    CreateProjectFromProjectProfilePolicyGrantDetail}}
  [DelegateCreateEnvironmentProfile](#cfn-datazone-policygrant-policygrantdetail-delegatecreateenvironmentprofile): {{Json}}
  [OverrideDomainUnitOwners](#cfn-datazone-policygrant-policygrantdetail-overridedomainunitowners): {{
    OverrideDomainUnitOwnersPolicyGrantDetail}}
  [OverrideProjectOwners](#cfn-datazone-policygrant-policygrantdetail-overrideprojectowners): {{
    OverrideProjectOwnersPolicyGrantDetail}}
```

## Properties
<a name="aws-properties-datazone-policygrant-policygrantdetail-properties"></a>

`AddToProjectMemberPool`  <a name="cfn-datazone-policygrant-policygrantdetail-addtoprojectmemberpool"></a>
Specifies that the policy grant is to be added to the members of the project.
*Required*: No
*Type*: [AddToProjectMemberPoolPolicyGrantDetail](aws-properties-datazone-policygrant-addtoprojectmemberpoolpolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateAssetType`  <a name="cfn-datazone-policygrant-policygrantdetail-createassettype"></a>
Specifies that this is a create asset type policy.
*Required*: No
*Type*: [CreateAssetTypePolicyGrantDetail](aws-properties-datazone-policygrant-createassettypepolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateDomainUnit`  <a name="cfn-datazone-policygrant-policygrantdetail-createdomainunit"></a>
Specifies that this is a create domain unit policy.
*Required*: No
*Type*: [CreateDomainUnitPolicyGrantDetail](aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateEnvironment`  <a name="cfn-datazone-policygrant-policygrantdetail-createenvironment"></a>
Specifies that this is a create environment policy.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateEnvironmentFromBlueprint`  <a name="cfn-datazone-policygrant-policygrantdetail-createenvironmentfromblueprint"></a>
Specifies that this is a create environment from blueprint policy.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateEnvironmentProfile`  <a name="cfn-datazone-policygrant-policygrantdetail-createenvironmentprofile"></a>
Specifies that this is a create environment profile policy.
*Required*: No
*Type*: [CreateEnvironmentProfilePolicyGrantDetail](aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateFormType`  <a name="cfn-datazone-policygrant-policygrantdetail-createformtype"></a>
Specifies that this is a create form type policy.
*Required*: No
*Type*: [CreateFormTypePolicyGrantDetail](aws-properties-datazone-policygrant-createformtypepolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateGlossary`  <a name="cfn-datazone-policygrant-policygrantdetail-createglossary"></a>
 Specifies that this is a create glossary policy.
*Required*: No
*Type*: [CreateGlossaryPolicyGrantDetail](aws-properties-datazone-policygrant-createglossarypolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateProject`  <a name="cfn-datazone-policygrant-policygrantdetail-createproject"></a>
Specifies that this is a create project policy.
*Required*: No
*Type*: [CreateProjectPolicyGrantDetail](aws-properties-datazone-policygrant-createprojectpolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreateProjectFromProjectProfile`  <a name="cfn-datazone-policygrant-policygrantdetail-createprojectfromprojectprofile"></a>
Specifies whether to create a project from project profile.
*Required*: No
*Type*: [CreateProjectFromProjectProfilePolicyGrantDetail](aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DelegateCreateEnvironmentProfile`  <a name="cfn-datazone-policygrant-policygrantdetail-delegatecreateenvironmentprofile"></a>
Specifies that this is the delegation of the create environment profile policy.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverrideDomainUnitOwners`  <a name="cfn-datazone-policygrant-policygrantdetail-overridedomainunitowners"></a>
Specifies whether to override domain unit owners.
*Required*: No
*Type*: [OverrideDomainUnitOwnersPolicyGrantDetail](aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverrideProjectOwners`  <a name="cfn-datazone-policygrant-policygrantdetail-overrideprojectowners"></a>
Specifies whether to override project owners.
*Required*: No
*Type*: [OverrideProjectOwnersPolicyGrantDetail](aws-properties-datazone-policygrant-overrideprojectownerspolicygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
