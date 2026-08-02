---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflow-registrymapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow RegistryMapping
<a name="aws-properties-omics-workflow-registrymapping"></a>

If you are using the ECR pull through cache feature, the registry mapping maps between the ECR repository and the upstream registry where container images are pulled and synchronized.

## Syntax
<a name="aws-properties-omics-workflow-registrymapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflow-registrymapping-syntax.json"></a>

```
{
  "[EcrAccountId](#cfn-omics-workflow-registrymapping-ecraccountid)" : {{String}},
  "[EcrRepositoryPrefix](#cfn-omics-workflow-registrymapping-ecrrepositoryprefix)" : {{String}},
  "[UpstreamRegistryUrl](#cfn-omics-workflow-registrymapping-upstreamregistryurl)" : {{String}},
  "[UpstreamRepositoryPrefix](#cfn-omics-workflow-registrymapping-upstreamrepositoryprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-workflow-registrymapping-syntax.yaml"></a>

```
  [EcrAccountId](#cfn-omics-workflow-registrymapping-ecraccountid): {{String}}
  [EcrRepositoryPrefix](#cfn-omics-workflow-registrymapping-ecrrepositoryprefix): {{String}}
  [UpstreamRegistryUrl](#cfn-omics-workflow-registrymapping-upstreamregistryurl): {{String}}
  [UpstreamRepositoryPrefix](#cfn-omics-workflow-registrymapping-upstreamrepositoryprefix): {{String}}
```

## Properties
<a name="aws-properties-omics-workflow-registrymapping-properties"></a>

`EcrAccountId`  <a name="cfn-omics-workflow-registrymapping-ecraccountid"></a>
Account ID of the account that owns the upstream container image.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EcrRepositoryPrefix`  <a name="cfn-omics-workflow-registrymapping-ecrrepositoryprefix"></a>
The repository prefix to use in the ECR private repository.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpstreamRegistryUrl`  <a name="cfn-omics-workflow-registrymapping-upstreamregistryurl"></a>
The URI of the upstream registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpstreamRepositoryPrefix`  <a name="cfn-omics-workflow-registrymapping-upstreamrepositoryprefix"></a>
The repository prefix of the corresponding repository in the upstream registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `2`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
