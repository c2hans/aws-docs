---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordCredentialProviderConfiguration
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration"></a>

A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record's source URL.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-syntax.json"></a>

```
{
  "[CredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovider)" : {{RegistryRecordCredentialProviderUnion}},
  "[CredentialProviderType](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovidertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-syntax.yaml"></a>

```
  [CredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovider): {{
    RegistryRecordCredentialProviderUnion}}
  [CredentialProviderType](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovidertype): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-properties"></a>

`CredentialProvider`  <a name="cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovider"></a>
The credential provider details corresponding to the specified credential provider type.
*Required*: Yes
*Type*: [RegistryRecordCredentialProviderUnion](aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProviderType`  <a name="cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovidertype"></a>
The type of credential provider.
*Required*: Yes
*Type*: String
*Allowed values*: `OAUTH | IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
