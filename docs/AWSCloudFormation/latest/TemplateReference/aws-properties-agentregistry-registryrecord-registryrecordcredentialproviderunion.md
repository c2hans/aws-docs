---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordCredentialProviderUnion
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion"></a>

The credential provider details for a registry record. Exactly one member is populated, matching the configured credential provider type.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion-syntax.json"></a>

```
{
  "[IamCredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-iamcredentialprovider)" : {{RegistryRecordIamCredentialProvider}},
  "[OauthCredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-oauthcredentialprovider)" : {{RegistryRecordOAuthCredentialProvider}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion-syntax.yaml"></a>

```
  [IamCredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-iamcredentialprovider): {{
    RegistryRecordIamCredentialProvider}}
  [OauthCredentialProvider](#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-oauthcredentialprovider): {{
    RegistryRecordOAuthCredentialProvider}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion-properties"></a>

`IamCredentialProvider`  <a name="cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-iamcredentialprovider"></a>
The IAM role credential provider details.
*Required*: No
*Type*: [RegistryRecordIamCredentialProvider](aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OauthCredentialProvider`  <a name="cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-oauthcredentialprovider"></a>
The OAuth 2.0 credential provider details.
*Required*: No
*Type*: [RegistryRecordOAuthCredentialProvider](aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
