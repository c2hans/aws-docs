---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillMdSourceFromUrl

URL-based source of agent skills content.

With an `s3://` URL, the registry reads the Amazon S3 object when you create the record. It reads the object again when you change the URL, the credential provider, or the bucket owner. To synchronize again from an unchanged source, change the URL, for example to a new object key.

An `https://` URL is a reference URL that the registry doesn't synchronize from. In Regions where skill synchronization from Amazon S3 is available, the registry accepts an `https://` URL only on a record that already stores it, when you provide the content inline in `SkillMd.Data`.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax.json"></a>

```json
{
  "[CredentialProviderConfigurations](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-credentialproviderconfigurations)" : {{[ SkillSourceCredentialProviderConfiguration, ... ]}},
  "[Url](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax.yaml"></a>

```yaml
  [CredentialProviderConfigurations](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-credentialproviderconfigurations): {{
    - SkillSourceCredentialProviderConfiguration}}
  [Url](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-url): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-properties"></a>

`CredentialProviderConfigurations`  <a name="cfn-agentregistry-registryrecord-skillmdsourcefromurl-credentialproviderconfigurations"></a>
The credential providers that the registry uses to read the source. The list can contain at most one entry. For an Amazon S3 source, specify an IAM role in your account that the `agent-registry.amazonaws.com` service principal can assume and that can read the object.
To read a publicly readable object, omit this property and set `BucketOwnerAccountId` in `SourceConfiguration.S3` instead.
*Required*: No
*Type*: Array of [SkillSourceCredentialProviderConfiguration](aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-agentregistry-registryrecord-skillmdsourcefromurl-url"></a>
The URL of the source. To synchronize, specify an `s3://{{bucket}}/{{key}}` URL that names one object in a bucket in the same AWS Region as the registry. For `SkillMd`, name a SKILL.md object. For `SkillPackage`, name a skill package ZIP object.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
