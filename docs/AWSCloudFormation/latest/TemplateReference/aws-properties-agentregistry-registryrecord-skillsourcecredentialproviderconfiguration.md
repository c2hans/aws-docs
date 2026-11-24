---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillSourceCredentialProviderConfiguration

A credential provider configuration that the registry uses to read an agent skills source. For an Amazon S3 source, specify an IAM role.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-syntax.json"></a>

```json
{
  "[CredentialProvider](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovider)" : {{SkillSourceCredentialProviderUnion}},
  "[CredentialProviderType](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovidertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-syntax.yaml"></a>

```yaml
  [CredentialProvider](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovider): {{
    SkillSourceCredentialProviderUnion}}
  [CredentialProviderType](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovidertype): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-properties"></a>

`CredentialProvider`  <a name="cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovider"></a>
The credential provider details for the specified credential provider type.
*Required*: Yes
*Type*: [SkillSourceCredentialProviderUnion](aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProviderType`  <a name="cfn-agentregistry-registryrecord-skillsourcecredentialproviderconfiguration-credentialprovidertype"></a>
The type of the credential provider.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
